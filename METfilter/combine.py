from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle
import ROOT as root

filename = "signal_sample_hist_root/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root"

c1 = root.TCanvas("c1","c1", 1300, 1000)
#c1.Divide(1,2,0.01,0.01)

file = root.TFile(filename)
leg = root.TLegend(0.55,0.7,0.85,0.85)
leg.SetBorderSize(0)
leg.SetTextSize(0.027)
gStyle.SetOptStat(0)

'''
c1.cd(1)
leg.Clear()
c1.GetPad(1).SetLogy()
h = file.Get("h")
h.SetTitle("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_CP3Tune_13TeV_new_0000_0")
h.SetLineColor(2)
h.SetLineWidth(4)
h.GetXaxis().SetTitle("MET (GeV)")
h.GetYaxis().SetTitle("Number of Events")
leg.AddEntry(h, "MET Before Cut")
h6 = file.Get("h6")
h6.SetLineColor(3)
h6.SetLineWidth(4)
leg.AddEntry(h6, "MET After 7 Filters")
h.Draw()
h6.Draw("histsame")
leg.Draw()
'''

#c1.cd(2)
#leg.Clear()
h = file.Get("h")
h.SetTitle("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0")
h.SetLineColor(2)
h.SetLineWidth(4)
h.GetXaxis().SetTitle("MET (GeV)")
h.GetYaxis().SetTitle("Number of Events")
leg.AddEntry(h, "MET Before Cut")
h6 = file.Get("h6")
h6.SetLineColor(3)
h6.SetLineWidth(4)
leg.AddEntry(h6, "MET After 7 Filters")
h.Draw()
h6.Draw("histsame")
leg.Draw()


c1.cd()
c1.Update()
c1.SaveAs("EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.pdf")
