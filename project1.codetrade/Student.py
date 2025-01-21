class LoginUser:
    """
        Description: Login Class that takes the username and password and checks if both are correct.
    """

    def check_user_info(self):
        """
            Description: Function that checks if the entered username and password match any entry in a CSV file.
        """
        max_attempts = 3  # Max no. of attemps you can
        attempts = 0

        while (attempts < max_attempts):
            self.user_name = input("Enter  your username or mail_id: ")
            self.password = input("Enter  your password: ")
            try:
                with open("CredentialsDetails.csv", 'r') as user_info:  # Open the credentialsDetails.csv to check for user
                    user_data = user_info.readlines()[1:]  # Read data and then check 
                    user_data = [line.strip().split(',') for line in user_data] # here we are creating the list of user_data by splitting them by ,
                    for data in user_data:
                        if (data[3] == self.user_name or data[6] == self.user_name) and data[4] == self.password:  # Successful login
                            print(f"Login Successful as {self.user_name}")
                            return True, data[7], self.user_name, self.password  # Return success with role information
                        
                    print("Invalid username or password. Try again.")
                    attempts += 1
                    attempts_left  = max_attempts - attempts
                    print(f"{attempts_left} attempts left")

            except IOError as ioe:
                print(f"Something went wrong, failed to check for the user:{str(ioe)}")
                return False, 'Error', 'Error', 'Error'
            
        print("Maximum attempts exceeded. please try again after sometime")
        return False, False, 'False', 'False'
    
class StudentTest:
    """
        Desciption: Student test class is responsible for the tetest student is appearing for their score and exam  
    """
    def __init__(self, username, password):
        """
            summary_ Constructor to set the username and password and initialize score and total questions
        """
        self.username = username
        self.password = password
        self.test_score = 0
        self.total_questions=0
    
    def test_started(self):
        """summary_ this function is responsible for giving student questions and answers
        """ 
        print("Test Started\n")
        try:
            with open('questions.csv','r') as question_file, open('answers.csv','r') as answers_file:
                question_list = question_file.readlines()[1:]
                answers_list = answers_file.readlines()[1:]

                self.total_questions = len(question_list)

                if len(question_list) != len(answers_list):
                    print("please enter equal number of answers for the questions")
                    return
                for i in range(len(question_list)):
                    question = question_list[i].split(":")[1].strip()   #take question from questions_list and split thwm ,
                    answer = question_list[i].split(',')[1:]  # take answes from ans_list','
                    answer_list=[]  #list for storing correct ans 

                    right_answer = None  # mark the right answer None initially when we havent taken input from user
                    for element in range(len(answer)):
                        if '[' in answer[element]:
                            right_answer = chr(element + 97)  # storing after typecasting the answers
                        answer_list.extend(answer[element].replace('[',"").replace(']',"").split(','))  # replace the '[' and ']' with empty " "

                    print(f"Ques {i+1}: {question}")
                    for index in range(len(answer_list)):
                        print(f"{chr(97+index)}:{answer_list[index]}")
                    
                    user_input = None  # set the user answer None and get the answer from the user then 
                    while user_input not in ['a','b','c','d']:
                        user_input = input("Enter your answer (a,b,c,d): ").lower()
                        print("please choose a valid choice among(a,b,c,d)")

                    if user_input == right_answer:
                        self.test_score += 1
                      
                self.display_result()

        except Exception as exe:
            print(f"Something went wrong while opening Questions or Answers file {str(exe)}")

    def display_result(self):
        """this functions is used to display the result to the student.
        """
        try:
            per = (self.test_score / self.total_questions) * 100 if self.total_questions else 0
            print(f"\nYour result: {per:.2f}%")
            self.store_result(per)

        except Exception as exe:
            print(f"Error in displaying Result: {str(exe)}")
        
    def store_result(self, percentage):
        """
        Description: Store the student's result in a CSV file.
        """
        try:
            with open("results.csv", 'a', newline='') as result_file:
                if result_file.tell() == 0:  # checks if it is header or not if it is at 0 then write the header 
                    result_file.write("Username,Password,Score,Percetage\n")
                result_file.write(f"{self.username},{self.password}, {self.test_score}, {percentage:.2f}%\n")  # store the username,password,score,percentage in result csv file

            print("Result saved successfully!")

        except IOError:
            print(f"Error while storing the result: {str(IOError)}")

# if __name__ == "_main":
#     login = LoginUser()
#     login.check_user_info()