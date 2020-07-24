import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, gStyle, TGraphAsymmErrors, gPad, TMultiGraph, TLatex, TGraphErrors, TPaveText, TPad
import array as arr
import numpy as np


#get the normalized number of background events AND the the errors#

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root", "crab_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root","crab_ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.root","crab_WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0, 300.95, 72.15,  3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6, 0.01222, 0.006185, 0.3654, 0.2819, 0.07924, 0.1565]

h_FJetMassBkgM1 = TH1F("h_FJetMassBkgM1","Background FJetMass Medium1",40,0.6,1.0)
h_FJetMassBkgM1_final = TH1F("h_FJetMassBkgM1_final","Background FJetMass Medium1",40,0.6,1.0)

L = 41000.0 #1/pb

for i in range(len(bkgname)):
    openbkg = TFile(path+bkgname[i])
    h_total_mcweight_bkg = openbkg.Get("h_total_mcweight")
    eventsbkg = h_total_mcweight_bkg.Integral()
    treebkg = openbkg.Get("monoHbb_SR_boosted")
    preEventsbkg = treebkg.GetEntries()
    
    for j in range(preEventsbkg):
        treebkg.GetEntry(j)
        FJetMassBkg = getattr(treebkg, 'FJetMass')
        FJetCSVBkg = getattr(treebkg, 'FJetCSV')
        dPhiBkg = getattr(treebkg, 'min_dPhi')
        nJetsBkg = getattr(treebkg, 'nJets')
        if (FJetCSVBkg > 0.86) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (dPhiBkg > 0.4) and (nJetsBkg <= 2.0):
            h_FJetMassBkgM1.Fill(0.86)


    #number of expected obs events in data
    h_FJetMassBkgM1 = h_FJetMassBkgM1*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM1_final += h_FJetMassBkgM1
    h_FJetMassBkgM1.Reset()

NbkgM1final = h_FJetMassBkgM1_final.Integral()

Nbkg_err = []


for i in range(40):
    NbkgM1i_content = h_FJetMassBkgM1_final.GetBinContent(i)
    #print i, "NbkgM1i_content", NbkgM1i_content
    if (NbkgM1i_content == 0.0):
        continue
    else:
        NbkgM1_err = h_FJetMassBkgM1_final.GetBinError(i)
        Nbkg_err.append(NbkgM1_err)


#print "Normalized number of total background events", NbkgM1final
#print "Nbkg_err", Nbkg_err




#get the punzi significance uncertainty#

filename = "singlevaluesignal3.root"
file = TFile(filename, "read")

nfile = 7
nbin = 17

name = ["300", "400", "600", "1000", "1200", "1400", "1600"]

err_sigeff_M1 = []


xM1 = ROOT.Double(0)
yM1 = ROOT.Double(0)


for i in range(nfile):
    preselect = file.Get("h_preselect_"+str(i))
    med1 = file.Get("h_med1_"+str(i))

    effM1 = TGraphAsymmErrors(med1,preselect,"cl=0.683 b(1,1) mode")
    effM1.SetTitle("Medium 1")
    binM1 = effM1.GetN()
    for j in range(binM1):
        effM1.GetPoint(j, xM1, yM1)
        if (yM1 == 0):
            continue
        else:
            errM1 = effM1.GetErrorY(j)
            err_sigeff_M1.append(errM1)
    #print "errM1_"+str(name[i]), errM1

'''
print "####################################"
print "err_sigeff_M1", err_sigeff_M1
print "####################################"
'''

    
#Punzi Significance errors

effM1_value = [0.010810810810810811, 0.030612244897959183, 0.04139715394566624, 0.11196443007275667, 0.2798152675903287, 0.2979099431381589, 0.28516998827667056, 0.18267419962335216]


errM1bkg = Nbkg_err[0]

errPS_M1 = arr.array('d')

for i in range(nfile):
    dx_M1 = err_sigeff_M1[i]
    dP_M1 = TMath.Sqrt((dx_M1/(1+TMath.Sqrt(NbkgM1final)))**2 + (effM1_value[i]*errM1bkg/(2*(TMath.Sqrt(NbkgM1final))*(1+(TMath.Sqrt(NbkgM1final)))**2))**2)
    errPS_M1.append(dP_M1)

print "errPS_M1", errPS_M1
