import psutil


def get_thresholds():
    cpu_threshold = float(input("Enter CPU usage threshold (%): "))
    memory_threshold = float(input("Enter Memory usage threshold (%): "))
    disk_threshold = float(input("Enter Disk usage threshold (%): "))
    return cpu_threshold, memory_threshold, disk_threshold


def check_system_health(cpu_t, mem_t, disk_t):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print("\n--- System Health Report ---")
    print(f"CPU Usage    : {cpu_usage}%")
    print(f"Memory Usage : {memory_usage}%")
    print(f"Disk Usage   : {disk_usage}%\n")

    if cpu_usage > cpu_t:
        print("⚠️ CPU usage is above threshold!")
    else:
        print("✅ CPU usage is within limits.")

    if memory_usage > mem_t:
        print("⚠️ Memory usage is above threshold!")
    else:
        print("✅ Memory usage is within limits.")

    if disk_usage > disk_t:
        print("⚠️ Disk usage is above threshold!")
    else:
        print("✅ Disk usage is within limits.")


def main():
    cpu_t, mem_t, disk_t = get_thresholds()
    check_system_health(cpu_t, mem_t, disk_t)


if __name__ == "__main__":
    main()
