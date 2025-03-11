# test_mock/device_scanner.py
import subprocess
import re
import socket
import struct
import platform
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
import netifaces

class NetworkScanner:
    def __init__(self):
        self.oui_db = self._load_oui_database()
        self.interface = self._detect_primary_interface()
        self.network_info = self._get_network_info()

    def scan_devices(self) -> List[Dict]:
        """Varre a rede usando múltiplos métodos de descoberta"""
        devices = []
        seen_ips = set()

        # Método 1: Varredura ICMP
        icmp_devices = self._icmp_scan()
        devices.extend(icmp_devices)

        # Método 2: ARP Scan
        arp_devices = self._arp_scan()
        for device in arp_devices:
            if device['ip'] not in seen_ips:
                devices.append(device)
                seen_ips.add(device['ip'])

        # Método 3: Análise do ARP Cache
        arp_cache_devices = self._arp_cache_scan()
        for device in arp_cache_devices:
            if device['ip'] not in seen_ips:
                devices.append(device)
                seen_ips.add(device['ip'])

        return devices

    def _get_network_info(self) -> Dict:
        """Obtém informações da rede primária"""
        try:
            netmask = netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['netmask']
            cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
            return {
                'subnet': self._calculate_subnet(),
                'cidr': cidr,
                'gateway': netifaces.gateways()['default'][netifaces.AF_INET][0]
            }
        except Exception as e:
            print(f"Erro ao obter informações de rede: {e}")
            return {}

    def _calculate_subnet(self) -> str:
        """Calcula a sub-rede completa para varredura"""
        ip = netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['addr']
        netmask = netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['netmask']
        network = socket.inet_ntoa(
            struct.pack('!I', struct.unpack('!I', socket.inet_aton(ip))[0] &
            struct.unpack('!I', socket.inet_aton(netmask))[0])
        )
        return f"{network}/{self.network_info['cidr']}"

    def _icmp_scan(self) -> List[Dict]:
        """Varredura ICMP usando threads"""
        devices = []
        ip_list = [f"{self.network_info['subnet'].split('.')[0]}.{self.network_info['subnet'].split('.')[1]}.{self.network_info['subnet'].split('.')[2]}.{i}" 
                  for i in range(1, 255)]

        with ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(self._ping_host, ip_list)
            for result in results:
                if result:
                    devices.append(result)
        return devices

    def _ping_host(self, ip: str) -> Dict:
        """Envia ping para um host específico"""
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', '-W', '1', ip]
            if subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                return self._resolve_device_info(ip)
        except Exception:
            pass
        return None

    def _resolve_device_info(self, ip: str) -> Dict:
        """Resolve informações do dispositivo usando múltiplos métodos"""
        mac = self._get_mac_from_arp(ip)
        return {
            'ip': ip,
            'mac': mac or 'Desconhecido',
            'manufacturer': self._get_manufacturer(mac),
            'connection_type': self._determine_connection_type(ip)
        }

    def _get_mac_from_arp(self, ip: str) -> str:
        """Obtém MAC do cache ARP"""
        try:
            output = subprocess.check_output(["arp", "-n", ip], text=True)
            match = re.search(r"(([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2})", output)
            return match.group(0).lower() if match else None
        except Exception:
            return None

    def _determine_connection_type(self, ip: str) -> str:
        """Determina o tipo de conexão usando TTL e análise de rede"""
        try:
            ttl = self._get_ttl(ip)
            if 64 <= ttl <= 128:  # TTL típico para dispositivos Linux/Windows
                return "Ethernet/Cabo"
            elif ttl <= 64:  # TTL comum em dispositivos IoT/embarcados
                return "Wi-Fi"
        except Exception:
            pass
        return "Desconhecido"

    def _get_ttl(self, ip: str) -> int:
        """Obtém TTL através de traceroute"""
        try:
            result = subprocess.check_output(
                ["traceroute", "-m", "1", ip],
                stderr=subprocess.DEVNULL,
                text=True
            )
            match = re.search(r"\((\d+)\)", result)
            return int(match.group(1)) if match else 0
        except Exception:
            return 0

    def _load_oui_database(self) -> Dict:
        """Carrega banco de dados de fabricantes"""
        oui_db = {}
        try:
            with open('/usr/share/ieee-data/oui.txt', 'r') as f:
                for line in f:
                    if "(base 16)" in line:
                        parts = line.split()
                        oui_db[parts[0].replace('-', ':').lower()] = ' '.join(parts[3:])
        except FileNotFoundError:
            print("Banco de dados OUI não encontrado")
        return oui_db

    def _get_manufacturer(self, mac: str) -> str:
        """Identifica fabricante pelo OUI"""
        if mac and len(mac) >= 8:
            oui = mac[:8].lower()
            return self.oui_db.get(oui, "Desconhecido")
        return "Desconhecido"

    def _detect_primary_interface(self) -> str:
        """Detecta a interface de rede ativa"""
        try:
            gateways = netifaces.gateways()
            return gateways['default'][netifaces.AF_INET][1]
        except Exception:
            return 'eth0'
