import ROOT
import numpy as np

ROOT.gInterpreter.Declare('#include "/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"')
ROOT.gSystem.Load("/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/ExRootAnalysis/libExRootAnalysis.so")
#ROOT.gSystem.Load("/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/Delphes/libDelphes.so")

# LINKS
# pyROOT tutorial: https://indico.cern.ch/event/704163/contributions/2936719/attachments/1693833/2726445/Tutorial-PyROOT.pdf
# Particle Properties: http://home.thep.lu.se/~torbjorn/pythia81html/ParticleProperties.html
# PDG Codes: https://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf

# =============== Read Input Files ===============

files = {
'pp_hhjj_bbbbjj':'/lstore/calo/lcoelho/MG_samples/VBF_hh_loop_sm/Events/run_01_LO_decayed_1/output_Delphes.root',
}

print('Input files:')
for key in files.keys():
    print('>', key, 'events:', files[key])

file_hh = ROOT.TFile.Open(files['pp_hhjj_bbbbjj'], 'READ')
tree_hh = file_hh.Get('Delphes')

# =============== Create Histograms ===============

TH1D_PTb1 = ROOT.TH1D("PT_b1", "P_{T}(b_{1})", 30, 0, 400)
TH1D_PTb1.Sumw2()

TH1D_PTb2 = ROOT.TH1D("PT_b2", "P_{T}(b_{2})", 30, 0, 400)
TH1D_PTb2.Sumw2()

TH1D_PTb3 = ROOT.TH1D("PT_b3", "P_{T}(b_{3})", 30, 0, 400)
TH1D_PTb3.Sumw2()

TH1D_PTb4 = ROOT.TH1D("PT_b4", "P_{T}(b_{4})", 30, 0, 400)
TH1D_PTb4.Sumw2()

TH1D_PTj1 = ROOT.TH1D("PT_j1", "P_{T}(j_{1})", 30, 0, 400)
TH1D_PTj1.Sumw2()

TH1D_PTj2 = ROOT.TH1D("PT_j2", "P_{T}(j_{2})", 30, 0, 400)
TH1D_PTj2.Sumw2()

TH1D_Mjj = ROOT.TH1D("M_jj", "M(j_{1}j_{2})", 30, 0, 2500)
TH1D_Mjj.Sumw2()

TH1D_Mh1 = ROOT.TH1D("M_h1", "M(h_{1})", 30, 0, 400)
TH1D_Mh1.Sumw2()

TH1D_Mh2 = ROOT.TH1D("M_h2", "M(h_{2})", 30, 0, 400)
TH1D_Mh2.Sumw2()

TH1D_Mhh = ROOT.TH1D("M_hh", "M(hh)", 30, 0, 1500)
TH1D_Mhh.Sumw2()

TH1D_PTh1 = ROOT.TH1D("PT_h1", "P_{T}(h_{1})", 30, 0, 400)
TH1D_PTh1.Sumw2()

TH1D_PTh2 = ROOT.TH1D("PT_h2", "P_{T}(h_{2})", 30, 0, 400)
TH1D_PTh2.Sumw2()

TH1D_Etah1 = ROOT.TH1D("Eta_h1", "#eta(h_{1})", 30, -10, 10)
TH1D_Etah1.Sumw2()

TH1D_Etah2 = ROOT.TH1D("Eta_h2", "#eta(h_{2})", 30, -10, 10)
TH1D_Etah2.Sumw2()

TH1D_Phih1 = ROOT.TH1D("Phi_h1", "#Phi(h_{1})", 30, -6, 6)
TH1D_Phih1.Sumw2()

TH1D_Phih2 = ROOT.TH1D("Phi_h2", "#Phi(h_{2})", 30, -6, 6)
TH1D_Phih2.Sumw2()

TH1D_deltaEtahh = ROOT.TH1D("deltaEtahh", "#Delta #eta(h_{1}h_{2})", 30, -10, 10)
TH1D_deltaEtahh.Sumw2()

TH1D_deltaPhihh = ROOT.TH1D("deltaPhihh", "#Delta #Phi(h_{1}h_{2})", 30, -6, 6)
TH1D_deltaPhihh.Sumw2()

