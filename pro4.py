dataset = []
two_d_data = False
summary = {}

def make_one_dimension(items):
    if not items:
        return []

    if isinstance(items[0], list):
        result = []
        for item in items:
            result += item
        return result

    return items


def find_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def calculate_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = find_average(numbers)

    return minimum, maximum, total, avg


def calculate_factorial(number):
    if number <= 1:
        return 1

    return number * calculate_factorial(number - 1)


def display_samples(*values):
    print("Sample values:", values)


def show_information(**details):
    print("\nDataset Information:")

    for name, value in details.items():
        print(f"{name}: {value}")


def create_summary(numbers):
    summary["total"] = len(numbers)
    summary["average"] = round(find_average(numbers), 2)



def get_dataset():
    global dataset, two_d_data

    print("\nSelect Data Type")
    print("1. One Dimensional")
    print("2. Two Dimensional")

    option = input("Enter option: ").strip()

    if option == "2":
        two_d_data = True
        dataset = []

        number_of_rows = int(input("Enter number of rows: "))

        for row_number in range(number_of_rows):
            values = input(
                f"Enter values for row {row_number + 1}: "
            ).split()

            row = []

            for value in values:
                row.append(int(value))

            dataset.append(row)

    else:
        two_d_data = False

        values = input("Enter numbers separated by spaces: ")
        dataset = [int(value) for value in values.split()]

    print("\nData stored successfully!")



def show_summary():
    if not dataset:
        print("\nPlease enter data first.")
        return

    numbers = make_one_dimension(dataset)

    create_summary(numbers)

    print("\n========== DATA SUMMARY ==========")
    print("Total Elements :", len(numbers))
    print("Minimum Value  :", min(numbers))
    print("Maximum Value  :", max(numbers))
    print("Total Sum      :", sum(numbers))
    print("Average        :", summary["average"])

    if two_d_data:
        print("\n2D Data:")

        for row in dataset:
            print(row)

    display_samples(*numbers[:5])

    show_information(
        rows=len(dataset) if two_d_data else 1,
        elements=len(numbers)
    )


def factorial_menu():
    number = int(input("\nEnter a number: "))

    answer = calculate_factorial(number)

    print(f"Factorial of {number} = {answer}")

def filter_numbers():
    if not dataset:
        print("\nPlease enter data first.")
        return

    numbers = make_one_dimension(dataset)

    limit = int(input("Enter minimum value: "))

    result = list(filter(lambda value: value >= limit, numbers))

    print("\nFiltered Values:")

    if result:
        print(*result, sep=", ")
    else:
        print("No values found.")



def sort_dataset():
    global dataset

    if not dataset:
        print("\nPlease enter data first.")
        return

    print("\nSorting Menu")
    print("1. Ascending")
    print("2. Descending")

    option = input("Enter option: ")

    descending = option == "2"

    if two_d_data:

        sorted_data = sorted(
            dataset,
            key=lambda row: sum(row),
            reverse=descending
        )

        print("\nSorted Rows:")

        for row in sorted_data:
            print(row)

    else:

        dataset.sort(reverse=descending)

        print("\nSorted Data:")
        print(*dataset, sep=", ")



def show_statistics():
    if not dataset:
        print("\nPlease enter data first.")
        return

    numbers = make_one_dimension(dataset)

    minimum, maximum, total, average = calculate_statistics(numbers)

    print("\n========== STATISTICS ==========")
    print("Minimum :", minimum)
    print("Maximum :", maximum)
    print("Sum     :", total)
    print("Average :", round(average, 2))



def start_program():

    print("   DATA ANALYZER AND TRANSFORMER")

    while True:

        print("\-- MAIN MENU --")
        print("1. Enter Dataset")
        print("2. View Dataset Summary")
        print("3. Find Factorial")
        print("4. Filter Dataset")
        print("5. Sort Dataset")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            get_dataset()

        elif choice == "2":
            show_summary()

        elif choice == "3":
            factorial_menu()

        elif choice == "4":
            filter_numbers()

        elif choice == "5":
            sort_dataset()

        elif choice == "6":
            show_statistics()

        elif choice == "7":
            print("\nProgram closed successfully. Thank you!")
            break

        else:
            print("\nInvalid option! Please try again.")

if __name__ == "__main__":
    start_program()