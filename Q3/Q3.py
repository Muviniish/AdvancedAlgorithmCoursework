import random
import threading
import time

def generate_random_numbers(index):
    start_time = time.time_ns()
    _ = [random.randint(0, 10000) for _ in range(100)]
    end_time = time.time_ns()
    results[index] = (start_time, end_time)

def generate_random_numbers2():
    start_time2 = time.time_ns()
    _ = [random.randint(0, 10000) for _ in range(100)]
    end_time2 = time.time_ns()
    return (start_time2, end_time2)

all_total_time = []
all_total_time2 = []
rounds = 10

print("\nRound-by-Round Performance Comparison:")
print("+-------------------+-----------------------------+-------------------------------+----------------------------+")
print("| Round             | Multithreading Time (ns)    | Non-Multithreading Time (ns)  | Difference (ns)            |")
print("+-------------------+-----------------------------+-------------------------------+----------------------------+")

for i in range(rounds):
    results = [None, None, None]

    t1 = threading.Thread(target=generate_random_numbers, args=(0,))
    t2 = threading.Thread(target=generate_random_numbers, args=(1,))
    t3 = threading.Thread(target=generate_random_numbers, args=(2,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    start_times = [t[0] for t in results]
    end_times = [t[1] for t in results]
    total_time = max(end_times) - min(start_times)
    all_total_time.append(total_time)

    results2 = [generate_random_numbers2() for _ in range(3)]
    start_times2 = [t[0] for t in results2]
    end_times2 = [t[1] for t in results2]
    total_time2 = max(end_times2) - min(start_times2)
    all_total_time2.append(total_time2)

    difference = total_time - total_time2
    print(f"| {i+1:^17} | {total_time:^27,} | {total_time2:^29,} | {difference:^26,} |")

print("+-------------------+-----------------------------+-------------------------------+----------------------------+")

total_thread = sum(all_total_time)
total_sequential = sum(all_total_time2)
avr_total_thread = total_thread / rounds
avr_total_sequential = total_sequential / rounds
total_diff = total_thread - total_sequential
avr_total_diff = avr_total_thread - avr_total_sequential

print("\nSummary of Results:")
print("+-------------------+-----------------------------+-------------------------------+----------------------------+")
print("| Metric            | With Threads (ns)           | Without Threads (ns)          | Time Difference (ns)       |")
print("+-------------------+-----------------------------+-------------------------------+----------------------------+")
print(f"| Total Time        | {total_thread:^27,} | {total_sequential:^29,} | {total_diff:^26,} |")
print(f"| Average Time      | {avr_total_thread:^27,.1f} | {avr_total_sequential:^29,.1f} | {avr_total_diff:^26,.1f} |")
print("+-------------------+-----------------------------+-------------------------------+----------------------------+")
