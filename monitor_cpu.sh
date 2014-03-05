#!/bin/bash

TOP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT_FILE="cpu_usage.txt"

echo "Monitoring CPU usage and saving to ${TOP_DIR}/${OUT_FILE} (Ctrl+C to stop)."

top -b -d 1 > ${TOP_DIR}/${OUT_FILE}
