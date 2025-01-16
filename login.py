
from question import question
def loginUp(user_name, password):
    """this function takes an argument as user name and password and validate the username and password
    Args:
        user_name (string): this is id which user will use in signing the application
        password (string): password use for the same
    """
    try:
        with open('credentialsDetails.csv', 'r') as file:
            next(file) # next is here used for skipping the first column
            for list in file:
                # Split the list into fields
                fields = list.strip().split(',')
                prev_user = fields[3].strip()  
                previous_pass = fields[4].strip()  
                if user_name == prev_user:
                    if password == previous_pass:
                        print("You are logged in successfully.")
                        return  
                    else:
                        print("Incorrect password.")
                        return  
            print("User not found. Please sign up.")

    except FileNotFoundError:
        print("Error: credentialsDetails.csv file not found")



def main():
    """this is main function computing validity of the user
    """
    user_name = input("enter your email id")
    password = input("enter your password")
    
    loginUp(user_name, password)
    

if __name__ == "__main__":
    main()