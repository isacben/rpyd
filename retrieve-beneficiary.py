#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Retrieve Beneficiary")
parser.add_argument("token", help="the beneficiary token")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/payouts/beneficiary/{args.token}'

response = make_request(env=args.env, method='get', path=path)
    
if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"first_name: {response['data']['first_name']}\n" \
        f"last_name: {response['data']['last_name']}\n"
    print(s)
