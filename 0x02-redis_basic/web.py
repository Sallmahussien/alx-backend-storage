#!/usr/bin/env python3
"""Defines get_page function"""

import requests


def get_page(url: str) -> str:
    """"""
    return requests.get(url).text
