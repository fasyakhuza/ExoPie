from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle, TGaxis, TPad
import ROOT as root

filename = "signal_sample_hist_root/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.root"

file = root.TFile(filename)

#get hist before any cuts
h = file.Get("h")
h.SetLineColor(2)
h.SetLineWidth(4)
h.SetTitle("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0")
h.GetXaxis().SetTitle("MET (GeV)")
h.GetYaxis().SetTitle("Number of Events")
h.GetYaxis().SetTitleSize(20)
h.GetYaxis().SetTitleFont(43)
h.GetYaxis().SetTitleOffset(1.7)
h.SetStats(0)

#get hist after 7 filters
h6 = file.Get("h6")
h6.SetLineColor(3)
h6.SetLineWidth(4)

#create ratio plot
hratio = h6.Clone("hratio")
hratio.SetLineColor(1)
hratio.SetMarkerStyle(21)
hratio.SetLineWidth(1)
hratio.SetTitle("")
hratio.SetMinimum(0.5)
hratio.SetMaximum(1.5)
##set up plot for markers and errors
hratio.Sumw2()
hratio.SetStats(0)
hratio.Divide(h)
##adjust y-axis settings
y = hratio.GetYaxis()
y.SetTitle("ratio h1/h2 ")
y.SetNdivisions(505)
y.SetTitleSize(20)
y.SetTitleFont(43)
y.SetTitleOffset(1.7)
y.SetLabelFont(43)
y.SetLabelSize(15)
##adjust x-axis settings
x = hratio.GetXaxis()
x.SetTitle("MET (GeV)")
x.SetTitleSize(20)
x.SetTitleFont(43)
x.SetTitleOffset(4.0)
x.SetLabelFont(43)
x.SetLabelSize(15)

#create canvas and pads
c1 = root.TCanvas("c1","c1", 800, 800)
#upper histogram plot is pad1
pad1 = TPad("pad1","pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0) #joins upper and lower plot
pad1.Draw()
#lower ratio plot is pad2
c1.cd() #returns to main canvas before defining pad2
pad2 = TPad("pad2","pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0) #joins upper and lower plot
pad2.SetBottomMargin(0.2)
pad2.Draw()

#legend settings
leg = root.TLegend(0.55,0.7,0.85,0.85)
leg.SetBorderSize(0)
leg.SetTextSize(0.027)
gStyle.SetOptStat(0)
leg.Clear()
leg.AddEntry(h, "MET Before Cut")
leg.AddEntry(h6, "MET After 7 Filters")
leg.Draw()

#pad1
pad1.cd()
h.Draw("e")
h6.Draw("esame")

#pad2
pad2.cd()
hratio.Draw("e")

c1.SetFrameBorderMode(0)
c1.cd()
c1.Update()
c1.SaveAs("ratio_EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0.pdf")

