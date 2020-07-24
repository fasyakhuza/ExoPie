# created by Fasya Khuzaimah on 2019.12.09

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad, TGraphAsymmErrors
import array as arr
import numpy as np


#produce root

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]


preselect = []
med1 = []

signalname = ["MH3_300","MH3_400","MH3_600","MH3_1000","MH3_1200","MH3_1400","MH3_1600"]
nhist = len(fname)
MH3 = [300, 400, 600, 1000, 1200, 1400, 1600]

effM1 = arr.array('d')
h_FJetMassM1 = TH1F("h_FJetMassM1","FJetMass Medium1",40,0,1000)

outfile = TFile("singlevaluesignal3.root", "recreate")

for i in range(nhist):
    preselect_name = "h_preselect_"+str(i)
    preselect.append(TH1F(preselect_name,signalname[i],17,0,1700))
    med1_name = "h_med1_"+str(i)
    med1.append(TH1F(med1_name,signalname[i],17,0,1700))

for i in range(len(fname)):
    openf = TFile(path+fname[i], "read")
    treef = openf.Get("monoHbb_SR_boosted")
    preEvents = treef.GetEntries()
    
    for j in range(preEvents):
        treef.GetEntry(j)
        preselect[i].Fill(MH3[i])
        FJetMass = getattr(treef, 'FJetMass')
        FJetCSV = getattr(treef, 'FJetCSV')
        dPhi = getattr(treef, 'min_dPhi')
        nJets = getattr(treef, 'nJets')
        if (FJetCSV > 0.86) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            med1[i].Fill(MH3[i])
            h_FJetMassM1.Fill(FJetMass)

    nFJetMassM1 = h_FJetMassM1.Integral()
    effM1.append(nFJetMassM1/preEvents)
    h_FJetMassM1.Reset()


outfile.Write()
outfile.Close()


print "signal efficiency", effM1
