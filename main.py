import psutil
cpu = psutil.cpu_percent(interval=1)
mem_total, mem_available, mem_percent, mem_used, mem_free = psutil.virtual_memory()

print(f'CPU: {cpu}%')
print(f'RAM: {mem_percent}% - {(mem_used / 1000000000):.2f} / {(mem_total / 1000000000):.2f}')