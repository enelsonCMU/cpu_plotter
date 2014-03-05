#!/bin/bash
#THIS_DIR="/home/erik/Python/Scripts/cpu_monitoring"
TOP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IN_FILE="cpu_usage.txt"
OUT_FILE="cpu_process_usage.txt"

# 1 Read the file
# 2 Search for lines containing the argument string
# 3 Grab the lines corresponding to CPU usage
# 4 Stick a comma in
# 5 Add line numbers
# 6 Write to file
cat ${TOP_DIR}/${IN_FILE} | grep $1 | cut -c 43-45 | awk '{print ","$0}' | nl -i 1 > ${TOP_DIR}/${OUT_FILE}
