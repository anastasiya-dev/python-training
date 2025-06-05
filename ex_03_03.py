score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error, not a number")
    exit()
if score < 0 or score > 1:
    print("Error, not a grade")
    exit()
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
