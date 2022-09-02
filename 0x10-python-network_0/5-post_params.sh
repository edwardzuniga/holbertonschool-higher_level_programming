#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the re
curl -sX POST "$1" -d "email=test@gmail.com.com&subject=I will always be here for PLD"
