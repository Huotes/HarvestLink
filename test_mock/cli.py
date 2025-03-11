# test_mock/cli.py
import click
import time
from device_scanner import NetworkScanner
from device_manager import DeviceController
from traffic_monitor import TrafficMonitor

def print_banner():
    click.clear()
    click.secho(r"""
    HarvestLink
    """, fg='green', bold=True)
    click.secho("\nSistema de Gerenciamento de Rede para Agronegócio", fg='yellow')
    click.secho("Versão 1.0 - Pumpkin Box\n", fg='blue')

def show_help_menu():
    print_banner()
    click.secho("COMANDOS PRINCIPAIS:", fg='cyan', underline=True)

    click.secho("\n[SCAN] - Varredura de Rede:", fg='green')
    click.echo("  scan        Listar dispositivos conectados na rede")

    click.secho("\n[MANAGE] - Gerenciamento:", fg='blue')
    click.echo("  block       Bloquear dispositivo por IP")
    click.echo("  unblock     Desbloquear dispositivo por IP")

    click.secho("\n[MONITOR] - Monitoramento:", fg='magenta')
    click.echo("  monitor     Monitorar tráfego de rede em tempo real")

    click.secho("\n[HELP] - Ajuda:", fg='yellow')
    click.echo("  help        Exibir este menu de ajuda")
    click.echo("  --help      Exibir ajuda detalhada de comandos")

    click.secho("\nExemplo de uso:", fg='white')
    click.echo("  sudo python cli.py scan")
    click.echo("  sudo python cli.py block 192.168.1.100\n")

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Sistema Inteligente de Conectividade Segura para o Agronegócio"""
    if ctx.invoked_subcommand is None:
        show_help_menu()

@cli.command()
def scan():
    """Varre a rede em busca de dispositivos conectados"""
    scanner = NetworkScanner()
    devices = scanner.scan_devices()

    click.secho("\nDISPOSITIVOS ENCONTRADOS:", fg='cyan')
    for device in devices:
        conn_color = 'yellow' if device['connection_type'] == 'Wi-Fi' else 'blue'
        click.echo(
                    f"IP: {click.style(device['ip'], fg='green')} | "
                    f"MAC: {device['mac']} | "
                    f"Tipo: {click.style(device['connection_type'], fg=conn_color)} | "
                    f"Fabricante: {click.style(device['manufacturer'], fg='blue')}"
                )

@cli.command()
@click.argument('ip')
def block(ip):
    """Bloqueia um dispositivo na rede"""
    controller = DeviceController()
    controller.block_device(ip)
    click.secho(f"\nDispositivo {click.style(ip, fg='red', bold=True)} bloqueado com sucesso!", blink=True)

@cli.command()
@click.argument('ip')
def unblock(ip):
    """Desbloqueia um dispositivo na rede"""
    controller = DeviceController()
    controller.unblock_device(ip)
    click.secho(f"\nDispositivo {click.style(ip, fg='green', bold=True)} desbloqueado!")

@cli.command()
@click.option('--interval', default=3, help='Intervalo de atualização em segundos')
def monitor(interval):
    """Monitora o tráfego de rede em tempo real"""
    monitor = TrafficMonitor()

    try:
        while True:
            stats = monitor.update_stats()
            print_banner()
            click.secho("MONITORAMENTO DE TRÁFEGO:", fg='cyan')

            for interface, data in stats.items():
                upload = data['upload'] / 1024
                download = data['download'] / 1024

                click.secho(f"\nInterface: {click.style(interface, fg='yellow')}", bold=True)
                click.echo(f"⬆ Upload: {click.style(f'{upload:.2f} KB', fg='green')}")
                click.echo(f"⬇ Download: {click.style(f'{download:.2f} KB', fg='red')}")

            click.secho(f"\nAtualizando em {interval}s... (CTRL+C para sair)", fg='white')
            time.sleep(interval)

    except KeyboardInterrupt:
        click.secho("\nMonitoramento encerrado!", fg='yellow')

@cli.command()
def help():
    """Exibe o menu de ajuda completo"""
    show_help_menu()

if __name__ == '__main__':
    cli()
