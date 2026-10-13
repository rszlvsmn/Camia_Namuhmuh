
#Ask For User's Name
name = input("Please enter your name: ")


#Display Title & Add a Separator
def display_header():
    print(" Student Performance Evaluator")
    print("========================================")

#Get Student's Scores
def get_student_info():
    score1 = input("Please enter assessment 1 score:   ")
    score2 = input("Please enter assessment 2 score:   ")
    score3 = input("Please enter assessment 3 score:   ")
    return score1, score2, score3

# Calculate Average and Evaluate Performance Level
def evaluate_performance():
    average = (score1 + score2 + score3) / 3
    if average >= 90:
        status = "Outstanding"
    elif average <= 89 and average >= 85:
        status = "Very Satisfactory"
    elif average <= 84 and average >= 80:
        status = "Satisfactory"
    elif average <= 79 and average >= 75:
        status = "Fairly Satisfactory"
    else:
        status = "Needs Improvement"
    return average, status


#Display Name, Score, Average, Performance Level
def display_report():
    print("STUDENT PERFORMANCE REPORT")
    print(f"Name: {name}")
    print(f"Score 1: {score1}")
    print(f"Score 2: {score2}")
    print(f"Score 3: {score3}")
    print(f"Average: {average}.2f ")
    print(f"Performance Level: {status}")

display_header()
get_student_info()
evaluate_performance()
display_report()

# Russell Jake A. Namuhmuh, 8 - Camia







