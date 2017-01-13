#!/usr/bin/python
import sys
import json
import requests


class cloudatcost():
    """cloudatcost API python wrapper

    This module allows you to perform all API actions documented in
    https://panel.cloudatcost.com/api-details.php.

    Example:
    List all servers
    ```
        cl = cloudatcost(key, login)
        cl.request("listservers")
        print cl.response()
    ```
    Rename server
    ```
        cl = cloudatcost(key, login)
        cl.request("listservers",['sid=123123123','name=test'])
        print cl.response()
    ```
    Return Ansible dynamic inventory
    http://docs.ansible.com/ansible/intro_dynamic_inventory.html
    ```
        cl = cloudatcost(key, login)
        cl.request("listservers",['sid=123123123','name=test'])
        print cl.ansible_inventory()
    ```

    To Do

    refactor var names, some of them might be misleading atm
    """
    def __init__(self, key, login):
        self.value = "init"
        self.cloud_at_cost_url = 'https://panel.cloudatcost.com'
        self.key = key
        self.login = login
        self.request_get_list = {
            "listservers": "/api/v1/listservers.php",
            "listtemplates": "/api/v1/listtemplates.php",
            "listtasks": "/api/v1/listtasks.php",
            "cloudpro-resources": "/api/v1/cloudpro/resources.php"}

        self.request_post_list = {
            "powerop": "/api/v1/powerop.php",
            "renameserver": "/api/v1/renameserver.php",
            "rdns": "/api/v1/rdns.php",
            "console": "/api/v1/console.php",
            "runmode": "/api/v1/runmode.php",
            "cloudpro-build": "/api/v1/cloudpro/build.php",
            "cloudpro-delete": "/api/v1/cloudpro/delete.php", }

    def _build_params(self):
        """_build_params
           private function, called by request() to get request params
        """
        data = {}
        for param in self.params:
            param = param.split('=', 1)
            data[param[0]] = param[1:]
        url = self.cloud_at_cost_url + self.request_uri
        data['key'] = self.key
        data['login'] = self.login
        return url, data

    def request(self, request, params=[]):
        """ request
            build and perform the actual request, the result is returned
            as self.req
        """
        self.params = params
        self.request = request
        if request in self.request_get_list:
            self.request_uri = self.request_get_list[request]
            self.request_type = "get"
        elif request in self.request_post_list:
            self.request_uri = self.request_post_list[request]
            self.request_type = "post"
        else:
            print "Your request: {} is not valid check"\
                "docs at https://panel.cloudatcost.com/api-details.php"\
                .format(request)
            sys.exit(1)
        url, request_data = self._build_params()
        print request_data
        if self.request_type == "get":
            self.req = requests.get(url, params=request_data)
        elif self.request_type == "post":
            self.req = requests.post(url, data=request_data)
        else:
            print "Ups something gone wrong, invalid request type {}"\
                .format(self.request_type)
            sys.exit(1)
        return self.req

    def response(self):
        """ response
            print the response from request()
        """
        if self.req.ok is True:
            # print self.req.text
            print self.req.url
            req_json = json.loads(self.req.text)
            if req_json["status"] == "ok":
                # print json.dumps(req_json, indent=4)
                if self.request_type == "post":
                    return json.dumps(req_json, indent=4)
                elif self.request_type == "get":
                    return json.dumps(req_json["data"], indent=4)
                else:
                    print "Ups something gone wrong, invalid request type {}"\
                        .format(self.request_type)
                    sys.exit(1)
        else:
            print "the request {} failed, status: {}, message: {}"\
                .format(self.req.url,
                        self.req.status_code,
                        self.req.text)

    def ansible_inventory(self):
        """ return server list in ansible dynamic inventory format
        """
        hosts = []
        hostvars = {}
        inventory = {}
        if self.req.ok is True:
            req_json = json.loads(self.req.text)
            if req_json["status"] == "ok":
                servers = req_json["data"]
                for server in servers:
                    hosts.append(server["ip"])
                    hostvars[server["ip"]] = server
            inventory = {"cloudatcost": {"hosts": hosts},
                         "_meta": {"hostvars": hostvars},
                         }
        return inventory
