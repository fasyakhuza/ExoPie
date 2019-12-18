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


    
#Punzi Significance errors

effL_value = [0.016216216216216217, 0.04846938775510204, 0.0724450194049159, 0.18310428455941793, 0.42162455854387393, 0.4382972183802059, 0.42174677608440797, 0.2693032015065913]
effM1_value = [0.010810810810810811, 0.03571428571428571, 0.054333764553686936, 0.13217461600646727, 0.33170334148329256, 0.3520823728292608, 0.34232121922626024, 0.2184557438794727]
effM2_value = [0.005405405405405406, 0.017857142857142856, 0.037516170763260026, 0.07679870654810024, 0.2330888345558272, 0.2619486706623636, 0.2543962485345838, 0.17702448210922786]

NdataLfinal = 7041.22753906
NdataM1final = 2516.92724609
NdataM2final = 1264.01574707

errLbkg = 100.33962118877793
errM1bkg = 60.62274327217933
errM2bkg = 46.11500290405923

errPS_L = []
errPS_M1 = []
errPS_M2 = []

for i in range(nfile):
    dx_L = err_sigeff_L[i]
    dx_M1 = err_sigeff_M1[i]
    dx_M2 = err_sigeff_M2[i]
    dP_L = TMath.Sqrt((dx_L/(1+TMath.Sqrt(NdataLfinal)))**2 + (effL_value[i]*errLbkg/(2*(TMath.Sqrt(NdataLfinal))*(1+(TMath.Sqrt(NdataLfinal)))**2))**2)
    errPS_L.append(dP_L)
    dP_M1 = TMath.Sqrt((dx_M1/(1+TMath.Sqrt(NdataM1final)))**2 + (effM1_value[i]*errM1bkg/(2*(TMath.Sqrt(NdataM1final))*(1+(TMath.Sqrt(NdataM1final)))**2))**2)
    errPS_M1.append(dP_M1)
    dP_M2 = TMath.Sqrt((dx_M2/(1+TMath.Sqrt(NdataM2final)))**2 + (effM2_value[i]*errM2bkg/(2*(TMath.Sqrt(NdataM2final))*(1+(TMath.Sqrt(NdataM2final)))**2))**2)
    errPS_M2.append(dP_M2)

print "errPS_L", errPS_L
print "errPS_M1", errPS_M1
print "errPS_M2", errPS_M2
