# created by Fasya Khuzaimah on 2019.11.13

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad
import array as arr
import numpy as np

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

FJetMassL = []
FJetMassM1 = []
FJetMassM2 = []

effL = arr.array('d')
effM1 = arr.array('d')
effM2 = arr.array('d')

h_FJetMassBfr = TH1F("h_FJetMassBfr","FJetMass Before Deep Double",40,0,1000)
h_FJetMassL = TH1F("h_FJetMassL","FJetMass Loose",40,0,1000)
h_FJetMassM1 = TH1F("h_FJetMassM1","FJetMass Medium1",40,0,1000)
h_FJetMassM2 = TH1F("h_FJetMassM2","FJetMass Medium2",40,0,1000)

countL = 0
countM1 = 0
countM2 = 0

for i in range(len(fname)):
    openf = TFile(path+fname[i], "read")
    treef = openf.Get("monoHbb_SR_boosted")
    preEvents = treef.GetEntries()
    h_FJetMassBfr.Fill(preEvents)
    #print fname[i], preEvents
    
    for j in range(preEvents):
        treef.GetEntry(j)
        FJetMass = getattr(treef, 'FJetMass')
        FJetCSV = getattr(treef, 'FJetCSV')
        dPhi = getattr(treef, 'min_dPhi')
        nJets = getattr(treef, 'nJets')
        if (FJetCSV > 0.7) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            countL = countL + 1
            h_FJetMassL.Fill(FJetMass)
        if (FJetCSV > 0.86) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            countM1 = countM1 + 1
            h_FJetMassM1.Fill(FJetMass)
        if (FJetCSV > 0.89) and (FJetMass > 100.0) and (FJetMass < 150.0) and (dPhi > 0.4) and (nJets <= 2.0):
            countM2 = countM2 + 1
            h_FJetMassM2.Fill(FJetMass)

    FJetMassL.append(countL)
    FJetMassM1.append(countM1)
    FJetMassM2.append(countM2)

    nFJetMassL = h_FJetMassL.Integral()
    nFJetMassM1 = h_FJetMassM1.Integral()
    nFJetMassM2 = h_FJetMassM2.Integral()

    effL.append(nFJetMassL/preEvents)
    effM1.append(nFJetMassM1/preEvents)
    effM2.append(nFJetMassM2/preEvents)

    h_FJetMassL.Reset()
    h_FJetMassM1.Reset()
    h_FJetMassM2.Reset()

    '''
    print fname[i]
    print "countL", countL
    print "nFJetMassL", nFJetMassL
    print "countM1", countM1
    print "nFJetMassM1", nFJetMassM1
    print "countM2", countM2
    print "nFJetMassM2", nFJetMassM2
    '''

    countL = 0
    countM1 = 0
    countM2 = 0


print "###############################################"
print "effL", effL
print "effM1", effM1
print "effM2", effM2




#BACKGROUND#

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root","crab_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root","crab_ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.root","crab_WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0047, 300.9498, 72.1455, 3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6, 0.01222, 0.006185, 0.3654, 0.2819, 0.07924, 0.1565]

MH3name = arr.array('d', [300, 400, 500, 600, 1000, 1200, 1400, 1600])

h_FJetMassBkgL = TH1F("h_FJetMassBkgL","Background FJetMass Loose",40,0,1000)
h_FJetMassBkgM1 = TH1F("h_FJetMassBkgM1","Background FJetMass Medium1",40,0,1000)
h_FJetMassBkgM2 = TH1F("h_FJetMassBkgM2","Background FJetMass Medium2",40,0,1000)
h_sumbkgL = TH1F("h_sumbkgL","Sum Number of After Loose B-Tagging Events of All HT Points QCD Background",40,0,1000)
h_sumbkgM1 = TH1F("h_sumbkgM1","Sum Number of After Medium1 B-Tagging Events of All HT Points QCD Background",40,0,1000)
h_sumbkgM2 = TH1F("h_sumbkgM2","Sum Number of After Medium2 B-Tagging Events of All HT Points QCD Background",40,0,1000)

#FJetMassBkgL = []
#FJetMassBkgM1 = []
#FJetMassBkgM2 = []

L = 41000.0 #1/pb

NdataL = 0
NdataM1 = 0
NdataM2 = 0

NdataLfinal = 0
NdataM1final = 0
NdataM2final = 0

