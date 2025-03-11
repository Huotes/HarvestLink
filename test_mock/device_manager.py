import subprocess

class DeviceController:
    def block_device(self, ip: str):
        """Bloqueia dispositivo usando iptables"""
        subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        print(f"Dispositivo {ip} bloqueado com sucesso")

    def unblock_device(self, ip: str):
        """Desbloqueia dispositivo"""
        subprocess.run(
            ["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        print(f"Dispositivo {ip} desbloqueado")
