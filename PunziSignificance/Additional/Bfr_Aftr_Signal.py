from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle

filename = "Summary_Signal.root"

name = ["300", "400", "500", "600", "600_new", "1000", "1200", "1400", "1600"]

c1 = TCanvas("c1", "c1", 900, 900)
c1.SetLeftMargin(0.15)
#c1.Divide(1,9,0.01,0.01)

file = TFile(filename)
nhist = 8

for i in range(nhist):
    #c1.cd(1)
    #leg.Clear()
    h = file.Get("h_FJetMassBfr_"+str(i))
    h_loose = file.Get("h_FJetMassL_"+str(i))
    h_medium1 = file.Get("h_FJetMassM1_"+str(i))
    h_medium2 = file.Get("h_FJetMassM2_"+str(i))
    
    leg = TLegend(0.55, 0.7, 0.85, 0.85)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.027)
    gStyle.SetOptStat(0)
    
    h.SetTitle("Fat Jet Mass Before and After Deep Double B-Tagger for MH3_" + str(name[i]))
    h.SetLineColor(803)
    h.SetFillColor(803)
    #h.SetLineWidth(5)
    h.GetXaxis().SetTitle("Fat Jet Mass (GeV)")
    h.GetYaxis().SetTitle("Number of Events")

    h_loose.SetLineColor(5)
    h_loose.SetFillColor(5)
    #h_loose.SetLineWidth(5)

    h_medium1.SetLineColor(634)
    h_medium1.SetFillColor(634)
    #h_medium1.SetLineWidth(5)

    h_medium2.SetLineColor(823)
    h_medium2.SetFillColor(823)
    #h_medium2.SetLineWidth(5)

    leg.AddEntry(h, "No Cut")
    leg.AddEntry(h_loose, "After Loose Cut")
    leg.AddEntry(h_medium1, "After Medium1 Cut")
    leg.AddEntry(h_medium2, "After Medium2 Cut")

    h.Draw("hist")
    h_loose.Draw("histsame")
    h_medium1.Draw("histsame")
    h_medium2.Draw("histsame")
    leg.Draw()

    c1.cd()
    c1.Update()
    c1.SaveAs("FJesMass_MH3_" + name[i] + "_Signal.pdf")