Nbkgdata = arr.array('d')
#err_Nbkgdata = arr.array('d')

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
        if (FJetCSVBkg > 0.7) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (dPhiBkg > 0.4) and (nJetsBkg <= 2.0):
            #FJetMassBkgL.append(FJetMassBkg)
            h_FJetMassBkgL.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.86) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (dPhiBkg > 0.4) and (nJetsBkg <= 2.0):
            #FJetMassBkgM1.append(FJetMassBkg)
            h_FJetMassBkgM1.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.89) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (dPhiBkg > 0.4) and (nJetsBkg <= 2.0):
            #FJetMassBkgM2.append(FJetMassBkg)
            h_FJetMassBkgM2.Fill(FJetMassBkg)

    
    h_FJetMassBkgL_without = h_FJetMassBkgL.Integral()
    h_FJetMassBkgM1_without = h_FJetMassBkgM1.Integral()
    h_FJetMassBkgM2_without = h_FJetMassBkgM2.Integral()
    
    #number of expected obs events in data
    h_FJetMassBkgL = h_FJetMassBkgL*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM1 = h_FJetMassBkgM1*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM2 = h_FJetMassBkgM2*(L*xsBkg[i]/eventsbkg)

    NdataL = h_FJetMassBkgL.Integral()
    NdataM1 = h_FJetMassBkgM1.Integral()
    NdataM2 = h_FJetMassBkgM2.Integral()


    print bkgname[i]
    #print "Number of background events Before normalization (Loose)", h_FJetMassBkgL_without
    print "Number of background events After normalization (Loose)", NdataL
    #print "Number of background events Before normalization (Medium 1)", h_FJetMassBkgM1_without
    print "Number of background events After normalization (Medium 1)", NdataM1
    #print "Number of background events Before normalization (Medium 2)", h_FJetMassBkgM2_without
    print "Number of background events After normalization (Medium 2)", NdataM2
    print " "


    #sum all number of expected obs background events in data for all QCD HT
    
    NdataLfinal += NdataL
    NdataM1final += NdataM1
    NdataM2final += NdataM2

    #h_sumbkgL += h_FJetMassBkgL
    #h_sumbkgM1 += h_FJetMassBkgM1
    #h_sumbkgM2 += h_FJetMassBkgM2
    
    h_FJetMassBkgL.Reset()
    h_FJetMassBkgM1.Reset()
    h_FJetMassBkgM2.Reset()

Nbkgdata.append(NdataLfinal)
Nbkgdata.append(NdataM1final)
Nbkgdata.append(NdataM2final)

#NbkgL_Sum = h_sumbkgL.Integral()
#NbkgM1_Sum = h_sumbkgM1.Integral()
#NbkgM2_Sum = h_sumbkgM2.Integral()

print "########################################################"
#print "countBkgLnorm", countBkgLnorm
print "expected # of bkg obs events in data L", NdataLfinal
#print "countBkgM1norm", countBkgM1norm
print "expected # of bkg obs events in data M1", NdataM1final
#print "countBkgM2norm", countBkgM2norm
print "expected # of bkg obs events in data M2", NdataM2final

print "########################################################"
print "Nbkg for each FJetCSV selections", Nbkgdata

#print "########################################################"
#print "h_sumbkgL", NbkgL_Sum
#print "h_sumbkgM1", NbkgM1_Sum
#print "h_sumbkgM2", NbkgM2_Sum

#Calculate Punzi Significance
PS_L_list = arr.array('d')
PS_M1_list = arr.array('d')
PS_M2_list = arr.array('d')


n = 8

for i in range(len(fname)):
    PS_L = effL[i]/(1+TMath.Sqrt(NdataLfinal))
    PS_L_list.append(PS_L)
    PS_M1 = effM1[i]/(1+TMath.Sqrt(NdataM1final))
    PS_M1_list.append(PS_M1)
    PS_M2 = effM2[i]/(1+TMath.Sqrt(NdataM2final))
    PS_M2_list.append(PS_M2)


print "########################################"
print "PS_L", PS_L_list
print "PS_M1", PS_M1_list
print "PS_M2", PS_M2_list


'''
for i in range(len(name)):
    h_PS_L.GetXaxis().SetBinLabel(i+1,str(name[i]))
    h_PS_M1.GetXaxis().SetBinLabel(i+1,str(name[i]))
    h_PS_M2.GetXaxis().SetBinLabel(i+1,str(name[i]))


h_PS_L.GetXaxis().SetTitle("MH3")
h_PS_L.GetYaxis().SetTitle("Punzi Significance")
#h_PS_L.GetYaxis().SetRangeUser(0.0004, 0.002)
h_PS_L.SetLineColor(1)
h_PS_M1.SetLineColor(2)
h_PS_M2.SetLineColor(3)
h_PS_L.Draw("C")
h_PS_M1.Draw("Csame")
h_PS_M2.Draw("Csame")
'''

zero1 = np.zeros(8)


#Draw Punzi Significance

errPS_L = arr.array('d', [0.00024717073889838465, 0.00027674730883115004, 0.00023707708612228496, 0.00019931550792351275, 0.0001600304400442039, 0.0001295716331722805, 0.00022394633266038672, 0.000489505030564238])
errPS_M1 = arr.array('d', [0.00034287732312390454, 0.0003954453544029015, 0.00034222553317496944, 0.0002896563044122645, 0.0002651230867486092, 0.00022505137387711502, 0.000365601276538445, 0.0007539338627194009])
errPS_M2 = arr.array('d', [0.00036380153699832436, 0.00039375232755952105, 0.00039652258004984107, 0.00031592606466020054, 0.000347406458221962, 0.00031724045826028887, 0.0004814937176075917, 0.0009651024251403215])

c1 = TCanvas("c1","c1",900,700) #width-height
c1.SetLeftMargin(0.15)

