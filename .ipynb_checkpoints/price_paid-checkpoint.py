#!/usr/bin/env python3

import requests


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

    print('Grabbing price paid data')

    price_paid_latest = r'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/' \
                     r'pp-monthly-update-new-version.csv'

    price_paid_all = r'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/' \
                     r'pp-complete.csv'

    response = requests.get(price_paid_latest)
    text = response.text

    with open('latest.csv', 'w+') as f:
        f.writelines(text)



if __name__ == '__main__':
    main()