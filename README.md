# cpu_plotter:

## A python-based CPU plotting utility

## To download:

      cd ~/DOWNLOAD_PATH
      git clone https://github.com/enelsonCMU/cpu_plotter.git

## Use:

From the cpu_plotter directory, record your CPU usage by calling

      ./monitor_cpu.sh

Pick a process name to plot, and call cpu_plot using that process as an argument

      ./cpu_plot.py PROCESS_NAME

For example, a plot of the CPU usage of process "laser_ukf" over time might look like the following

![ScreenShot](https://raw.github.com/enelsonCMU/cpu_plotter/master/example.png)

This plot will also be saved to the "plots" directory.
