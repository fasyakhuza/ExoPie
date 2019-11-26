# created by Fasya Khuzaimah on 2019.11.13

import ROOT
from ROOT import TFile, TTree, TH1F
import array as arr
import numpy as np

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

signalname = ["MH3_300","MH3_400","MH3_500","MH3_600","MH3_600_new","MH3_1000","MH3_1200","MH3_1400","MH3_1600"]

h_FJetMassBfr = []
h_FJetMassL = []
h_FJetMassM1 = []
h_FJetMassM2 = []

outfile = TFile("Bfr_Aftr_signal.root","recreate")

for i in range(len(fname)):
    bfr_name = "h_FJetMassBfr_"+str(i)
    h_FJetMassBfr.append(TH1F(bfr_name,signalname[i],40,0,1000))
    L_name = "h_FJetMassL_"+str(i)
    h_FJetMassL.append(TH1F(L_name,signalname[i],40,0,1000))
    M1_name = "h_FJetMassM1_"+str(i)
    h_FJetMassM1.append(TH1F(M1_name,signalname[i],40,0,1000))
    M2_name = "h_FJetMassM2_"+str(i)
    h_FJetMassM2.append(TH1F(M2_name,signalname[i],40,0,1000))
    
for i in range(len(fname)):
    openf = TFile(path+fname[i], "read")
    treef = openf.Get("monoHbb_SR_boosted")
    preEvents = treef.GetEntries()
    print signalname[i], preEvents
    
    for j in range(preEvents):
        treef.GetEntry(j)
        FJetMass = getattr(treef, 'FJetMass')
        FJetCSV = getattr(treef, 'FJetCSV')
        h_FJetMassBfr[i].Fill(FJetMass)
        if (FJetCSV > 0.7):
            h_FJetMassL[i].Fill(FJetMass)
        if (FJetCSV > 0.86):
            h_FJetMassM1[i].Fill(FJetMass)
        if (FJetCSV > 0.89):
            h_FJetMassM2[i].Fill(FJetMass)

outfile.Write()
outfile.Close()
