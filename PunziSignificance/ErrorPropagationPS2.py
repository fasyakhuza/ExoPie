import ROOT
from ROOT import TFile, TTree, TH1F, TMath, TCanvas, TLegend, gStyle, TGraphAsymmErrors, gPad, TMultiGraph, TLatex, TGraphErrors
import array as arr
import numpy as np

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
    effL.SetTitle("Loose")
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

    effM2 = TGraphAsymmErrors(med2,preselect,"cl=0.683 b(1,1) mode")
    effM2.SetTitle("Medium 2")
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

effL_value = [0.016216216216216217, 0.03826530612244898, 0.05304010349288486, 0.15481002425222312, 0.3579190437381146, 0.3712924542800061, 0.35199296600234464, 0.2222222222222222]
effM1_value = [0.010810810810810811, 0.030612244897959183, 0.04139715394566624, 0.11196443007275667, 0.2798152675903287, 0.2979099431381589, 0.28516998827667056, 0.18267419962335216]
effM2_value = [0.005405405405405406, 0.015306122448979591, 0.027166882276843468, 0.06588520614389652, 0.19654985058408042, 0.22252958352543414, 0.21336459554513482, 0.1431261770244821]

NdataLfinal = 1476.63879395
NdataM1final = 525.63659668
NdataM2final = 267.509887695

errLbkg = 21.836138315888665
errM1bkg = 12.45983719415238
errM2bkg = 10.025671552656473

errPS_L = arr.array('d')
errPS_M1 = arr.array('d')
errPS_M2 = arr.array('d')

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

leg = TLegend(0.65,0.2,0.89,0.39)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)

c1 = TCanvas("c1","c1",900,700) #width-height
c1.SetLeftMargin(0.15)

zero1 = np.zeros(8)
MH3name = arr.array('d', [300, 400, 500, 600, 1000, 1200, 1400, 1600])

PS_L_list = arr.array('d', [0.0004112969599897861, 0.0009705349183432452, 0.001345272721656976, 0.00392649502830454, 0.009078012567736165, 0.009417206558938311, 0.008927707606030736, 0.0056362916739341054])
PS_M1_list = arr.array('d', [0.00045182964994290115, 0.0012794155903995414, 0.0017301626957710058, 0.0046794685552392825, 0.011694667182371611, 0.012450920442342712, 0.011918463677897409, 0.007634729819421243])
PS_M2_list = arr.array('d', [0.00031144825327401876, 0.0008819070437095939, 0.0015652994359244023, 0.003796168988471316, 0.011324794914451026, 0.012821693266796396, 0.012293625659714199, 0.008246633598931645])

gPad.Modified()
gr1 = TGraphErrors(nfile, MH3name, PS_L_list, zero1, errPS_L)
gr1.SetTitle("Loose")
gr1.GetYaxis().SetNdivisions(505)
gr1.GetYaxis().SetLabelOffset(1.4)
gr1.GetXaxis().SetTitleOffset(4.0)
gr1.SetLineColor(1)
gr1.SetLineWidth(5)
gr1.SetMarkerStyle(20)
gr1.SetMarkerColor(1)

gr2 = TGraphErrors(nfile, MH3name, PS_M1_list, zero1, errPS_M1)
gr2.SetTitle("Medium 1")
gr2.GetYaxis().SetNdivisions(505)
gr2.GetYaxis().SetLabelOffset(1.4)
gr2.GetXaxis().SetTitleOffset(4.0)
gr2.SetLineColor(2)
gr2.SetLineWidth(5)
gr2.SetMarkerStyle(21)
gr2.SetMarkerColor(2)

gr3 = TGraphErrors(nfile, MH3name, PS_M2_list, zero1, errPS_M2)
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
leg.AddEntry(gr1, "Loose")
leg.AddEntry(gr2, "Medium 1")
leg.AddEntry(gr3, "Medium 2")
leg.Draw()

c1.cd()
c1.Update()
c1.SaveAs("PS_all_new2_add.pdf")
