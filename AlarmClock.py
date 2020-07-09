import datetime
print("Required format : hr:min:sec--> 07:20:45")
WakeupTimw = input("WakeUp time? :")
WakeupList = WakeupTimw.split(":")
hour = int(WakeupList[0])
minutes = int(WakeupList[1])


def validation(hr,min):
    if hr > 24:
        print("Hours should not exceed 24")
        return False
    if min > 60:
        print("Minutes should not exceed 24")
        return False

    return True

print("waiting for the alarm ", hour, ":", minutes)


while True:
    if validation(hour,minutes):
        if (hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().min):
            print("Time to wakeup kid!!!")
            break






