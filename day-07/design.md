# Log Analyzer CLI – Design Plan

## What problem am I solving?

In production systems, application logs become very large and manual checking is not practical.
This script helps automatically analyze logs and count how many INFO, WARNING, and ERROR messages are present.

---

## What input does my script need?

- Log file path (example: app.log)
- Output file path (example: summary.txt)
- Optional log level filter (INFO / WARNING / ERROR)

---

## What output should my script give?

- Print log summary on terminal  
- Write the same summary into an output file

Example Output:

INFO: 12  
WARNING: 3  
ERROR: 1  

---

## What are the main steps?

1. User runs CLI command with file paths
2. Script reads the log file
3. Script checks each line and counts log levels
4. Script prints summary to terminal
5. Script writes summary into output file

---

## Why this planning is important?

- Helps avoid confusion before writing code  
- Makes script logic clear  
- Reduces bugs in automation
