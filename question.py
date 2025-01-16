import csv
def question():
    """taking the input from the user in which i am taking 
    """
    n = int(input("enter the number of questions"))
    list = []
    for i in range(n):
        questions = input(f"enter the {i} question")
        list.append(questions)
    try:
        with open("questions.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            for q in list:
                writer.writerow([q]) 
            print("Questions have been saved to 'questions.csv'.")
    except Exception as e:
            print("an error occured here")
def main():
    question()

if __name__ == "__main__":
    main()