#!/usr/bin/env python3

import requests
import argparse
import datetime

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        help='File type to download: latest | all',
                        default='latest')
    


    return parser.parse_args()

def schema():
    # Dictionary object with data type for
    # https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd
    dict_data_types = {
        'transaction_id': 'string',
        'price': 'long',
        'date_of_transfer': 'timestamp',
        'postcode': 'string',
        'property_type': 'string',
        'old_or_new': 'string',
        'duration': 'string',
        'paon': 'string',
        'saon': 'string',
        'street': 'string',
        'locality': 'string',
        'town_city': 'string',
        'district': 'string',
        'county': 'string',
        'ppd_category': 'string',
        'record_status': 'string'
    }

    return dict_data_types


def main():

    args = parse_args()
    print('Grabbing price paid data')

    if args.d == 'latest':
        download_url = r'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/' \
                       r'pp-monthly-update-new-version.csv'
        download_fname = args.d
    
    elif args.d == 'all':
        download_url = r'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/' \
                       r'pp-complete.csv'

    response = requests.get(download_url)
    text = response.text
    date = str(datetime.date.today())
    fname = f"{args.d}-{date}.csv"

    with open(fname, 'w+') as f:
        f.writelines(text)



if __name__ == '__main__':
    main()