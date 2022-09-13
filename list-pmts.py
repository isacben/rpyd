#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="List Payment Methods By Country")
parser.add_argument("params", help="the url parameters between quotes, for example 'country=US&currency=USD'")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")
parser.add_argument("-f", "--filter", help="filters the payment method type category", dest="filter", default="", type=str)

args = parser.parse_args()

path = f'/v1/payment_methods/country?{args.params}'

response = make_request(env=args.env, method='get', path=path)

if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

for r in response['data']:
    if args.filter == '' or args.filter in r['category']:
        s = f"{r['type']}, " \
            f"{r['category']}, " \
            f"{r['country']}, " \
            f"{r['currencies']}, "
       
        print(s)
