# SPDX-License-Identifier: MIT
"""Temporary self-signed HTTPS server for repository CA certificate tests."""

from __future__ import absolute_import, division, print_function

import os
import ssl
import sys

try:
    from http.server import HTTPServer, SimpleHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler


class CertificateHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/unattended/public/foreman_raw_ca":
            self.send_error(404)
            return
        SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, *args):
        pass


def main():
    os.chdir(sys.argv[1])
    server = HTTPServer(("127.0.0.1", 0), CertificateHandler)
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.load_cert_chain("server.crt", "server.key")
    server.socket = context.wrap_socket(server.socket, server_side=True)
    server.timeout = 1
    with open("port", "w") as port_file:
        port_file.write(str(server.server_port))
    try:
        while not os.path.exists("stop"):
            server.handle_request()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
