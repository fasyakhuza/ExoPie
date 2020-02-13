#created by Fasya Khuzaimah
#February 12, 2020
#optimization for b-tagging in resolved analysis

import ROOT
from ROOT import TFile, TTree, TMath, TH1F, TCanvas, TLegend, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad
import array as arr
import numpy as np

medium_signal_path = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/2017_AnalyserOutput/V0_fixedJetID_photonVeto_signal/"

########
#SIGNAL#
########

signalname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

h_looseSignalEntries = TH1F("h_looseSignalEntries", "Number of Signal Events (Loose)", 3, 0, 3)
h_mediumSignalEntries = TH1F("h_mediumSignalEntries", "Number of Signal Events (Medium)", 3, 0, 3)

looseSignal = arr.array('d')
mediumSignal = arr.array('d')
LSignal_error = arr.array('d')
MSignal_error = arr.array('d')

for i in range(len(signalname)):
    print loose_path+signalname[i]
    openLooseSignal = TFile(loose_signal_path+signalname[i], "read")
    looseSignalTree = openLooseSignal.Get("monoHbb_SR_resolved")
    looseSignalEntries = looseSignalTree.GetEntries()
    h_looseSignalEntries.Fill(looseSignalEntries)
    for j in range(3):
        jLSignal = h_looseSignalEntries.GetBinContent(j)
        if (jLSignal == 0.0):
            continue
        else:
            jLSignal_error = h_looseSignalEntries.GetBinError(j)
            LSignal_error.append(jLSignal_error)
    looseSignal.append(looseSignalEntries)

    print medium_path+signalname[i]
    openMediumSignal = TFile(medium_signal_path+signalname[i], "read")
    mediumSignalTree = openMediumSignal.Get("monoHbb_SR_resolved")
    mediumSignalEntries = mediumSignalTree.GetEntries()
    h_mediumSignalEntries.Fill(mediumSignalEntries)
    for j in range(3):
        jMSignal = h_mediumSignalEntries.GetBinContent(j)
        if (jMSignal == 0.0):
            continue
        else:
            jMSignal_error = h_mediumSignalEntries.GetBinError(j)
            MSignal_error.append(jMSignal_error)
    mediumSignal.append(mediumSignalEntries)

print "Nsignal (loose)", looseSignal
print "Signal Error (loose)", LSignal_error
print "Nsignal (medium)", mediumSignal
print "Signal Error (medium)", MSignal_error

############
#BACKGROUND#
############

loose_bkg_path = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/2017_AnalyserOutput/V0_Bjetlwp_resol_Fasya/"
medium_bkg_path = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/2017_AnalyserOutput/V0_fixedJetID_updatedEleSF_MWPbJetVeto_photonVeto/"

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root","crab_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root","crab_ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.root","crab_WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0047, 300.9498, 72.1455, 3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6, 0.01222, 0.006185, 0.3654, 0.2819, 0.07924, 0.1565]

L = 41000 #1/pb

h_looseNbkg = TH1F("h_looseNbkg", "Normalized Number of Background Events (Loose)", 3, 0, 3)
h_mediumNbkg = TH1F("h_mediumNbkg", "Normalized Number of Background Events (Medium)", 3, 0, 3)

Nbkg = arr.array('d')
Nbkg_error = arr.array('d')

looseBkgSum = 0
mediumBkgSum = 0

for i in range(len(bkgname)):
    print loose_path+bkgname[i]
    openLooseBkg = TFile(loose_bkg_path+bkgname[i], "read")
    looseBkgTree = openLooseBkg.Get("monoHbb_SR_resolved")
    loose_h_total_mcweight = openLooseBkg.Get("h_total_mcweight")
    looseBkgEntries = looseBkgTree.GetEntries()
    loose_preevents = loose_h_total_mcweight.Integral()
    looseBkgNormalized = looseBkgEntries*L*xsBkg[i]/loose_preevents
    looseBkgSum += looseBkgNormalized
    
    print medium_path+bkgname[i]
    openMediumBkg = TFile(medium_bkg_path+bkgname[i], "read")
    mediumBkgTree = openMediumBkg.Get("monoHbb_SR_resolved")
    medium_h_total_mcweight = openMediumBkg.Get("h_total_mcweight")
    mediumBkgEntries = mediumBkgTree.GetEntries()
    medium_preevents = medium_h_total_mcweight.Integral()
    mediumBkgNormalized = mediumBkgEntries*L*xsBkg[i]/medium_preevents
    mediumBkgSum += mediumBkgNormalized

