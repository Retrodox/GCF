# Greatest Common Factor Calculator

This Python project calculates the greatest common factor (GCF) of two integers. It utilizes prime factorization to determine the GCF effectively. The application runs in a loop, allowing the user to perform multiple calculations until they choose to exit.

## Modules

The project is split into three main files:

- `main.py`: The main script that users interact with. It takes input from the user, calculates the GCF using functions from other modules, and displays the result.
- `prime_factorization.py`: Contains a function `get_prime_factors` that returns the prime factors of a given number.
- `combine_factors.py`: Uses the `get_prime_factors` function to calculate the greatest common factor of two numbers.

## Setup

To run this application, you need Python installed on your machine. No external libraries are required as the project uses only built-in modules.

### Installation

Clone or download the repository to your local machine
To start the application, run: py main.py
Follow the on-screen prompts to enter the numbers for which you want to find the GCF. After displaying the GCF, the program will ask if you wish to perform another calculation.

### How It Works
get_prime_factors(unfactored): Determines the prime factors of the input number.
find_gcf(num1, num2): Calculates the GCF of two numbers based on their prime factors.
The application will continue running, allowing multiple calculations until the user decides to exit by entering 'N' or 'no' when prompted.