TH1D_bb1_bb2_angle = ROOT.TH1D("bb1_bb2_angle", "#Theta^{Lab}(b #bar{b}_{1} V b #bar{b}_{2})", 30, 0, 3.14159265)
TH1D_bb1_bb2_angle.Sumw2()

TH1D_hh_jj_angle = ROOT.TH1D("hh_jj_angle", "#Theta^{Lab}(hh V jj)", 30, 0, 3.14159265)
TH1D_hh_jj_angle.Sumw2()

TH1D_jj_bb1_angle = ROOT.TH1D("jj_bb1_angle", "#Theta^{Lab}(jj V b #bar{b}_{1})", 30, 0, 3.14159265)
TH1D_jj_bb1_angle.Sumw2()

TH1D_jj_bb2_angle = ROOT.TH1D("jj_bb2_angle", "#Theta^{Lab}(jj V b #bar{b}_{2})", 30, 0, 3.14159265)
TH1D_jj_bb2_angle.Sumw2()

TH1D_bb1_bb2_angle_hhframe = ROOT.TH1D("bb1_bb2_angle_hhframe", "#Theta^{hh}(b #bar{b}_{1} V b #bar{b}_{2})", 30, 0, 3.14159266)
TH1D_bb1_bb2_angle_hhframe.Sumw2()

TH1D_hh_jj_angle_hhjjframe = ROOT.TH1D("hh_jj_angle_hhjjframe", "#Theta^{hhjj}(hh V jj)", 30, 0, 3.14159266)
TH1D_hh_jj_angle_hhjjframe.Sumw2()

TH1D_jj_bb1_angle_hhframe = ROOT.TH1D("jj_bb1_angle_hhframe", "#Theta^{hh}(jj V b #bar{b}_{1})", 30, 0, 3.14159266)
TH1D_jj_bb1_angle_hhframe.Sumw2()

TH1D_jj_bb2_angle_hhframe = ROOT.TH1D("jj_bb2_angle_hhframe", "#Theta^{hh}(jj V b #bar{b}_{2})", 30, 0, 3.14159266)
TH1D_jj_bb2_angle_hhframe.Sumw2()

TH1D_j1hh_hh_angle = ROOT.TH1D("j1hh_hh_angle", "#Theta^{j1hh}_{hh}", 30, 0, 3.14159266)
TH1D_j1hh_hh_angle.Sumw2()

TH1D_hh_h1_angle = ROOT.TH1D("hh_h1_angle", "#Theta^{hh}_{h1}", 30, 0, 3.14159266)
TH1D_hh_h1_angle.Sumw2()

TH1D_hh_h2_angle = ROOT.TH1D("hh_h2_angle", "#Theta^{hh}_{h2}", 30, 0, 3.14159266)
TH1D_hh_h2_angle.Sumw2()

TH1D_cos_Y_h1 = ROOT.TH1D("cos_Y_h1", "|cos(#Theta^{j1hh}_{hh})cos(#Theta^{hh}_{h1})|", 30, 0, 1)
TH1D_cos_Y_h1.Sumw2()

TH1D_cos_Y_h2 = ROOT.TH1D("cos_Y_h2", "|cos(#Theta^{j1hh}_{hh})cos(#Theta^{hh}_{h2})|", 30, 0, 1)
TH1D_cos_Y_h2.Sumw2()

# =============== Loop Over the Particles of Each Event ===============

for entry in tree_hh:
    #print(entry)

    # ===== VBF signal topology selections =====
    # At least two forward jets with (PT > 30, |Eta| > 2) and exactly 4 b-tagged jets with (PT > 40, |Eta| < 2)

    bjet_list = []
    jet_list = []

    number_of_jets = tree_hh.Jet.GetEntries()
    for jet_index in range(number_of_jets):

        jet = ROOT.TLorentzVector()
        jet_PT = tree_hh.GetLeaf("Jet.PT").GetValue(jet_index)
        jet_Eta = tree_hh.GetLeaf("Jet.Eta").GetValue(jet_index)
        jet_Phi = tree_hh.GetLeaf("Jet.Phi").GetValue(jet_index)
        jet_Mass = tree_hh.GetLeaf("Jet.Mass").GetValue(jet_index)
        jet.SetPtEtaPhiM(jet_PT, jet_Eta, jet_Phi, jet_Mass)

        if tree_hh.GetLeaf("Jet.BTag").GetValue(jet_index) == True and len(bjet_list) != 4:
            bjet_list.append(jet)

        else:
            jet_list.append(jet)  

    number_of_btagged_jets = len(bjet_list)
    number_of_forward_jets = len(jet_list)

