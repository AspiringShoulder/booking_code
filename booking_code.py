# Since this is theoretically supposed to be a browser application, we want to keep the information
# in separate functions

# also look up different modules and libraries you need to import in Python
# see if you can have the program to process multiple rows from a csv
import datetime
import booking.write_csv
import pandas as pd
pd.set_option("display.max_columns", None)
pd.options.display.width = 0

people = pd.read_csv("C:/Users/capst/projects/booking/data/booking_quotes.csv")
print(type(people))
print(people.head())
shipping_data_raw = people.to_dict()
shipping_data = dict()

# NB: syntax of "variable_one, variable_two" automatically makes them tuples, regardless of ()
# look it up and make sure that the size thing for a DataFrame is .size
for index in range(0, people.size):
    for booking_field, booking_field_value in shipping_data_raw.items():
        # use pandas method to calculate # of rows in DataFrame
        # process multiple rows in this way: booking_field_value[row_number], etc
        shipping_data[booking_field] = booking_field_value[index]

print(shipping_data)
exit()

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

def get_inputs():
    inputs = dict()
    inputs["customer_name"] = input("Please enter the customer's name: ")
    inputs["package_info"] = input("Please enter information about the package: ")
    inputs["danger"] = input("Are the contents of the package dangerous? Enter 1 for yes and 2 for no: ")
    inputs["weight"] = input("Please enter the weight of the package in kilograms: ")
    inputs["volume"] = input("Please enter the volume of the package in square meters: ")
    inputs["required_date"] = input("Please enter the date that the package must be delivered by in yyyy-mm-dd format: ")
    inputs["today"] = datetime.date.today()

    return inputs

def import_inputs():
    pass

def get_business_day_intervals():
    # days_of_week gives number of calendar days that need to pass for package to not be urgent
    # keys are days of week, values are numbers of calendar days
    days_of_week = dict()
    days_of_week[SUNDAY] = 3
    days_of_week[MONDAY] = 3
    days_of_week[TUESDAY] = 3
    days_of_week[WEDNESDAY] = 5
    days_of_week[THURSDAY] = 5
    days_of_week[FRIDAY] = 5
    days_of_week[SATURDAY] = 4

    return days_of_week

def validate_inputs(shipping_data, business_day_intervals):
    ship_it = False
    if int(shipping_data["weight"]) < 10 or int(shipping_data["volume"]) < 5:
        ship_it = True

    fly_it = True
    if shipping_data["danger"] == "1":
        fly_it = False

    day_of_week = datetime.datetime.today().weekday()
    urgent_calendar_duration = business_day_intervals[day_of_week]
    last_urgent_date = datetime.datetime.today() + datetime.timedelta(days=urgent_calendar_duration)
    required_delivery_date = datetime.datetime.strptime(shipping_data["required_date"], "%Y-%m-%d")
    #experiment with date math stuff in testing grounds before coming back and finishing this section
    urgent = False
    if last_urgent_date >= required_delivery_date:
        urgent = True

    fly_weight_cost = 10 * int(shipping_data["weight"])
    fly_volume_cost = 20 * int(shipping_data["volume"])
    if fly_weight_cost >= fly_volume_cost:
        fly_final_cost = fly_weight_cost
    else:
        fly_final_cost = fly_volume_cost

    truck_shipment_cost = 25
    if urgent == True:
        truck_shipment_cost = 45

    ocean_shipment_cost = 30

    return (
        ship_it,
        fly_it,
        fly_final_cost,
        truck_shipment_cost,
        urgent
    )

def display_shipping_data(shipment_information):
    print("Can be shipped: ")
    print(ship_it)
    if ship_it == True:
        print("Shipping Rate: $30")

    print("Can be flown: ")
    print(fly_it)
    if fly_it == True:
        print("Flying Rate: $")
        print(fly_final_cost)

    print("Trucking rate: $")
    print(truck_shipment_cost)

    print("Urgent: ")
    print(urgent)

    return True

def main():
    while True:
        print("1. Enter data")
        print("2. Load data from file")
        print("9. Quit")
        option = input("Enter your choice: ")

        if option not in ["1", "2", "9"]:
            print("Invalid input. Try again: ")
            continue

        break

    if option == "9":
        exit()

    business_day_intervals = get_business_day_intervals()

    if option == "1":
        shipping_data = get_inputs()

    if option == "2":
        shipping_data = import_inputs()

    shipping_information = validate_inputs(shipping_data, business_day_intervals)

if __name__ == "__main__":
    main()




