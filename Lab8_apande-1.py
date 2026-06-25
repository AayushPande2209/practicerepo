# -User enters UPC code
# -Strips whitespace and checks if it has any other chars besides numbers, and if len(upc) != 12
while True:
    upc = input("Enter a 12-digit UPC: ").strip()

    if len(upc) != 12:
        print(f"Error: Input must be exactly 12 digits (got {len(upc)}). Please try again.\n")
        continue
    if not upc.isdigit():
        print("Error: Input must contain only numbers. Please try again.\n")
        continue

    break

upc_code11 = upc[:11]
provided_check = upc[11]

#function to calc 12th digit/validate upc
def find_UPC(upc_code11):
    total = 0
    for i, digit in enumerate(upc_code11):
        if i % 2 == 0:
            total += int(digit) * 3
        else:
            total += int(digit) * 1
    check_digit = (10 - (total % 10)) % 10
    return check_digit


print(f"\nThe first 11 digits are '{upc_code11}'.")
print(f"The provided check digit is '{provided_check}'.")
print("\nCalculating")

expected_check = find_UPC(upc_code11)
print(f"The expected check digit is {expected_check}.")

if int(provided_check) == expected_check:
    print("\nThis is a VALID UPC.")
else:
    print("\nThis is an INVALID UPC.")