# created by Fasya Khuzaimah on 2019.11.13

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TPad, TLegend, TAttPad
import array as arr

c1 = TCanvas("c1","c1",1000,700) #width-height

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

#FJetMassL = []
#FJetMassM1 = []
#FJetMassM2 = []
effL = []
effM1 = []
effM2 = []

h_FJetMassL = TH1F("h_FJetMassL","FJetMass Loose",40,0,1000)
h_FJetMassM1 = TH1F("h_FJetMassM1","FJetMass Medium1",40,0,1000)
h_FJetMassM2 = TH1F("h_FJetMassM2","FJetMass Medium2",40,0,1000)


for i in range(len(fname)):
    openf = TFile(path+fname[i], "read")
    treef = openf.Get("monoHbb_SR_boosted")
    preEvents = treef.GetEntries()

    
    for j in range(preEvents):
        treef.GetEntry(j)
        FJetMass = getattr(treef, 'FJetMass')
        FJetCSV = getattr(treef, 'FJetCSV')
        if (FJetCSV > 0.7):
            #FJetMassL.append(FJetMass)
            h_FJetMassL.Fill(FJetMass)
            nFJetMassL = h_FJetMassL.Integral()
        if (FJetCSV > 0.86):
            #FJetMassM1.append(FJetMass)
            h_FJetMassM1.Fill(FJetMass)
            nFJetMassM1 = h_FJetMassM1.Integral()
        if (FJetCSV > 0.89):
            #FJetMassM2.append(FJetMass)
            h_FJetMassM2.Fill(FJetMass)
            nFJetMassM2 = h_FJetMassM2.Integral()


    effL.append(nFJetMassL/preEvents)
    effM1.append(nFJetMassM1/preEvents)
    effM2.append(nFJetMassM2/preEvents)

    h_FJetMassL.Reset()
    h_FJetMassM1.Reset()
    h_FJetMassM2.Reset()


print "effL", effL
print "effM1", effM1
print "effM2", effM2




#BACKGROUND#

bkgname = ["QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root","QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root"]

xsBkg = [1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24]
HTname = arr.array('d', [300, 400, 500, 600, 600, 1000, 1200, 1400, 1600])

h_FJetMassBkgL = TH1F("h_FJetMassBkgL","Background FJetMass Loose",40,0,1000)
h_FJetMassBkgM1 = TH1F("h_FJetMassBkgM1","Background FJetMass Medium1",40,0,1000)
h_FJetMassBkgM2 = TH1F("h_FJetMassBkgM2","Background FJetMass Medium2",40,0,1000)
h_sumbkgL = TH1F("h_sumbkgL","Sum Number of After Loose B-Tagging Events of All HT Points QCD Background",40,0,1000)
h_sumbkgM1 = TH1F("h_sumbkgM1","Sum Number of After Medium1 B-Tagging Events of All HT Points QCD Background",40,0,1000)
h_sumbkgM2 = TH1F("h_sumbkgM2","Sum Number of After Medium2 B-Tagging Events of All HT Points QCD Background",40,0,1000)

#FJetMassBkgL = []
#FJetMassBkgM1 = []
#FJetMassBkgM2 = []

L = 150000.0 #1/pb

NdataL = 0
NdataM1 = 0
NdataM2 = 0