gPad.Modified()
gr1 = TGraphErrors(n, MH3name, PS_L_list, zero1, errPS_L)
gr1.SetTitle("Loose")
gr1.GetYaxis().SetNdivisions(505)
gr1.GetYaxis().SetLabelOffset(1.4)
gr1.GetXaxis().SetTitleOffset(4.0)
gr1.SetLineColor(1)
gr1.SetLineWidth(5)
gr1.SetMarkerStyle(20)
gr1.SetMarkerColor(1)

gr2 = TGraphErrors(n, MH3name, PS_M1_list, zero1, errPS_M1)
gr2.SetTitle("Medium 1")
gr2.GetYaxis().SetNdivisions(505)
gr2.GetYaxis().SetLabelOffset(1.4)
gr2.GetXaxis().SetTitleOffset(4.0)
gr2.SetLineColor(2)
gr2.SetLineWidth(5)
gr2.SetMarkerStyle(21)
gr2.SetMarkerColor(2)

gr3 = TGraphErrors(n, MH3name, PS_M2_list, zero1, errPS_M2)
gr3.SetTitle("Medium 2")
gr3.GetYaxis().SetNdivisions(505)
gr3.GetYaxis().SetLabelOffset(1.4)
gr3.GetXaxis().SetTitleOffset(4.0)
gr3.SetLineColor(4)
gr3.SetLineWidth(5)
gr3.SetMarkerStyle(22)
gr3.SetMarkerColor(4)

mg = TMultiGraph("mg","")
mg.SetTitle("Punzi Significance; MH3 (GeV); Punzi Significance")
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetLabelOffset(1.4)
mg.GetXaxis().SetTitleOffset(4.0)
mg.Add(gr1, "ALP")
mg.Add(gr2, "ALP")
mg.Add(gr3, "ALP")
mg.Draw("ALP")
c1.BuildLegend()

c1.cd()
c1.Update()
c1.SaveAs("PS_all_new_add.pdf")


#Draw Signal Efficiency

c2 = TCanvas("c2","c2",900,700) #width-height
c2.SetLeftMargin(0.15)

gPad.Modified()
gr4 = TGraph(n,MH3name,effL)
gr4.SetTitle("Loose")
gr4.GetYaxis().SetNdivisions(505)
gr4.GetYaxis().SetLabelOffset(1.4)
gr4.GetXaxis().SetTitleOffset(4.0)
gr4.SetLineColor(1)
gr4.SetLineWidth(5)
gr4.SetMarkerStyle(20)
gr4.SetMarkerColor(1)

gr5 = TGraph(n,MH3name,effM1)
gr5.SetTitle("Medium 1")
gr5.GetYaxis().SetNdivisions(505)
gr5.GetYaxis().SetLabelOffset(1.4)
gr5.GetXaxis().SetTitleOffset(4.0)
gr5.SetLineColor(2)
gr5.SetLineWidth(5)
gr5.SetMarkerStyle(21)
gr5.SetMarkerColor(2)

gr6 = TGraph(n,MH3name,effM2)
gr6.SetTitle("Medium 2")
gr6.GetYaxis().SetNdivisions(505)
gr6.GetYaxis().SetLabelOffset(1.4)
gr6.GetXaxis().SetTitleOffset(4.0)
gr6.SetLineColor(4)
gr6.SetLineWidth(5)
gr6.SetMarkerStyle(22)
gr6.SetMarkerColor(4)

mg2 = TMultiGraph("mg2","")
mg2.SetTitle("Signal Efficiency; MH3 (GeV); Efficiency")
mg2.GetYaxis().SetNdivisions(505)
mg2.GetYaxis().SetLabelOffset(1.4)
mg2.GetXaxis().SetTitleOffset(4.0)
mg2.Add(gr4, "ALP")
mg2.Add(gr5, "ALP")
mg2.Add(gr6, "ALP")
mg2.Draw("ALP")
c2.BuildLegend()

c2.cd()
c2.Update()
c2.SaveAs("SignalEfficiency_new_add.pdf")

#Draw Number of Expected Bkg Events in Data after deep double b-tagger

m = 3
selections = arr.array('d', [0.70, 0.86, 0.89])

c3 = TCanvas("c3","c3",900,700) #width-height
c3.SetLeftMargin(0.15)

gPad.Modified()
gr7 = TGraph(m,selections,Nbkgdata)
gr7.GetYaxis().SetNdivisions(505)
gr7.GetYaxis().SetLabelOffset(1.4)
gr7.GetXaxis().SetTitleOffset(4.0)
gr7.SetLineColor(2)
gr7.SetLineWidth(5)
gr7.SetMarkerStyle(21)

mg3 = TMultiGraph("mg3","")
mg3.SetTitle("Normalized Number of Background Events; Fat Jet CSV; Number of Events")
mg3.GetYaxis().SetNdivisions(505)
mg3.GetYaxis().SetLabelOffset(1.4)
mg3.GetXaxis().SetTitleOffset(4.0)
mg3.Add(gr7, "ALP")
mg3.Draw("ALP")

c3.cd()
c3.Update()
c3.SaveAs("Nbkg_new_add.pdf")

