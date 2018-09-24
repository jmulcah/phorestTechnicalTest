# Graduate Technical Test - Phorest


CLI that uses phorest's API to search for client's using their email or phone number and allows the user to create 

vouchers for them and post the data back.

The API is a REST API and using JSON.


### Prerequisites

Using Python 3.7 with the following imports
-urllib
-requests
-json
-HTTPBaiscAuth



### Structure of program

1. Takes input from user using the '@' symbol to determine if it is an email or phone number
2. Requests client information based off email or phone number from API
3. Gets client ID from request
4. Takes input from user about voucher amount
5. Requests client's voucher balance/account
6. Updates client's voucher balance/account
7. Posts client's updated account back to API
8. Prints amount entered and success message if transaction is successful
