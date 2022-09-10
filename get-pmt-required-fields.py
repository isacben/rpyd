from utilities import make_request
import json
import argparse 

parser = argparse.ArgumentParser(description="Get Payment Method Required Fields")
parser.add_argument("pmt", help="the payment method type")
parser.add_argument("env", help="the rapyd environment")
parser.add_argument("-a", "--all", help="outputs all rapyd's api response", action="store_true")

args = parser.parse_args()

path = f'/v1/payment_methods/required_fields/{args.pmt}'

response = make_request(env=args.env, method='get', path=path)
    
if args.all:
    print(json.dumps(response, indent=4))
    exit(0)

for r in response['data']['fields']:
    s = f"{r['name']}, " \
        f"{r['type']}, " \
        f"is required {r['is_required']}, " \
        f"{r['regex']}"
    print(s)
