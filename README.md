# cloudatcost API python wrapper and command line tool

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
## Help message 
```
[vmindru@vmutil cloudatcostapi]$ cloudatcost help
powerop: Activate server power operations, sid = SERVERID, action = [poweron, poweroff, reset]

renameserver: Rename server, name = NAME, sid = SERVERID

listtemplates: List all available templates

rdns: Modify reverse dns (ptr),sid = SERVERID, hostname = HOSTNAME

console: Returns request URL for console, sid = SERVERID

cloudpro-build: Request new server build,cpu = [1,2,3,4,5..16],ram = 1024,storage = [10,20,30..1000],os=templateid

listtasks: List running tasks

listservers: List all available servers

runmode: Change run mode, sid = SERVERID,mode=[normal,safe]

cloudpro-resources: List cloudpro-resources

cloudpro-delete: Request server deletion, sid = SERVERID

[vmindru@vmutil cloudatcostapi]$ 
```


## CLI

use cloudatcost-cli.py ,you can copy this into /usr/bin/cloudatcost 
```
cloudatcost help
```

## Ansible dynamic inventory 

cloudatcost-api will return all your servers in Ansible dynamic inventory format

```
cloudatcost-api
```

## To Do

* refactor var names, some of them might be misleading atm
* add verbose output

## Installation

clone this repo, and copy cloudatcost.py into your PYTHON path, e.g. /usr/lib/python2.7/site-packages/ 

## Demo !! 
![](/examples/example.gif)

##Donate 
https://www.paypal.me/vmindru
