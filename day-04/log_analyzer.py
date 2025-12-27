def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                raise ValueError("Log file is empty")

            return lines

    except FileNotFoundError:
        print("❌ Log file not found!")
        return None

    except ValueError as e:
        print(f"❌ {e}")
        return None


def analyze_logs(file_path):
    lines = read_log_file(file_path)

    if not lines:
        return

    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1

    print_summary(log_counts)
    write_summary_to_file(log_counts)


def print_summary(log_counts):
    print("\n--- Log Summary ---")
    for level, count in log_counts.items():
        print(f"{level}: {count}")


def write_summary_to_file(log_counts):
    try:
        with open("log_summary.txt", "w") as file:
            file.write("Log Summary\n")
            file.write("------------------\n")
            for level, count in log_counts.items():
                file.write(f"{level}: {count}\n")

        print("\n✅ Summary written to log_summary.txt")

    except Exception as e:
        print(f"❌ Failed to write summary: {e}")


if __name__ == "__main__":
    analyze_logs("app.log")
