from dynamic_arry import DynamicArray
from stupid_arry import SlowArray
import time
import matplotlib.pyplot as plt


def measure_time_for_append(container, max_size):
    times, sizes = [], []
    start_time = time.time()

    for size in range(max_size + 1):
        container.append(1)
        times.append(time.time() - start_time)
        sizes.append(size)

    return times, sizes, time.time() - start_time


dynamic_array = DynamicArray()
slow_array = SlowArray()
max_size = 1000

time_dyn, no_obj_dyn, fin_time_dyn = measure_time_for_append(dynamic_array, max_size)
time_slo, no_obj_slo, fin_time_slo = measure_time_for_append(slow_array, max_size)

print(fin_time_dyn, fin_time_slo)

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.plot(no_obj_dyn, time_dyn, marker='o', color='blue', label='DynamicArray', markersize=3, linewidth=1, alpha=0.7)
ax.plot(no_obj_slo, time_slo, marker='x', color='red', label='Python list', markersize=3, linewidth=1, alpha=0.7)

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

ax.set_ylim([0, max(max(time_dyn), max(time_slo)) * 1.1])

plt.show()
