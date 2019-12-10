from ROOT import TFile, TH1F, TCanvas, TLegend, gStyle, TGraphAsymmErrors, gPad, TMultiGraph, TLatex

filename = "Summary_Signal.root"

name = ["300", "400", "500", "600", "1000", "1200", "1400", "1600"]

c1 = TCanvas("c1", "c1", 900, 900)
c1.SetLeftMargin(0.15)
#c1.Divide(1,9,0.01,0.01)
lt = TLatex()

leg = TLegend(0.55,0.75,0.89,0.89)
#leg.SetBorderSize(0)
leg.SetTextSize(0.022)

file = TFile(filename)
nhist = 8

'''
for i in range(nhist):
    #c1.cd(1)
    #leg.Clear()
    h = file.Get("h_FJetMassBfr_"+str(i))
    #h.Sumw2()
    h_loose = file.Get("h_FJetMassL_"+str(i))
    #h_loose.Sumw2()
    h_medium1 = file.Get("h_FJetMassM1_"+str(i))
    #h_medium1.Sumw2()
    h_medium2 = file.Get("h_FJetMassM2_"+str(i))
    #h_medium2.Sumw2()
    
    effL = h_loose.Clone("effL")
    effL.Divide(h_loose,h,1.0,1.0,"B") #binomial errors
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
    effL.SetMarkerStyle(21)
    effL.SetMarkerColor(803)

    effM1.SetLineColor(5)
    effM1.SetLineWidth(5)
    effM1.SetMarkerStyle(21)
    effM1.SetMarkerColor(5)

    effM2.SetLineColor(634)
    effM2.SetLineWidth(5)
    effM2.SetMarkerStyle(21)
    effM2.SetMarkerColor(634)

    leg.AddEntry(effL, "Signal Efficiency (Loose)")
    leg.AddEntry(effM1, "Signal Efficiency (Medium 1)")
    leg.AddEntry(effM2, "Signal Efficiency (Medium 2)")

    effL.Draw("e")
    effM1.Draw("esame")
    effM2.Draw("esame")
    c1.BuildLegend()

    c1.cd()
    c1.Update()
    c1.SaveAs("SignalEfficiency_MH3_" + name[i] + ".pdf")
'''

for i in range(nhist):
    #c1.cd(1)
    leg.Clear()
    h = file.Get("h_FJetMassBfr_"+str(i))
    h_loose = file.Get("h_FJetMassL_"+str(i))
    h_medium1 = file.Get("h_FJetMassM1_"+str(i))
    h_medium2 = file.Get("h_FJetMassM2_"+str(i))

    gPad.Modified()
    effL = TGraphAsymmErrors(h_loose,h,"cl=0.683 b(1,1) mode")
    effL.SetTitle("Loose (FJetCSV > 0.7)")
    effL.SetMarkerColor(2)
    effL.SetMarkerStyle(21)
    effL.SetLineColor(2)
    
    effM1 = TGraphAsymmErrors(h_medium1,h,"cl=0.683 b(1,1) mode")
    effM1.SetTitle("Medium1 (FJetCSV > 0.86)")
    effM1.SetMarkerColor(3)
    effM1.SetMarkerStyle(20)
    effM1.SetLineColor(3)
    
    effM2 = TGraphAsymmErrors(h_medium2,h,"cl=0.683 b(1,1) mode")
    effM2.SetTitle("Medium2 (FJetCSV > 0.89)")
    effM2.SetMarkerColor(4)
    effM2.SetMarkerStyle(22)
    effM2.SetLineColor(4)
    
    mg = TMultiGraph("mg","")
    mg.SetTitle("Signal Efficiency; Fat Jet Mass (GeV); Efficiency")
    mg.GetYaxis().SetNdivisions(505)
    mg.GetYaxis().SetLabelOffset(1.4)
    mg.GetXaxis().SetTitleOffset(4.0)
    mg.Add(effL, "AP")
    mg.Add(effM1, "AP")
    mg.Add(effM2, "AP")
    mg.Draw("AP")
    
    leg.AddEntry(effL,"Loose (FJetCSV > 0.7)")
    leg.AddEntry(effM1,"Medium1 (FJetCSV > 0.86)")
    leg.AddEntry(effM2,"Medium2 (FJetCSV > 0.89)")
    leg.Draw()
    #c1.BuildLegend()
    
    lt.DrawLatexNDC(0.1,0.91,"MH3-"+name[i])

    c1.cd()
    c1.Update()
    c1.SaveAs("SigEff_MH3_" + name[i] + ".pdf")

