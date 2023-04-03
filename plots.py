a1 = '/home/t3atlas/lcoelho/subMad/HH_pheno/plots/'
l_parton = [
'PTb1',
'PTb2',
'PTb3',
'PTb4',
'PTj1',
'PTj2',
'PTh1',
'PTh2',
'Mjj',
'Mh1',
'Mh2',
'Mhh',
'Etah1',
'Etah2',
'Phih1',
'Phih2',
'deltaEtahh',
'deltaPhihh',
'bb1_bb2_angle','hh_jj_angle','jj_bb1_angle','jj_bb2_angle',
'bb1_bb2_angle_hhframe','hh_jj_angle_hhjjframe','jj_bb1_angle_hhframe','jj_bb2_angle_hhframe',
'j1hh_hh_angle','hh_h1_angle','hh_h2_angle',
'cos_Y_h1','cos_Y_h2',
]

l_reco_nocut = ['reco_nocut_level_'+i for i in l_parton]
l_reco_cut = ['reco_cut_level_'+i for i in l_parton]
l_parton = ['parton_level_'+i for i in l_parton]

f = open("plots.tex", "w")

f.write("\\documentclass[a4paper,onecolumn,final,11pt]{article} \n")
f.write("\\usepackage[utf8]{inputenc} \n")
f.write("\\usepackage[a4paper,top=1cm, bottom=1cm, left=0.2cm, right=0.2cm]{geometry} \n")
f.write("\\usepackage{graphicx} \n")
f.write("\\usepackage{float} \n")
f.write("\\usepackage{fancybox} \n")
f.write("\\usepackage{underscore} \n")
f.write("\\usepackage[english]{babel} \n")

f.write("\\begin{document} \n")


c1 = 0
for i in range(int(len(l_parton))):
	print(l_parton[c1])
	f.write("\\begin{figure}[H] \n")
	f.write("\\centering \n")
	f.write("\\begin{minipage}{.32\\textwidth} \n")
	f.write("        \\centering \n")
	f.write("        \\hspace{0cm} \n")
	f.write("        \\includegraphics[width=1.\\textwidth]{"+a1.replace('_', '\string_')+l_parton[c1].replace('_', '\string_')+"} \n")
	f.write("        \\caption{"+l_parton[c1]+"} \n")
	f.write("\\end{minipage} \n")
	f.write("\\hfill \n")
	f.write("\\begin{minipage}{.32\\textwidth} \n")
	f.write("        \\centering \n")
	f.write("        \\hspace{0cm} \n")
	f.write("    \\includegraphics[width=1.\\textwidth]{"+a1.replace('_', '\string_')+l_reco_nocut[c1].replace('_', '\string_')+"} \n")
	f.write("        \\caption{"+l_reco_nocut[c1]+"} \n")
	f.write("\\end{minipage} \n")
	f.write("\\hfill \n")
	f.write("\\begin{minipage}{.32\\textwidth} \n")
	f.write("        \\centering \n")
	f.write("        \\hspace{0cm} \n")
	f.write("    \\includegraphics[width=1.\\textwidth]{"+a1.replace('_', '\string_')+l_reco_cut[c1].replace('_', '\string_')+"} \n")
	f.write("        \\caption{"+l_reco_cut[c1]+"} \n")
	f.write("\\end{minipage} \n")
	f.write("\\end{figure} \n")
	f.write(" \n")
	c1 += 1


f.write("\\end{document} \n")

