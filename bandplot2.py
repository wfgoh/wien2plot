import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import ast
from scipy import constants
import argparse
import os

def readene(fermi,filename) :
	fermi=fermi
	f = open(filename,'r')
	f_inp = f.readlines()	
	f.close()
	nbnd=maxbnd
	ib=maxkpt
	ene=np.zeros((maxbnd,maxkpt))
	ik=0
	klabel=[]
	kindex=[]
	label=[]
	i = 0
	
	for line in f_inp:
		if line.isupper() or line.islower() :
			break
		i += 1
	
	for line in f_inp[i:]:
		if isinstance(ast.literal_eval(line.split()[0]),float):
			if list(line.split()[2])[-1].isalpha():
				for char in list(line.split()[2]):
					if char.isalpha():
						if char != 'E':
							label.append(char)
				klabel.append(''.join(label).replace('GAMMA','$\Gamma$'))
				kindex.append(ik)
				label=[]
			ik+=1
			nbnd=min(nbnd,ib)
			ib=0
		else:
			ib+=1
			ene[ib][ik]=(float(line.split()[1])-fermi)*constants.Rydberg*constants.h*constants.c/constants.eV
	return ene, nbnd, ik, kindex, klabel

def plotene(ene,kpoint,nbnd,label,color) :
	for ib in range(nbnd):
		myplot = plt.plot(kpoint, ene[ib+1][kpoint+1], color)
	myplot = plt.plot(kpoint, ene[1][kpoint+1], color, label=label)
	return myplot


parser = argparse.ArgumentParser()
parser.add_argument('-n', choices=[1,2,3,4,5,6], default=2, type=int, help='specify number of bandplots (default: %(default)s)')
parser.add_argument('-f', metavar='FILENAME', nargs='+', default=[os.path.basename(os.getcwd())+'.energy', os.path.basename(os.getcwd())+'.energyso'], help='specify band energy filenames (default: %(default)s)')
parser.add_argument('-e', metavar='FERMIENERGY', nargs='+', default=[0.0, 0.0], type=float, help='specify Fermi energy (in Ry) in the order of the filenames given (default: %(default)s)')
parser.add_argument('-l', metavar='LEGEND', nargs='+', default=['Legend1', 'Legend2'], help='specify legend descriptions in the order of the filenames given (default: %(default)s)')
parser.add_argument('-r', metavar='ENERGY', nargs=2, default=[-2.0, 2.0], type=float, help='[Optional] specify energy range (default: %(default)s)')
parser.add_argument('-s', metavar='FERMILEVEL', nargs='+', default=0.0, type=float, help='[Optional] specify Fermi level (in eV) for plotting (default: %(default)s)')
parser.add_argument('-o', metavar='FILENAME', default='band.eps', help='[Optional] Specify output filenames (default: %(default)s)')
parser.add_argument('-b', metavar='INTEGER', default=200, type=int, help='[Optional] Specify an integer greater than the number of bands in case.energy (default: %(default)s)')
parser.add_argument('-k', metavar='INTEGER', default=800, type=int, help='[Optional] Specify an integer greater than the number of k-points in case.klist_band (default: %(default)s)')
#parser.add_argument('-i', action='store_true', help='[Optional] Read input from input file bandplot.inp')
args = parser.parse_args()
'''
if args.i :
	f = open('bandplot.inp','r')
	finp = f.readlines()
	f.close()
	fnam = []
	efer = []
	lege = []
	args.n = ast.literal_eval(finp[0])
	for i in range(args.n) :
		fnam.append(finp[i+1].split()[0])
		efer.append(ast.literal_eval(finp[i+1].split()[1]))
		lege.append(finp[i+1].split()[2])
	args.f = fnam
	args.e = efer
	args.l = lege
	rang = [ast.literal_eval(finp[args.n+1].split()[0]),ast.literal_eval(finp[args.n+1].split()[1])]
	args.r = rang
	args.s = ast.literal_eval(finp[args.n+2])
	args.o = finp[args.n+3]
	args.b = ast.literal_eval(finp[args.n+4])
	args.k = ast.literal_eval(finp[args.n+5])
'''		
maxbnd = args.b
maxkpt = args.k
color = ['b-','g-','r-','c-', 'm-', 'y-']

for i in range(args.n):
	ene,nbnd,nkpt,kindex,klabel = readene(args.e[i],args.f[i])
	kpoint=np.arange(nkpt)
	myplot = plotene(ene,kpoint,nbnd,args.l[i],color[i])

efermi = args.s #fermi*constants.Rydberg*constants.h*constants.c/constants.eV
emin = efermi + args.r[0]
emax = efermi +  args.r[1]
kmin = kpoint[0]
kmax = kpoint[nkpt - 1]
matplotlib.rc('figure', figsize=(8.0, 6.0))
matplotlib.rc('axes', linewidth=1.5)
matplotlib.rc('lines', linewidth=1.5)
matplotlib.rc('font', size=18.0)
matplotlib.rc('xtick.major', size=0.0, pad=8.0)
matplotlib.rc('xtick.minor', size=0.0, pad=8.0)
matplotlib.rc('ytick.major', size=6.0, pad=8.0)
matplotlib.rc('ytick.minor', size=3.0, pad=8.0)
kvalue = []
for i in range(len(kindex)):
    kvalue.append(kpoint[kindex[i]])
myxticks = plt.xticks(kvalue, klabel)
for i in range(len(kindex)):
    if kvalue[i] != kmin and kvalue[i] != kmax:
        myplot = plt.plot([kvalue[i], kvalue[i]], [emin, emax], 'k-')
myplot = plt.plot([kmin, kmax], [efermi, efermi], 'k-')
mygca = plt.gca()
for i in mygca.get_xticklines() + mygca.get_yticklines():
    i.set_markeredgewidth(1.5)
myaxis = plt.axis([kmin, kmax, emin, emax])
myxlabel = plt.xlabel('Wavevector')
myylabel = plt.ylabel('Energy (eV)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
plt.savefig(args.o, bbox_inches='tight')
