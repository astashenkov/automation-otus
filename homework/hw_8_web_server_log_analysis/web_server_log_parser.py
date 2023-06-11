import os
import json
import argparse
from dataclasses import dataclass
from sys import argv


@dataclass
class RequestInfo:
    """Dataclass to define the request structure."""
    ip: str = ''
    duration: str = ''
    method: str = ''
    url: str = ''
    date: str = ''
    time: str = ''


def total_completed_requests(file) -> int:
    """Calculation of the total number of executed requests."""
    file.seek(0)
    counter: int = 0

    for line in file:
        if len(line) > 1:
            counter += 1

    return counter


def total_http_requests(file) -> dict:
    """Counting the total number of executed requests by HTTP methods."""
    file.seek(0)
    request = RequestInfo()
    method_counter: dict = {}
    result: dict = {}

    for line in file:
        request.method = line.split()[5][1:]
        method_counter.setdefault(request.method, 0)
        method_counter[request.method] += 1

    for method, count in sorted(method_counter.items(), key=lambda x: x[1], reverse=True):
        result[method] = count

    return result


def three_most_frequently_used_ip(file) -> dict:
    """Calculation of the top 3 IP addresses from which requests were made."""
    file.seek(0)
    request = RequestInfo()

    all_ips: dict = {}
    for line in file:
        request.ip = line.split()[0]
        all_ips.setdefault(request.ip, 0)
        all_ips[request.ip] += 1

    top_three_ips: dict = {}
    sorted_ips: list = sorted(all_ips.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        top_three_ips[sorted_ips[i][0]] = sorted_ips[i][1]

    return top_three_ips


def three_longest_requests(file) -> list:
    """Calculation of the top 3 longest requests."""
    file.seek(0)
    request = RequestInfo()

    all_requests: dict = {}
    for line in file:
        request.duration = int(line.split()[-1])
        request.ip = line.split()[0]
        request.method = line.split()[5][1:]
        request.url = line.split()[10][1:-1]
        request.date = line.split()[3][1:12]
        request.time = line.split()[3][13:]

        all_requests[request.duration] = {
            'ip': request.ip,
            'method': request.method,
            'url': request.url,
            'date': request.date,
            'time': request.time
        }

    top_three_delay_request: list = []
    sorted_request: list = sorted(all_requests.items(), reverse=True)
    for i in range(3):
        updated_request = sorted_request[i][1]
        updated_request['duration'] = sorted_request[i][0]
        top_three_delay_request.append(updated_request)

    return top_three_delay_request


def parse_arguments():
    """Processing command line arguments."""
    parser = argparse.ArgumentParser(description='Log file analysis')
    parser.add_argument('log_path', metavar='log_path', type=str, help='Path to log file or directory')
    parser.add_argument('-o', '--output', metavar='output_file', type=str, help='JSON output file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    log_path = args.log_path
    output_file = args.output

    if os.path.isfile(log_path):
        log_files = [log_path]
    elif os.path.isdir(log_path):
        log_files = [os.path.join(log_path, file) for file in os.listdir(log_path) if file.endswith('.log')]
    else:
        raise ValueError('The specified path is not a directory or file')

    results: list = []
    for log_file in log_files:
        with open(log_file, 'r', encoding='UTF-8') as file:
            result: dict = {
                'Log file': file.name.split('/')[-1],
                'Total completed requests': total_completed_requests(file),
                'Number of requests by HTTP methods': total_http_requests(file),
                'Top 3 IP addresses from which requests were made': three_most_frequently_used_ip(file),
                'Top 3 longest requests': three_longest_requests(file)
            }
            results.append(result)

    if output_file:
        with open(output_file, 'w', encoding='UTF-8') as file:
            json.dump(results, file, indent=4)

    for result in results:
        print(f'Log File: {result["Log file"]}')
        print(f'Total completed requests: {result["Total completed requests"]}')
        print('Number of requests by HTTP methods:')
        for method, count in result['Number of requests by HTTP methods'].items():
            print(f'  {method}: {count}')
        print('Top 3 IP addresses from which requests were made:')
        for ip, count in result['Top 3 IP addresses from which requests were made'].items():
            print(f'  "{ip}" – {count}')
        print('Top 3 longest requests:')
        for request in result['Top 3 longest requests']:
            print(f'  Method: {request["method"]}')
            print(f'  URL: {request["url"]}')
            print(f'  IP: {request["ip"]}')
            print(f'  Duration: {request["duration"]} ms')
            print(f'  Date: {request["date"]}')
            print(f'  Time: {request["time"]}')
            print()
