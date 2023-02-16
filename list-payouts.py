#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="List Payouts")
parser.add_argument("params", help="the url parameters between quotes, for example 'merchant_reference_id=780-456-67G'; params: beneficiary, created_after, created_before, ending_before, ewallet, invoice&limit, merchant_reference_id, payout_method_type, sender, sender_country, sender_currency, starting_after, subscription. See https://docs.rapyd.net/build-with-rapyd/reference/payout#list-payouts")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/payouts?{args.params}'

response = make_request(env=args.env, method='get', path=path)

if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

for r in response['data']:
    s = f"{r['id']}, {r['sender']['id'] if r['sender'] is not None else 'no_sender'}, {r['beneficiary']['id'] if r['beneficiary'] is not None else 'no_beneficiary'}, {r['sender_amount']}, {r['sender_currency']}, {r['status']}"
    print(s)
