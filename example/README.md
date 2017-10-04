This example plots band structure of Ca3BiN with GGA, GW and mBJ.

python wien2plot.py -n 3 -f gga.energyso gw.energyso mbj.energyso -e 0.315 0.295 0.286 -l GGA GW mBJ

evince band.eps