Nbkg.append(looseBkgSum)
Nbkg.append(mediumBkgSum)

h_looseNbkg.Fill(looseBkgSum)
for j in range(3):
    jLBkg = h_looseNbkg.GetBinContent(j)
    if (jLBkg == 0.0):
        continue
    else:
        jLBkg_error = h_looseNbkg.GetBinError(j)
        Nbkg_error.append(jLBkg_error)

h_mediumNbkg.Fill(mediumBkgSum)
for j in range(3):
    jMBkg = h_mediumNbkg.GetBinContent(j)
    if (jMBkg == 0.0):
        continue
    else:
        jMBkg_error = h_mediumNbkg.GetBinError(j)
        Nbkg_error.append(jMBkg_error)

print "Normalized number of background events", Nbkg
print "Nbkg error", Nbkg_error

####################
#SIGNIFICANCE#
####################

LPS_list = arr.array('d')
MPS_list = arr.array('d')
for i in range (len(signalname)):
    LPS = looseSignal[i]/(TMath.Sqrt(Nbkg[0]))
    LPS_list.append(LPS)
    MPS = mediumSignal[i]/(TMath.Sqrt(Nbkg[1]))
    MPS_list.append(MPS)

##########################
#SIGNIFICANCE ERROR#
##########################

LPS_error = arr.array('d')
MPS_error = arr.array('d')
for i in range(len(signalname)):
    LPS_err = TMath.Sqrt((((LSignal_error[i])^2)/Nbkg[0])+(((LPS_list)^2)*((Nbkg_error[0])^2)/(4*(Nbkg[0])^3)))
    LPS_error.append(LPS_err)
    MPS_err = TMath.Sqrt((((MSignal_error[i])^2)/Nbkg[1])+(((MPS_list)^2)*((Nbkg_error[1])^2)/(4*(Nbkg[1])^3)))
    MPS_error.append(MPS_err)


##########################
#DRAW SIGNIFICANCE#
#########################

leg = TLegend(0.65,0.15,0.88,0.35)
leg.SetBorderSize(0)
leg.SetTextSize(0.05)

c1 = TCanvas("c1","c1",900,700)
c1.SetLeftMargin(0.15)

zero = np.zeros(8)
MA = arr.array('d', [300, 400, 500, 600, 1000, 1200, 1400, 1600])

gPad.Modified()
gr1 = TGraphErrors(8, MA, LPS_list, zero, LPS_error) #err_x, err_y
gr1.SetTitle("Loose")
gr1.GetYaxis().SetNdivisions(505)
gr1.GetYaxis().SetLabelOffset(1.4)
gr1.GetXaxis().SetTitleOffset(4.0)
gr1.SetLineColor(1)
gr1.SetLineWidth(5)
gr1.SetMarkerStyle(20)
gr1.SetMarkerColor(1)

gr2 = TGraphErrors(8, MA, MPS_list, zero, MPS_error) #err_x, err_y
gr2.SetTitle("Medium")
gr2.GetYaxis().SetNdivisions(505)
gr2.GetYaxis().SetLabelOffset(1.4)
gr2.GetXaxis().SetTitleOffset(4.0)
gr2.SetLineColor(2)
gr2.SetLineWidth(5)
gr2.SetMarkerStyle(21)
gr2.SetMarkerColor(2)

mg = TMultiGraph("mg","")
mg.SetTitle("Punzi Significance; M_{A} (GeV); Punzi Significance")
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetLabelOffset(1.4)
mg.GetXaxis().SetTitleOffset(4.0)
mg.Add(gr1, "ALP")
mg.Add(gr2, "ALP")
mg.Draw("ALP")
leg.AddEntry(gr1, "Loose")
leg.AddEntry(gr2, "Medium")
leg.Draw()

c1.cd()
c1.Update()
c1.SaveAs("resolved_PS.pdf")
