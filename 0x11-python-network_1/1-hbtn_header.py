#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""

import sys
import urllib.request


def get_request_id(url):
    """ the get request_id method"""

    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.headers.get('X-Request-Id')
            if request_id:
                return request_id
            else:
                print("X-Request-Id not found in the response headers.")
                return None
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        request_id = get_request_id(url)
        if request_id:
            print(f"{request_id}")
