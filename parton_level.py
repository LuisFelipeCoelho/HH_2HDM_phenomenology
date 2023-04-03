from math import isclose
import numpy as np
import ROOT

ROOT.gInterpreter.Declare('#include "/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"')
ROOT.gSystem.Load("/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/ExRootAnalysis/libExRootAnalysis.so")
ROOT.gSystem.Load("/home/t3atlas/lcoelho/subMad/MG5_aMC_v2_9_1_2/Delphes/libDelphes.so")

# LINKS
# pyROOT tutorial: https://indico.cern.ch/event/704163/contributions/2936719/attachments/1693833/2726445/Tutorial-PyROOT.pdf
# Particle Properties: http://home.thep.lu.se/~torbjorn/pythia81html/ParticleProperties.html
# PDG Codes: https://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf

# =============== Read Input Files ===============

files = {
'pp_hhjj_bbbbjj':'/lstore/calo/lcoelho/MG_samples/VBF_hh_loop_sm/Events/run_01_LO_decayed_1/parton_level.root',
}

print('Input files:')
for key in files.keys():
    print('>', key, 'events:', files[key])

file_hh = ROOT.TFile.Open(files['pp_hhjj_bbbbjj'], 'READ')
tree_hh = file_hh.Get('LHEF')

# =============== Create Histograms ===============

TH1D_PTb1 = ROOT.TH1D("PT_b1", "P_{T}(b_{1})", 80, 0, 400)
TH1D_PTb1.Sumw2()

TH1D_PTb2 = ROOT.TH1D("PT_b2", "P_{T}(b_{2})", 80, 0, 400)
TH1D_PTb2.Sumw2()

TH1D_PTb3 = ROOT.TH1D("PT_b3", "P_{T}(b_{3})", 80, 0, 400)
TH1D_PTb3.Sumw2()

TH1D_PTb4 = ROOT.TH1D("PT_b4", "P_{T}(b_{4})", 80, 0, 400)
TH1D_PTb4.Sumw2()

TH1D_PTj1 = ROOT.TH1D("PT_j1", "P_{T}(j_{1})", 80, 0, 400)
TH1D_PTj1.Sumw2()

TH1D_PTj2 = ROOT.TH1D("PT_j2", "P_{T}(j_{2})", 80, 0, 400)
TH1D_PTj2.Sumw2()

TH1D_Mjj = ROOT.TH1D("M_jj", "M(j_{1}j_{2})", 80, 0, 2500)
TH1D_Mjj.Sumw2()

TH1D_Mh1 = ROOT.TH1D("M_h1", "M(h_{1})", 80, 0, 400)
TH1D_Mh1.Sumw2()

TH1D_Mh2 = ROOT.TH1D("M_h2", "M(h_{2})", 80, 0, 400)
TH1D_Mh2.Sumw2()

TH1D_Mhh = ROOT.TH1D("M_hh", "M(hh)", 80, 0, 1500)
TH1D_Mhh.Sumw2()

TH1D_PTh1 = ROOT.TH1D("PT_h1", "P_{T}(h_{1})", 80, 0, 400)
TH1D_PTh1.Sumw2()

TH1D_PTh2 = ROOT.TH1D("PT_h2", "P_{T}(h_{2})", 80, 0, 400)
TH1D_PTh2.Sumw2()

TH1D_Etah1 = ROOT.TH1D("Eta_h1", "#eta(h_{1})", 80, -10, 10)
TH1D_Etah1.Sumw2()

TH1D_Etah2 = ROOT.TH1D("Eta_h2", "#eta(h_{2})", 80, -10, 10)
TH1D_Etah2.Sumw2()

TH1D_Phih1 = ROOT.TH1D("Phi_h1", "#phi(h_{1})", 80, -6, 6)
TH1D_Phih1.Sumw2()

TH1D_Phih2 = ROOT.TH1D("Phi_h2", "#phi(h_{2})", 80, -6, 6)
TH1D_Phih2.Sumw2()

TH1D_deltaEtahh = ROOT.TH1D("deltaEtahh", "#Delta #eta(h_{1}h_{2})", 80, -10, 10)
TH1D_deltaEtahh.Sumw2()

TH1D_deltaPhihh = ROOT.TH1D("deltaPhihh", "#Delta #phi(h_{1}h_{2})", 80, -6, 6)
TH1D_deltaPhihh.Sumw2()

