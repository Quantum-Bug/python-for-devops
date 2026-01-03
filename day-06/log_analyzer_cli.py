import argparse


class LogAnalyzer:
    def __init__(self, log_file, level=None):
        self.log_file = log_file
        self.level = level
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
            print(f"Error: Log file '{self.log_file}' not found.")
            return []

    def analyze_logs(self, lines):
        for line in lines:
            for level in self.log_counts:
                if level in line:
                    if self.level is None or self.level == level:
                        self.log_counts[level] += 1

    def write_summary(self, output_file):
        with open(output_file, "w") as file:
            file.write("Log Analysis Summary\n")
            for level, count in self.log_counts.items():
                file.write(f"{level}: {count}\n")

    def print_summary(self):
        print("\nLog Analysis Summary")
        for level, count in self.log_counts.items():
            print(f"{level}: {count}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI Log Analyzer Tool")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", default="log_summary.txt",
                        help="Output file path (default: log_summary.txt)")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR"],
                        help="Filter by log level (optional)")
    return parser.parse_args()


def main():
    args = parse_arguments()

    analyzer = LogAnalyzer(args.file, args.level)
    lines = analyzer.read_logs()
    analyzer.analyze_logs(lines)
    analyzer.write_summary(args.out)
    analyzer.print_summary()
    print(f"\nSummary saved to: {args.out}")


if __name__ == "__main__":
    main()
