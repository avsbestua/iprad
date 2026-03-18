import click
import shutil
from iprad.core.ipinfo_client import IPinfoClient
from iprad.core.whois_client import WhoIsClient

@click.group(invoke_without_command=True)
@click.pass_context

def main(ctx) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.argument('ip', required=True)
def check(ip: str) -> None:
    client_ipinfo = IPinfoClient()
    client_ipinfo.check_ip(ip)

    client_whois = WhoIsClient()
    client_whois.check_ip(ip)

    


@main.command()
def rmcache() -> None:
    from iprad.utils.cache import CACHE
    from rich.console import Console

    #Checking if cache exist
    console = Console()
    if CACHE.exists():
        try:
            shutil.rmtree(CACHE)

            console.print(">[bold green] Cache removed successfully")

        except Exception as e:
            console.print(f">[bold red] Cache wasn`t removed due {e}")
    else:
        console.print(f">[bold purple] There aren`t any cache files! ")