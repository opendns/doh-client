#### Dig Over HTTP/S

A DiG-like DoH client in Python3 from a hackathon.

1. Clone the repo or Download the code via [Github Releases](https://github.com/opendns/doh-client/releases/latest)
2. Install requirements `pip3 install -r requirements.txt`
2. Rename/move doh.py to `/usr/local/bin/doh` and use it like [dig](https://en.wikipedia.org/wiki/Dig_(command)).

`doh -h` for usage.

```
~ $ doh cisco.com
; <<>> DoH Client 0.1 <<>> cisco.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21541
;; flags: QR RD RA

;; QUESTION:
cisco.com. IN A

;; ANSWER:
cisco.com. 2695 IN A 72.163.4.185

;; Server: https://doh.opendns.com
;; Query time: 44 msec


~ $ doh facebook.com AAAA @dns.google
; <<>> DoH Client 0.1 <<>> facebook.com AAAA @dns.google
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 22164
;; flags: QR RD RA

;; QUESTION:
facebook.com. IN AAAA

;; ANSWER:
facebook.com. 299 IN AAAA 2a03:2880:f101:83:face:b00c:0:25de

;; Server: https://dns.google
;; Query time: 81 msec
```

## LICENSE

Copyright (C) 2019 OpenDNS Inc.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

  * Neither the name of OpenDNS Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
