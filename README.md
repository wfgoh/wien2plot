# wien2k-bandplot
Plot multiple bands in WIEN2k

This code written in Python allows one to plot multiple bands in WIEN2k.

The only input files required are the energy file, eg. case.energy(so).

Usage: 

python bandplot.py -n 2 -f case.energy case.energyso -e 0.3 0.35 -l GGA GGA+SOC

For more information: 

python bandplot.py -h