#    print('========')
#    print(number_of_btagged_jets, number_of_forward_jets)

    if number_of_forward_jets < 2 or number_of_btagged_jets != 4:
        continue

    #print(1)
    # ======= Get the 2 Forward Jets and the 4 b-Jets =========

    j1 = jet_list[0]
    j2 = jet_list[1]

    b1 = bjet_list[0]
    b2 = bjet_list[1]
    b3 = bjet_list[2]
    b4 = bjet_list[3]

    jj_pair = j2 + j1
    bbbb_jets = b1 + b2 + b3 + b4 
    bb_lead = b1 + b2
    bb_subl = b3 + b4

    # Pairs with minimum D(HH)
    b1b2_pair = b1 + b2
    b3b4_pair = b3 + b4

    b1b3_pair = b1 + b3
    b2b4_pair = b2 + b4

    b1b4_pair = b1 + b4
    b2b3_pair = b2 + b3

    D_HH_1 = np.sqrt((b1b2_pair.M())**2+(b3b4_pair.M())**2)*abs(np.sin((1/np.tan(b3b4_pair.M()/b1b2_pair.M()))-(1/np.tan(116.5/123.7))))
    D_HH_2 = np.sqrt((b1b3_pair.M())**2+(b2b4_pair.M())**2)*abs(np.sin((1/np.tan(b2b4_pair.M()/b1b3_pair.M()))-(1/np.tan(116.5/123.7))))
    D_HH_3 = np.sqrt((b1b4_pair.M())**2+(b2b3_pair.M())**2)*abs(np.sin((1/np.tan(b2b3_pair.M()/b1b4_pair.M()))-(1/np.tan(116.5/123.7))))

    if D_HH_1 < D_HH_2 and D_HH_1 < D_HH_3:
        D_HH_best = D_HH_1
        h1 = b1b2_pair
        h2 = b3b4_pair
        b11_best = b1
        b12_best = b2
        b21_best = b3
        b22_best = b4
    if D_HH_2 < D_HH_1 and D_HH_2 < D_HH_3:
        D_HH_best = D_HH_2
        h1 = b1b3_pair
        h2 = b2b4_pair
        b11_best = b1
        b12_best = b3
        b21_best = b2
        b22_best = b4
    if D_HH_3 < D_HH_1 and D_HH_3 < D_HH_2:
        D_HH_best = D_HH_3
        h1 = b1b4_pair
        h2 = b2b3_pair
        b11_best = b1
        b12_best = b4
        b21_best = b2
        b22_best = b3

    hh_pair = h1 + h2
    
    # Fill histograms
    TH1D_PTb1.Fill(b1.Pt())
    TH1D_PTb2.Fill(b2.Pt())
    TH1D_PTb3.Fill(b3.Pt())
    TH1D_PTb4.Fill(b4.Pt())
    TH1D_PTj1.Fill(j1.Pt())
    TH1D_PTj2.Fill(j2.Pt())
    TH1D_Mjj.Fill(abs(jj_pair.M()))
    TH1D_Mh1.Fill(abs(h1.M()))
    TH1D_Mh2.Fill(abs(h2.M()))
    TH1D_Mhh.Fill(abs(hh_pair.M()))
    TH1D_PTh1.Fill(h1.Pt())
    TH1D_PTh2.Fill(h2.Pt())
    TH1D_Etah1.Fill(h1.Eta())
    TH1D_Etah2.Fill(h2.Eta())
    TH1D_Phih1.Fill(h1.Phi())
    TH1D_Phih2.Fill(h2.Phi())
    TH1D_deltaEtahh.Fill(h2.Eta()-h1.Eta())
    TH1D_deltaPhihh.Fill(h2.Phi()-h1.Phi())

    # angles between bb_pair1 and bb_pair2
    v_bb1 = b11_best.Vect().Cross(b12_best.Vect())
    v_bb2 = b21_best.Vect().Cross(b22_best.Vect())
    bb1_bb2_angle = v_bb1.Angle(v_bb2)

    # angles between hh_pair and jj_pair
    v_hh = h1.Vect().Cross(h2.Vect())
    v_jj = j1.Vect().Cross(j2.Vect())
    hh_jj_angle = v_hh.Angle(v_jj)

    # angle between jj_pair and bb_pair1
    jj_bb1_angle = v_jj.Angle(v_bb1)

    # angle between jj_pair and bb_pair2
    jj_bb2_angle = v_jj.Angle(v_bb2)

    TH1D_bb1_bb2_angle.Fill(bb1_bb2_angle)
    TH1D_hh_jj_angle.Fill(hh_jj_angle)
    TH1D_jj_bb1_angle.Fill(jj_bb1_angle)
    TH1D_jj_bb2_angle.Fill(jj_bb2_angle)

    # =========== HH rest frame ==============

    # define new particles
    b1_hhframe = b11_best
    b2_hhframe = b21_best
    b1_bar_hhframe = b12_best
    b2_bar_hhframe = b22_best
    h1_hhjjframe = h1
    h2_hhjjframe = h2
    j1_hhjjframe = j1
    j2_hhjjframe = j2
    j1_hhframe = j1
    j2_hhframe = j2
    hhjj_pair = jj_pair + hh_pair

    # boost them to the hh and hhjj frames
    b1_hhframe.Boost(-hh_pair.BoostVector())
    b2_hhframe.Boost(-hh_pair.BoostVector())
    b1_bar_hhframe.Boost(-hh_pair.BoostVector())
    b2_bar_hhframe.Boost(-hh_pair.BoostVector())
    h1_hhjjframe.Boost(-hhjj_pair.BoostVector())
    h2_hhjjframe.Boost(-hhjj_pair.BoostVector())
    j1_hhjjframe.Boost(-hhjj_pair.BoostVector())
    j2_hhjjframe.Boost(-hhjj_pair.BoostVector())
    j1_hhframe.Boost(-hh_pair.BoostVector())
    j2_hhframe.Boost(-hh_pair.BoostVector())

    # find the angles
    v_bb1_hhframe = b1_hhframe.Vect().Cross(b1_bar_hhframe.Vect())
    v_bb2_hhframe = b2_hhframe.Vect().Cross(b2_bar_hhframe.Vect())
    bb1_bb2_angle_hhframe = v_bb1_hhframe.Angle(v_bb2_hhframe)

    v_hh_hhjjframe = h1_hhjjframe.Vect().Cross(h2_hhjjframe.Vect())
    v_jj_hhjjframe = j1_hhjjframe.Vect().Cross(j2_hhjjframe.Vect())
    hh_jj_angle_hhjjframe = v_hh_hhjjframe.Angle(v_jj_hhjjframe)

    v_jj_hhframe = j1_hhframe.Vect().Cross(j2_hhframe.Vect())
    jj_bb1_angle_hhframe = v_jj_hhframe.Angle(v_bb1_hhframe)
    jj_bb2_angle_hhframe = v_jj_hhframe.Angle(v_bb2_hhframe)

    TH1D_bb1_bb2_angle_hhframe.Fill(bb1_bb2_angle_hhframe)
    TH1D_hh_jj_angle_hhjjframe.Fill(hh_jj_angle_hhjjframe)
    TH1D_jj_bb1_angle_hhframe.Fill(jj_bb1_angle_hhframe)
    TH1D_jj_bb2_angle_hhframe.Fill(jj_bb2_angle_hhframe)

    # =========== Crazy angles ===============
    j1hh = j1 + hh_pair
    j1hh_hhjjframe = j1 + hh_pair
    hh_j1hhframe = hh_pair
    h1_hhframe = h1
    h2_hhframe = h2

    j1hh_hhjjframe.Boost(-hhjj_pair.BoostVector())
    hh_j1hhframe.Boost(-j1hh.BoostVector())
    h1_hhframe.Boost(-hh_pair.BoostVector())
    h2_hhframe.Boost(-hh_pair.BoostVector())

    j1hh_hh_angle = j1hh_hhjjframe.Vect().Angle(hh_j1hhframe.Vect())
    hh_h1_angle = h1_hhframe.Vect().Angle(hh_j1hhframe.Vect())
    hh_h2_angle = h2_hhframe.Vect().Angle(hh_j1hhframe.Vect())

    TH1D_j1hh_hh_angle.Fill(j1hh_hh_angle)
    TH1D_hh_h1_angle.Fill(hh_h1_angle)
    TH1D_hh_h2_angle.Fill(hh_h2_angle)

    TH1D_cos_Y_h1.Fill(abs(np.cos(j1hh_hh_angle)*np.cos(hh_h1_angle)))
    TH1D_cos_Y_h2.Fill(abs(np.cos(j1hh_hh_angle)*np.cos(hh_h2_angle)))

