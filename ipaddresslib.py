import ipaddress

net = ipaddress.IPv4Network('192.168.1.0/24')
net_list = list(net)

print(net)

print(net.overlaps(ipaddress.IPv4Network('192.168.1.0/30')))

print(ipaddress.ip_address('8.8.8.8').reverse_pointer)