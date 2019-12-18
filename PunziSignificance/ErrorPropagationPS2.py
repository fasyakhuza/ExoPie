import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, gStyle, TGraphAsymmErrors, gPad, TMultiGraph, TLatex

filename = "singlevaluesignal3.root"
file = TFile(filename, "read")

nfile = 8
nbin = 17

name = ["300", "400", "500", "600", "1000", "1200", "1400", "1600"]

err_sigeff_L = []
err_sigeff_M1 = []
err_sigeff_M2 = []

xL = ROOT.Double(0)
yL = ROOT.Double(0)

xM1 = ROOT.Double(0)
yM1 = ROOT.Double(0)

xM2 = ROOT.Double(0)
yM2 = ROOT.Double(0)

for i in range(nfile):
    preselect = file.Get("h_preselect_"+str(i))
    loo = file.Get("h_loo_"+str(i))
    med1 = file.Get("h_med1_"+str(i))
    med2 = file.Get("h_med2_"+str(i))

    #gPad.Modified()
    effL = TGraphAsymmErrors(loo,preselect,"cl=0.683 b(1,1) mode")
    effL.SetTitle("Loose (FJetCSV > 0.7)")
    binL = effL.GetN()
    for j in range(binL):
        effL.GetPoint(j, xL, yL)
        if (yL == 0):
            continue
        else:
            errL = effL.GetErrorY(j)
            err_sigeff_L.append(errL)
    #print "errL_"+str(name[i]), errL

    effM1 = TGraphAsymmErrors(med1,preselect,"cl=0.683 b(1,1) mode")
    effM1.SetTitle("Medium1 (FJetCSV > 0.86)")
    binM1 = effM1.GetN()
    for j in range(binM1):
        effM1.GetPoint(j, xM1, yM1)
        if (yM1 == 0):
            continue
        else:
            errM1 = effM1.GetErrorY(j)
            err_sigeff_M1.append(errM1)
    #print "errM1_"+str(name[i]), errM1

    effM2 = TGraphAsymmErrors(med2,preselect,"cl=0.683 b(1,1) mode")
    effM2.SetTitle("Medium2 (FJetCSV > 0.89)")
    binM2 = effM2.GetN()
    for j in range(binM2):
        effM2.GetPoint(j, xM2, yM2)
        if (yM2 == 0):
            continue
        else:
            errM2 = effM2.GetErrorY(j)
            err_sigeff_M2.append(errM2)
    #print "errM2_"+str(name[i]), errM2

print "####################################"
print "err_sigeff_L", err_sigeff_L
print "err_sigeff_M1", err_sigeff_M1
print "err_sigeff_M2", err_sigeff_M2
print "####################################"


#NUMBER OF BACKGROUND EVENTS

path = "/afs/cern.ch/work/d/dekumar/public/monoH/Analyzer/CMSSW_10_3_0/src/ExoPieProducer/ExoPieAnalyzer/OutputForRaman/"

bkgname = ["DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "ZJetsToNuNu_HT-100To200_13TeV-madgraph.root", "ZJetsToNuNu_HT-200To400_13TeV-madgraph.root", "ZJetsToNuNu_HT-400To600_13TeV-madgraph.root", "ZJetsToNuNu_HT-600To800_13TeV-madgraph.root", "ZJetsToNuNu_HT-800To1200_13TeV-madgraph.root", "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph.root", "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph.root", "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root", "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root", "crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root", "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "ZZ_TuneCP5_13TeV-pythia8.root", "WW_TuneCP5_13TeV-pythia8.root", "WZ_TuneCP5_13TeV-pythia8.root"]

xsBkg = [161.1, 48.66, 6.968, 1.743, 0.8052, 0.1933, 0.003468, 280.35, 77.67, 10.73, 2.559, 1.1796, 0.28833, 0.006945, 1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 20790.0, 9238.0, 2305.0, 93.46, 23700000.0, 1547000.0, 322600.0, 32100.0, 6831.0, 1207.0, 119.9, 25.24, 314.0, 300.95, 72.15,  3.74, 67.91, 113.3, 34.97, 34.91, 12.14, 75.8, 27.6]

h_FJetMassBkgL = TH1F("h_FJetMassBkgL","Background FJetMass Loose",30,0,300)
h_FJetMassBkgM1 = TH1F("h_FJetMassBkgM1","Background FJetMass Medium1",30,0,300)
h_FJetMassBkgM2 = TH1F("h_FJetMassBkgM2","Background FJetMass Medium2",30,0,300)
h_FJetMassBkgL_normal = TH1F("h_FJetMassBkgL_normal","Background FJetMass Loose",30,0,300)
h_FJetMassBkgM1_normal = TH1F("h_FJetMassBkgM1_normal","Background FJetMass Medium1",30,0,300)
h_FJetMassBkgM2_normal = TH1F("h_FJetMassBkgM2_normal","Background FJetMass Medium2",30,0,300)

