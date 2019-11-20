#!/usr/bin/env python3
#
# Dig Over Http/s (DoH)
# https://github.com/opendns/doh-client
#
#
import time, sys
import ssl
import dns.message
from urllib import request

DEFAULT_SERVER = "https://doh.opendns.com"
RR_TYPES = dns.rdatatype._by_text.keys()

def usage():
    print("Usage: doh [@[http[s]://]server[:port]] [TYPE] [+nosslverify] domain")

def print_packet(dnsr):
    print(";; ->>HEADER<<- opcode: {}, status: {}, id: {}".format(dns.opcode.to_text(dnsr.opcode()), dns.rcode.to_text(dnsr.rcode()), dnsr.id))
    print(";; flags: {}".format(dns.flags.to_text(dnsr.flags)))
    print()

    is_update = dns.opcode.is_update(dnsr.flags)
    print(";; ZONE:") if is_update else print(";; QUESTION:")
    for rrset in dnsr.question:
        print(rrset.to_text())
    print()

    print(";; PREREQ:") if is_update else print(";; ANSWER:")
    for rrset in dnsr.answer:
        print(rrset.to_text())
    print()

    if dnsr.authority and len(dnsr.authority) > 0:
        print(";; UPDATE:") if is_update else print(";; AUTHORITY:")
        for rrset in dnsr.authority:
            print(rrset.to_text())
        print()

    if dnsr.additional and len(dnsr.additional) > 0:
        print(";; ADDITIONAL:")
        for rrset in dnsr.additional:
            print(rrset.to_text())
        print()

def build_dns_query(domain, record_type):
    dnsq = dns.message.make_query(
        qname=domain,
        rdtype=record_type,
        want_dnssec=False,
    )
    return dnsq

class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        print("Redirect:", headers["location"])
        return None

def main(argv):
    record_name = ""
    record_type = "A"
    server = DEFAULT_SERVER
    ssl_ctx = None

    for arg in argv[1:]:
        if arg == "-h" or arg == "--help":
            usage()
            return 0

        if arg.startswith("@"):
            server=arg[1:]
            continue

        if arg.startswith("+"):
            if arg == "+nosslverify" and ssl_ctx == None:
                ssl_ctx = ssl.create_default_context()
                ssl_ctx.check_hostname = False
                ssl_ctx.verify_mode = ssl.CERT_NONE
            continue

        if arg.upper() in RR_TYPES:
            record_type = arg.upper()
            continue

        if record_name == "":
            record_name = arg
            continue

        print("Invalid argument:", arg)
        return 1

    if record_name == "":
        usage()
        return 0

    print("; <<>> DoH Client 0.1 <<>> " + " ".join(argv[1:]))

    # verify server name
    if "://" in server:
        if server.startswith("http://") or server.startswith("https://"):
            pass
        else:
            print("Invalid protocol in server name")
            return 1
    else:
        server = "https://" + server

    time_start = time.time()
    try:
        dnsq = build_dns_query(record_name, record_type)

        opener = request.build_opener(NoRedirect)
        request.install_opener(opener)

        req = request.Request(server + "/dns-query", data=dnsq.to_wire())
        req.add_header('accept', 'application/dns-message')
        req.add_header('content-type', 'application/dns-message')
        dnsr = dns.message.from_wire(request.urlopen(req, context=ssl_ctx).read())
    except Exception as e:
        sys.stderr.write("Error")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return 2

    time_end = time.time()
    print(";; Got answer:")
    print_packet(dnsr)
    print(";; Server: {}".format(server))
    print(";; Query time: {} msec".format(int((time_end - time_start) * 1000)))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
