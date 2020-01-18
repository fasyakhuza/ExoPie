# created by Fasya Khuzaimah on 2020.01.17
#vetos working point optimization

import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, TAxis, TGraph, TMultiGraph, TGraphErrors, TPad, TLegend, gPad
import array as arr
import numpy as np

path = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/2017_AnalyserOutput/V0_no_nBjets_cond/"

fname = ["EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150_MH2_500_MHC_500_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150_MH2_1200_MHC_1200_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1400_MH4_150_MH2_1400_MHC_1400_CP3Tune_13TeV_0000_0.root","EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150_MH2_1600_MHC_1600_CP3Tune_13TeV_0000_0.root"]

#NsigL = []
#NsigM = []

effL = arr.array('d')
effM = arr.array('d')

h_sigBfr = TH1F("h_sigBfr","Number of Signal Events Before Veto ID Selection",40,0,1000)
h_sigL = TH1F("h_sigL","Number of Signal Events Pass Loose Veto ID",40,0,1000)
h_sigM = TH1F("h_sigM","Number of Signal Events Pass Medium Veto ID",40,0,1000)

countL = 0
countM = 0

for i in range(len(fname)):
    openf = TFile(path+fname[i], "read")
    treef = openf.Get("monoHbb_SR_boosted")
    preEvents = treef.GetEntries()
    h_sigBfr.Fill(preEvents)
    #print fname[i], preEvents
    
    for j in range(preEvents):
        treef.GetEntry(j)
        #FJetMass = getattr(treef, 'FJetMass')
        Nbjets_LPassID = getattr(treef, 'Nbjets_LPassID')
        Nbjets_MPassID = getattr(treef, 'Nbjets_MPassID')
        if (Nbjets_LPassID == 0):
            #countL = countL + 1
            h_sigL.Fill(Nbjets_LPassID)
        if (Nbjets_MPassID == 0):
            #countM = countM + 1
            h_sigM.Fill(Nbjets_MPassID)

    #NsigL.append(countL)
    #NsigM.append(countM)

    TotalsigL = h_sigL.Integral()
    TotalsigM = h_sigM.Integral()

    effL.append(TotalsigL/preEvents)
    effM.append(TotalsigM/preEvents)

    h_sigL.Reset()
    h_sigM.Reset()


    print fname[i]
    #print "countL", countL
    print "TotalsigL", TotalsigL
    #print "countM", countM
    print "TotalsigM", TotalsigM


    countL = 0
    countM = 0


print "###############################################"
print "effL", effL
print "effM", effM




#BACKGROUND#

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root","crab_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root","crab_ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8.root","crab_WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8.root","crab_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0047, 300.9498, 72.1455, 3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6, 0.01222, 0.006185, 0.3654, 0.2819, 0.07924, 0.1565]

MH3name = arr.array('d', [300, 400, 500, 600, 1000, 1200, 1400, 1600])

h_BkgL = TH1F("h_BkgL","Number of Background Events Pass Loose Veto ID",40,0,1000)
h_BkgM = TH1F("h_BkgM","Number of Background Events Pass Medium Veto ID",40,0,1000)
h_sumbkgL = TH1F("h_sumbkgL","Sum Number of Background Events Pass Loose Veto ID",40,0,1000)
h_sumbkgM = TH1F("h_sumbkgM","Sum Number of Background Events Pass Medium Veto ID",40,0,1000)

#FJetMassBkgL = []
#FJetMassBkgM = []

L = 41000.0 #1/pb

NdataL = 0
NdataM = 0

NdataLfinal = 0
NdataMfinal = 0

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
        #FJetMassBkg = getattr(treebkg, 'FJetMass')
        Nbjets_LPassID_Bkg = getattr(treebkg, 'Nbjets_LPassID')
        Nbjets_MPassID_Bkg = getattr(treebkg, 'Nbjets_MPassID')
        if (Nbjets_LPassID_Bkg == 0):
            #FJetMassBkgL.append(FJetMassBkg)
            h_BkgL.Fill(Nbjets_LPassID_Bkg)
        if (Nbjets_MPassID_Bkg == 0):
            #FJetMassBkgM1.append(FJetMassBkg)
            h_BkgM.Fill(Nbjets_MPassID_Bkg)

    
    h_BkgL_without = h_BkgL.Integral()
    h_BkgM_without = h_BkgM.Integral()
    
    #number of expected obs events in data
    h_BkgL = h_BkgL*(L*xsBkg[i]/eventsbkg)
    h_BkgM = h_BkgM*(L*xsBkg[i]/eventsbkg)

    NdataL = h_BkgL.Integral()
    NdataM = h_BkgM.Integral()


    print bkgname[i]
    #print "Number of background events Before normalization (Loose)", h_BkgL_without
    print "Number of background events After normalization (Loose)", NdataL
    #print "Number of background events Before normalization (Medium)", h_BkgM_without
    print "Number of background events After normalization (Medium)", NdataM
    print " "


    #sum all number of expected obs background events in data for all QCD HT
    
    NdataLfinal += NdataL
    NdataMfinal += NdataM

    #h_sumbkgL += h_BkgL
    #h_sumbkgM += h_BkgM
    
    h_BkgL.Reset()
    h_BkgM.Reset()

Nbkgdata.append(NdataLfinal)
Nbkgdata.append(NdataMfinal)

#NbkgL_Sum = h_sumbkgL.Integral()
#NbkgM_Sum = h_sumbkgM.Integral()

print "########################################################"
print "expected # of bkg obs events in data L", NdataLfinal
print "expected # of bkg obs events in data M", NdataMfinal

