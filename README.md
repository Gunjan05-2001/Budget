## Budget App

The Budget App is a simple Python-based application to help users manage their financial transactions. It allows users to register, log in, add transactions, and view their financial history. Each user’s data is stored securely and accessed through their unique profile.

---

## Features

- *User Registration and Login*: Securely register and log in using a profile name and PIN.
- *Add Transactions*: Add details such as date, description, category, and amount for financial tracking.
- *View Transactions*: View all logged transactions in a user-friendly table format.
- *Data Persistence*: Save and load transaction data for each user.

---

## Screenshots

*App Interface*:

![image alt](https://github.com/Gunjan05-2001/Budget/blob/main/budget1.JPG)

![image alt](https://github.com/Gunjan05-2001/Budget/blob/main/budget2.JPG)
---


## Prerequisites

Before running the app, ensure you have the following installed:

1. *Python 3.x*: [Download Python](https://www.python.org/downloads/)
2. *Required Python Libraries*:
   - pandas
   - tkinter (comes pre-installed with Python)

To install missing libraries, use the command:

bash
pip install pandas


---

## How to Run the App

1. Clone the repository:

   bash
   git clone https://github.com/Gunjan05-2001/Budget
   

2. Navigate to the project directory:

   bash
   cd budget-app
   

3. Run the script:

   bash
   python budget_app.py
   

---

## Project Structure

- budget_app.py: Main application script.
- profiles.txt: Stores user credentials in profile_name:PIN format.
- user_data/: Directory where user-specific transaction data is stored as CSV files.

---

## Usage

1. *Login/Register*:
   - Enter a profile name and a PIN to log in or register.
   - For new users, click the Register button.
   - For existing users, click the Login button.

2. *Add Transactions*:
   - After logging in, enter the transaction details (date, description, category, amount) and click Add Transaction.

3. *View Transactions*:
   - View all past transactions in the table by clicking View Transactions.

---

---

## Known Issues

- Ensure all fields are filled correctly when adding a transaction. Incorrect or missing data may cause errors.
- Use the correct format for the date field (YYYY-MM-DD).

---


Enjoy managing your finances with the *Budget App*! 🎉
