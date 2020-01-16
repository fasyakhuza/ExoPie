# created by Fasya Khuzaimah on 2019.12.09

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad, TGraphAsymmErrors
import array as arr
import numpy as np


#produce root

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

#effL = arr.array('d')
#effM1 = arr.array('d')
#effM2 = arr.array('d')

preselect = []
loo = []
med1 = []
med2 = []

signalname = ["MH3_300","MH3_400","MH3_500","MH3_600","MH3_1000","MH3_1200","MH3_1400","MH3_1600"]
nhist = 8
#color = [419, 861, 803, 400, 407, 393, 920, 616]
MH3 = [300, 400, 500, 600, 1000, 1200, 1400, 1600]

outfile = TFile("singlevaluesignal3.root", "recreate")

for i in range(nhist):
    preselect_name = "h_preselect_"+str(i)
    preselect.append(TH1F(preselect_name,signalname[i],17,0,1700))
    loo_name = "h_loo_"+str(i)
    loo.append(TH1F(loo_name,signalname[i],17,0,1700))
    med1_name = "h_med1_"+str(i)
    med1.append(TH1F(med1_name,signalname[i],17,0,1700))
    med2_name = "h_med2_"+str(i)
    med2.append(TH1F(med2_name,signalname[i],17,0,1700))

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
        if (FJetCSV > 0.7) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            loo[i].Fill(MH3[i])
        if (FJetCSV > 0.86) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            med1[i].Fill(MH3[i])
        if (FJetCSV > 0.89) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            med2[i].Fill(MH3[i])

outfile.Write()
outfile.Close()


#plot efficiency

c1 = TCanvas("c1", "c1", 900, 900)
c1.SetLeftMargin(0.15)
#c1.Divide(1,9,0.01,0.01)
#lt = TLatex()

leg = TLegend(0.55,0.15,0.7,0.3)
leg.SetBorderSize(0)
leg.SetTextSize(0.027)
nhist = 8
openf = TFile("singlevaluesignal3.root", "read")

mg = TMultiGraph("mg","")
mg.SetTitle("Signal Efficiency; MH3 (GeV); Efficiency")
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetLabelOffset(1.4)
mg.GetXaxis().SetTitleOffset(4.0)


for i in range(nhist):
    preselect = openf.Get("h_preselect_"+str(i))
    loo = openf.Get("h_loo_"+str(i))
    med1 = openf.Get("h_med1_"+str(i))
    med2 = openf.Get("h_med2_"+str(i))

    gPad.Modified()
    #effL_name = "effL"+str(i)
    effL = TGraphAsymmErrors(loo,preselect,"cl=0.683 b(1,1) mode")
    effL.SetTitle("Loose")
    effL.SetMarkerColor(1)
    effL.SetMarkerStyle(21)
    #effL.SetMarkerSize(1.5)
    effL.SetLineColor(1)
    effL.SetLineWidth(4)

    #effM1_name = "effM1"+str(i)
    effM1 = TGraphAsymmErrors(med1,preselect,"cl=0.683 b(1,1) mode")
    effM1.SetTitle("Medium 1")
    effM1.SetMarkerColor(2)
    effM1.SetMarkerStyle(20)
    #effM1.SetMarkerSize(1.5)
    effM1.SetLineColor(2)
    effM1.SetLineWidth(4)

    #effM2_name = "effM2"+str(i)
    effM2 = TGraphAsymmErrors(med2,preselect,"cl=0.683 b(1,1) mode")
    effM2.SetTitle("Medium 2")
    effM2.SetMarkerColor(4)
    effM2.SetMarkerStyle(22)
    #effM2.SetMarkerSize(1.5)
    effM2.SetLineColor(4)
    effM2.SetLineWidth(4)

    mg.Add(effL, "AP")
    mg.Add(effM1, "AP")
    mg.Add(effM2, "AP")

mg.Draw("AP")

leg.AddEntry(effL, "Loose")
leg.AddEntry(effM1, "Medium 1")
leg.AddEntry(effM2, "Medium 2")
leg.Draw()

c1.cd()
c1.Update()
c1.SaveAs("sigeffFJetCSV_new_add.pdf")

