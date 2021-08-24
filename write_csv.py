import csv
# try writing more than one row into CSV
def write_file():
    # think: is it possible to just define 'fieldnames' once, then not have to repeat its keys throughout the file?
    with open('data/booking_quotes.csv', mode='w') as csv_file:
        fieldnames = ['customer_name',
                      'package_info',
                      'danger',
                      'weight',
                      'volume',
                      'required_date',
                      'urgent',
                      'can_it_be_shipped',
                      'shipping_rate',
                      'can_it_be_flown',
                      'flying_rate',
                      'trucking_rate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    with open('data/booking_quotes.csv', mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'customer_name': 'James Han',
                         'package_info': 'It is a fridge.',
                         'danger': 'no',
                         'weight': '10 kg',
                         'volume': '4 sq. m.',
                         'required_delivery_date': '2021-06-30',
                         'urgent': 'yes',
                         'can_it_be_shipped': 'yes',
                         'shipping_rate': '$30',
                         'can_it_be_flown': 'yes',
                         'flying_rate': '$100',
                         'trucking_rate': '$45'})

