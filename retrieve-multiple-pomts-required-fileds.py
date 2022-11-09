#!/usr/bin/env python3

from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Multiple Payout Methods Required Fields")
parser.add_argument("filename", help="the file containing the list of POMTs")
parser.add_argument("env", help="the rapyd environment")

args = parser.parse_args()

f = open(f'{args.filename}', 'r')
pomts = f.read().splitlines()
f.close()

for pomt in pomts:
    params = f'{pomt}/details?sender_country=MX&sender_currency=MXN&beneficiary_country=MX&payout_currency=MXN&sender_entity_type=company&beneficiary_entity_type=company&payout_amount=1000'

    path = f'/v1/payouts/{params}'
    response = make_request(env=args.env, method='get', path=path)

    print(f"{pomt},headers,,{response['data']['batch_file_header']}")
    for r in response['data']['beneficiary_required_fields']:
        print(f"{pomt},beneficiary,{r['name']},{r['type']},{r['is_required']},{r['regex']}")

    for r in response['data']['sender_required_fields']:
        print(f"{pomt},sender,{r['name']},{r['type']},{r['is_required']},{r['regex']}")

    if response['data']['payout_options']:
        for r in response['data']['payout_options']:
            print(f"{pomt},options,{r['name']},{r['type']},r{['is_required']},{r['regex']}")