L = 150000.0 #1/pb

errNbkg = []

NdataL = 0
NdataM1 = 0
NdataM2 = 0

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
            h_FJetMassBkgL.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.86) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (abs(dPhi) > 0.4):
            h_FJetMassBkgM1.Fill(FJetMassBkg)
        if (FJetCSVBkg > 0.89) and (FJetMassBkg > 100.0) and (FJetMassBkg < 150.0) and (abs(dPhi) > 0.4):
            h_FJetMassBkgM2.Fill(FJetMassBkg)

    #number of expected obs events in data
    h_FJetMassBkgL_normal = h_FJetMassBkgL*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM1_normal = h_FJetMassBkgM1*(L*xsBkg[i]/eventsbkg)
    h_FJetMassBkgM2_normal = h_FJetMassBkgM2*(L*xsBkg[i]/eventsbkg)

    NdataL = h_FJetMassBkgL_normal.Integral()
    NdataM1 = h_FJetMassBkgM1_normal.Integral()
    NdataM2 = h_FJetMassBkgM2_normal.Integral()

    NdataL += NdataL
    NdataM1 += NdataM1
    NdataM2 += NdataM2

    h_FJetMassBkgL_normal += h_FJetMassBkgL_normal
    h_FJetMassBkgM1_normal += h_FJetMassBkgM1_normal
    h_FJetMassBkgM2_normal += h_FJetMassBkgM2_normal
    
    h_FJetMassBkgL.Reset()
    h_FJetMassBkgM1.Reset()
    h_FJetMassBkgM2.Reset()


errLbkg = h_FJetMassBkgL_normal.GetMeanError()
errNbkg.append(errLbkg)

errM1bkg = h_FJetMassBkgM1_normal.GetMeanError()
errNbkg.append(errM1bkg)

errM2bkg = h_FJetMassBkgM2_normal.GetMeanError()
errNbkg.append(errM2bkg)

print "NdataL", NdataL
print "NdataM1", NdataM1
print "NdataM2", NdataM2
print "errNbkg", errNbkg
print "###################################"

#Punzi Significance errors

PS_L = [0.002443172780651487, 0.007302510479583313, 0.010914734802737991, 0.027586916583467777, 0.06352293478046318, 0.06603487641654308, 0.06354134835884483, 0.040573845519231065]
PS_M1 = [0.0022285507953798372, 0.007362176734736961, 0.011200413764619234, 0.02724660072079694, 0.06837764145807858, 0.07257859431072793, 0.0705664208478422, 0.045032674264455085]
PS_M2 = [0.0011839992010865593, 0.003911425932160955, 0.008217536499132459, 0.016821977331524882, 0.05105574387081487, 0.057377198106136076, 0.05572291667950753, 0.038775416397166224]

effL_value = [0.016216216216216217, 0.04846938775510204, 0.0724450194049159, 0.18310428455941793, 0.42162455854387393, 0.4382972183802059, 0.42174677608440797, 0.2693032015065913]
effM1_value = [0.010810810810810811, 0.03571428571428571, 0.054333764553686936, 0.13217461600646727, 0.33170334148329256, 0.3520823728292608, 0.34232121922626024, 0.2184557438794727]
effM2_value = [0.005405405405405406, 0.017857142857142856, 0.037516170763260026, 0.07679870654810024, 0.2330888345558272, 0.2619486706623636, 0.2543962485345838, 0.17702448210922786]

errPS_L = []
errPS_M1 = []
errPS_M2 = []

for i in range(nfile):
    dx_L = err_sigeff_L[i]
    dx_M1 = err_sigeff_M1[i]
    dx_M2 = err_sigeff_M2[i]
    dP_L = TMath.Sqrt((dx_L/(1+TMath.Sqrt(NdataL)))**2 + (effL_value[i]*errLbkg/(2*(TMath.Sqrt(NdataL))*(1+(TMath.Sqrt(NdataL)))**2))**2)
    errPS_L.append(dP_L)
    dP_M1 = TMath.Sqrt((dx_M1/(1+TMath.Sqrt(NdataM1)))**2 + (effM1_value[i]*errM1bkg/(2*(TMath.Sqrt(NdataM1))*(1+(TMath.Sqrt(NdataM1)))**2))**2)
    errPS_M1.append(dP_M1)
    dP_M2 = TMath.Sqrt((dx_M2/(1+TMath.Sqrt(NdataM2)))**2 + (effM2_value[i]*errM2bkg/(2*(TMath.Sqrt(NdataM2))*(1+(TMath.Sqrt(NdataM2)))**2))**2)
    errPS_M2.append(dP_M2)

print "errPS_L", errPS_L
print "errPS_M1", errPS_M1
print "errPS_M2", errPS_M2
