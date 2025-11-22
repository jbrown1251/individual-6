def problem1():
    # Create a list of days in the week
    Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Create a list of sales for each day
    Sale_list = [50, 75, 150, 125, 100]

    # Find the maximum sales value
    max_sale = Sale_list[0]
    max_day = Week_list[0]

    # Loop through all sales to find the highest
    for i in range(len(Sale_list)):
        if Sale_list[i] > max_sale:
            max_sale = Sale_list[i]
            max_day = Week_list[i]

    # Display the result
    print(f"\nThe Max sales is $ {max_sale}")
    print(f"The Max sales day is {max_day}")
# -------------------------------------------------------------

def problem2():
    # Create an empty list to store numbers
    num_list = []

    # Ask user for input values
    value = float(input("\nEnter value (or 0 to end): "))

    # Keep asking for numbers until user enters 0
    while value != 0:
        num_list.append(value)
        value = float(input("Enter value (or 0 to end): "))

    # Display the list entered by the user
    print(f"\n{num_list}")

    # Check if the list has at least one number
    if len(num_list) > 0:
        # Find the range (difference between max and min)
        range_value = max(num_list) - min(num_list)
        print(f"Range = {range_value:.1f}")
    else:
        print("No numbers were entered.")
