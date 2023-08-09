#Goodmorning World

import time

print("goodMorning Running x")

def goodMorning():
    input("\nGood Morning Louis!, Love you x\n")

def runInMorning(hour, minute):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            goodMorning()
            break
        time.sleep(60)

#if __name__ == "__main__":
target_hour = 9
target_minute = 30

runInMorning(target_hour,target_minute)