TH1D_bb1_bb2_angle = ROOT.TH1D("bb1_bb2_angle", "#Theta^{Lab}(b #bar{b}_{1} V b #bar{b}_{2})", 80, 0, 3.14159266)
TH1D_bb1_bb2_angle.Sumw2()

TH1D_hh_jj_angle = ROOT.TH1D("hh_jj_angle", "#Theta^{Lab}(hh V jj)", 80, 0, 3.14159266)
TH1D_hh_jj_angle.Sumw2()

TH1D_jj_bb1_angle = ROOT.TH1D("jj_bb1_angle", "#Theta^{Lab}(jj V b #bar{b}_{1})", 80, 0, 3.14159266)
TH1D_jj_bb1_angle.Sumw2()

TH1D_jj_bb2_angle = ROOT.TH1D("jj_bb2_angle", "#Theta^{Lab}(jj V b #bar{b}_{2})", 80, 0, 3.14159266)
TH1D_jj_bb2_angle.Sumw2()

TH1D_bb1_bb2_angle_hhframe = ROOT.TH1D("bb1_bb2_angle_hhframe", "#Theta^{hh}(b #bar{b}_{1} V b #bar{b}_{2})", 80, 0, 3.14159266)
TH1D_bb1_bb2_angle_hhframe.Sumw2()

TH1D_hh_jj_angle_hhjjframe = ROOT.TH1D("hh_jj_angle_hhjjframe", "#Theta^{hhjj}(hh V jj)", 80, 0, 3.14159266)
TH1D_hh_jj_angle_hhjjframe.Sumw2()

TH1D_jj_bb1_angle_hhframe = ROOT.TH1D("jj_bb1_angle_hhframe", "#Theta^{hh}(jj V b #bar{b}_{1})", 80, 0, 3.14159266)
TH1D_jj_bb1_angle_hhframe.Sumw2()

TH1D_jj_bb2_angle_hhframe = ROOT.TH1D("jj_bb2_angle_hhframe", "#Theta^{hh}(jj V b #bar{b}_{2})", 80, 0, 3.14159266)
TH1D_jj_bb2_angle_hhframe.Sumw2()

TH1D_j1hh_hh_angle = ROOT.TH1D("j1hh_hh_angle", "#Theta^{j1hh}_{hh}", 80, 0, 3.14159266)
TH1D_j1hh_hh_angle.Sumw2()

TH1D_hh_h1_angle = ROOT.TH1D("hh_h1_angle", "#Theta^{hh}_{h1}", 80, 0, 3.14159266)
TH1D_hh_h1_angle.Sumw2()

TH1D_hh_h2_angle = ROOT.TH1D("hh_h2_angle", "#Theta^{hh}_{h2}", 80, 0, 3.14159266)
TH1D_hh_h2_angle.Sumw2()

TH1D_cos_Y_h1 = ROOT.TH1D("cos_Y_h1", "|cos(#Theta^{j1hh}_{hh})cos(#Theta^{hh}_{h1})|", 80, 0, 1)
TH1D_cos_Y_h1.Sumw2()

TH1D_cos_Y_h2 = ROOT.TH1D("cos_Y_h2", "|cos(#Theta^{j1hh}_{hh})cos(#Theta^{hh}_{h2})|", 80, 0, 1)
TH1D_cos_Y_h2.Sumw2()


# =============== Loop Over the Particles of Each Event ===============

