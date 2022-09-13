#!/usr/bin/env python3
from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="List Customers")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-l", "--limit", help="the maximum number of customers to return", dest='limit', default=10, type=int)

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
