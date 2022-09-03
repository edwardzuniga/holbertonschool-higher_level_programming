#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response with Requests library
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
