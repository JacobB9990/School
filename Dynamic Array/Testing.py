from dynamic_arry import DynamicArray
from stupid_arry import SlowArray
import time
import matplotlib.pyplot as plt
import ctypes


def measure_time_for_append(container: ctypes.Array, max_size: int) -> tuple[list[float], list[int], float, list[int]]:
    times: list[float] = []
    sizes: list[int] = []
    capacity: list[int] = []

    start_time: float = time.time()

    for size in range(0, max_size + 1):
        container.append(1)  # Append an element

        times.append(time.time() - start_time)  # Record time
        sizes.append(size)  # Record size
        cap: int = container.findCapacity()  # Get current capacity
        capacity.append(cap)

    final_time: float = time.time() - start_time  # Total time taken

    return times, sizes, final_time, capacity


# Initialize DynamicArray and SlowArray instances
dynamic_array: DynamicArray = DynamicArray()
slow_array: SlowArray = SlowArray()
max_size: int = 1000  # Define the maximum size for the test

# Measure the time for appending elements to each array
time_dyn, no_obj_dyn, fin_time_dyn, capacity_dyn = measure_time_for_append(dynamic_array, max_size)
time_slo, no_obj_slo, fin_time_slo, capacity_slo = measure_time_for_append(slow_array, max_size)

# Not important
# print("Dynamic Array size: ")
# print(f'{time_dyn} \n'
#       f'{no_obj_dyn} \n'
#       f'{fin_time_dyn}\n'
#       f'Capacity: {capacity_dyn} \n')
# print("Slow Array size: ")
# print(f'{time_slo} \n'
#       f'{no_obj_slo} \n'
#       f'{fin_time_slo}\n'
#       f'Capacity: {capacity_slo} \n')

# print(fin_time_dyn, fin_time_slo)

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.plot(no_obj_dyn, time_dyn, 'o', color='blue', label='DynamicArray', markersize=3)
ax.plot(no_obj_slo, time_slo, 'o', color='red', label='Stupid List', markersize=3)

# Coloring
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.title.set_color('white')

# Labels
plt.title('Performance Comparison: Dynamic Array vs. Slow List')
plt.xlabel('No. of elements')
plt.ylabel('Time (sec)')
plt.legend()

ax.set_ylim([max(max(time_dyn), max(time_slo)) * -0.25, max(max(time_dyn), max(time_slo)) * 1.1])

plt.show()
