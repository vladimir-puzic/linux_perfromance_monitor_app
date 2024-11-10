import psutil
cpu = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
mem_percent = mem[2]
mem_used = mem[3]
mem_total = mem[0]

disks = psutil.disk_partitions()


print(f'CPU: {cpu}%')
print(f'RAM: {mem_percent}% - {(mem_used / 1000000000):.2f} GB / {(mem_total / 1000000000):.2f} GB')
for disk in disks:
    disk_total, disk_used, disk_free, disk_percent = psutil.disk_usage(disk[0])

    print (disk[0], f'- {disk_percent} %')
    
    print (f'Total space: {(disk_total / 1000000000):.2f} GB')
    print (f'Used space: {(disk_used / 1000000000):.2f} GB')
    print (f'Free space: {(disk_free / 1000000000):.2f} GB')