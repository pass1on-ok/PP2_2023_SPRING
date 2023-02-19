import json


with open('sample-data.json', 'r') as f:
    data = json.load(f)


print("Interface Status")
print("="*80)
print("{:<50} {:<25} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)


for intf in data['imdata']:
    dn = intf['l1PhysIf']['attributes']['dn']
    descr = intf['l1PhysIf']['attributes']['descr']
    speed = intf['l1PhysIf']['attributes']['speed']
    mtu = intf['l1PhysIf']['attributes']['mtu']
    print("{:<50} {:<25} {:<8} {:<6}".format(dn, descr, speed, mtu))
