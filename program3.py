import time


def current_milli_time():
  return time.time_ns() // 1_000_000


def is_prime(x):
  
    if x <= 1:
        return False

   
    for i in range(2, x):
        if x % i == 0:
            return False  

    return True


rs = 1000
re = 2000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re-rs), "numbers searched in", end-start, "milliseconds")
