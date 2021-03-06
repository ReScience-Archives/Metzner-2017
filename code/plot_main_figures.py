# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017, Christoph Metzner
# Distributed under the (new) BSD License.
#
# Contributors: Christoph Metzner (c.metzner@herts.ac.uk)
# -----------------------------------------------------------------------------
# References:
#
# * Vierling-Claassen, D., Siekmeier, P., Stufflebeam, S., & Kopell, N. (2008). 
#   Modeling GABA alterations in schizophrenia: a link between impaired 
#   inhibition and altered gamma and beta range auditory entrainment. 
#   Journal of neurophysiology, 99(5), 2656-2671.
# -----------------------------------------------------------------------------
# A script that generates the main figures of the replication study.
#
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from analysis import calcPowerSpectrum,getSingleSpikeTimes,getSpikeTimes
from plot_utility import plot_MEG_summary,plot_PSD_summary,plot_single_trial

# Load data
ctrl_avg_meg_20 = np.load('../data/Data-Average/sims_ctrl_avg_20Hz.npy')
ctrl_avg_meg_30 = np.load('../data/Data-Average/sims_ctrl_avg_30Hz.npy')
ctrl_avg_meg_40 = np.load('../data/Data-Average/sims_ctrl_avg_40Hz.npy')

schiz_avg_meg_20 = np.load('../data/Data-Average/sims_schiz_avg_20Hz.npy')
schiz_avg_meg_30 = np.load('../data/Data-Average/sims_schiz_avg_30Hz.npy')
schiz_avg_meg_40 = np.load('../data/Data-Average/sims_schiz_avg_40Hz.npy')

# Parameters
sim_time = 500
s = 2**13
dt = float(sim_time)/float(s)
time = np.linspace(0,sim_time,int(sim_time/dt))


# Calculate PSDs
pxx_ctrl_20,freqs = calcPowerSpectrum(ctrl_avg_meg_20,dt,sim_time)
pxx_schiz_20,_ = calcPowerSpectrum(schiz_avg_meg_20,dt,sim_time)
pxx_ctrl_30,_ = calcPowerSpectrum(ctrl_avg_meg_30,dt,sim_time)
pxx_schiz_30,_ = calcPowerSpectrum(schiz_avg_meg_30,dt,sim_time)
pxx_ctrl_40,_ = calcPowerSpectrum(ctrl_avg_meg_40,dt,sim_time)
pxx_schiz_40,_ = calcPowerSpectrum(schiz_avg_meg_40,dt,sim_time)


# Flags
savefig = 1	# set savefig to 1 if you want to store the figures
showfig = 0	# set plotfi to 1 if you want to show the figures


########### Figure 1 - Replication of Figure 4 from Vierling-Claassen et al.

data_meg = [ctrl_avg_meg_40,schiz_avg_meg_40,ctrl_avg_meg_30,schiz_avg_meg_30,ctrl_avg_meg_20,schiz_avg_meg_20] 
xlabel = 'Time (ms)'
ylabel = 'Simulated MEG'
annotations = ['40Hz \n Drive','30Hz \n Drive','20Hz \n Drive','Control','Schizophrenia']
plot_MEG_summary(time,data_meg,xlabel,ylabel,annotations,savefig,'../data/Figures/Replication-Figure4',[25,35,25])

########### Figure 2 - Replication of Figure 54 from Vierling-Claassen et al.
data_psd = [pxx_ctrl_40,pxx_schiz_40,pxx_ctrl_30,pxx_schiz_30,pxx_ctrl_20,pxx_schiz_20] 
xlabel = 'Frequency (Hz)'
ylabel = 'Power Spectral Density'
annotations = ['40Hz \n Drive','30Hz \n Drive','20Hz \n Drive','Control','Schizophrenia']
plot_PSD_summary(freqs*1000,data_psd,xlabel,ylabel,annotations,savefig,'../data/Figures/Replication-Figure5',[25,35,25])



