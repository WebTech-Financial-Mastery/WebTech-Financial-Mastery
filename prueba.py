from scapy.all import ARP, Ether, srp

def scan_devices(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Ejemplo de uso:
ip_range = "00-16-EB-E6-B7-A7"  # Cambia esto por tu rango de IP local
devices = scan_devices(ip_range)

print("Dispositivos conectados a la red:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
