import ipaddress

VLAN = '3512'
WL = '036808'
SubnetIP = ipaddress.ip_address('10.255.12.72') + 254
print(SubnetIP)

# Q : au démarrage du script, p WL et SubnetIP