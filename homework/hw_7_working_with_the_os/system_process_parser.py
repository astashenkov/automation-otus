import subprocess
from datetime import datetime
from operator import itemgetter

print('Start of processing\n...')

current_processes = subprocess.run(['ps', 'aux'], capture_output=True, text=True, check=True).stdout
lines = current_processes.split('\n')

current_processes_count = 0
max_cpu_process = [0, '']
max_memory_process = [0, '']
total_memory = 0
total_cpu = 0
users = set()
user_processes = {}

for line in lines[1:]:
    if line:
        values = line.split()

        current_processes_count += 1
        total_cpu += float(values[2])
        total_memory += float(values[3])

        user = values[0]
        users.add(user)

        user_processes.setdefault(user, 0)
        user_processes[user] += 1

        if float(values[3]) > max_memory_process[0]:
            max_memory_process[0] = float(values[3])
            max_memory_process[1] = values[10]

        if float(values[2]) > max_cpu_process[0]:
            max_cpu_process[0] = float(values[2])
            max_cpu_process[1] = values[10]

report = "Отчёт о состоянии системы\n\n"
report += "Пользователи системы:\n"
for user in sorted(users):
    report += f"{user}\n"
report += f"\nПроцессов запущено: {current_processes_count}\n"
report += "Пользовательских процессов:\n"
for user, count in sorted(user_processes.items(), key=itemgetter(1), reverse=True):
    report += f"{user} – {count}\n"
report += f"\nВсего памяти используется: {total_memory:.1f}%\n"
report += f"Всего CPU используется: {total_cpu:.1f}%\n"
report += f"Больше всего памяти использует: {max_memory_process[1]} ({max_memory_process[0]}%)\n"
report += f"Больше всего CPU использует: {max_cpu_process[1]} ({max_cpu_process[0]}%)\n"

current_datetime = datetime.now().strftime("%d-%m-%Y-%H:%M")
filename = f"{current_datetime}-scan.txt"
with open(filename, 'w', encoding='utf-8') as file:
    file.write(report)

print('DONE')
