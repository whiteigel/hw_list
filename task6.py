import random
import time

activities = ["SyncSwap", "Izumi Finance", "Rhino Bridge", "Owlto Daily", "Rubyscore Daily",
              "Maverick", "Element Market", "Clusters", "SyncFutures", "SuperForm"]

activities_target = int(input("Введите желаемое число активностей: "))
activity_count = activities_target

rand = random.choice(activities)
while activities_target > 0:
    print(rand)
    activities_target -= 1
    time.sleep(random.uniform(0.5, 1.5))

print(f"Активность {rand} была выполнена {activity_count} раз")
