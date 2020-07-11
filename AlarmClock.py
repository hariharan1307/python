import datetime
print("Required format : hr:min am/pm--> 07:20 am")
inputTime = input("WakeUp time? :")
WakeupList = inputTime.split(" ")
DayOrNight=WakeupList[1]
Time = WakeupList[0]
WakeupTime=Time.split(":")
hour=int(WakeupTime[0])
minutes = int(WakeupTime[1])

if DayOrNight=="pm":
    hour+=12


def validation(hr,min):
    if hr > 24:
        if min > 60:
            print("hours and minutes should not exceed the standard time limits")
            return False
        print("hours should not exceed 24")
        return False

    print("waiting for the alarm ", str(hour).zfill(2), ":", str(minutes).zfill(2),DayOrNight)

    return True


if validation(hour,minutes):
    while True:
        if hour==datetime.datetime.now().hour and minutes== datetime.datetime.now().minute:
            print("its ",str(hour).zfill(2),":",str(minutes).zfill(2),DayOrNight, " time to wakeup kid!!!!")
            break
