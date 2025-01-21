class QuestionPaper:

    """
        Description: Class to take the Questions from the user and store them in questions.csv file
    """

    def __init__(self):
        """ Constructor to ask the user for the number of question and store them in csv file """
        
        self.total_question = int(input("Enter the number of questions you want to enter: "))  # ask the user to enter the number of question 
        self.add_questions()  # calling the add_questions_to_file() to add the questions to the file

    def add_questions(self):
        """ this functions take the ans from the input of the user and """
        try:
            with open('questions.csv','w') as question_file:
                question_file.write("Question Number:Question\n")  # writing header in the file

                for i in range(self.total_question):  
                    Questions = input(f"Enter the question {i+1}: ")  # taking the question from the user, question_number+1 because loop start from 0 
                    question_file.write(f"{i+1}:{Questions}\n")  # write each question to the file 

            print("Questions added successfully")
        except Exception as exe:
            print(f"Something went wrong,please try again later:{str(exe)}")  # handle the exception if any error occur in writing the question to file

class AddAnswer:
    """_summary_ here we make the answer set 
    """
    def __init__(self,total_question):
        """ Description: Constructor to assign the value to total_questions """
        self.total_question = total_question

    def add_answers(self):
        """Description: This function open the questions file in read mode and for each question it takes the 4 option and and identifies the correct option"""
        try:
            with open("questions.csv",'r') as read_question:
                questionlines=read_question.readlines()[1:]  # read the complete question file except the header

            with open("answers.csv",'w') as answer_file:  # open the answer or creates it if it does not exist in write mode
                answer_file.write("s.no.: option 1, option 2, option 3, option 4\n")  # write the header in the answer file
                for i in range(len(questionlines)):
                    print(f"\nEnter answers for Question {i + 1}:")
                    options = [input("Option A: "), input("Option B: "), input("Option C: "), input("Option D: ")]  # store the options in list
                    correct_option = input("Which option is correct (a,b,c,d)? ").lower()  # ask the user which option is correct 
                    options[ord(correct_option)-97] = f"[{options[ord(correct_option)-97]}]"  # usef to mark the correct 
                    answer_file.write(f"{i + 1}, {options[0]},  {options[1]}, {options[2]},  {options[3]}\n")  # store the options in the answer file 

            print("answers added successfully")
        except Exception as exe:
            print(f"Something is wrong please try again after sometime:{str(exe)}")  # handle exception
