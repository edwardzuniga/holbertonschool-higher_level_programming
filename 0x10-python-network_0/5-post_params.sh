#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the re
curl -s "$1"-X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
