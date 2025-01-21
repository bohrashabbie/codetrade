import re
import csv
class UserRegistration:
    """
    A class to handle user registration with validation and CSV storage.
    """

    def __init__(self, csv_file="credentialsDetails.csv"):
        self.csv_file = csv_file
        self.initialize_csv()

    def initialize_csv(self):
        """
        Initializes the CSV file with a header if it doesn't already exist or is empty.
        """
        try:
            with open(self.csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                if not any(reader):
                    raise FileNotFoundError
        except (FileNotFoundError, csv.Error):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["first_name", "middle_name", "last_name", "email_id", "password", "contact_number", "user_name", "is_admin"])

    @staticmethod
    def check_password(password):
        """
        Validates the password based on the following criteria:
        1. Contains at least one uppercase letter.
        2. Contains at least one lowercase letter.
        3. Contains at least one digit.
        4. Contains at least one special symbol.
        5. Length is between 8 and 20 characters.
        """
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*?&]{8,20}$"
        return re.fullmatch(reg, password)

    @staticmethod
    def validate_email(email_id):
        """
        Validates the email based on the format:
        1. Contains valid characters before and after '@'.
        2. Ends with a valid domain format.
        """
        reg = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.fullmatch(reg, email_id)

    @staticmethod
    def validate_contact(contact_number):
        """
        Validates the contact number to ensure it's 10-15 digits.
        """
        return re.fullmatch(r"\d{10,15}", contact_number)
    def check_email(self, email):
        """_summary_ this function is handling duplicate email id
        """
        try:
            with open("credentialsDetails.csv", 'r') as file:
                data_file = csv.reader(file)
                next(data_file)
                for data in data_file:
                    if data[3] == email:
                        print("This email is already register please enter some another email")
                        return False
        except Exception  as exe:
            print(f"error occur during the execution{exe}")
        return True
    def append_to_csv(self, first, mid, last, email, password, contact,user_name, is_admin):
        """
        Appends the credentials to the CSV file.
        """
        try:
            with open(self.csv_file, 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([first, mid, last, email, password, contact,user_name, is_admin])
            print("Credentials appended successfully.")
        except Exception as e:
            print(f"Error appending to CSV: {e}")
    
    def take_input(self, label, mandatory=False):
        if mandatory:
            while True:
                input_ = input(f"Enter your {label}: ").strip()
                if input_:
                    return input_
                print(f"please enter {label}")
        input_ = input(f"Enter your {label}: ").strip()
        return input_

    
    def register_user(self):
        """
        Collects user input and validates credentials.
        """
        # Ask if the user is an admin
        is_admin_input = input("Are you an admin? (y/n): ").strip().lower()
        if is_admin_input == 'y':
            is_admin = True
        elif is_admin_input == 'n':
            is_admin = False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            return self.register_user()

        # Collect other user details
        
        first_name = self.take_input("First Name", mandatory=True)
        # while True:
        #     first_name = input("Enter your first name: ").strip()
        #     if first_name:
        #         break
        #     print("please enter first name")
        
        middle_name = input("Enter your middle name: ").strip()
        # while True:
        #     last_name = input("Enter your last name: ").strip()
        #     if last_name:
        #         break
        #     print("please enter first name")
        last_name = self.take_input("last_name", mandatory= True)
        
        # while True:
        #     email = input("Enter your email: ").strip()
        #     if self.validate_email(email) and self.check_email(email):
        #         break
        #     print("Invalid email format.")
        email = self.take_input("email_id", mandatory=True)
        
            
        # while True:
        #     password = input("Enter your password: ").strip()
        #     if  self.check_password(password):
        #         break
        #     print("Invalid password. Ensure 8-20 characters, an uppercase letter, a lowercase letter, a digit, and a special character./n")
        password = self.take_input("password", mandatory=True)
        
        
        # while True:
        #     contact_number = input("Enter your phone number: ").strip()
        # # Validate input
        #     if self.validate_contact(contact_number):
        #         break
        #     print("Invalid phone number.")
        contact_number = self.take_input("contact_number", mandatory=True)
            
        print("your user name is :")
        User_name = first_name[0] + last_name
        print(User_name)

        # Append data to CSV
        self.append_to_csv(first_name, middle_name, last_name, email, password, contact_number, User_name, is_admin)

if __name__ == "__main__":
    object = UserRegistration()
    object.register_user()