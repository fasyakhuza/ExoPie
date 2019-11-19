from ROOT import TFile, TH1F, TCanvas
import ROOT as root

filename = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/skimmedFiles/V0_filters_study/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root"
file = root.TFile(filename)
mytree = file.Get("outTree")

c1 = root.TCanvas("c1","c1", 900, 900)

met = root.TH1F("met","st_pfMetCorrPt", 100, 0, 1000)
filterStatus = root.TH1F("filterStatus", "st_filterStatus", 10, 0, 2)
filters = root.TH1F("filters", "st_filters", 10, 0, 10)

pdfname = "test.pdf"

c1.Print(pdfname+"[")
mytree.Draw("st_pfMetCorrPt>>met")
c1.Print(pdfname)
mytree.Draw("st_filterStatus>>filterStatus")
c1.Print(pdfname)
mytree.Draw("st_filters>>filters")
c1.Print(pdfname)

#c1.cd()
#c1.Update()

c1.Print(pdfname+"]")
