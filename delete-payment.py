#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Delete Payment")
parser.add_argument("token", help="the payment token")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/payments/{args.token}'

response = make_request(env=args.env, method='delete', path=path)
    
if args.all:
    print(json.dumps(response, indent=4))
else:
    s = f"token: {response['data']['id']}\n" \
        f"amount: {response['data']['original_amount']}\n" \
        f"currency: {response['data']['currency_code']}\n" \
        f"status: {response['data']['status']}\n" \
        f"textual_codes: {response['data']['textual_codes']}\n" \
        f"redirect_url: {response['data']['redirect_url']}"
    print(s)