for i in range(len(bkgname)):
    openbkg = TFile(path+bkgname[i])
    treebkg = openbkg.Get("monoHbb_SR_boosted")
    preEventsbkg = treebkg.GetEntries()

    for j in range(preEventsbkg):
        treebkg.GetEntry(j)
        FJetMassBkg = getattr(treebkg, 'FJetMass')
        FJetCSVBkg = getattr(treebkg, 'FJetCSV')
        if (FJetCSVBkg > 0.7):
            #FJetMassBkgL.append(FJetMassBkg)
            h_FJetMassBkgL.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.86):
            #FJetMassBkgM1.append(FJetMassBkg)
            h_FJetMassBkgM1.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.89):
            #FJetMassBkgM2.append(FJetMassBkg)
            h_FJetMassBkgM2.Fill(FJetMassBkg)

    #number of expected obs events in data
    h_FJetMassBkgL = h_FJetMassBkgL*(L*xsBkg[i]/preEventsbkg)
    h_FJetMassBkgM1 = h_FJetMassBkgM1*(L*xsBkg[i]/preEventsbkg)
    h_FJetMassBkgM2 = h_FJetMassBkgM2*(L*xsBkg[i]/preEventsbkg)
    
    NdataL = h_FJetMassBkgL.Integral()
    NdataM1 = h_FJetMassBkgM1.Integral()
    NdataM2 = h_FJetMassBkgM2.Integral()
    
    h_FJetMassBkgL.Reset()
    h_FJetMassBkgM1.Reset()
    h_FJetMassBkgM2.Reset()

    #sum all number of expected obs background events in data for all QCD HT
    NdataL += NdataL
    NdataM1 += NdataM1
    NdataM2 += NdataM2

print "# of obs data L", NdataL
print "# of obs data M1", NdataM1
print "# of obs data M2", NdataM2


#Calculate Punzi Significance
PS_L_list = arr.array('d')
PS_M1_list = arr.array('d')
PS_M2_list = arr.array('d')

#h_PS_L = TH1F("h_PS_L", "", 21, 300, 1600)
#h_PS_M1 = TH1F("h_PS_M1", "", 21, 300, 1600)
#h_PS_M2 = TH1F("h_PS_M2", "", 21, 300, 1600)

n = 9

for i in range(len(fname)):
    PS_L = effL[i]/(1+TMath.Sqrt(NdataL))
    #h_PS_L.Fill(PS_L)
    PS_L_list.append(PS_L)
    PS_M1 = effM1[i]/(1+TMath.Sqrt(NdataM1))
    #h_PS_M1.Fill(PS_M1)
    PS_M1_list.append(PS_M1)
    PS_M2 = effM2[i]/(1+TMath.Sqrt(NdataM2))
    #h_PS_M2.Fill(PS_M2)
    PS_M2_list.append(PS_M2)

print "PS_L", PS_L_list
print "PS_M1", PS_M1_list
print "PS_M2", PS_M2_list

'''
for i in range(len(name)):
    h_PS_L.GetXaxis().SetBinLabel(i+1,str(name[i]))
    h_PS_M1.GetXaxis().SetBinLabel(i+1,str(name[i]))
    h_PS_M2.GetXaxis().SetBinLabel(i+1,str(name[i]))


h_PS_L.GetXaxis().SetTitle("HT")
h_PS_L.GetYaxis().SetTitle("Punzi Significance")
#h_PS_L.GetYaxis().SetRangeUser(0.0004, 0.002)
h_PS_L.SetLineColor(1)
h_PS_M1.SetLineColor(2)
h_PS_M2.SetLineColor(3)
h_PS_L.Draw("C")
h_PS_M1.Draw("Csame")
h_PS_M2.Draw("Csame")
'''

gr1 = TGraph(n,HTname,PS_L_list)
gr1.SetTitle("Loose (FJetCSV > 0.7)")
gr1.SetLineColor(2)
gr1.SetLineWidth(5)
gr1.SetMarkerStyle(20)

gr2 = TGraph(n,HTname,PS_M1_list)
gr2.SetTitle("Medium1 (FJetCSV > 0.86)")
gr2.SetLineColor(3)
gr2.SetLineWidth(5)
gr2.SetMarkerStyle(21)

gr3 = TGraph(n,HTname,PS_M2_list)
gr3.SetTitle("Medium2 (FJetCSV > 0.89)")
gr3.SetLineColor(4)
gr3.SetLineWidth(5)
gr3.SetMarkerStyle(22)

mg = TMultiGraph("mg","")
mg.SetTitle("QCD Background; HT (GeV); Punzi Significance")
#mg.GetYaxis().SetTitleOffset(0.1)
mg.Add(gr1, "ALP")
mg.Add(gr2, "ALP")
mg.Add(gr3, "ALP")
mg.Draw("ALP")
c1.BuildLegend()

c1.cd()
c1.Update()
c1.SaveAs("PS_test.png")

