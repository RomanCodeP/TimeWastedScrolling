print("welcome to the reel/tiktok calculator, with this you can see how many reels/tiktok you have seen")
print("----------------")
print("You have to input the amount of hours and minutes in 2 different questions")
print("----------------")

hours = int(input("input the amount the hours youve used instagram today: "))
minutes = int(input("input the amount of minutes you have use instagram today: "))

TotalMinutes = (hours * 60) + (minutes)
print("------------------------------------")
print("you have passed around", (TotalMinutes * 7), ("reels/tiktoks"))
print("------------------------------------")
print("With that time you could have done:")
print("------------------------------------")
print("   ")
if TotalMinutes < 30:
    print("Walked 1–2 miles, completed a short Python lesson, or prepared a meal")
elif TotalMinutes < 60:
    print("Finished a workout or studied a math topic")
elif TotalMinutes < 120:
    print("Gone to the gym, studied seriously for an exam, or built a small programming project")
elif TotalMinutes < 180:
    print("Finished several assignments, done gym + study, or made solid progress on a coding project")
elif TotalMinutes < 240:
    print("Studied almost a full unit, built a small Python project, or read around 100 pages")
elif TotalMinutes < 300:
    print("Had a long study session, built a major part of a project, or learned a new skill")
elif TotalMinutes < 360:
    print("Completed basically a full school or work day")
elif TotalMinutes < 420:
    print("Worked a full shift and still had some time left")
print("   ")
print("------------------------------------")


#7 minutes per reel
