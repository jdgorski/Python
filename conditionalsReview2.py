# #Create a Python script that assigns a grade to a student based on their exam score.

    #functions allow me to wrap up code and reuse it
def scoreMe():
    score = int(input("Enter your score: "))
    print("You entered", score)
    # Ask the user to input a score. Assume the score is out of 100.
    # Implement the logic to determine the grade based on the score:
    # A score of 90 and above is an "A".
    if score >= 90 and score < 100:
        print("A")
    # A score of 80 to 89 is a "B".
    elif score >= 80 and score < 90:
        print("B")
    # A score of 70 to 79 is a "C".
    elif score >= 70 and score < 80:
        print("C")
    # A score of 60 to 69 is a "D".
    elif score >= 60 and score < 70:
        print("D")
    # A score below 60 is an "F".
    elif score >= 0:
        print("F")
    # Ensure the score entered is within the valid range (0-100). If not, print an error message.
    elif score > 100:
        print("You must enter a score within the range of 0-100")
    elif score < 0:
        print("You must enter a score within the range of 0-100")
    else:
        print("F")
# call the function
scoreMe()
scoreMe()
scoreMe()