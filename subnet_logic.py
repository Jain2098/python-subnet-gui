import ipaddress


def validate_ip_and_subnet(ip_input, subnet_input):
    try:
        # Handle subnet input
        if '/' in subnet_input:
            subnet = subnet_input.strip('/')
        else:
            # Convert dotted decimal to CIDR
            subnet = ipaddress.IPv4Network(f"0.0.0.0/{subnet_input}").prefixlen
        # Validate IP address and subnet
        ip_interface = ipaddress.IPv4Interface(f"{ip_input}/{subnet}")
        print(ip_interface)
        return ip_interface
    except ValueError as e:
        raise ValueError(str(e))


def calculate_network_address(ip_interface):
    return ip_interface.network.network_address


def calculate_broadcast_address(ip_interface):
    return ip_interface.network.broadcast_address


def calculate_host_range(ip_interface):
    hosts = list(ip_interface.network.hosts())
    if hosts:
        first_host = hosts[0]
        last_host = hosts[-1]
        return first_host, last_host
    else:
        return None, None


def get_subnet_mask(ip_interface):
    return ip_interface.network.netmask


def get_wildcard_mask(ip_interface):
    netmask = ip_interface.network.netmask
    wildcard_mask = ipaddress.IPv4Address(int(netmask) ^ 0xFFFFFFFF)
    return wildcard_mask


def get_cidr_notation(ip_interface):
    return ip_interface.network.prefixlen


def get_total_ips(ip_interface):
    return ip_interface.network.num_addresses


def calculate_usable_hosts(ip_interface):
    num_addresses = ip_interface.network.num_addresses
    if num_addresses >= 2:
        return num_addresses - 2  # Exclude network and broadcast addresses
    elif num_addresses == 1:
        return 1  # Only one address available
    else:
        return 0


def get_ip_class(ip_address):
    first_octet = int(str(ip_address).split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 254:
        return 'E'
    else:
        return 'Unknown'


def ip_to_binary(ip_address):
    return '.'.join(f'{int(octet):08b}' for octet in str(ip_address).split('.'))
