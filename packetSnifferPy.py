from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Print a summary of the captured packet

if __name__ == "__main__":
    print("Starting packet sniffer for TCP traffic on port 80...")
    sniff(prn=packet_callback, store=False, filter="tcp port 80")  # Sniff only TCP packets on port 80
