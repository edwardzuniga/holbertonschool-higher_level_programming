#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
'''
import urllib.request
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    with urllib.request.urlopen(argument) as response:
        print(response.headers['X-Request-Id'])
