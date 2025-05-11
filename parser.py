# parser.py

import re
from datetime import datetime

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+|-)'
)

def parse_log_datetime(dt_str):
    return datetime.strptime(dt_str, '%d/%b/%Y:%H:%M:%S %z')

def load_logs(file_path):
    entries = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                ip = match.group('ip')
                dt = parse_log_datetime(match.group('datetime'))
                entries.append((ip, dt))
    return entries
