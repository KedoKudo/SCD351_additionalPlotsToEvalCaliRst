# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from SCD_Reduction.SCDCalibratePanels2PanelDiagnostics import SCDCalibratePanels2PanelDiagnosticsPlot

# prep data
Load(Filename='/home/8cz/Workbench/MANTID/SCD364_removeToleranceCheckInSCDCalibratePanels2/data/PwsTOPAZIDeal.nxs', OutputWorkspace='PwsTOPAZIDeal')
RenameWorkspace(InputWorkspace='PwsTOPAZIDeal', OutputWorkspace='pws_eng')
CloneWorkspace(InputWorkspace='pws_eng', OutputWorkspace='pws_cali')
LoadIsawDetCal(InputWorkspace='pws_cali', Filename='/home/8cz/Workbench/MANTID/SCD351_additionalPlotsToEvalCaliRst/SCDCalibrate2.DetCal')
ApplyInstrumentToPeaks(InputWorkspace='pws_cali', InstrumentWorkspace='pws_cali', OutputWorkspace='pws_cali')
mtd.importAll()

# run
SCDCalibratePanels2PanelDiagnosticsPlot(pws_eng, pws_cali)