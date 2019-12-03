from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle

filename = "Summary_Signal.root"

name = ["300", "400", "500", "600", "600_new", "1000", "1200", "1400", "1600"]

c1 = TCanvas("c1", "c1", 900, 900)
c1.SetLeftMargin(0.15)
#c1.Divide(1,9,0.01,0.01)

file = TFile(filename)
nhist = 1 #8

for i in range(nhist):
    #c1.cd(1)
    #leg.Clear()
    h = file.Get("h_FJetMassBfr_"+str(i))
    h.Sumw2()
    h_loose = file.Get("h_FJetMassL_"+str(i))
    h_loose.Sumw2()
    h_medium1 = file.Get("h_FJetMassM1_"+str(i))
    h_medium1.Sumw2()
    h_medium2 = file.Get("h_FJetMassM2_"+str(i))
    h_medium2.Sumw2()
    
    effL = h_loose.Clone("effL")
    effL.Divide(h_loose,h,1.0,1.0,"B")
    effM1 = h_medium1.Clone("effM1")
    effM1.Divide(h_medium1,h,1.0,1.0,"B")
    effM2 = h_medium2.Clone("effM2")
    effM2.Divide(h_medium2,h,1.0,1.0,"B")
    
    leg = TLegend(0.55, 0.7, 0.85, 0.85)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.027)
    gStyle.SetOptStat(0)
    
    effL.SetTitle("Signal Efficiency for MH3_" + str(name[i]))
    effL.SetLineColor(803)
    effL.SetLineWidth(5)

    effM1.SetLineColor(5)
    effM1.SetLineWidth(5)

    effM2.SetLineColor(634)
    effM2.SetLineWidth(5)

    leg.AddEntry(effL, "Signal Efficiency (Loose)")
    leg.AddEntry(effM1, "Signal Efficiency (Medium 1)")
    leg.AddEntry(effM2, "Signal Efficiency (Medium 2)")

    effL.Draw("e")
    effM1.Draw("esame")
    effM2.Draw("esame")
    leg.Draw()

    c1.cd()
    c1.Update()
    c1.SaveAs("SignalEfficiency_MH3_" + name[i] + ".pdf")


