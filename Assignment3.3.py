while True:
    try:
        score = input("Enter Score: ")
        score = float(score)
        if 0.1 <= score <= 1.0:
            break
        else:
            print("Rejected enter digit b/w 0.1 & 1.0")
    except:
        print("Not a valid score.")
        quit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
