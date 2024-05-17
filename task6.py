import random
import time
"""
Создайте список из 10 разных активностей. Программа должна спрашивать сколько транзакций нужно выполнить.
Создайте программу которая будет рандомно выбирать одну из активностей и выполнять ее (печатать в консоль), после рандомной паузы повторяет
пока не сделает запрошенное количество транзакций.

HARD LEVEL:
доработай программу так чтобы она печатала сколько раз была выполнена каждая активность.
"""

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
