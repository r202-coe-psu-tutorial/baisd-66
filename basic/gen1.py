import datetime

def first_n(n):
    '''Build and return a list'''
    print('start generate')
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    print('stop generate')
    return nums

start_time = datetime.datetime.now()

data = first_n(100_000_000)
stop_gen_time = datetime.datetime.now()
sum_of_first_n = sum(data)
stop_time = datetime.datetime.now()

print('time gen', stop_gen_time-start_time)
print('time sum', stop_time-stop_gen_time)
print('total', stop_time-start_time)