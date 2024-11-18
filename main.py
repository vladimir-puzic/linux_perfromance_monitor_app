import psutil
import os

cpu = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
mem_percent = mem[2]
mem_used = mem[3]
mem_total = mem[0]

disks = psutil.disk_partitions()

processes =[] 
for process in psutil.process_iter(['pid']):
    processes.append((process.pid, process.cpu_percent(interval=0.1)))

def order_by_cpu_usage(process):
    return process[1]

processes.sort(key=order_by_cpu_usage, reverse=True)

cpu_usage_top_five = []
for process in processes[0:5]:
    process_info = psutil.Process(pid=process[0])
    cpu_usage_top_five.append(f'{process_info.name()}: {process[1]}%')


print(f'CPU: {cpu}%')
print(f'RAM: {mem_percent}% - {(mem_used / 1000000000):.2f} GB / {(mem_total / 1000000000):.2f} GB')
print()
print ('Top 5 processes by CPU usage:')
for item in cpu_usage_top_five:
    print (item)
print()
for disk in disks:
    disk_total, disk_used, disk_free, disk_percent = psutil.disk_usage(disk[0])

    print (disk[0], f'- {disk_percent} %')
    
    print (f'Total space: {(disk_total / 1000000000):.2f} GB')
    print (f'Used space: {(disk_used / 1000000000):.2f} GB')
    print (f'Free space: {(disk_free / 1000000000):.2f} GB')

os.system('pause')