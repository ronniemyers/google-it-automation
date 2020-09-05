#!/usr/bin/env python3

import socket
import requests

def check_localhost():
  """checks whether the local host is correctly configured"""
  localhost = socket.gethostbyname('localhost')
  if localhost == "127.0.0.1":
    return True
  return False

def check_connectivity():
  """checks whether the computer can make successful calls to the internet"""
  request = requests.get("http://www.google.com")
  response = request.status_code

  if response == 200:
    return True
  return False

print(check_localhost())
print(check_connectivity())