########### Figure 3 - Replication of Figure 6 from Vierling-Claassen et al.
# Load data
data_ex  = np.load('../data/Single-Trial-Data-40Hz/sims_ctrl_40Hz0-Ex.npy')
data_inh = np.load('../data/Single-Trial-Data-40Hz/sims_ctrl_40Hz0-Inh.npy')
data_meg = np.load('../data/Single-Trial-Data-40Hz/sims_ctrl_40Hz0-MEG.npy')

spike_times = [None,None]
spike_times[0] = getSpikeTimes(data_ex,dt)
spike_times[1] = getSpikeTimes(data_inh,dt)

data_psd,freqs = calcPowerSpectrum(data_meg,dt,sim_time)

xlabels = ['Time (ms)','Frequency (Hz)']
ylabels = ['Simulated MEG','Power']
annotations = ['I cells','E cells']

plot_single_trial(sim_time,spike_times,freqs,data_psd,time,data_meg,xlabels,ylabels,annotations,savefig,'../data/Figures/Replication-Figure6',[30,25,25])

########### Figure 4 - Replication of Figure 7 from Vierling-Claassen et al.
# Load data
data_ex  = np.load('../data/Single-Trial-Data-40Hz/sims_schiz_40Hz0-Ex.npy')
data_inh = np.load('../data/Single-Trial-Data-40Hz/sims_schiz_40Hz0-Inh.npy')
data_meg = np.load('../data/Single-Trial-Data-40Hz/sims_schiz_40Hz0-MEG.npy')

spike_times = [None,None]
spike_times[0] = getSpikeTimes(data_ex,dt)
spike_times[1] = getSpikeTimes(data_inh,dt)

data_psd,freqs = calcPowerSpectrum(data_meg,dt,sim_time)

xlabels = ['Time (ms)','Frequency (Hz)']
ylabels = ['Simulated MEG','Power']
annotations = ['I cells','E cells']

plot_single_trial(sim_time,spike_times,freqs,data_psd,time,data_meg,xlabels,ylabels,annotations,savefig,'../data/Figures/Replication-Figure7',[30,25,25])

########### Figure 5 - Replication of Figure 10 from Vierling-Claassen et al.
# Load data
data_ex  = np.load('../data/Single-Trial-Data-20Hz/sims_ctrl_20Hz13-Ex.npy')
data_inh = np.load('../data/Single-Trial-Data-20Hz/sims_ctrl_20Hz13-Inh.npy')
data_meg = np.load('../data/Single-Trial-Data-20Hz/sims_ctrl_20Hz13-MEG.npy')

spike_times = [None,None]
spike_times[0] = getSpikeTimes(data_ex,dt)
spike_times[1] = getSpikeTimes(data_inh,dt)

data_psd,freqs = calcPowerSpectrum(data_meg,dt,sim_time)

xlabels = ['Time (ms)','Frequency (Hz)']
ylabels = ['Simulated MEG','Power']
annotations = ['I cells','E cells']

plot_single_trial(sim_time,spike_times,freqs,data_psd,time,data_meg,xlabels,ylabels,annotations,savefig,'../data/Figures/Replication-Figure10',[30,25,25])

########### Figure 6 - Replication of Figure 11 from Vierling-Claassen et al.
# Load data
data_ex  = np.load('../data/Single-Trial-Data-20Hz/sims_schiz_20Hz13-Ex.npy')
data_inh = np.load('../data/Single-Trial-Data-20Hz/sims_schiz_20Hz13-Inh.npy')
data_meg = np.load('../data/Single-Trial-Data-20Hz/sims_schiz_20Hz13-MEG.npy')

spike_times = [None,None]
spike_times[0] = getSpikeTimes(data_ex,dt)
spike_times[1] = getSpikeTimes(data_inh,dt)

data_psd,freqs = calcPowerSpectrum(data_meg,dt,sim_time)

xlabels = ['Time (ms)','Frequency (Hz)']
ylabels = ['Simulated MEG','Power']
annotations = ['I cells','E cells']

plot_single_trial(sim_time,spike_times,freqs,data_psd,time,data_meg,xlabels,ylabels,annotations,savefig,'../data/Figures/Replication-Figure11',[30,25,25])


if showfig:
	plt.show()
