#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="List Payout Methods Types")
parser.add_argument("params", help="the url parameters between quotes, for example 'payout_currency=usd&limit=2'; params: category, sender_country, sender_currency, sender_entity_type, beneficiary_country, payout_currency, beneficiary_entity_type, is_cancelable, is_location_specific, is_expirable, starting_after, ending_before, limit")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")
parser.add_argument("-f", "--filter", help="filters the payment method type category", dest="filter", default="", type=str)

args = parser.parse_args()

path = f'/v1/payouts/supported_types?{args.params}'

response = make_request(env=args.env, method='get', path=path)

if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

for r in response['data']:
    if args.filter == '' or args.filter in r['category']:
        s = f"{r['payout_method_type']}, " \
            f"{r['name']}, " \
            f"{r['category']}, " \
            f"{r['beneficiary_country']}, " \
            f"payout curr: {r['payout_currencies']}, " \
            f"sender curr: {r['sender_currencies']}"
       
        print(s)
