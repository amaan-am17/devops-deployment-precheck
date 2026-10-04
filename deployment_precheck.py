import sys
import os
import json
import requests

print("========================")
print("DEPLOYMENT PRE-CHECK")
print("========================")

environment = sys.argv[1]

with open("config.json") as config:
    data = json.load(config)

try:
    api_url = data[environment]["api_url"]
    config_ok = "VALID"
except KeyError:
    config_ok = "INVALID"

api_key = os.getenv("API_KEY")

if api_key is None:
    api_key_status = "MISSING"
else:
    api_key_status = "OK"

if config_ok == "VALID":
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        api_status = "HEALTHY"
    except requests.RequestException:
        api_status = "UNHEALTHY"
else:
    api_status = "UNHEALTHY"

if (
    config_ok == "VALID"
    and api_key is not None
    and api_status == "HEALTHY"
):
    overall_status = "READY"
else:
    overall_status = "NOT READY"

print("ENVIRONMENT:", environment)
print("CONFIG:", config_ok)
print("API KEY:", api_key_status)
print("API:", api_status)
print("OVERALL:", overall_status)

if overall_status == "READY":
    sys.exit(0)
else:
    sys.exit(1)