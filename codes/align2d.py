from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='8sowaa', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='8sowaa', atom_files='8sowaa.pdb')
aln.append(file='TvLDH.ali', align_codes='TvLDH')
aln.align2d(max_gap_length=50)
aln.write(file='TvLDH-1bdmA.ali', alignment_format='PIR')
aln.write(file='TvLDH-1bdmA.pap', alignment_format='PAP')
