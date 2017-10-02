# wien2k-bandplot
Plot multiple bands in WIEN2k

This code written in Python allows one to plot multiple bands in WIEN2k.

The only input files required are the energy file, eg. case.energy(so).

To download:__
git hub https://github.com/wfgoh/wien2k-bandplot.git

Install required python libs:__
pip install numpy matplotlib pyplot ast scipy argparse os

Usage: 

python bandplot.py -n 2 -f case.energy case.energyso -e 0.3 0.35 -l GGA GGA+SOC

Help: 

python bandplot.py -h
