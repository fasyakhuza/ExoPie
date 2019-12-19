# created by Fasya Khuzaimah on 2019.12.09

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad, TGraphAsymmErrors, gStyle
import array as arr
import numpy as np


path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0, 300.95, 72.15,  3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6]

h_FJetMassBkgL = TH1F("h_FJetMassBkgL","Background FJetMass Loose",40,0.6,1.0)
h_FJetMassBkgM1 = TH1F("h_FJetMassBkgM1","Background FJetMass Medium1",40,0.6,1.0)
h_FJetMassBkgM2 = TH1F("h_FJetMassBkgM2","Background FJetMass Medium2",40,0.6,1.0)
h_FJetMassBkgL_final = TH1F("h_FJetMassBkgL_final","Background FJetMass Loose",40,0.6,1.0)
h_FJetMassBkgM1_final = TH1F("h_FJetMassBkgM1_final","Background FJetMass Medium1",40,0.6,1.0)
h_FJetMassBkgM2_final = TH1F("h_FJetMassBkgM2_final","Background FJetMass Medium2",40,0.6,1.0)

h_FJetMassBkgL_fjet = TH1F("h_FJetMassBkgL_fjet","Background FJetMass Loose",30,0,300)
h_FJetMassBkgM1_fjet = TH1F("h_FJetMassBkgM1_fjet","Background FJetMass Medium1",30,0,300)
h_FJetMassBkgM2_fjet = TH1F("h_FJetMassBkgM2_fjet","Background FJetMass Medium2",30,0,300)
h_FJetMassBkgL_fjet_final = TH1F("h_FJetMassBkgL_fjet_final","Background FJetMass Loose",30,0,300)
h_FJetMassBkgM1_fjet_final = TH1F("h_FJetMassBkgM1_fjet_final","Background FJetMass Medium1",30,0,300)
h_FJetMassBkgM2_fjet_final = TH1F("h_FJetMassBkgM2_fjet_final","Background FJetMass Medium2",30,0,300)

L = 150000.0 #1/pb

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
        dPhi = getattr(treebkg, 'min_dPhi')
        if (FJetCSVBkg > 0.7) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (abs(dPhi) > 0.4):
            #FJetMassBkgL.append(FJetMassBkg)
            h_FJetMassBkgL.Fill(0.7)
            h_FJetMassBkgL_fjet.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.86) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (abs(dPhi) > 0.4):
            #FJetMassBkgM1.append(FJetMassBkg)
            h_FJetMassBkgM1.Fill(0.86)
            h_FJetMassBkgM1_fjet.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.89) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (abs(dPhi) > 0.4):
            #FJetMassBkgM2.append(FJetMassBkg)
            h_FJetMassBkgM2.Fill(0.89)
            h_FJetMassBkgM2_fjet.Fill(FJetMassBkg)

    #number of expected obs events in data
    h_FJetMassBkgL = h_FJetMassBkgL*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM1 = h_FJetMassBkgM1*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM2 = h_FJetMassBkgM2*(L*xsBkg[i]/eventsbkg)
    
    h_FJetMassBkgL_fjet = h_FJetMassBkgL_fjet*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM1_fjet = h_FJetMassBkgM1_fjet*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM2_fjet = h_FJetMassBkgM2_fjet*(L*xsBkg[i]/eventsbkg)
    
    h_FJetMassBkgL_final += h_FJetMassBkgL
    h_FJetMassBkgM1_final += h_FJetMassBkgM1
    h_FJetMassBkgM2_final += h_FJetMassBkgM2
    
    h_FJetMassBkgL_fjet_final += h_FJetMassBkgL_fjet
    h_FJetMassBkgM1_fjet_final += h_FJetMassBkgM1_fjet
    h_FJetMassBkgM2_fjet_final += h_FJetMassBkgM2_fjet
    
    h_FJetMassBkgL.Reset()
    h_FJetMassBkgM1.Reset()
    h_FJetMassBkgM2.Reset()

    h_FJetMassBkgL_fjet.Reset()
    h_FJetMassBkgM1_fjet.Reset()
    h_FJetMassBkgM2_fjet.Reset()

NdataLfinal = h_FJetMassBkgL_final.Integral()
NdataM1final = h_FJetMassBkgM1_final.Integral()
NdataM2final = h_FJetMassBkgM2_final.Integral()

Nbkg_err = []

#h_FJetMassBkgL_final.Sumw2()
#h_FJetMassBkgM1_final.Sumw2()
#h_FJetMassBkgM2_final.Sumw2()

for i in range(40):
    NbkgLi_content = h_FJetMassBkgL_final.GetBinContent(i)
    #print i, "NbkgLi_content", NbkgLi_content
    if (NbkgLi_content == 0.0):
        continue
    else:
        NbkgL_err = h_FJetMassBkgL_final.GetBinError(i)
        Nbkg_err.append(NbkgL_err)

for i in range(40):
    NbkgM1i_content = h_FJetMassBkgM1_final.GetBinContent(i)
    #print i, "NbkgM1i_content", NbkgM1i_content
    if (NbkgM1i_content == 0.0):
        continue
    else:
        NbkgM1_err = h_FJetMassBkgM1_final.GetBinError(i)
        Nbkg_err.append(NbkgM1_err)

