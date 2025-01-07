import datetime
from write import *
from read import *



import datetime



def display_rented_lands(rented_lands):
    ''' Display details of rented lands. '''

    if not rented_lands:
        print("No lands are currently rented.")
        return

    print("\n\t\t\tRented Lands\n")
    print("------------------------------------------------------------------------")
    print("{:<10} {:<12} {:<15} {:<20} {:<10}".format(
        "Land ID", "City", "LandFace", "Expected Return Date", "Status"))
    print("------------------------------------------------------------------------")

    for land in rented_lands:
        if len(land) == 5:  # Ensure the list has all required fields
            print("{:<10} {:<12} {:<15} {:<20} {:<10}".format(
                land[0],  # Land ID
                land[1],  # City
                land[2],  # LandFace
                land[3],  # Expected Return Date
                land[4]   # Status
            ))
        else:
            print("Incomplete land information: {}".format(land))






def land_rent(lands):
    ''' Handle the process of renting lands. '''

    import datetime

def validate_input(prompt, condition_func):
    while True:
        user_input = input(prompt)
        if condition_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def is_valid_name(name):
    ''' Validates a name input. '''
    return name and not name.isdigit()

def is_valid_phone(phone):
    ''' Validates a phone number input. '''
    return phone and phone.isdigit() and len(phone) == 10

def calculate_total_amount(rented_lands):

    return sum([land["rate"] * land["duration"] for land in rented_lands])

def process_rented_lands(rented_lands, customer_name, phone_number, lands):

    total_amount = calculate_total_amount(rented_lands)

    transaction_details = {
        "land_ids": [land["land_id"] for land in rented_lands],
        "city_districts": [land["city_district"] for land in rented_lands],
        "land_areas": [land["land_area"] for land in rented_lands],
        "expected_return_dates": [land["expected_return_date"] for land in rented_lands],
        "duration": [land["duration"] for land in rented_lands],
        "customer_name": customer_name,
        "Phone": phone_number,
        "total_amount": total_amount
    }

    generate_rent_invoice(transaction_details)
    write_lands("lands.txt", lands)

    print("Land(s) rented successfully.\n")
    display_rented_lands(rented_lands)

def land_rent(lands):

    lands_available = [land for land in lands if "Available" in land[-1]]

    if not lands_available:
        print("This Land is not available for rent.")
        return

    print("\n\t\t\tAvailable Lands\n")
    print("------------------------------------------------------------------------")
    print("KittaNo\tCity\tLandFace\tAnna\tPrice\tStatus")
    print("------------------------------------------------------------------------")

    for land in lands_available:
        print(land)

    rented_lands = []

    while True:
        land_id = validate_input("Enter the Kitta Number you want to rent (or type 'done' to finish): ",
                                 lambda x: x.lower() == 'done' or any(land[0].replace(" ", "") == x for land in lands_available))

        if land_id.lower() == 'done':
            if not rented_lands:
                print("No land rented. Exiting...")
                return
            else:
                break

        # Check if the land with the specified ID is available for rent
        land_to_rent = next((land for land in lands_available if land[0] == land_id), None)

        if land_to_rent is None or "Not Available" in land_to_rent[-1]:
            print("Land {} is not available for rent.".format(land_id))
            continue

        print("Land {} is available for rent.".format(land_id))

        duration = int(validate_input("Enter the duration of rent for land {} (in months): ".format(land_id),
                                      lambda x: x.isdigit() and int(x) > 0))# validates x is a digit and greater than 0
        expected_return_date = datetime.datetime.now() + datetime.timedelta(days=duration * 30)
        rented_lands.append({
            "land_id": land_id,
            "city_district": land_to_rent[1],
            "land_area": land_to_rent[3],
            "expected_return_date": expected_return_date,
            "duration": duration,
            "rate": int(land_to_rent[4])  # Adding the rate of the land
        })

        land_to_rent[-1] = "Not Available"
        print("Land {} added to the rental list.".format(land_id))

    customer_name = validate_input("Enter your name: ", is_valid_name)
    phone_number = validate_input("Enter your phone number: ", is_valid_phone)

    process_rented_lands(rented_lands, customer_name, phone_number, lands)



    
def return_land(lands):
    ''' Added a function to handle the process of returning lands. '''

    def calculate_fine(rented_on, return_on):
        ''' Added a nested function to calculate the fine for returning a land. '''

        try:
            rented_date = datetime.datetime.strptime(rented_on, "%Y-%m-%d")
            return_date = datetime.datetime.strptime(return_on, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format.")
            return None

        if rented_date > return_date:
            print("Error: Return date is before rent date.")
            return None
    
        days_diff = (return_date - rented_date).days
        if days_diff > 30:
            fine = (days_diff - 30) * 10  # Assuming fine of $10 per day after 30 days
            return fine
        else:
            return 0

    while True:
        land_id = input("Enter the land ID you want to return (or type 'done' to finish): ")

        if land_id.lower() == 'done':
            break

        valid_id = any(land[0] == land_id for land in lands)
        if not valid_id:
            print("Invalid land ID. Please enter a valid ID.")
            return

        rented = False
        for land in lands:
            if land[0] == land_id and "Not Available" in land[-1]:
                rented = True
                land[-1] = "Available"

                rented_on = input("Enter the date of rent (YYYY-MM-DD): ")
                return_on = input("Enter the date of return (YYYY-MM-DD): ")

                fine = calculate_fine(rented_on, return_on)
                if fine is None:
                    print("Error: Fine calculation failed.")
                    return

                total_amount = round(int(land[4]) * int(land[3]), 2) + fine
                write_lands("lands.txt", lands)

                transaction_details = {
                    "land_id": land_id,
                    "customer_name": input("Enter your name: "),
                    "duration": int(land[3]),
                    "return_date": return_on,
                    "total_amount": total_amount,
                    "fine": fine
                }

                generate_return_invoice(transaction_details, land)
                return

        if not rented:
            print("Land with ID {} is not currently rented.".format(land_id))


