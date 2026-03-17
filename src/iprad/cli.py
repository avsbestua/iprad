import click
from iprad.core.ipinfo_client import IPinfoClient

@click.command()
@click.argument('ip')
def main(ip: str):
    client = IPinfoClient()

    client.check_ip(ip)