from dynamic_arry import DynamicArray
from stupid_arry import SlowArray
import time
import matplotlib.pyplot as plt
import threading

# just initializing these variables
time_dyn = None
fin_time_dyn = None
time_slo = None
fin_time_slo = None


def measure_time_for_append(container, max_size: int) -> tuple[list[float], float]:
    times: list[float] = []

    for size in range(max_size + 1):
        start_time: float = time.perf_counter()
        container.append(1)  # Append an element
        elapsed_time: float = time.perf_counter() - start_time
        times.append(elapsed_time)

    final_time: float = sum(times)  # Total time taken

    return times, final_time


def measure_dynamic_array():  # These are Threads
    global time_dyn, fin_time_dyn
    time_dyn, fin_time_dyn = measure_time_for_append(dynamic_array, max_size)


def measure_slow_array():  # These are Threads
    global time_slo, fin_time_slo
    time_slo, fin_time_slo = measure_time_for_append(slow_array, max_size)


# Initialize DynamicArray and SlowArray instances
dynamic_array: DynamicArray = DynamicArray()
slow_array: SlowArray = SlowArray()
max_size: int = 10000  # Define the maximum size for the test

# Threading runs both Dynamic and Slow at the same time to speed up the program
thread_dyn = threading.Thread(target=measure_dynamic_array)
thread_slo = threading.Thread(target=measure_slow_array)

thread_dyn.start()
thread_slo.start()

thread_dyn.join()
thread_slo.join()

# print(f"Dynamic Array total time: {fin_time_dyn}")
# print(f"Slow Array total time: {fin_time_slo}")
#
# print("Dynamic Array times: ")
# print(f'{time_dyn}\n')
# print("Slow Array times: ")
# print(f'{time_slo}\n')

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.plot(range(max_size + 1), time_dyn, 'o', color='blue', label='DynamicArray', markersize=3)
ax.plot(range(max_size + 1), time_slo, 'o', color='red', label='SlowArray', markersize=3)

# Coloring
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.title.set_color('white')

# Labels
plt.title('Performance Comparison: Dynamic Array vs. Slow Array')
plt.xlabel('Number of elements')
plt.ylabel('Time (sec)')
plt.legend()

# Adjust the y-axis limits to fit the data
ax.set_ylim([0, max(max(time_dyn), max(time_slo)) * 1.1])

plt.show()
