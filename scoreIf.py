# 3.3 Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

score = input("Enter Score between 0.0 an 1.0 : ")
sc = float(score)
if sc < 0.0:
    print("A valid score should equal too, or larger than 0.0 ")
    exit()
elif sc > 1.0:
    print("A valid score should be less than or smaller than 1.0 ")
    exit()
elif sc >= 0.9:
    print("A")
    exit()
elif sc >= 0.8:
    print("B")
    exit()
elif sc >= 0.7:
    print("C")
    exit()
elif sc >= 0.6:
    print("D")
    exit()
elif sc < 0.6:
    print("F")
    exit()
