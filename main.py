# main.py

from config import LOG_FILE, REQUEST_THRESHOLD, TIME_WINDOW_SECONDS
from parser import load_logs
from analyzer import find_suspicious_ips
from reporter import print_report, save_report_to_file

def main():
    entries = load_logs(LOG_FILE)
    suspicious_ips = find_suspicious_ips(entries, REQUEST_THRESHOLD, TIME_WINDOW_SECONDS)
    print_report(suspicious_ips)
    save_report_to_file(suspicious_ips)

if __name__ == "__main__":
    main()
