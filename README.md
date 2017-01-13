# cloudatcost API python wrapper

This module allows you to perform all API actions documented in
https://panel.cloudatcost.com/api-details.php.

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
    cl.request("listservers",['sid=123123123','name=test'])
    print cl.response()
```
## Return Ansible dynamic inventory
http://docs.ansible.com/ansible/intro_dynamic_inventory.html
```
    cl = cloudatcost(key, login)
    cl.request("listservers",['sid=123123123','name=test'])
    print cl.ansible_inventory()
```

## To Do

* refactor var names, some of them might be misleading atm
* add verbose output

## Demo !! 
![](/examples/example.gif)
