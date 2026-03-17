import requests
import json
import time
from iprad.utils.functions import get_flag
from rich.console import Console
from rich.panel import Panel

#IPinfo module
class IPinfoClient:
    BASE_URL = "https://ipinfo.io/"

    def check_ip(self, ip: str):
        url = f"{self.BASE_URL}/{ip}/json"
        
        console = Console()
        console.clear()

        #Fetching data from ipinfo.io
        with console.status("[bold green]Fetching and processing Data...") as status:
            try:
                # response = requests.get(url)
                # response.raise_for_status()

                # data = response.json()

                with open('data.json', 'r') as file:
                    data = json.load(file)
                
                info = (
                    f"[bold green]IP:[/] {data.get('ip')}\n"
                    f"[bold green]Hostname:[/] {data.get('hostname')}\n\n"
                    f"[bold cyan]City:[/] {data.get('city')}\n"
                    f"[bold cyan]Region:[/] {data.get('region')}\n"
                    f"[bold cyan]Country:[/] {data.get('country')} {get_flag(data.get('country'))}\n\n"
                    f"[bold yellow]Provider:[/] {data.get('org')}\n"
                    f"[bold yellow]Timezone:[/] {data.get('timezone')}\n"
                )

            except requests.exceptions.HTTPError as e:
                console.print(f"[bold red]HTTP ERROR![/] Failed to fetch data. Status: {response.status_code}")
            except requests.exceptions.ConnectionError:
                console.print("[bold red]CONNECTION ERROR![/] Check internet connection")

        console.print(Panel(info, title=f"[bold cyan]IPInfo Report for {data.get('ip')}"))