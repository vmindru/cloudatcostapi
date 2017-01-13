#!/usr/bin/python
import sys
import json
import requests


class cloudatcost():
    def __init__(self, key, login):
        self.value = "init"
        self.cac_url = 'https://panel.cloudatcost.com'
        self.key = key
        self.login = login
        self.request_list = {
            "listservers": "/api/v1/listservers.php",
            "listtemplates": "/api/v1/listtemplates.php",
            "listtasks": "/api/v1/listtasks.php",
            "powerop": "/api/v1/powerop.php",
            "renameserver": "/api/v1/renameserver.php",
            "rdns": "/api/v1/rdns.php",
            "console": "/api/v1/console.php",
            "runmode": "/api/v1/runmode.php",
            "cloudpro-build": "/api/v1/cloudpro/build.php",
            "cloudpro-delete": "/api/v1/cloudpro/delete.php",
            "cloudpro-resources": "/api/v1/cloudpro/resources.php"}

    def _build_url(self):
        url = self.cac_url + self.request + "?" + "key=" + self.key + "&&" \
            "login=" + self.login
        return url

    def request(self, request):
        if request in self.request_list:
            self.request = self.request_list[request]
        else:
            print "Your request: {} is not valid check"\
                "docs at https://panel.cloudatcost.com/api-details.php"\
                .format(request)
            sys.exit(1)
        self.req = requests.get(self._build_url())
        return self.req

    def listservers(self):
        if self.req.ok is True:
            req_json = json.loads(self.req.text)
            if req_json["status"] == "ok":
                return json.dumps(req_json["data"], indent=4)

    def ansible_inventory(self):
        if self.req.ok is True:
            req_json = json.loads(self.req.text)
            hosts = []
            hostvars = {}
            if req_json["status"] == "ok":
                servers = req_json["data"]
                for server in servers:
                    hosts.append(server["ip"])
                    hostvars[server["ip"]] = server
            inventory = {"cloudatcost": {"hosts": hosts},
                         "_meta": {"hostvars": hostvars},
                         }
            return inventory
