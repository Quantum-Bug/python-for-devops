class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def read_logs(self):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()

                if not lines:
                    print("Log file is empty.")
                    return []

                return lines

        except FileNotFoundError:
            print("Log file not found.")
            return []

    def analyze_logs(self, lines):
        for line in lines:
            if "INFO" in line:
                self.log_counts["INFO"] += 1
            elif "WARNING" in line:
                self.log_counts["WARNING"] += 1
            elif "ERROR" in line:
                self.log_counts["ERROR"] += 1

    def write_summary(self):
        with open("log_summary.txt", "w") as file:
            file.write("Log Analysis Summary\n")
            for level, count in self.log_counts.items():
                file.write(f"{level}: {count}\n")

    def print_summary(self):
        print("\nLog Analysis Summary")
        for level, count in self.log_counts.items():
            print(f"{level}: {count}")


def main():
    analyzer = LogAnalyzer("app.log")
    lines = analyzer.read_logs()
    analyzer.analyze_logs(lines)
    analyzer.write_summary()
    analyzer.print_summary()


if __name__ == "__main__":
    main()