import threading
import time


def my_max(values, message):
    result = max(values)
    print(f"{message} {result}")



def my_min(values, message):
    result = min(values)
    print(f"{message} {result}")



values = [3,5,1,15,25,104]

thread1 = threading.Thread(target=my_max, args=(values, "Max = ",))
thread2 = threading.Thread(target=my_min, args=(values, "Min = ",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


