import subprocess
from dataclasses import dataclass
from datetime import datetime

current_processes = subprocess.run(['ps', 'aux'], capture_output=True, text=True, check=True).stdout
lines = [line for line in current_processes.split('\n') if line][1:]


@dataclass
class ProcessInfo:
    name: str = None
    value: float = 0


max_cpu_process = ProcessInfo()
max_memory_process = ProcessInfo()

current_processes_count: int = 0
total_memory: float = 0
total_cpu: float = 0
users = set()
user_processes = {}

for line in lines:
    values = line.split()
    cpu = float(values[2])
    mem = float(values[3])

    current_processes_count += 1
    total_cpu += cpu
    total_memory += mem

    user = values[0]
    users.add(user)

    user_processes.setdefault(user, 0)
    user_processes[user] += 1

    if mem > max_memory_process.value:
        max_memory_process.value = mem
        max_memory_process.name = values[10]

    if cpu > max_cpu_process.value:
        max_cpu_process.value = cpu
        max_cpu_process.name = values[10]

report: str = "SYSTEM STATUS REPORT\n\n"
report += "System users:\n"
for user in sorted(users):
    report += f"{user}\n"
report += f"\nProcesses are running: {current_processes_count}\n"
report += "User processes:\n"
for user, count in sorted(user_processes.items(), key=lambda x: x[1], reverse=True):
    report += f"{user} – {count}\n"
report += f"\nTotal memory used: {total_memory:.1f}%\n"
report += f"Total CPU used: {total_cpu:.1f}%\n"
report += f"The most memory usage is: {max_memory_process.name} ({max_memory_process.value}%)\n"
report += f"The most CPU usage is: {max_cpu_process.name} ({max_cpu_process.value}%)\n"

current_datetime = datetime.now().strftime("%d-%m-%Y-%H:%M")
filename = f"{current_datetime}-scan.txt"
with open(filename, 'w', encoding='utf-8') as file:
    file.write(report)

print(report)
