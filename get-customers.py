#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Customers")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-l", "--limit", help="the maximum number of customers to return", dest='limit', default=10, type=int)
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/customers?limit={args.limit}'

response = make_request(env=args.env, method='get', path=path)
    
for r in response['data']:
    s = f"{r['id']}, " \
        f"{r['name']}, " \
        f"{r['email']}, " \
        f"{r['phone_number']}, " \
        f"{r['ewallet']}"

    print(s)
