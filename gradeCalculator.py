def main():
    work = ['homework', 'daily work', 'major grade work']
    work2 = ['homework', 'daily work', 'major grade work']
    PercentInt = list()
    GradeInt = list()
    y = 0
    x = 0

    def percentage(number1):
        return float(number1 / 100)

    def multiply(number1, number2):
        return int(number1 * number2)

    def grade(number1, number2, number3):
        return int(number1 + number2 + number3)

    for i in work:
        PercentInt.append(int(input("what percentage of your grade is " + str(work[y]) + ":")))
        y += 1

    for j in work2:
        GradeInt.append(int(input("what is your average " + str(work2[x]) + " grade:")))
        x += 1

    HwPercentage = percentage(PercentInt[0])
    dailyPercentage = percentage(PercentInt[1])
    majorPercentage = percentage(PercentInt[2])

    avgHwGrade = GradeInt[0]
    avgDailyGrade = GradeInt[1]
    avgMajorGrade = GradeInt[2]

    if HwPercentage + dailyPercentage + majorPercentage == 1:
        HwGrade = multiply(HwPercentage, avgHwGrade)
        dailyGrade = multiply(dailyPercentage, avgDailyGrade)
        majorGrade = multiply(majorPercentage, avgMajorGrade)

        yourGrade = grade(HwGrade, dailyGrade, majorGrade)
        if yourGrade < 0:
            print(
                "I have no idea what happened \n How do you get a negative grade??? \n you probably put in a negative "
                "grade on accident \n how do you accidentally type the - symbol.")
        if yourGrade > 0:
            print("Your grade is: " + str(yourGrade))
        else:
            print("your grade is either 0 or there is a bug here that i couldn't for see \n and if your grade is 0 wtf "
                  "are you doing \n you could turn in literally garbage and probably have at least a 40")

    else:
        print("your percentages do not add up so any answer give to you would be wrong")


if __name__ == '__main__':
    main()
