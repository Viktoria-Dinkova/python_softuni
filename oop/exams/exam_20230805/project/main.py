"""
1.	Class BaseLoan
In the base_loan.py file, the class BaseLoan should be implemented. It is a base class for any type of loan, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	interest_rate: float
o	The value represents the interest rate of the loan.
•	amount: float
o	The value represents the amount of the loan.
Methods
__init__(interest_rate: float, amount: float)
•	In the __init__ method, all the needed attributes must be set.
increase_interest_rate()
•	Method increases the loan’s interest rate. Keep in mind that each type of loan implements the method differently.
2.	Class StudentLoan
In the student_loan.py file, the class StudentLoan should be implemented. A student loan is a type of loan. Each student loan has an interest rate of 1.5 percent and an amount of 2000.0 EUR.
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
increase_interest_rate()
•	The method increases the interest rate by 0.2 percent.
3.	Class MortgageLoan
In the mortgage_loan.py file, the class MortgageLoan should be implemented. A mortgage loan is a type of loan. Each mortgage loan has an interest rate of 3.5 percent and an amount of 50000.0 EUR.
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
increase_interest_rate()
•	The method increases the interest rate by 0.5 percent.
4.	Class BaseClient
In the base_client.py file, the class BaseClient should be implemented. It is a base class for any type of client, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	name: str
o	The value represents the name of the client.
o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Client name cannot be empty!"
•	client_id: str
o	The value represents the id number of a client. It should contain exactly 10 symbols.
o	If the client’s id is not 10 symbols long, raise a ValueError with the message: "Client ID should be 10 symbols long!"
•	income: float
o	The value represents the income of a client.
o	If the client’s income is less than or equal to 0.0, raise a ValueError with the message: "Income must be greater than zero!"
•	interest: float
o	The value represents the client’s interest.
•	loans: list
o	Empty list that will contain loans (objects) each client has.
Methods
__init__(name: str, client_id: str, income: float, interest: float)
•	In the __init__ method, all the needed attributes must be set.
increase_clients_interest()
•	Increases the client’s interest. Keep in mind that each type of client implements the method differently.
5.	Class Student
In the student.py file, the class Student should be implemented. The student is a type of client. Each student has an initial interest of 2.0 percent.
Methods
__init__(name: str, client_id: str, income: float)
•	In the __init__ method, all the needed attributes must be set.
increase_clients_interest()
•	The method increases the client’s interest by 1.0 percent.
6.	Class Adult
In the adult.py file, the class Adult should be implemented. The adult is a type of client. Each adult has an initial interest of 4.0 percent.
Methods
__init__(name: str, client_id: str, income: float)
•	In the __init__ method, all the needed attributes must be set.
increase_clients_interest()
•	The method increases the client’s interest by 2.0 percent.
7.	Class BankApp
In the bank_app.py file, the class BankApp should be implemented. It will contain the functionality of the project.
Structure
The class should have the following attributes:
•	capacity: int
o	The number of clients а Bank can have.
•	loans: list
o	Empty list that will contain all loans (objects) that are created.
•	clients: list
o	Empty list that will contain all clients (objects) that are created.
Methods
__init__(capacity: int)
•	In the __init__ method, all the needed attributes must be set.
add_loan(loan_type: str)
The method creates a loan of the given type and adds it to the loans collection.
•	If the loan’s type is not valid, raise an Exception with the following message:
"Invalid loan type!"
•	Otherwise, create the loan, add it to the loans list, and return the following message:
"{loan_type} was successfully added."
•	Valid types of loans are: "StudentLoan" and "MortgageLoan"
add_client(client_type: str, client_name: str, client_id: str, income: float)
The method creates a client of the given type and adds them to the clients collection.
All clients’ IDs will be unique.
•	First, check if the client type is valid and if not raise an Exception with the following message:
"Invalid client type!"
•	Then, check if there is available bank capacity, and if not return the following message:
"Not enough bank capacity."
•	Otherwise, create the client, add it to the clients list, and return the following message:
"{client_type} was successfully added."

•	Valid types of clients are: "Student" and "Adult".
grant_loan(loan_type: str, client_id: str)
The method adds the loan of the given type to the client’s loans collection. Both loan and client will always exist.
•	First, check if the loan can be granted to the client. The student client can get ONLY a student type of loan and the adult client can get ONLY a mortgage type of loan. In case of a mismatch, raise an Exception with the following message:
"Inappropriate loan type!"
•	If the loan can be granted successfully to the client, remove it from the bank's loan collection, and add it to the client’s loan collection. Return the following message:
"Successfully granted {loan_type} to {client_name} with ID {client_id}."
o	Take the first loan of the given type from the collection.
remove_client(client_id: str)
The method removes the client with the given ID from the bank.
•	First, check if there is a client with the given ID in the client’s collection. If not, raise an Exception with the following message:
"No such client!"
•	Then, check if the client has loans. If so, raise an Exception with the following message:
"The client has loans! Removal is impossible!"
•	If the client can be removed successfully, remove them from the bank, and return the following message: "Successfully removed {client_name} with ID {client_id}."
increase_loan_interest(loan_type: str)
The method increases the interest rates for all loans of the given type that are in the bank’s loan collection. The loan type will be one of the valid types (StudentLoan or MortgageLoan). When all rates for the given loan type are successfully changed (hint: use increase_interest_rate() method), return the following message:
"Successfully changed {number_of_changed_loans} loans."
o	Loans that are already granted to clients should not be affected.
increase_clients_interest(min_rate: float)
The method increases the interest rates for all clients that are in the bank’s client collection who currently have an interest rate less than the min_rate value. When rates are successfully changed (hint: use increase_clients_interest() method), return the following message:
"Number of clients affected: {changed_client_rates_number}."
get_statistics()
Returns information about the bank’s loans and its clients. Each string is on a new line.
"Active Clients: {total_clients_count}
Total Income: {total_clients_income}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum}
Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum}
Average Client Interest Rate: {avg_client_interest_rate}"
o	All sums and rates should be formatted to the 2nd decimal place.
o	Average Client Interest Rate refers to the property interest each client has.
o	Avoid ZeroDivisionError

"""
from project.bank_app import BankApp

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())

"""
StudentLoan was successfully added.
MortgageLoan was successfully added.
StudentLoan was successfully added.
MortgageLoan was successfully added.
Student was successfully added.
Adult was successfully added.
Student was successfully added.
Not enough bank capacity.
Successfully granted StudentLoan to Peter Simmons with ID 1234567891.
Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.
Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.
Successfully removed Simon Mann with ID 1234567999.
Successfully changed 1 loans.
Successfully changed 0 loans.
Number of clients affected: 0.
Number of clients affected: 1.
Active Clients: 2
Total Income: 1500.00
Granted Loans: 3, Total Sum: 102000.00
Available Loans: 1, Total Sum: 2000.00
Average Client Interest Rate: 3.50
"""