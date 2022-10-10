import csv #CSV module to parse data from csv files

#Request input from the user and display information about
#the csv file associated with their request
def read_animal_csv():
    try:
        animal = input("\nType of animal (Ctrl + C to exit): ").strip()
    except KeyboardInterrupt: #Exit key was pressed, leave program
        print("\nThank you!")
        return False
    
    file = f"{animal}.csv" #Try to make csv file name based on input

    #Try to open csv file whose name is from input and print the name, age,
    #and breed of every animal in the file
    try:
        with open(file, newline="") as csv_file:
            reader = csv.DictReader(csv_file, skipinitialspace=True)
            for row in reader:
                print(f"{row['name']} is a {row['age']} year old {row['breed']}")
    except FileNotFoundError: #File with name of input not found
        print(f"Sorry, we don't have any {animal} here")
    except: #Something else went wrong
        print(f"Sorry, something went wrong with your request for {animal}")

    return True #Continue requesting user input

#Continue requesting user input until they enter exit key
while read_animal_csv():
    pass