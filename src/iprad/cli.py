import click
import shutil
from iprad.core.ipinfo_client import IPinfoClient

@click.group(invoke_without_command=True)
@click.pass_context

def main(ctx):
    if ctx.invoked_subcommand is None:
        # Тут можна або показувати help, або зробити дефолтну перевірку свого IP
        click.echo(ctx.get_help())


@main.command()
@click.argument('ip', required=True)
def check(ip: str):
    client = IPinfoClient()
    client.check_ip(ip)


@main.command()
def rmcache():
    from iprad.utils.cache import CACHE
    from rich import print as rprint

    if CACHE.exists():
        try:
            shutil.rmtree(CACHE)

            rprint(">[bold green] Cache removed successfully")

        except Exception as e:
            rprint(f">[bold red] Cache wasn`t removed due {e}")
    else:
        rprint(f">[bold purple] There aren`t any cache files! ")