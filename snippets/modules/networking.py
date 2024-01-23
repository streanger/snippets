import ipaddress
from scapy.all import *


def ipv4_is_private(ip):
    """checks if the string is a private IPv4 address"""
    return ipaddress.IPv4Address(ip).is_private


def validate_ipv4(ip):
    """checks if the string is a valid IPv4 address"""
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False


def dhcp_sniffer(timeout=10):
    """scapy dhcp packets sniffer

    from scapy.all import *
    """
    def parse_dhcp_packet(packet):
        dhcp_info = {
            'chaddr': packet[Ether].src,
            'giaddr': packet[Ether].dst,
            'message-type': None,
            'requested_addr': None,
            'hostname': None
        }
        fields = {'message-type', 'requested_addr', 'hostname'}
        for option in packet[DHCP].options:
            if (option == 'end'):
                continue
            name, value, *_ = option
            if name in fields:
                dhcp_info[name] = value
        return dhcp_info

    # sniff
    dhcp_filter = "udp and (port 67 or port 68)"
    print(f'[*] scapy dhcp sniffer working')
    print(f'[*] sniff filter: {dhcp_filter}')
    print(f'[*] sniff timeout: {timeout}')
    packets = sniff(filter=dhcp_filter, timeout=timeout)
    parsed_packets = [parse_dhcp_packet(packet) for packet in packets]
    return parsed_packets


def send_fake_dhcp():
    """simulate dhcp requests

    from scapy.all import *
    """
    conf.checkIPaddr = False
    fam,hw = get_if_raw_hwaddr(conf.iface)
    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/ \
                   IP(src="0.0.0.0", dst="255.255.255.255")/ \
                   UDP(sport=68, dport=67)/ \
                   BOOTP(chaddr=hw)/ \
                   DHCP(options=[("message-type","discover"), "end"])
    sendp(dhcp_discover, iface=conf.iface)


if __name__ == "__main__":
    print(f'{validate_ipv4("192.168.0.1")=}')
    print(f'{validate_ipv4("255.255.255.255")=}')
    print(f'{validate_ipv4("192.168.0.256")=}')
    print(f'{validate_ipv4("123.45")=}')
    print()
    print(f'{ipv4_is_private("192.168.0.1")=}')
    print(f'{ipv4_is_private("10.0.0.1")=}')
    print(f'{ipv4_is_private("172.16.0.1")=}')
    print(f'{ipv4_is_private("8.8.8.8")=}')
    print(f'{ipv4_is_private("114.114.114.114")=}')
