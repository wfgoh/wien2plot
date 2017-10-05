# wien2plot
**Plot multiple bandstructures in WIEN2k**

This code written in Python allows one to plot multiple bandstructure in WIEN2k.

The only input files required are the energy files, eg. case.energy(so).

**To download:** <br />
git clone https://github.com/wfgoh/wien2plot.git

**Install required python libs:**<br />
pip install numpy matplotlib pyplot ast scipy argparse os

**Example of Usage:** <br />
python wien2plot.py -n 3 -f gga.energyso gw.energyso mbj.energyso -e 0.315 0.295 0.286 -l GGA GW mBJ
![](https://github.com/wfgoh/wien2plot/example/band.jpg)

**Help:** <br />
python bandplot.py -h
