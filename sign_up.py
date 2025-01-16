import re
import csv

def checkpass(password):
    """
    Validates the password based on the following criteria:
    1. Contains at least one uppercase letter.
    2. Contains at least one lowercase letter.
    3. Contains at least one digit.
    4. Contains at least one special symbol.
    5. Length is between 6 and 20 characters.
    """
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*?&]{6,20}$"
    return re.fullmatch(reg, password)

def validate_email(email_id):
    """
    Validates the email based on the format:
    1. Contains valid characters before and after '@'.
    2. Ends with a valid domain format.
    """
    reg = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(reg, email_id)

def append(first, mid, last, email, password, contact):
    """
    Appends the credentials to the CSV file.

    Args:
        first (str): First name.
        mid (str): Middle name.
        last (str): Last name.
        email (str): Email ID.
        password (str): Password.
        contact (str): Contact number.
    """
    with open("credentialsDetails.csv", 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first, mid, last, email, password, contact])
    print("Credentials appended successfully.")

def main():
    """
    Main function to collect user input and validate credentials.
    """
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Validate phone number input
    try:
        contact_number = input("Enter your phone number: ")
        if not re.fullmatch(r"\d{10,15}", contact_number):
            raise ValueError("Phone number must be between 10 to 15 digits.")
    except ValueError as e:
        print(f"Invalid phone number: {e}")
        return
        
    if checkpass(password) and validate_email(email):
        try:
            with open("credentialsDetails.csv", 'r', newline='') as file:
                reader = csv.reader(file)
                if not any(reader):  
                    with open("credentialsDetails.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["first_name", "middle_name", "last_name", "email_id", "password", "contact_number"])
                    append(first_name, middle_name, last_name, email, password, contact_number)
                else:
                    append(first_name, middle_name, last_name, email, password, contact_number)
        except FileNotFoundError:
            append(first_name, middle_name, last_name, email, password, contact_number)
    else:
        print("Incorrect password or email format.")

if __name__ == "__main__":
    main()
