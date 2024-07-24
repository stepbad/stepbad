# QAP Project 4Q1: Python Functions, Lists, and Data Files

## Description

The One Stop Insurance Company needs a program to enter and calculate new insurance policy information for its customers. This program saves the client information in `ClientInfo.dat` and claim information in `Claim.dat`.

## Author

- Stephen Badcock

## Date

- July 23, 2024

## Requirements

- Python 3.x
- Required libraries: `datetime`, `FormatValues` (custom module)

## Installation

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your machine.
3. Place the `FormatValues.py` module in the same directory as `qap4q1stepbad.py`.

## Usage

Run the script to enter and calculate new insurance policy information for customers. The program processes and stores client and claim information in data files.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `qap4q1stepbad.py`.
3. Run the script using the following command:
   ```bash
   python qap4q1stepbad.py

**User Interaction**
The script will prompt the user to enter various pieces of information about the insurance policy and the customer. Follow the on-screen prompts to provide the necessary information.

**Functions**

**calculate_payment(pay_method, total_cost, down_pay_amt, processing_fee)**
Calculates the payment method and payment details based on the provided payment method.

Parameters:
pay_method: The method of payment selected by the user.
total_cost: The total cost of the insurance policy.
down_pay_amt: The down payment amount.
processing_fee: The processing fee for the policy.
Returns:
A tuple containing the payment method, down payment amount, processing fee, and pay amount.

**open_read_claim_file(file_name)**
Reads and processes the claims from the specified file.

Parameters:
file_name: The name of the file containing the claims.
Returns:
A list of tuples, each containing the claim number, claim amount, and claim date.

**open_const_read(file_name)**
Reads constants from the specified file.

Parameters:
file_name: The name of the file containing the constants.
Returns:
A tuple containing the constants read from the file.

**Data Files**
ClientInfo.dat: Stores client information.
Claim.dat: Stores claim information.
Const.dat: Stores constant values used in calculations.


**Notes**
Ensure that the FormatValues module is present in the same directory as qap4q1stepbad.py.
The script prompts the user for input and processes the entered data to generate and store insurance policy information.
