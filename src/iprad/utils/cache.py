import os
import json
import requests
from pathlib import Path
from iprad.utils.functions import get_flag

CACHE = Path(__file__).parent.parent.parent / '.cache'

def fetch(url: str, console):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        return data
        
    except requests.exceptions.HTTPError as e:
            console.print(f"[bold red]HTTP ERROR![/] Failed to fetch data. Status: {response.status_code}")
    except requests.exceptions.ConnectionError:
            console.print("[bold red]CONNECTION ERROR![/] Check internet connection")
    



def cache_processing(module_name: str, identifier: str, url: str, console):
    
    cache_file = CACHE / module_name / f"{identifier}.json"
    module_dir = CACHE / module_name

    from_cache = False

    if cache_file.exists():
        with open(cache_file, 'r') as f:
            from_cache = True
            return json.load(f), from_cache

        
    data = fetch(url, console)

    #Writing data to cache
    if data:
        module_dir.mkdir(parents=True, exist_ok=True)
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    else:
        console.print("[bold red]DATA PROCESSING ERROR![/]")

    return data, from_cache
                
