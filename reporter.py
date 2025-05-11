# reporter.py

def print_report(ips):
    if ips:
        print("Podejrzane adresy IP:")
        for ip in ips:
            print(ip)
    else:
        print("Brak podejrzanych adresów IP.")

def save_report_to_file(ips, filename='suspicious_ips.txt'):
    with open(filename, 'w') as f:
        for ip in ips:
            f.write(ip + '\n')
