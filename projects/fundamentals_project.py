#Develop a simple script that requests the user's grades in three subjects and determines whether they have passed or failed, based on the average obtained.**

#1. **Data input:** asks the user to enter grades for three subjects  
#2. **Average calculation:** calculates the average of the entered grades  
#3. **Academic status determination:** uses a control flow structure to determine if the student passes or fails  
#4. **Functions:** organizes the code using functions to modularize the logic  
#5. **Text strings:** forms simple messages to indicate the student's academic status

name = input("Enter your name: ")
subject1 = float(input("Enter the grade for subject 1: "))
subject2 = float(input("Enter the grade for subject 2: "))
subject3 = float(input("Enter the grade for subject 3: "))

def calculate_average(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return average

def determine_status(average):
    if average >= 6:
        return "passed"
    else:
        return "failed"
average_grade = calculate_average(subject1, subject2, subject3)
status = determine_status(average_grade)
print(f"Student {name} has {status} with an average grade of {average_grade:.2f}.")