#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Payout")
parser.add_argument("token", help="the payout token")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/payouts/{args.token}'

response = make_request(env=args.env, method='get', path=path)
    
if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"amount: {response['data']['original_amount']}\n" \
        f"currency: {response['data']['currency_code']}\n" \
        f"status: {response['data']['status']}"
    print(s)
