# created by Fasya Khuzaimah on 2019.11.13

import ROOT
from ROOT import TFile, TTree, TH1F
import array as arr
import numpy as np

outfile = TFile("Summary_Signal.root","recreate")

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

signalname = ["MH3_300","MH3_400","MH3_500","MH3_600","MH3_1000","MH3_1200","MH3_1400","MH3_1600"]

h_FJetMassBfr = []
h_FJetMassL = []
h_FJetMassM1 = []
h_FJetMassM2 = []


for i in range(len(fname)):
    bfr_name = "h_FJetMassBfr_"+str(i)
    h_FJetMassBfr.append(TH1F(bfr_name,signalname[i],30,0,300))
    L_name = "h_FJetMassL_"+str(i)
    h_FJetMassL.append(TH1F(L_name,signalname[i],30,0,300))
    M1_name = "h_FJetMassM1_"+str(i)
    h_FJetMassM1.append(TH1F(M1_name,signalname[i],30,0,300))
    M2_name = "h_FJetMassM2_"+str(i)
    h_FJetMassM2.append(TH1F(M2_name,signalname[i],30,0,300))

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

'''
#BACKGROUND#

outfile = TFile("Summary_Background.root","recreate")

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

bkgfname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root"]

bkgname = ["DYJetsToLL_M-50_HT-100to200", "DYJetsToLL_M-50_HT-200to400", "DYJetsToLL_M-50_HT-400to600", "DYJetsToLL_M-50_HT-600to800", "DYJetsToLL_M-50_HT-800to1200", "DYJetsToLL_M-50_HT-1200to2500", "DYJetsToLL_M-50_HT-2500toInf", "ZJetsToNuNu_HT-100To200", "ZJetsToNuNu_HT-200To400", "ZJetsToNuNu_HT-400To600", "ZJetsToNuNu_HT-600To800", "ZJetsToNuNu_HT-800To1200", "ZJetsToNuNu_HT-1200To2500", "ZJetsToNuNu_HT-2500ToInf", "WJetsToLNu_HT-100To200", "WJetsToLNu_HT-200To400", "WJetsToLNu_HT-400To600", "WJetsToLNu_HT-600To800", "WJetsToLNu_HT-800To1200", "WJetsToLNu_HT-1200To2500", "WJetsToLNu_HT-2500ToInf", "GJets_HT-40To100", "GJets_HT-100To200", "GJets_HT-200To400", "GJets_HT-600ToInf", "QCD_HT100to200", "QCD_HT200to300", "QCD_HT300to500", "QCD_HT500to700", "QCD_HT700to1000", "QCD_HT1000to1500", "QCD_HT1500to2000", "QCD_HT2000toInf", "TTToHadronic", "TTToSemiLeptonic", "TTTo2L2Nu", "ST_s-channel_4f_leptonDecays", "ST_t-channel_antitop_4f_inclusiveDecays", "ST_t-channel_top_4f_inclusiveDecays", "ST_tW_antitop_5f_inclusiveDecays", "ST_tW_top_5f_inclusiveDecays", "ZZ", "WW", "WZ"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0, 300.95, 72.15,  3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6]
L = 150000.0 #1/pb

h_FJetMassBkgL = []
h_FJetMassBkgM1 = []
h_FJetMassBkgM2 = []

for i in range(len(bkgfname)):
    Bkg_L = "h_FJetMassBkgL_"+str(i)
    h_FJetMassBkgL.append(TH1F(Bkg_L,bkgname[i],30,0,300))
    Bkg_M1 = "h_FJetMassBkgM1_"+str(i)
    h_FJetMassBkgM1.append(TH1F(Bkg_M1,bkgname[i],30,0,300))
    Bkg_M2 = "h_FJetMassBkgM2_"+str(i)
    h_FJetMassBkgM2.append(TH1F(Bkg_M2,bkgname[i],30,0,300))

for i in range(len(bkgfname)):
    openbkg = TFile(path+bkgfname[i], "read")
    h_total_mcweight_bkg = openbkg.Get("h_total_mcweight")
    eventsbkg = h_total_mcweight_bkg.Integral()
    treeBkg = openbkg.Get("monoHbb_SR_boosted")
    preEventsBkg = treeBkg.GetEntries()
    
    for j in range(preEventsBkg):
        treeBkg.GetEntry(j)
        FJetMassBkg = getattr(treeBkg, 'FJetMass')
        FJetCSVBkg = getattr(treeBkg, 'FJetCSV')
        if (FJetCSVBkg > 0.7):
            h_FJetMassBkgL[i].Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.86):
            h_FJetMassBkgM1[i].Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.89):
            h_FJetMassBkgM2[i].Fill(FJetMassBkg)

#h_FJetMassBkgL[i] = h_FJetMassBkgL[i]*(L*xsBkg[i]/eventsbkg)
#h_FJetMassBkgM1[i] = h_FJetMassBkgM1[i]*(L*xsBkg[i]/eventsbkg)
#h_FJetMassBkgM2[i] = h_FJetMassBkgM2[i]*(L*xsBkg[i]/eventsbkg)
    
outfile.Write()
outfile.Close()
'''
