"""
This class is a model that interact with the SPA environment.
"""
from data_repository.configuration import Definitions as df


class Model(object):

    @staticmethod
    def register_client(parameters):
        import urllib
        import re

        def register_client(server_addr, client_name, client_addr):

            res = None
            cont = "http://{0}:{1}/status?name={2}&address={3}&last_update=datetime.datetime.now()&last_load1=0.3&last_load5=0.4&last_load15=0.5&token=None".format(
                server_addr, 8080, client_name, client_addr)

            req = urllib.request.Request(url=cont, data=b"", method='POST')

            try:
                # nonlocal res
                res = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                print("{0}: Cannot reach the client: {1}".format(e.code, server_addr))

            return res.status

        # Check for number of parameters
        if len(parameters) == 0:
            return False

        if df.Services.get_string_client_alias() in parameters and \
           df.Services.get_string_client_addr() in parameters:
            client_name = parameters[df.Services.get_string_client_alias()].strip()
            client_addr = parameters[df.Services.get_string_client_addr()].strip()

            if len(client_name) == 0 or len(client_addr) == 0:
                return False

            # Check for ip address format
            pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
            if not pat.match(client_addr):
                return False

            # Register client
            # Client addr should be retrieved from Setting
            server_addr = "192.168.1.196"
            if register_client(server_addr, client_name, client_addr) == 200:
                return True

        return False

