# ipcidr = '192.168.100.1/24'
# ipaddr = ipcidr.split('/')[0]
# cidr = int(ipcidr.split('/')[1])
# print(ipaddr, cidr)

# ipaddr_list_str = ipaddr.split('.')
# print(ipaddr_list_str)

# ipaddr_list_int = [int(i) for i in ipaddr_list_str]
# print(ipaddr_list_int)

# ipaddr_list_bin = [(bin(i)[2:]).zfill(8) for i in ipaddr_list_int]
# print(ipaddr_list_bin)


# netmask32 = ''.join(['1' if i < cidr else '0' for i in range(32)])
# print(netmask32)

# netmask1 = netmask32[0:8]
# netmask2 = netmask32[8:16]
# netmask3 = netmask32[16:24]
# netmask4 = netmask32[24:32]
# print(netmask1, netmask2, netmask3, netmask4)

# netmask_list_str = [netmask32[i:i + 8] for i in range(0, 32, 8)]
# print(netmask_list_str)
# netmask_list_int = [str(int(i, 2)) for i in netmask_list_str]
# print(netmask_list_int)
# netmask = '.'.join(netmask_list_int)
# print(netmask)


def get_netmask(cidr):
    netmask32 = ''.join(['1' if i < cidr else '0' for i in range(32)])
    netmask_list_bin = [netmask32[i:i + 8] for i in range(0, 32, 8)]
    netmask_list_int = [str(int(i, 2)) for i in netmask_list_bin]
    return '.'.join(netmask_list_int)


# for i in range(33):
#     print('/'+str(i), ' ', get_netmask(i))

# print(get_netmask(24))

# def subnet_calc_class_c(ipcidr):
#     ipaddr = ipcidr.split('/')[0]
#     ipaddr4 = (int(ipaddr.split('.')[3]))
#     cidr = int(ipcidr.split('/')[1])
#
#     netmask32 = ''.join(['1' if i < cidr else '0' for i in range(32)])  # ex. 11111111111111111111111100000000
#     netmask_list_bin = [netmask32[i:i + 8] for i in range(0, 32, 8)]
#     # ex. ['11111111', '11111111', '11111111', '00000000']
#     netmask_list_intstr = [str(int(i, 2)) for i in netmask_list_bin]  # ex. ['255', '255', '255', '0']
#     subnet_mask = '.'.join(netmask_list_intstr)
#     netmask_list_int = [int(i) for i in netmask_list_intstr]  # ex. [255, 255, 255, 0]
#     no_of_addr_per_subnet = 256 - netmask_list_int[3]
#
#     ipstart = int(ipaddr4 / no_of_addr_per_subnet) * no_of_addr_per_subnet + 1
#     ipend = ipstart + no_of_addr_per_subnet - 3
#     ipaddr3 = '.'.join(ipaddr.split('.')[:3])
#     host_ipstart = ipaddr3 + '.' + str(ipstart)
#     host_ipend = ipaddr3 + '.' + str(ipend)
#     subnet_ip = ipaddr3 + '.' + str(ipstart - 1)
#     broadcast_ip = ipaddr3 + '.' + str(ipend + 1)
#     return subnet_mask, host_ipstart, host_ipend, subnet_ip, broadcast_ip


def subnet_calc_class_c(ipcidr):
    ipaddr = ipcidr.split('/')[0]
    ipaddr4 = (int(ipaddr.split('.')[3]))  # last octet of ip address
    cidr = int(ipcidr.split('/')[1])  # the value after / in cidr notation

    netmask32 = ''.join(['1' if i < cidr else '0' for i in range(32)])  # ex. 11111111111111111111111100000000
    netmask_list_bin = [netmask32[i:i + 8] for i in range(0, 32, 8)]
    # ex. ['11111111', '11111111', '11111111', '00000000']
    netmask_list_int = [int(i, 2) for i in netmask_list_bin]  # ex. [255, 255, 255, 0]
    subnet_mask = '.'.join([str(i) for i in netmask_list_int])  # ex. ['255.255.255.0']
    no_of_addr_per_subnet = 256 - netmask_list_int[3]

    ipstart = int(ipaddr4 / no_of_addr_per_subnet) * no_of_addr_per_subnet + 1
    ipend = ipstart + no_of_addr_per_subnet - 3
    ipaddr3 = '.'.join(ipaddr.split('.')[:3])  # first 3 octet of ip address ex. '192.168.100'
    host_ipstart = ipaddr3 + '.' + str(ipstart)
    host_ipend = ipaddr3 + '.' + str(ipend)
    subnet_ip = ipaddr3 + '.' + str(ipstart - 1)
    broadcast_ip = ipaddr3 + '.' + str(ipend + 1)
    return subnet_mask, host_ipstart, host_ipend, subnet_ip, broadcast_ip


def subnet_calc_class_c1(ipcidr):
    ipaddr_str = ipcidr.split('/')[0]
    ipaddr = [int(i) for i in ipaddr_str.split('.')]  # ex. [192, 168, 129, 130]

    cidr = int(ipcidr.split('/')[1])  # the value after / in cidr notation
    netmask32 = ''.join(['1' if i < cidr else '0' for i in range(32)])  # ex. 11111111111111111111111100000000
    netmask_list_bin = [netmask32[i:i + 8] for i in range(0, 32, 8)]
    # ex. ['11111111', '11111111', '11111111', '00000000']
    netmask = [int(i, 2) for i in netmask_list_bin]  # ex. [255, 255, 255, 0]

    subnet_ip = [ipaddr[i] & netmask[i] for i in range(4)]
    broadcast_ip = subnet_ip[0:3] + [subnet_ip[3] + 255 - netmask[3]]
    host_ipstart = subnet_ip[0:3] + [subnet_ip[3] + 1]
    host_ipend = broadcast_ip[0:3] + [broadcast_ip[3]-1]

    return '.'.join([str(i) for i in netmask]),\
           '.'.join([str(i) for i in host_ipstart]),\
           '.'.join([str(i) for i in host_ipend]),\
           '.'.join([str(i) for i in subnet_ip]),\
           '.'.join([str(i) for i in broadcast_ip])


sb, h1, h2, s, b = subnet_calc_class_c1('192.168.129.0/24')
print('Subnet Mask           : ' + sb)
print('Host address range    : ' + h1 + ' - ' + h2)
print('Subnet IP address     : ' + s)
print('Broadcast IP address  : ' + b)
