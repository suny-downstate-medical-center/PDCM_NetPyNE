'''
NetPyNE version of Potjans and Diesmann thalamocortical network

init.py -- code to run the simulation

to compile mod files: 
	nrnivmodl  
to run on single core: 
	python init.py
to run on multiple cores: 
	mpiexec -n 2 nrniv -python -mpi init.py 
'''

import matplotlib; matplotlib.use('Agg')  # to avoid graphics error in servers

from netpyne import sim
from neuron import h
from cfg import cfg
from netParams import netParams


############################################################
#               Create network and run simulation
############################################################

sim.initialize(
    simConfig = cfg,  
    netParams = netParams)          # create network object and set cfg and net params
sim.net.createPops()                    # instantiate network populations
sim.net.createCells()                   # instantiate network cells based on defined populations
sim.net.addStims()              # add network stimulation
sim.net.connectCells()                  # create connections between cells based on params
sim.setupRecording()                    # setup variables to record for each cell (spikes, V traces, etc)
sim.runSim()                            # run parallel Neuron simulation  
sim.gatherData()                        # gather spiking data and cell info from each node
sim.saveData()                          # save params, cell info and sim output to file (pickle,mat,txt,etc)#
sim.analysis.plotData()               # plot spike raster etc


# # Plot all electrodes separately; use electrode 6
# for elec in [3]: #range(15):
# 	sim.analysis.plotLFP(**{'plots': ['PSD'], 'electrodes': [elec], 'timeRange': [100,600], 'maxFreq':80, 'figSize': (7,4), 'fontSize': 16, 'saveData': False, 'saveFig': cfg.saveFolder+cfg.simLabel+'_LFP_PSD_elec_'+str(elec)+'.png', 'showFig': False})
# 	#sim.analysis.plotLFP(**{'plots': ['spectrogram'], 'electrodes': [elec], 'timeRange': [100,600], 'maxFreq':80, 'figSize': (8,4), 'fontSize': 16, 'saveData': False, 'saveFig': cfg.saveFolder+cfg.simLabel+'_LFP_spec_elec_'+str(elec)+'.png', 'showFig': False})


