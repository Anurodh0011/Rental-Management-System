import datetime


def invoice_heading(file):
    file.write("***************************************************************\n")
    file.write("                    Techno Property Nepal                      \n")
    file.write("                        021-000444                             \n")
    file.write("                   Putalisadak, Kathmandu                      \n")
    file.write("---------------------------------------------------------------\n")
    file.write("         The only trusted service provider in Nepal.           \n")
    file.write("***************************************************************\n")
        
        

def generate_rent_invoice(transaction_details):
    file_name = "Rent_Invoice_{}.txt".format(transaction_details["customer_name"])
    with open(file_name, "w") as file:

        invoice_heading(file)
        file.write("Transaction Details:\n")
        file.write("Customer Name: {}\n".format(transaction_details["customer_name"]))
        file.write("Phone Number: {}\n".format(transaction_details["Phone"]))  
        file.write("Total Amount: NPR: {}\n".format(transaction_details["total_amount"]))
        file.write("\n")
        file.write("Rented Lands:\n")
        for i in range(len(transaction_details["land_ids"])):
            file.write("Land ID: {}\n".format(transaction_details["land_ids"][i]))
            file.write("City/District: {}\n".format(transaction_details["city_districts"][i]))
            file.write("Land Area (anna): {}\n".format(transaction_details["land_areas"][i]))
            file.write("Rented Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            file.write("Expected Return Date: {}\n".format(transaction_details["expected_return_dates"][i]))
            file.write("Duration of Rent: {} months\n".format(transaction_details["duration"][i]))
            file.write("\n")
    # Print the generated invoice in the shell
    with open(file_name, "r") as file:
        print(file.read())

def generate_return_invoice(transaction_details, land):
    file_name = "Return_Invoice_{}.txt".format(transaction_details["customer_name"])
    with open(file_name, "w") as file:
        invoice_heading(file)

        file.write("\n\nTransaction Details:\n")
        file.write("Customer Name: {}\n".format(transaction_details["customer_name"]))
        file.write("Total Amount: NPR {}\n".format(transaction_details["total_amount"]))

        # Add fine details
        if "fine" in transaction_details:
            file.write("Fine Amount: NPR {}\n".format(transaction_details["fine"]))

        file.write("\n")
        file.write("Returned Land:\n")
        file.write("Land ID: {}\n".format(transaction_details["land_id"]))
        file.write("City/District: {}\n".format(land[1]))
        file.write("Land Area (anna): {}\n".format(land[3]))
        file.write("Returned Date: {}\n".format(transaction_details["return_date"]))
    # Print the generated invoice in the shell
    with open(file_name, "r") as file:
        print(file.read())




def write_lands(filename, lands):
    with open(filename, "w") as file:
        for land in lands:
            file.write(",".join(land) + "\n")