for i in range(40):
    NbkgM2i_content = h_FJetMassBkgM2_final.GetBinContent(i)
    #print i, "NbkgM2i_content", NbkgM2i_content
    if (NbkgM2i_content == 0.0):
        continue
    else:
        NbkgM2_err = h_FJetMassBkgM2_final.GetBinError(i)
        Nbkg_err.append(NbkgM2_err)

print "NdataLfinal", NdataLfinal
print "NdataM1final", NdataM1final
print "NdataM2final", NdataM2final
print "Nbkg_err", Nbkg_err

#Draw Nbkg in function of FJetCSV

c1 = TCanvas("c1", "c1", 900, 900)
c1.SetLeftMargin(0.15)

leg = TLegend(0.50,0.75,0.7,0.89)
leg.SetBorderSize(0)
leg.SetTextSize(0.027)

gStyle.SetOptStat(0)

h_FJetMassBkgL_final.SetLineColor(1)
h_FJetMassBkgL_final.SetLineWidth(4)
h_FJetMassBkgL_final.SetMarkerStyle(20)
h_FJetMassBkgL_final.SetMarkerColor(1)
h_FJetMassBkgL_final.GetXaxis().SetTitle("Fat Jet CSV")
h_FJetMassBkgL_final.GetYaxis().SetTitle("Number of Events")
h_FJetMassBkgL_final.SetTitle("Expected Nbkg in Data")

h_FJetMassBkgM1_final.SetLineColor(2)
h_FJetMassBkgM1_final.SetLineWidth(4)
h_FJetMassBkgM1_final.SetMarkerStyle(21)
h_FJetMassBkgM1_final.SetMarkerColor(2)

h_FJetMassBkgM2_final.SetLineColor(4)
h_FJetMassBkgM2_final.SetLineWidth(4)
h_FJetMassBkgM2_final.SetMarkerStyle(22)
h_FJetMassBkgM2_final.SetMarkerColor(4)

h_FJetMassBkgL_final.Draw("e")
h_FJetMassBkgM1_final.Draw("esame")
h_FJetMassBkgM2_final.Draw("esame")

leg.AddEntry(h_FJetMassBkgL_final, "Loose (FJetCSV > 0.7)")
leg.AddEntry(h_FJetMassBkgM1_final, "Medium1 (FJetCSV > 0.86)")
leg.AddEntry(h_FJetMassBkgM2_final, "Medium2 (FJetCSV > 0.89)")
leg.Draw()

c1.cd()
c1.Update()
c1.SaveAs("Nbkg_err_new.pdf")

#Draw Nbkg in function of Fat Jet Mass

c2 = TCanvas("c2", "c2", 900, 900)
c2.SetLeftMargin(0.15)

leg2 = TLegend(0.50,0.75,0.7,0.89)
leg2.SetBorderSize(0)
leg2.SetTextSize(0.027)

gStyle.SetOptStat(0)

h_FJetMassBkgL_fjet_final.Sumw2()
h_FJetMassBkgL_fjet_final.SetLineColor(1)
h_FJetMassBkgL_fjet_final.SetLineWidth(4)
h_FJetMassBkgL_fjet_final.SetMarkerStyle(20)
h_FJetMassBkgL_fjet_final.SetMarkerColor(1)
h_FJetMassBkgL_fjet_final.GetXaxis().SetTitle("Fat Jet Mass")
h_FJetMassBkgL_fjet_final.GetYaxis().SetTitle("Number of Events")
h_FJetMassBkgL_fjet_final.SetTitle("Expected Nbkg in Data")

h_FJetMassBkgM1_fjet_final.Sumw2()
h_FJetMassBkgM1_fjet_final.SetLineColor(2)
h_FJetMassBkgM1_fjet_final.SetLineWidth(4)
h_FJetMassBkgM1_fjet_final.SetMarkerStyle(21)
h_FJetMassBkgM1_fjet_final.SetMarkerColor(2)

h_FJetMassBkgM2_fjet_final.Sumw2()
h_FJetMassBkgM2_fjet_final.SetLineColor(4)
h_FJetMassBkgM2_fjet_final.SetLineWidth(4)
h_FJetMassBkgM2_fjet_final.SetMarkerStyle(22)
h_FJetMassBkgM2_fjet_final.SetMarkerColor(4)

h_FJetMassBkgL_fjet_final.Draw("e")
h_FJetMassBkgM1_fjet_final.Draw("esame")
h_FJetMassBkgM2_fjet_final.Draw("esame")

leg2.AddEntry(h_FJetMassBkgL_fjet_final, "Loose (FJetCSV > 0.7)")
leg2.AddEntry(h_FJetMassBkgM1_fjet_final, "Medium1 (FJetCSV > 0.86)")
leg2.AddEntry(h_FJetMassBkgM2_fjet_final, "Medium2 (FJetCSV > 0.89)")
leg2.Draw()

c2.cd()
c2.Update()
c2.SaveAs("Nbkg_FJetMass.pdf")
