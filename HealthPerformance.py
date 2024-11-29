import psutil
import time

def monitor_cpu(threshold=80):
    """
    Monitors the CPU usage of the local machine and raises an alert
    if the usage exceeds the given threshold.

    :param threshold: CPU usage percentage that triggers an alert.
    """
    print("Monitoring CPU usage...")
    try:
        while True:
            # Get the current CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            
            # Pause slightly to avoid excessive resource usage
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Define the CPU usage threshold
    THRESHOLD = 80

    # Start monitoring
    monitor_cpu(THRESHOLD)
