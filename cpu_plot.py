#!/usr/bin/env python

def make_plot(x, y, title):

  # Plot the data
  plt.plot(x, y, 'b-', linewidth=3)
  plt.title('CPU usage for ' + title, fontsize=20)
  plt.xlabel('Timestamp (s)', fontsize=20)
  plt.ylabel('CPU usage (%)', fontsize=20)
  plt.ylim([0,100])

  # Get the time, append it to the filename
  time = str(datetime.datetime.now())
  time = time.rpartition('.')[0]
  time = time.replace(' ', '-')
  time = time.replace(':', '-')

  # Save the figure
  plt.savefig('plots/' + title + '_' + time + '.png')

  # Show the plot
  plt.show()

def main(THIS_DIR):

  if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: >> ./cpu_plot PROCESS_NAME"
    sys.exit(1)

  process_id = sys.argv[1]

  # Calling this bash script will process the
  # cpu monitor file into a nice list of line numbers
  # and CPU% datapoints
  subprocess.call('./process_cpu.sh ' + process_id, shell=True);

  cpu_file = THIS_DIR + '/cpu_process_usage.txt'

  with open(cpu_file) as f:
    data = [line.strip() for line in f]

  times = [dpt.partition(',')[0].strip() for dpt in data]
  cpu = [dpt.partition(',')[2].strip() for dpt in data]

  # Make sure the plots directory exists
  PLOTS_DIR = THIS_DIR + '/plots'
  if (not os.path.exists(PLOTS_DIR)):
    os.makedirs(PLOTS_DIR)

  # Plot the data
  make_plot(times, cpu, process_id)

if __name__=='__main__':
  import sys, os, subprocess, datetime
  import matplotlib.pyplot as plt
  import numpy as np

  sys.dont_write_bytecode = True

  THIS_DIR = sys.path[0]

  main(THIS_DIR)
