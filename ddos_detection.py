import psutil
import time

# Thresholds for detecting potential DDoS attacks
CPU_THRESHOLD = 80.0  # in percent
NETWORK_THRESHOLD = 1000000  # in bytes per second (1 MB/s)

# Log file to record potential attacks
LOG_FILE = "/var/log/ddos_monitor.log"

def log_suspicious_activity(activity_type, value):
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.ctime()} - {activity_type}: {value}\n")

def monitor_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_suspicious_activity("High CPU Usage", cpu_usage)
    return cpu_usage

def monitor_network():
    net_io_start = psutil.net_io_counters()
    time.sleep(1)
    net_io_end = psutil.net_io_counters()
    
    bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
    bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv
    
    if bytes_sent > NETWORK_THRESHOLD or bytes_recv > NETWORK_THRESHOLD:
        log_suspicious_activity("High Network Traffic", f"Sent: {bytes_sent} bytes, Received: {bytes_recv} bytes")
    return bytes_sent, bytes_recv

def main():
    print("Starting DDoS monitoring script...")
    while True:
        cpu_usage = monitor_cpu()
        bytes_sent, bytes_recv = monitor_network()

        if cpu_usage > CPU_THRESHOLD and (bytes_sent > NETWORK_THRESHOLD or bytes_recv > NETWORK_THRESHOLD):
            print(f"Potential DDoS Attack Detected!\nCPU Usage: {cpu_usage}%\nNetwork Traffic - Sent: {bytes_sent} bytes, Received: {bytes_recv} bytes")

        time.sleep(1)

if __name__ == "__main__":
    main()