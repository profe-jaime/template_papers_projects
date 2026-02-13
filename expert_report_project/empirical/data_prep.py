#!/usr/bin/env python3
"""Simple data prep script for recommended causal datasets.

This script attempts to download or locate common causal inference benchmark datasets
and write cleaned CSVs to ./data/.
"""
import os
import urllib.request
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

SOURCES = {
    "ihdp": "https://raw.githubusercontent.com/AMLab-amherst/ihdp/master/ihdp.csv",
    "lalonde": "https://raw.githubusercontent.com/rdiaz02/lalonde-data/master/lalonde.csv",
    "twins": "https://raw.githubusercontent.com/uber/causalml/master/examples/data/twins.csv",
}


def download(name, url):
    out = DATA_DIR / f"{name}.csv"
    if out.exists():
        print(f"{out} already exists")
        return
    try:
        print(f"Downloading {name} from {url}")
        urllib.request.urlretrieve(url, out)
        print(f"Saved to {out}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")


if __name__ == "__main__":
    for n, u in SOURCES.items():
        download(n, u)
    print("Done. Check ./data for CSVs. If a URL fails, add alternative source or local copy.")
