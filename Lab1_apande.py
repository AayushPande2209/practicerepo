"""
Program: UPC Validator
Author: Your Name
Purpose: This program validates a 12-digit UPC-A code by calculating
         the expected check digit and comparing it to the check digit
         provided by the user.
Starter Code: None
Date: September 20, 2026
"""


def find_UPC(first_11_digits):
    """Calculate and return the expected UPC-A check digit."""

    # Add the digits in the odd positions (1st, 3rd, 5th, etc.)
    odd_sum = 0
    for i in range(0, 11, 2):
        odd_sum += int(first_11_digits[i])

    # Add the digits in the even positions (2nd, 4th, 6th, etc.)
    even_sum = 0
    for i in range(1, 11, 2):
        even_sum += int(first_11_digits[i])

    # UPC-A algorithm: multiply odd-position sum by 3
    total = (odd_sum * 3) + even_sum

    # Calculate the check digit needed to make the total a multiple of 10
    check_digit = (10 - (total % 10)) % 10

    return check_digit


# Main program
while True:
    upc = input("Enter a 12-digit UPC: ")

    # Validate the input before calculating the check digit
    if len(upc) != 12 or not upc.isdigit():
        print("Error: Please enter exactly 12 digits.")
        continue

    # Separate the first 11 digits and the provided check digit
    first_11 = upc[:11]
    actual_check_digit = int(upc[11])

    print()
    print(f"The first 11 digits are '{first_11}'.")
    print(f"The provided check digit is '{actual_check_digit}'.")
    print()
    print("Calculating...")

    # Call the required function
    expected_check_digit = find_UPC(first_11)

    print(f"The expected check digit is {expected_check_digit}.")
    print()

    # Compare the calculated check digit with the provided one
    if expected_check_digit == actual_check_digit:
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.")

    break