import click
from iprad.core.ipinfo_client import IPinfoClient

@click.command()
@click.argument('ip')
def main():
    client = IPinfoClient()

    client.check_ip("1.1.1.1")