"""Code below checks for the float input to be POSITIVE"""


def get_valid_float(prompt):  # This asks the variable that it's going to be assigned to put a FLOAT value
    while True:
        value = float(input(prompt))  # This turns the input into a float
        try:
            if value < 0:  # This make sures that the value is GREATER THAN ZERO
                print("Sorry, value must be positive.")
            else:
                return value

        except ValueError:  # This code checks the input to be a number, it cannot be letter/s
            print("Sorry, value must be an integer.")


def get_number_of_people():  # This function is responsible for getting the number of people
    while True:
        num_people = int(get_valid_float("Please enter the number of people: "))  # This turns the value into integers

        if num_people <= 0:  # This make sures that when the user writes 0, it will loop back again
            print("Sorry, must at least be one")
        else:
            return num_people


"""VARIABLES"""

while True:
    def main():
        total_bill = get_valid_float("Please enter the total bill: ")
        tip_percentage = get_valid_float("Please enter the tip percentage: ")

        """OPERATIONS"""
        tip_amount = total_bill * (tip_percentage / 100)  # calculates the tip amount needed to add for the total cost
        total_amount = total_bill + tip_amount

        print(f"Tip amount: ₱{tip_amount:.2f}")  # Prints out the information
        print(f"Total amount: ₱{total_amount:.2f}")

        num_people = get_number_of_people()  # This variable is just for the number of people
        amount_each_person = total_amount / num_people  # calculates how much each person pays for the total amount.

        print(f"Total amount for each person: ₱{amount_each_person:.2f}")

    if __name__ == "__main__":  # make sures that the code on line 20 - 42 functions on main script or import script.
        main()