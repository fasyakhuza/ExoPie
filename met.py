import ROOT as root

filename = "/eos/cms/store/group/phys_exotica/monoHiggs/monoHbb/skimmedFiles/V0_filters_study/EXO-ggToXdXdHToBB_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150_MH2_1000_MHC_1000_CP3Tune_13TeV_0000_0.root"
file = root.TFile(filename)
mytree = file.Get("outTree")
nevents = mytree.GetEntries()

for i in range(nevents):
    mytree.GetEvent(i)
	filters = getattr(mytree, 'st_filters')
	print filters

