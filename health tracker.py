def check_water(water):
    if water >=8:
        return"Great job! you drank enough water today."
    else:
        return"Try to drink at least 8 glasses of water."
    
def check_sleep(sleep):
    if sleep>=7:
        return"Nice! You got good sleep."
    else:
        return("Try to get at least 7hr of sleep")

def check_mood(mood):
    if mood >=7:
        return"you seem to be in good today!"
    else:
        return"take some time for self-care to boost yours mood."     


import csv
from datetime import date


def save_data(data):
    with open ('data.csv','a',newline ='')as file:
        writer= csv.writer(file)
        writer.writerow(data)

def main():
    print("Welcome to Healthy Habits Tracker!")
    water=int(input("Enter glasses of water you drank today:"))
    sleep=float(input('Enter hours of sleep you got last night:'))
    mood=int(input("Enter Rate your mood today(1-10):"))

    #check health_goals
    water_feedback=check_water(water)
    sleep_feedback=check_sleep(sleep)
    mood_feedback=check_mood(mood)

    #display feedback
    print(water_feedback)
    print(sleep_feedback)
    print(mood_feedback)

    #save data
    today =date.today().isoformat()
    save_data([today,water ,sleep,mood])

if __name__=="__main__":
    main()    