print(tree_hh.GetEntries())


# ============ Close the Input File ===============

TH1D_list = []
variables_lsit = ['PTb1','PTb2','PTb3','PTb4','PTj1','PTj2','Mjj','Mh1','Mh2','Mhh','PTh1','PTh2','Etah1','Etah2','Phih1','Phih2','deltaEtahh','deltaPhihh','bb1_bb2_angle','hh_jj_angle','jj_bb1_angle','jj_bb2_angle','bb1_bb2_angle_hhframe','hh_jj_angle_hhjjframe','jj_bb1_angle_hhframe','jj_bb2_angle_hhframe','j1hh_hh_angle','hh_h1_angle','hh_h2_angle','cos_Y_h1','cos_Y_h2']
TH1D_list.append(TH1D_PTb1)
TH1D_list.append(TH1D_PTb2)
TH1D_list.append(TH1D_PTb3)
TH1D_list.append(TH1D_PTb4)
TH1D_list.append(TH1D_PTj1)
TH1D_list.append(TH1D_PTj2)
TH1D_list.append(TH1D_Mjj)
TH1D_list.append(TH1D_Mh1)
TH1D_list.append(TH1D_Mh2)
TH1D_list.append(TH1D_Mhh)
TH1D_list.append(TH1D_PTh1)
TH1D_list.append(TH1D_PTh2)
TH1D_list.append(TH1D_Etah1)
TH1D_list.append(TH1D_Etah2)
TH1D_list.append(TH1D_Phih1)
TH1D_list.append(TH1D_Phih2)
TH1D_list.append(TH1D_deltaEtahh)
TH1D_list.append(TH1D_deltaPhihh)
TH1D_list.append(TH1D_bb1_bb2_angle)
TH1D_list.append(TH1D_hh_jj_angle)
TH1D_list.append(TH1D_jj_bb1_angle)
TH1D_list.append(TH1D_jj_bb2_angle)
TH1D_list.append(TH1D_bb1_bb2_angle_hhframe)
TH1D_list.append(TH1D_hh_jj_angle_hhjjframe)
TH1D_list.append(TH1D_jj_bb1_angle_hhframe)
TH1D_list.append(TH1D_jj_bb2_angle_hhframe)
TH1D_list.append(TH1D_j1hh_hh_angle)
TH1D_list.append(TH1D_hh_h1_angle)
TH1D_list.append(TH1D_hh_h2_angle)
TH1D_list.append(TH1D_cos_Y_h1)
TH1D_list.append(TH1D_cos_Y_h2)

for hist in TH1D_list:
    hist.SetDirectory(0)
file_hh.Close()

# ============ Write Histograms to Output File ===============

outHistFile = ROOT.TFile.Open("plots/reco_nocut_level.root" ,"RECREATE")
outHistFile.cd()
for hist in TH1D_list:
    hist.Write()
outHistFile.Close()

canvas = ROOT.TCanvas("canvas")
canvas.cd()
for hist_i, hist in enumerate(TH1D_list):
    hist.Draw('h')
    canvas.Print('plots/reco_nocut_level_'+variables_lsit[hist_i]+'.pdf')
