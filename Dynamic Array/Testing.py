from dynamic_arry import DynamicArray
import time
import matplotlib.pyplot as plt


def measure_time_for_append(container, max_size):
    times = []
    sizes = []
    start_time = time.time()

    for size in range(0, max_size + 1):
        append_start_time = time.time()
        container.append(1)
        append_total_time = time.time() - append_start_time

        times.append(append_total_time)
        sizes.append(size)

    total_time = time.time() - start_time
    return times, sizes, total_time,


a = DynamicArray()
b = []
max_size = 10000

time_n1, no_obj1, total_time_a = measure_time_for_append(a, max_size)
print("DynamicArray:")
print("Total time:", total_time_a)

time_n2, no_obj2, total_time_b = measure_time_for_append(b, max_size)
print("Python list:")
print("Total time:", total_time_b)

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.plot(no_obj1, time_n1, marker='o', color='blue', label='DynamicArray')
ax.plot(no_obj2, time_n2, marker='x', color='red', label='Python list')

ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.title.set_color('white')

plt.title('Performance Comparison: DynamicArray vs. Python List')
plt.xlabel('No. of elements')
plt.ylabel('Time (sec)')
plt.legend()
plt.show()