print "########################################################"
print "Nbkg for each Veto ID selections", Nbkgdata

#print "########################################################"
#print "h_sumbkgL", NbkgL_Sum
#print "h_sumbkgM", NbkgM_Sum

#Calculate Punzi Significance
PS_L_list = arr.array('d')
PS_M_list = arr.array('d')


n = 8

for i in range(len(fname)):
    PS_L = effL[i]/(1+TMath.Sqrt(NdataLfinal))
    PS_L_list.append(PS_L)
    PS_M = effM[i]/(1+TMath.Sqrt(NdataMfinal))
    PS_M_list.append(PS_M)


print "########################################"
print "PS_L", PS_L_list
print "PS_M", PS_M_list


zero = np.zeros(8)


#Draw Punzi Significance

#errPS_L = arr.array('d', [0.00024717073889838465, 0.00027674730883115004, 0.00023707708612228496, 0.00019931550792351275, 0.0001600304400442039, 0.0001295716331722805, 0.00022394633266038672, 0.000489505030564238])
#errPS_M = arr.array('d', [0.00034287732312390454, 0.0003954453544029015, 0.00034222553317496944, 0.0002896563044122645, 0.0002651230867486092, 0.00022505137387711502, 0.000365601276538445, 0.0007539338627194009])

c1 = TCanvas("c1","c1",900,700) #width-height
c1.SetLeftMargin(0.15)

gPad.Modified()
gr1 = TGraphErrors(n, MH3name, PS_L_list, zero, zero)
gr1.SetTitle("Loose")
gr1.GetYaxis().SetNdivisions(505)
gr1.GetYaxis().SetLabelOffset(1.4)
gr1.GetXaxis().SetTitleOffset(4.0)
gr1.SetLineColor(1)
gr1.SetLineWidth(5)
gr1.SetMarkerStyle(20)
gr1.SetMarkerColor(1)

gr2 = TGraphErrors(n, MH3name, PS_M_list, zero, zero)
gr2.SetTitle("Medium")
gr2.GetYaxis().SetNdivisions(505)
gr2.GetYaxis().SetLabelOffset(1.4)
gr2.GetXaxis().SetTitleOffset(4.0)
gr2.SetLineColor(2)
gr2.SetLineWidth(5)
gr2.SetMarkerStyle(21)
gr2.SetMarkerColor(2)

mg = TMultiGraph("mg","")
mg.SetTitle("Punzi Significance; MH3 (GeV); Punzi Significance")
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetLabelOffset(1.4)
mg.GetXaxis().SetTitleOffset(4.0)
mg.Add(gr1, "ALP")
mg.Add(gr2, "ALP")
mg.Draw("ALP")
c1.BuildLegend()

c1.cd()
c1.Update()
c1.SaveAs("vetos_PS.pdf")


#Draw Signal Efficiency

c2 = TCanvas("c2","c2",900,700) #width-height
c2.SetLeftMargin(0.15)

gPad.Modified()
gr3 = TGraph(n,MH3name,effL)
gr3.SetTitle("Loose")
gr3.GetYaxis().SetNdivisions(505)
gr3.GetYaxis().SetLabelOffset(1.4)
gr3.GetXaxis().SetTitleOffset(4.0)
gr3.SetLineColor(1)
gr3.SetLineWidth(5)
gr3.SetMarkerStyle(20)
gr3.SetMarkerColor(1)

gr4 = TGraph(n,MH3name,effM)
gr4.SetTitle("Medium")
gr4.GetYaxis().SetNdivisions(505)
gr4.GetYaxis().SetLabelOffset(1.4)
gr4.GetXaxis().SetTitleOffset(4.0)
gr4.SetLineColor(2)
gr4.SetLineWidth(5)
gr4.SetMarkerStyle(21)
gr4.SetMarkerColor(2)

mg2 = TMultiGraph("mg2","")
mg2.SetTitle("Signal Efficiency; MH3 (GeV); Efficiency")
mg2.GetYaxis().SetNdivisions(505)
mg2.GetYaxis().SetLabelOffset(1.4)
mg2.GetXaxis().SetTitleOffset(4.0)
mg2.Add(gr3, "ALP")
mg2.Add(gr4, "ALP")
mg2.Draw("ALP")
c2.BuildLegend()

c2.cd()
c2.Update()
c2.SaveAs("vetos_SignalEfficiency.pdf")
'''
#Draw Number of Expected Bkg Events in Data after deep double b-tagger

m = 2
selections = arr.array["Nbjets_LPassID", "Nbjets_MPassID"]

c3 = TCanvas("c3","c3",900,700) #width-height
c3.SetLeftMargin(0.15)

gPad.Modified()
gr5 = TGraph(m,selections,Nbkgdata)
gr5.GetYaxis().SetNdivisions(505)
gr5.GetYaxis().SetLabelOffset(1.4)
gr5.GetXaxis().SetTitleOffset(4.0)
gr5.SetLineColor(2)
gr5.SetLineWidth(5)
gr5.SetMarkerStyle(21)

mg3 = TMultiGraph("mg3","")
mg3.SetTitle("Normalized Number of Background Events; Selections; Number of Events")
mg3.GetYaxis().SetNdivisions(505)
mg3.GetYaxis().SetLabelOffset(1.4)
mg3.GetXaxis().SetTitleOffset(4.0)
mg3.Add(gr5, "ALP")
mg3.Draw("ALP")

c3.cd()
c3.Update()
c3.SaveAs("vetos_Nbkg.pdf")
'''
