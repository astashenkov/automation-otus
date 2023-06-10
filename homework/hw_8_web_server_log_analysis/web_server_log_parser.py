import json
from dataclasses import dataclass
from sys import argv


@dataclass
class RequestInfo:
    ip: str = ''
    delay: str = ''
    method: str = ''
    url: str = ''
    date: str = ''
    time: str = ''


if len(argv) > 1:
    directory: str = argv[1]
else:
    directory: str = ''


def total_completed_requests(file) -> int:
    """Calculation of the total number of executed requests."""
    log.seek(0)
    counter: int = 0
    for line in file:
        if len(line) > 1:
            counter += 1

    return counter


def total_http_requests(file):
    """Counting the total number of executed requests by HTTP methods."""
    log.seek(0)
    REQUEST_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']
    request = RequestInfo()
    counter: int = 0

    for line in file:
        request.method = line.split()[5][1:]
        if request.method in REQUEST_METHODS:
            counter += 1

    return counter


def three_most_frequently_used_ip(file):
    """Calculation of the top 3 IP addresses from which requests were made."""
    log.seek(0)
    request = RequestInfo()

    all_ips: dict = {}
    for line in file:
        request.ip = line.split()[0]
        all_ips.setdefault(request.ip, 0)
        all_ips[request.ip] += 1

    top_three_ips: str = ''
    sorted_ips: list = sorted(all_ips.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        top_three_ips += f'\n"{sorted_ips[i][0]}" – {sorted_ips[i][1]}'

    return top_three_ips


def three_longest_requests(file):
    """Calculation of the top 3 longest requests."""
    log.seek(0)
    request = RequestInfo()

    all_requests: dict = {}
    for line in file:
        request.delay = int(line.split()[-1])
        request.ip = line.split()[0]
        request.method = line.split()[5][1:]
        request.url = line.split()[10][1:-1]
        request.date = line.split()[3][1:12]
        request.time = line.split()[3][13:]

        all_requests[request.delay] = {
            'ip': request.ip,
            'method': request.method,
            'url': request.url,
            'date': request.date,
            'time': request.time
        }

    top_three_delay_request: str = ''
    sorted_request: list = sorted(all_requests.items(), reverse=True)
    for i in range(3):
        top_three_delay_request += f'\nDelay: {sorted_request[i][0]} – {sorted_request[i][1]}'

    return top_three_delay_request


result: str = '\nLOGS ANALYSIS REPORT\n\n'

with open(f'{directory}access.log', encoding='utf-8') as log:
    result += f'Total number of completed requests: {total_completed_requests(log)}\n'
    result += f'Number of requests by HTTP methods: {total_http_requests(log)}\n'
    result += f'Top 3 IP addresses from which requests were made: {three_most_frequently_used_ip(log)}\n'
    result += f'Top 3 longest requests: {three_longest_requests(log)}\n'

with open('analysis_log.json', 'w', encoding="utf-8") as json_file:
    json.dump(result, json_file)

print(result)
