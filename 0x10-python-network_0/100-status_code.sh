#!/bin/bash
# a script to display status code of server
curl -sLX HEAD -w "%{http_code}" "$1"
