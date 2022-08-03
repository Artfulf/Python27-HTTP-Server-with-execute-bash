#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer
import cgitb;
import sys


cgitb.enable()  # Error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)

httpd = server(server_address, handler)
httpd.serve_forever()
