#!/bin/bash
# takes in a URL, sends a request it, displays the size of the body of response
curl -Is "$1" | grep "Content-Length" | cut -d "" -f2
