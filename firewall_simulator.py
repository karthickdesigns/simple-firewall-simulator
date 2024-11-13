import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define blocked ports (you can customize these)
BLOCKED_PORTS = [80, 443, 22]

def packet_filter(ip, port):
    """Simulate a firewall that blocks certain ports."""
    if port in BLOCKED_PORTS:
        logging.warning(f"Blocked packet to {ip}:{port}")
        return f"Packet to {ip}:{port} BLOCKED"

    logging.info(f"Allowed packet from {ip}:{port}")
    return f"Packet from {ip}:{port} ALLOWED"

def read_packet():
    """Simulate reading an incoming packet."""
    ip = input("Enter source IP address: ")
    port = int(input("Enter destination port: "))
    result = packet_filter(ip, port)
    print(result)

if __name__ == "__main__":
    print("Welcome to the Simple Firewall Simulator!")
    while True:
        read_packet()

