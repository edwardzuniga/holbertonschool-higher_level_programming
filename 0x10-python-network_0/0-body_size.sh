#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size
curl -si "$1" | grep -i Content-Length | cut -d " " -f2