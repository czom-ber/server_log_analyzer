# analyzer.py

from collections import defaultdict
from datetime import timedelta

def find_suspicious_ips(entries, threshold, window_seconds):
    ip_timestamps = defaultdict(list)

    for ip, timestamp in entries:
        ip_timestamps[ip].append(timestamp)
    
    suspicious_ips = set()
    
    for ip, timestamps in ip_timestamps.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window_start = timestamps[i]
            window_end = window_start + timedelta(seconds=window_seconds)
            count = 1
            for j in range(i + 1, len(timestamps)):
                if timestamps[j] <= window_end:
                    count += 1
                else:
                    break
            if count >= threshold:
                suspicious_ips.add(ip)
                break
    
    return suspicious_ips
