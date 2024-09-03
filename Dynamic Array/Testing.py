from dynamic_arry import DynamicArray
from stupid_arry import SlowArray
import time
import matplotlib.pyplot as plt


def measure_time_for_append(container, max_size):
    times, sizes, capacity = [], [], []
    start_time = time.time()

    for size in range(0, max_size + 1):
        container.append(1)
        times.append(time.time() - start_time)
        sizes.append(size)
        cap = container.findCapacity()
        capacity.append(cap)

    final_time = time.time() - start_time

    return times, sizes, final_time, capacity


dynamic_array = DynamicArray()
slow_array = SlowArray()
max_size = 1000

time_dyn, no_obj_dyn, fin_time_dyn, capacity_dyn = measure_time_for_append(dynamic_array, max_size)
time_slo, no_obj_slo, fin_time_slo, capacity_slo = measure_time_for_append(slow_array, max_size)


print("Dynamic Array size: ")
print(f'{time_dyn} \n'
      f'{no_obj_dyn} \n'
      f'{fin_time_dyn}\n'
      f'Capacity: {capacity_dyn} \n')
print("Slow Array size: ")
print(f'{time_slo} \n'
      f'{no_obj_slo} \n'
      f'{fin_time_slo}\n'
      f'Capacity: {capacity_slo} \n')

print(fin_time_dyn, fin_time_slo)

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
