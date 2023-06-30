#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
-You must use the packages requests and sys
-You are not allow to import other packages than requests and sys
"""

import requests
import sys


def get_x_request_id(url):
    '''get request id.'''
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print(f"{x_request_id}")
        else:
            print("X-Request-Id not found in the response header.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
