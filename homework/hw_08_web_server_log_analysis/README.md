# Script for analyzing *.log files

This script analyzes *.log files, collects statistics and saves the results in JSON format.

## Requirements

- Python 3.x

## Using

Run the script with the following command:

```
python3 web_server_log_parser.py log_path [-o output_file]
```

Where:

- log_path: the path to the log file or directory containing the log files.
- output_file (optional): path to output JSON file.

The script analyzes all log files in a specified directory or a specified log file. The results of the analysis are
displayed in the terminal and can be saved in a JSON file if the -o option is used.

## Analysis results

The results of the analysis include:

- The total number of requests executed.
- The number of requests by HTTP methods.
- Top 3 IP addresses from which requests were made.
- Top 3 longest requests, including method, URL, IP address, duration, date and time of the request.
