# cloudatcost API python wrapper

This module allows you to perform cloudatcost API calls.

Cloudt At Cost: https://panel.cloudatcost.com/api-details.php.

## Example:
List all servers
```
    cl = cloudatcost(key, login)
    cl.request("listservers")
    print cl.response()
```
## Rename server
```
    cl = cloudatcost(key, login)
    cl.request("renameserver",['sid=123123123','name=test'])
    print cl.response()
```
## Return Ansible dynamic inventory
http://docs.ansible.com/ansible/intro_dynamic_inventory.html
```
    cl = cloudatcost(key, login)
    cl.request("listservers")
    print cl.ansible_inventory()
```

## To Do

* refactor var names, some of them might be misleading atm
* add verbose output

## Installation

clone this repo, and copy cloudatcost.py into your PYTHON path, e.g. /usr/lib/python2.7/site-packages/ 

## Demo !! 
![](/examples/example.gif)
