# wien2k-bandplot
Plot multiple bands in WIEN2k

This code written in Python allows one to plot multiple bands in WIEN2k.

The only input files required are the energy file, eg. case.energy(so).

To download:<br />
git hub https://github.com/wfgoh/wien2k-bandplot.git

Install required python libs:<br />
pip install numpy matplotlib pyplot ast scipy argparse os

Example of Usage: <br />
python bandplot.py -n 2 -f case.energy case.energyso -e 0.3 0.35 -l GGA GGA+SOC

Help: <br />
python bandplot.py -h
