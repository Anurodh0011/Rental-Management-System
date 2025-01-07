from operations import *

def read_lands(file_name):
    lands = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.replace("\n",'')
                lands.append(line.split(","))
    except FileNotFoundError:
        print("Error: File '{file_name}' not found.")
    return lands

# Read data from file
filename = "lands.txt"
rented_lands = read_lands(filename)



# Display rented lands
display_rented_lands(rented_lands)

