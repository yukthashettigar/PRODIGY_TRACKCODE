import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.http import HTTP
from colorama import init, Fore
from scapy.all import conf
conf.use_pcap = True


# Initialize colorama
init()

# Define colors
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

# Function to analyze packets
def packet_sniffer(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Print IP information
        print(f"{GREEN}Source IP: {src_ip}{RESET}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")

        # Analyze protocol-specific information
        if protocol == 6:  # TCP
            tcp_layer = packet[TCP]
            src_port = tcp_layer.sport
            dst_port = tcp_layer.dport
            print(f"Source Port: {src_port}")
            print(f"Destination Port: {dst_port}")
             # Check for HTTP layer
            if packet.haslayer(HTTP):
                http_layer = packet[HTTP]
                print(f"HTTP Request: {http_layer.path}")
                print(f"HTTP Method: {http_layer.method}")
                print(f"HTTP Response Status Code: {http_layer.status}")

        elif protocol == 17:  # UDP
            udp_layer = packet[UDP]
            src_port = udp_layer.sport
            dst_port = udp_layer.dport
            print(f"Source Port: {src_port}")
            print(f"Destination Port: {dst_port}")

        elif protocol == 1:  # ICMP
            icmp_layer = packet[ICMP]
            print(f"ICMP Type: {icmp_layer.type}")
            print(f"ICMP Code: {icmp_layer.code}")

        # Print payload
        print(f"Payload: {packet[IP].payload}")
        print("------------------------")

# Start sniffing packets
scapy.sniff(prn=packet_sniffer, count=100)


