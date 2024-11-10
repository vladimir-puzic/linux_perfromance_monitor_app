import psutil
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()
mem_percent = mem[2]
mem_used = mem[3]
mem_total = mem[0]

print(f'CPU: {cpu}%')
print(f'RAM: {mem_percent}% - {(mem_used / 1000000000):.2f} / {(mem_total / 1000000000):.2f}')