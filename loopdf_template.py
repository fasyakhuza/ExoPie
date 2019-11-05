


''' 

this is just an example about how to access the .root file and then convert it into a dataframe. 

Once converted how to looop over it

And how to apply selection on it 

''' 


import os,traceback
import sys, optparse,argparse
from array import array
import math
import numpy as numpy
import pandas
from root_pandas import read_root
from pandas import  DataFrame, concat
from pandas import Series
import time
import glob
from ROOT import TCanvas, TH1F, TFile
import ROOT



## add the file name 
filename = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/skimmedFiles/V0_filters_study/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root"


## make  alist of variables you want to access in this code. 
allvariables = ['st_pfMetCorrPt', 'st_filterStatus', 'st_filters']




## first of all open the rootfile in the chunk of 125000 
## this si just to make sure if the root file is big then we read a part of it and then read the next part of it and so on... 
## variables in the list "allvariables" will be read and saved in the df for 125000 events
ievent = 0
for df in read_root(filename, 'outTree', columns=allvariables, chunksize=125000):
    
    ## all the code should be inside following for loop. 
    
    ## make a zip of the varianbles which you want to read. This can be same as the allvariables or a subset of it. 
    ## variable in the zip are accessed using the df.VARNAME_YOU_ADDED_IN_THE_LIST
    varzip = zip (df.st_pfMetCorrPt, df.st_filterStatus, df.st_filters)
    
    ## now loop of these events 
    ## note the order of the zip and columns should be same. 
    ## met_, fstatus_, fnames_ are the names given by user, the vars will be refered to these names in rest of the code,
    
    outfile = TFile("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root", "recreate")
    #c1 = TCanvas("c1","c1",900,900)
    h = TH1F("h","Met Distribution",32,200,1000)
    h0 = TH1F("h0","Met Distribution",32,200,1000)
    h1 = TH1F("h1","Met Distribution",32,200,1000)
    h2 = TH1F("h2","Met Distribution",32,200,1000)
    h3 = TH1F("h3","Met Distribution",32,200,1000)
    h4 = TH1F("h4","Met Distribution",32,200,1000)
    h5 = TH1F("h5","Met Distribution",32,200,1000)
    h6 = TH1F("h6","Met Distribution",32,200,1000)
    
    
	
    for met_, fstatus_, fnames_ in varzip:
        print ievent, met_, fstatus_, fnames_
	h.Fill(met_)
	if met_ and (fstatus_[0]==True):
		h0.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True):
		h1.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True) and (fstatus_[2]==True):
		h2.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True) and (fstatus_[2]==True) and (fstatus_[3]==True):
		h3.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True) and (fstatus_[2]==True) and (fstatus_[3]==True) and (fstatus_[4]==True):
		h4.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True) and (fstatus_[2]==True) and (fstatus_[3]==True) and (fstatus_[4]==True) and (fstatus_[5]==True):
		h5.Fill(met_)
	if met_ and (fstatus_[0]==True) and (fstatus_[1]==True) and (fstatus_[2]==True) and (fstatus_[3]==True) and (fstatus_[4]==True) and (fstatus_[5]==True) and (fstatus_[6]==True):
		h6.Fill(met_)
  
	



        ievent = ievent +1

    outfile.Write()
    outfile.Close() 
