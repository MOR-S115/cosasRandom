import random as rm
import time as tm

random_time = rm.uniform(0,6)
tm.sleep(random_time)
time_start = tm.time()
input("¡AHORA!")
time_end = tm.time()
print (f"has tardado {time_end-time_start:.3f}s")

