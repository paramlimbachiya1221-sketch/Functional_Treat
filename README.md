# Data Analyzer and Transformer Program

## 📌 Project Description

The **Data Analyzer and Transformer Program** is a Python-based program that allows users to enter and analyze **1D or 2D data**.

The program provides different features such as:

* Input 1D or 2D data
* Display dataset summary
* Calculate factorial using recursion
* Filter data using a lambda function
* Sort data in ascending or descending order
* Display minimum, maximum, sum, and average
* Demonstrate `*args` and `**kwargs`
* Demonstrate global variables
* Flatten 2D data into 1D data

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Functions
* Recursion
* Lambda Functions
* Built-in Functions
* `*args`
* `**kwargs`
* Global Variables
* `filter()`
* `sorted()`

## ✨ Features

### 1. Input Data

The user can select:

* **1D Array**
* **2D Array**

Example 1D input:

```text
10 20 30 40 50
```

Example 2D input:

```text
1 2 3
4 5 6
7 8 9
```

### 2. Display Data Summary

The program displays:

* Total elements
* Minimum value
* Maximum value
* Sum of all values
* Grid view for 2D data

### 3. Factorial Calculation

The program uses **recursion** to calculate the factorial of a number.

Example:

```text
Enter a number to calculate its factorial: 5

Factorial of 5 is: 120
```

### 4. Filter Data

The program uses a **lambda function** and `filter()` to display values greater than or equal to a selected threshold.

Example:

```text
Enter a threshold value: 30

Filtered Data (values >= 30):
30, 40, 50
```

### 5. Sort Data

The program can sort data in:

* Ascending order
* Descending order

For 2D data, rows are sorted according to their total sum.

### 6. Dataset Statistics

The program displays:

* Minimum value
* Maximum value
* Sum
* Average

The statistics are returned together using **multiple return values**.

## 📂 Main Functions

| Function                | Purpose                              |
| ----------------------- | ------------------------------------ |
| `show_args()`           | Demonstrates `*args`                 |
| `dataset_info()`        | Demonstrates `**kwargs`              |
| `factorial()`           | Calculates factorial using recursion |
| `flatten()`             | Converts 2D data into 1D             |
| `average()`             | Calculates average                   |
| `get_stats()`           | Returns multiple statistics          |
| `summarize()`           | Stores dataset summary               |
| `input_data()`          | Takes 1D/2D input                    |
| `display_summary()`     | Displays dataset summary             |
| `calculate_factorial()` | Takes input for factorial            |
| `filter_data()`         | Filters values using lambda          |
| `sort_data()`           | Sorts the dataset                    |
| `display_stats()`       | Displays dataset statistics          |
| `main()`                | Runs the main menu                   |

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Save the Program

Save the Python code as:

```text
data_analyzer.py
```

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python data_analyzer.py
```

## 📋 Main Menu

When the program starts, it shows:

```text
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
```

## 🎯 Concepts Demonstrated

This project is useful for learning important Python concepts:

1. Functions
2. Lists
3. Conditional statements
4. Loops
5. Recursion
6. Lambda functions
7. `filter()`
8. `sorted()`
9. `*args`
10. `**kwargs`
11. Global variables
12. Multiple return values
13. Built-in functions

## 👨‍💻 Author

**Param Limbachiya**

## 📄 License

This project is created for **educational and learning purposes**.
