import datetime

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


start = datetime.datetime.now()
sum_of_first_n = sum(firstn(100_000_000))
stop = datetime.datetime.now()
print("data:", sum_of_first_n)
print("time", stop-start)