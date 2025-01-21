from Student import LoginUser, StudentTest
from sign_in import UserRegistration
from question_answer import QuestionPaper, AddAnswer  

class AdminRegistration:
    """_summary_ this adminregistration is responsible for the registering the user and validing them for exam
    """
    def register_admin(self):
        """
            function to check if the user is registered or not.
        """
        try:
            is_user_exist = input("please select among (y,n) to inform that you are register or not").lower().strip()
            
            while is_user_exist not in ['y', 'n']:  # Ensure valid input (either 'y' or 'n')
                print("Invalid input, please enter among y, n")
                is_user_exist = input("please select among (y,n) to inform that you are register or not : ").lower().strip()

            if is_user_exist == 'y':  # Check if the user exists or not
                user_login = LoginUser()  # here login class is used to check whether the user if register or not
                is_log_in, admin_info, username, password = user_login.check_user_info()  # Verifying user credentials

                if is_log_in:
                    admin_info = admin_info.strip()  
                    if admin_info == "True":
                        return 1, username, password  # User is admin, return admin access details
                    else:
                        return 2, username, password  # User is not admin, return regular user access details
                else:
                    if password == "Invalid" or username == "Invalid":
                        return 3, None, None  # Invalid credentials
                    else:
                        print("User is not registered")
                        return 0,None,None
                    
            else:  # User is not registered
                print("User is not registered.")
                return 4, None, None # here i am  calling the admin because admin has access to add a new user
            
        except Exception as exe:
            print(f"erro during the registration process: {str(exe)}")
            return 0, None, None

class AdminAccess:
    """
    This class is responsible for admin to add the user or set question paper
    """
    def provide_admin_access(self):
        """
        Description: Provides admin functionalities such as adding new users or creating question papers.
        """
        try:
            admin_role = int(input("Enter 1 for adding new user\nEnter 2 for setting question paper: "))
            if admin_role == 1: # adding the new user
                object = UserRegistration()
                object.register_user() # calling up the register user class for registering new user

            elif admin_role == 2:  
                question_paper = QuestionPaper()  # calling question_paper class
                total_questions = question_paper.total_question  # it is extracting the question_paper total_number of question
                answer_list = AddAnswer(total_questions)  # manages
                answer_list.add_answers_to_file()  # Sets the answers for the questions
          

            else:
                print("please enter the valid choice")
        except Exception as exe:
            print(f"error during the execution of the program {str(exe)}")

class MainFunction:
    """this class is responsible for the main execution of the function 
    """
    def __init__(self):
        self.admin_registration = AdminRegistration() 
        self.admin_access = AdminAccess()  

    def main_function(self):
        """the main function checks the functionality of the user and admin and decide accordingly
        """
        try:
            admin_number, username, password = self.admin_registration.register_admin()  # Check user registration and determine admin/student access

            if admin_number == 1: #admin acess
                self.admin_access.provide_admin_access()  # Admin access functionality 

            elif admin_number == 2:  # Student access
                print("Student functionalities coming soon.")
                StudentTest(username,password).test_started()

            elif admin_number == 3: 
                print("Invalid credentials. Please try again.")
            else:  # User not registered
                print("Please ask the administrator for registration.")

        except Exception as exe:
            print(f"Error during main execution: {str(exe)}")

# Entry point for the program
if __name__ == "__main__":
    object  = MainFunction()  # Instantiate the mainfunction 
    object.main_function()  # Execute the main function to start the program
