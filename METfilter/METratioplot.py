from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle, TGaxis, TPad, TGraphAsymmErrors, gPad, TRatioPlot, TEfficiency
import ROOT as root

#create canvas and pads
c1 = root.TCanvas("c1","c1", 800, 800)
c1.SetLeftMargin(0.15)

#c2 = root.TCanvas("c2","c2", 800, 800)
#c2.SetLeftMargin(0.15)

filename = "signal_sample_hist_root/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root"

file = root.TFile(filename)

#get hist before any cuts
h = file.Get("h")
h.SetLineColor(2)
#h.SetLineWidth(4)
h.SetTitle("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0")
h.GetXaxis().SetTitle("MET (GeV)")
h.GetYaxis().SetTitle("Number of Events")
h.GetYaxis().SetTitleSize(20)
h.GetYaxis().SetTitleFont(43)
h.GetYaxis().SetTitleOffset(1.7)
h.SetStats(0)

#get hist after 7 filters
h6 = file.Get("h6")
h6.SetLineColor(3)
#h6.SetLineWidth(4)

'''
#create ratio plot
hratio = TH1F("hratio", "hratio", 32, 200, 1000)
hratio.SetLineColor(1)
hratio.SetMarkerStyle(21)
hratio.SetLineWidth(1)
hratio.SetTitle("")
hratio.SetMinimum(0.5)
hratio.SetMaximum(1.5)

##set up plot for markers and errors
hratio.SetStats(0)
hratio.Divide(h6,h,1,1,"B")

##adjust y-axis settings
y = hratio.GetYaxis()
y.SetTitle("ratio h6/h")
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
'''


#create ratio plot using TGraphAsymmErrors
gPad.Modified()
ratio = TGraphAsymmErrors()
ratio.Divide(h6,h,"cl=0.683 b(1,1) mode")
ratio.SetMarkerColor(1)
ratio.SetMarkerStyle(21)
ratio.SetLineColor(1)
ratio.GetXaxis().SetTitleSize(0.1)
ratio.GetXaxis().SetLabelSize(0.1)
ratio.GetXaxis().SetRangeUser(200,1000)
ratio.GetXaxis().SetTitle("MET (GeV)")
ratio.GetYaxis().SetTitleSize(0.1)
ratio.GetYaxis().SetLabelSize(0.1)
ratio.GetYaxis().SetTitleOffset(0.4)
ratio.GetYaxis().SetTitle("ratio")
ratio.SetTitle("")

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
#leg.Draw()

#pad1
pad1.cd()
h.SetLineWidth(4)
h6.SetLineWidth(4)
h.Draw("e")
h6.Draw("esame")
leg.Draw()

#pad2
pad2.cd()
ratio.Draw("AP")

c1.SetFrameBorderMode(0)
c1.cd()
c1.Update()
c1.SaveAs("ratio_EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.pdf")