for entry in tree_hh:
    #print(entry, ' =====')
    bquarks_list = []
    b_list = []
    b_bar_list = []
    jets_list = []
    higgs_list = []
    for particle in entry.Particle:
        pStatus = particle.Status    # Status = 1: final state particle
        pID = particle.PID	     # ID = PDG code (5:b, 6:t, 23:Z, 24:W+, 25:H, 36:A) 
        pPx = particle.Px
        pPy = particle.Py
        pPz = particle.Pz
        pE  = particle.E
        pM  = particle.M
        pEta = particle.Eta
        pPhi = particle.Phi
        pPT = particle.PT
        #print(pStatus, 'ID: ',pID, 'Mother1: ', particle.Mother1, 'Mother2: ', particle.Mother2)
        #print(pPx, pPy, pPz, pE, pM)
        #print(pPT, pPhi, pEta)

        # get final state bottom quarks
        if pStatus == 1 and abs(pID) == 5:
            bquarks_list.append(particle)
        if pStatus == 1 and pID == -5:
            b_bar_list.append(particle)
        if pStatus == 1 and pID == 5:
            b_list.append(particle)
	# get the other quarks
        if pStatus == 1 and abs(pID) != 5:        
            jets_list.append(particle)
        # get higgs bosons
        if pStatus == 2 and pID == 25:
            higgs_list.append(particle)

    # sort particles based on PT
    bquarks_list = [p2 for pt,p2 in sorted(zip([p1.PT for p1 in bquarks_list], bquarks_list), reverse=True)]
    b_list = [p2 for pt,p2 in sorted(zip([p1.PT for p1 in b_list], b_list), reverse=True)]
    b_bar_list = [p2 for pt,p2 in sorted(zip([p1.PT for p1 in b_bar_list], b_bar_list), reverse=True)]
    jets_list = [p2 for pt,p2 in sorted(zip([p1.PT for p1 in jets_list], jets_list), reverse=True)]    
    higgs_list = [p2 for pt,p2 in sorted(zip([p1.PT for p1 in higgs_list], higgs_list), reverse=True)]    

    if len(bquarks_list) == 4:
        #print(bquarks_list[0].PT, bquarks_list[1].PT)
        TH1D_PTb1.Fill(bquarks_list[0].PT)
        TH1D_PTb2.Fill(bquarks_list[1].PT)
        TH1D_PTb3.Fill(bquarks_list[2].PT)
        TH1D_PTb4.Fill(bquarks_list[3].PT)

        b1 = ROOT.TLorentzVector() 
        b1_bar = ROOT.TLorentzVector() 
        b2 = ROOT.TLorentzVector() 
        b2_bar = ROOT.TLorentzVector() 

        if b_list[0].Mother1 == b_bar_list[0].Mother1 and isclose(b_list[0].E+b_bar_list[0].E, higgs_list[0].E, rel_tol=3)==True:
            b1.SetPtEtaPhiM(b_list[0].PT, b_list[0].Eta, b_list[0].Phi, b_list[0].M)
            b1_bar.SetPtEtaPhiM(b_bar_list[0].PT, b_bar_list[0].Eta, b_bar_list[0].Phi, b_bar_list[0].M)
            b2.SetPtEtaPhiM(b_list[1].PT, b_list[1].Eta, b_list[1].Phi, b_list[1].M)
            b2_bar.SetPtEtaPhiM(b_bar_list[1].PT, b_bar_list[1].Eta, b_bar_list[1].Phi, b_bar_list[1].M)

        elif b_list[0].Mother1 == b_bar_list[0].Mother1 and isclose(b_list[0].E+b_bar_list[0].E, higgs_list[1].E, rel_tol=3)==True:
            b2.SetPtEtaPhiM(b_list[0].PT, b_list[0].Eta, b_list[0].Phi, b_list[0].M)
            b2_bar.SetPtEtaPhiM(b_bar_list[0].PT, b_bar_list[0].Eta, b_bar_list[0].Phi, b_bar_list[0].M)
            b1.SetPtEtaPhiM(b_list[1].PT, b_list[1].Eta, b_list[1].Phi, b_list[1].M)
            b1_bar.SetPtEtaPhiM(b_bar_list[1].PT, b_bar_list[1].Eta, b_bar_list[1].Phi, b_bar_list[1].M)

        elif b_list[0].Mother1 == b_bar_list[1].Mother1 and isclose(b_list[0].E+b_bar_list[1].E, higgs_list[0].E, rel_tol=3)==True:
            b1.SetPtEtaPhiM(b_list[0].PT, b_list[0].Eta, b_list[0].Phi, b_list[0].M)
            b1_bar.SetPtEtaPhiM(b_bar_list[1].PT, b_bar_list[1].Eta, b_bar_list[1].Phi, b_bar_list[1].M)
            b2.SetPtEtaPhiM(b_list[1].PT, b_list[1].Eta, b_list[1].Phi, b_list[1].M)
            b2_bar.SetPtEtaPhiM(b_bar_list[0].PT, b_bar_list[0].Eta, b_bar_list[0].Phi, b_bar_list[0].M)

        elif b_list[0].Mother1 == b_bar_list[1].Mother1 and isclose(b_list[0].E+b_bar_list[1].E, higgs_list[1].E, rel_tol=3)==True:
            b2.SetPtEtaPhiM(b_list[0].PT, b_list[0].Eta, b_list[0].Phi, b_list[0].M)
            b2_bar.SetPtEtaPhiM(b_bar_list[1].PT, b_bar_list[1].Eta, b_bar_list[1].Phi, b_bar_list[1].M)
            b1.SetPtEtaPhiM(b_list[1].PT, b_list[1].Eta, b_list[1].Phi, b_list[1].M)
            b1_bar.SetPtEtaPhiM(b_bar_list[0].PT, b_bar_list[0].Eta, b_bar_list[0].Phi, b_bar_list[0].M)

        else:
            print('ERROR')


    if len(jets_list) >= 2:
        #print(jets_list[0].PT, jets_list[1].PT)
        TH1D_PTj1.Fill(jets_list[0].PT)
        TH1D_PTj2.Fill(jets_list[1].PT)
        j1 = ROOT.TLorentzVector() 
        j2 = ROOT.TLorentzVector() 
        j1.SetPtEtaPhiM(jets_list[0].PT, jets_list[0].Eta, jets_list[0].Phi, jets_list[0].M)
        j2.SetPtEtaPhiM(jets_list[1].PT, jets_list[1].Eta, jets_list[1].Phi, jets_list[1].M)
        jj_pair = j1 + j2
        TH1D_Mjj.Fill(jj_pair.M())

    if len(higgs_list) == 2:
        #print(higgs_list[0].Eta, higgs_list[1].Eta)
        TH1D_PTh1.Fill(higgs_list[0].PT)
        TH1D_PTh2.Fill(higgs_list[1].PT)
        TH1D_Mh1.Fill(higgs_list[0].M)
        TH1D_Mh2.Fill(higgs_list[1].M)
        TH1D_Etah1.Fill(higgs_list[0].Eta)
        TH1D_Etah2.Fill(higgs_list[1].Eta)
        TH1D_Phih1.Fill(higgs_list[0].Phi)
        TH1D_Phih2.Fill(higgs_list[1].Phi)
        TH1D_deltaEtahh.Fill(higgs_list[1].Eta-higgs_list[0].Eta)
        TH1D_deltaPhihh.Fill(higgs_list[1].Phi-higgs_list[0].Phi)

        print(higgs_list[0].M, higgs_list[1].M)

        h1 = ROOT.TLorentzVector()
        h2 = ROOT.TLorentzVector() 
        h1.SetPtEtaPhiM(higgs_list[0].PT, higgs_list[0].Eta, higgs_list[0].Phi, higgs_list[0].M)
        h2.SetPtEtaPhiM(higgs_list[1].PT, higgs_list[1].Eta, higgs_list[1].Phi, higgs_list[1].M)
        hh_pair = h1 + h2
        TH1D_Mhh.Fill(hh_pair.M())

    # angles between bb_pair1 and bb_pair2
    v_bb1 = b1.Vect().Cross(b1_bar.Vect())
    v_bb2 = b2.Vect().Cross(b2_bar.Vect())
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
    b1_hhframe = b1
    b2_hhframe = b2
    b1_bar_hhframe = b1_bar
    b2_bar_hhframe = b2_bar
    h1_hhjjframe = h1    
    h2_hhjjframe = h2    
    j1_hhjjframe = j1    
    j2_hhjjframe = j2
    j1_hhframe = j1    
    j2_hhframe = j2        
    hhjj_pair = jj_pair + hh_pair

    #print(j2_hhframe.Px())
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

    #print(j2_hhframe.Px())
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

    #print(jj_bb2_angle_hhframe)
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

outHistFile = ROOT.TFile.Open("plots/parton_level.root" ,"RECREATE")
outHistFile.cd()
for hist in TH1D_list:
    hist.Write()
outHistFile.Close()

canvas = ROOT.TCanvas("canvas")
canvas.cd()
for hist_i, hist in enumerate(TH1D_list):
    hist.Draw('h')
    canvas.Print('plots/parton_level_'+variables_lsit[hist_i]+'.pdf')
