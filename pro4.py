data = []              
is_2d = False           
dataset_summary = {}   

def show_args(*args):
    #Prints whatever values are passed in using *args.
    print("Sample values:", args)

def dataset_info(**kwargs):
    #Prints dataset characteristics passed as key-value pairs.
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def factorial(n):
    #Recursively calculates factorial of n."
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def flatten(lst):
    #Turns a 2D list into a 1D list. A 1D list is returned as is.
    if lst and isinstance(lst[0], list):
        flat = []
        for row in lst:
            flat.extend(row)
        return flat
    return lst

def average(values):
    #User-defined function to find the average of a list.
    return sum(values) / len(values) if values else 0

def get_stats(values):
    #Returns multiple stats at once: min, max, sum, average.
    return min(values), max(values), sum(values), average(values)

def summarize(values):
    #Stores a quick summary in the global dataset_summary dict.
    global dataset_summary
    dataset_summary["total_values"] = len(values)
    dataset_summary["overall_mean"] = round(average(values), 2)

def input_data():
    global data, is_2d
    choice = input("Enter 1 for 1D array or 2 for 2D array: ").strip()

    if choice == "2":
        rows = int(input("How many rows? "))
        data = []
        for i in range(rows):
            row = input(f"Enter row {i + 1} values (space separated): ")
            data.append([int(x) for x in row.split()])
        is_2d = True
    else:
        values = input("Enter data for a 1D array (separated by spaces): ")
        data = [int(x) for x in values.split()]
        is_2d = False

    print("Data has been stored successfully!")

def display_summary():
    if not data:
        print("No data yet, please input data first (option 1).")
        return

    flat = flatten(data)
    summarize(flat)

    print("\nData Summary:")
    print("- Total elements:", len(flat))
    print("- Minimum value:", min(flat))
    print("- Maximum value:", max(flat))
    print("- Sum of all values:", sum(flat))

    if is_2d:
        print("\nGrid view:")
        for row in data:
            print(row)

    show_args(*flat[:5])
    dataset_info(rows=len(data) if is_2d else 1, elements=len(flat))

def calculate_factorial():
    n = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {n} is: {factorial(n)}")

def filter_data():
    if not data:
        print("No data yet, please input data first (option 1).")
        return
    flat = flatten(data)
    threshold = int(input("Enter a threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x >= threshold, flat))
    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, filtered)))

def sort_data():
    if not data:
        print("No data yet, please input data first (option 1).")
        return

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    order = input("Enter your choice: ").strip()
    reverse = order == "2"

    if is_2d:
        sorted_rows = sorted(data, key=lambda row: sum(row), reverse=reverse)
        print("Sorted 2D data (rows sorted by their sum):")
        for row in sorted_rows:
            print(row)
    else:
        data.sort(reverse=reverse)
        label = "Descending" if reverse else "Ascending"
        print(f"Sorted Data in {label} Order:")
        print(", ".join(map(str, data)))

def display_stats():
    if not data:
        print("No data yet, please input data first (option 1).")
        return
    flat = flatten(data)
    lo, hi, total, avg = get_stats(flat)
    print("Dataset Statistics:")
    print("- Minimum value:", lo)
    print("- Maximum value:", hi)
    print("- Sum of all values:", total)
    print("- Average value:", round(avg, 2))

def main():
    print("Welcome to the Data Analyzer and Transformer Program")
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_stats()
        elif choice == "7":
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()