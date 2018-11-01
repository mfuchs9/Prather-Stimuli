#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.2),
    on October 30, 2018, at 18:09
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SpaceFiller'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Fill"
FillClock = core.Clock()
background = visual.Rect(
    win=win, name='background',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
zerozero = visual.Rect(
    win=win, name='zerozero',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.4, 0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
zeroone = visual.Rect(
    win=win, name='zeroone',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.2, 0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
zerotwo = visual.Rect(
    win=win, name='zerotwo',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
zerothree = visual.Rect(
    win=win, name='zerothree',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, 0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
zerofour = visual.Rect(
    win=win, name='zerofour',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.4, 0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
onezero = visual.Rect(
    win=win, name='onezero',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.4, 0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
oneone = visual.Rect(
    win=win, name='oneone',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.2, 0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)
onetwo = visual.Rect(
    win=win, name='onetwo',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
onethree = visual.Rect(
    win=win, name='onethree',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, 0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-9.0, interpolate=True)
onefour = visual.Rect(
    win=win, name='onefour',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.4, 0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-10.0, interpolate=True)
twozero = visual.Rect(
    win=win, name='twozero',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.4, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-11.0, interpolate=True)
twoone = visual.Rect(
    win=win, name='twoone',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.2, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-12.0, interpolate=True)
twotwo = visual.Rect(
    win=win, name='twotwo',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
twothree = visual.Rect(
    win=win, name='twothree',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
twofour = visual.Rect(
    win=win, name='twofour',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.4, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-15.0, interpolate=True)
threezero = visual.Rect(
    win=win, name='threezero',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.4, -0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-16.0, interpolate=True)
threeone = visual.Rect(
    win=win, name='threeone',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.2, -0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-17.0, interpolate=True)
threetwo = visual.Rect(
    win=win, name='threetwo',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, -0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-18.0, interpolate=True)
threethree = visual.Rect(
    win=win, name='threethree',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, -0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-19.0, interpolate=True)
threefour = visual.Rect(
    win=win, name='threefour',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.4, -0.2),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-20.0, interpolate=True)
fourzero = visual.Rect(
    win=win, name='fourzero',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.4, -0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-21.0, interpolate=True)
fourone = visual.Rect(
    win=win, name='fourone',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.2, -0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-22.0, interpolate=True)
fourtwo = visual.Rect(
    win=win, name='fourtwo',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-23.0, interpolate=True)
fourthree = visual.Rect(
    win=win, name='fourthree',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, -0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-24.0, interpolate=True)
fourfour = visual.Rect(
    win=win, name='fourfour',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.4, -0.4),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1.0, depth=-25.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Fill"-------
    t = 0
    FillClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    zerozero.setOpacity(np.random.randint(2))
    zeroone.setOpacity(np.random.randint(2))
    zerotwo.setOpacity(np.random.randint(2))
    zerothree.setOpacity(np.random.randint(2))
    zerofour.setOpacity(np.random.randint(2))
    onezero.setOpacity(np.random.randint(2))
    oneone.setOpacity(np.random.randint(2))
    onetwo.setOpacity(np.random.randint(2))
    onethree.setOpacity(np.random.randint(2))
    onefour.setOpacity(np.random.randint(2))
    twozero.setOpacity(np.random.randint(2))
    twoone.setOpacity(np.random.randint(2))
    twofour.setOpacity(np.random.randint(2))
    threezero.setOpacity(np.random.randint(2))
    threeone.setOpacity(np.random.randint(2))
    threetwo.setOpacity(np.random.randint(2))
    threethree.setOpacity(np.random.randint(2))
    threefour.setOpacity(np.random.randint(2))
    fourzero.setOpacity(np.random.randint(2))
    fourone.setOpacity(np.random.randint(2))
    fourtwo.setOpacity(np.random.randint(2))
    fourthree.setOpacity(np.random.randint(2))
    fourfour.setOpacity(np.random.randint(2))
    # keep track of which components have finished
    FillComponents = [background, zerozero, zeroone, zerotwo, zerothree, zerofour, onezero, oneone, onetwo, onethree, onefour, twozero, twoone, twotwo, twothree, twofour, threezero, threeone, threetwo, threethree, threefour, fourzero, fourone, fourtwo, fourthree, fourfour]
    for thisComponent in FillComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Fill"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FillClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background* updates
        if t >= 0.0 and background.status == NOT_STARTED:
            # keep track of start time/frame for later
            background.tStart = t
            background.frameNStart = frameN  # exact frame index
            background.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if background.status == STARTED and t >= frameRemains:
            background.setAutoDraw(False)
        
        # *zerozero* updates
        if t >= 0.0 and zerozero.status == NOT_STARTED:
            # keep track of start time/frame for later
            zerozero.tStart = t
            zerozero.frameNStart = frameN  # exact frame index
            zerozero.setAutoDraw(True)
        frameRemains = 0.8 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if zerozero.status == STARTED and t >= frameRemains:
            zerozero.setAutoDraw(False)
        
        # *zeroone* updates
        if t >= 0.0 and zeroone.status == NOT_STARTED:
            # keep track of start time/frame for later
            zeroone.tStart = t
            zeroone.frameNStart = frameN  # exact frame index
            zeroone.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zeroone.status == STARTED and t >= frameRemains:
            zeroone.setAutoDraw(False)
        
        # *zerotwo* updates
        if t >= 0.0 and zerotwo.status == NOT_STARTED:
            # keep track of start time/frame for later
            zerotwo.tStart = t
            zerotwo.frameNStart = frameN  # exact frame index
            zerotwo.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zerotwo.status == STARTED and t >= frameRemains:
            zerotwo.setAutoDraw(False)
        
        # *zerothree* updates
        if t >= 0.0 and zerothree.status == NOT_STARTED:
            # keep track of start time/frame for later
            zerothree.tStart = t
            zerothree.frameNStart = frameN  # exact frame index
            zerothree.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zerothree.status == STARTED and t >= frameRemains:
            zerothree.setAutoDraw(False)
        
        # *zerofour* updates
        if t >= 0.0 and zerofour.status == NOT_STARTED:
            # keep track of start time/frame for later
            zerofour.tStart = t
            zerofour.frameNStart = frameN  # exact frame index
            zerofour.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zerofour.status == STARTED and t >= frameRemains:
            zerofour.setAutoDraw(False)
        
        # *onezero* updates
        if t >= 0.0 and onezero.status == NOT_STARTED:
            # keep track of start time/frame for later
            onezero.tStart = t
            onezero.frameNStart = frameN  # exact frame index
            onezero.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if onezero.status == STARTED and t >= frameRemains:
            onezero.setAutoDraw(False)
        
        # *oneone* updates
        if t >= 0.0 and oneone.status == NOT_STARTED:
            # keep track of start time/frame for later
            oneone.tStart = t
            oneone.frameNStart = frameN  # exact frame index
            oneone.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if oneone.status == STARTED and t >= frameRemains:
            oneone.setAutoDraw(False)
        
        # *onetwo* updates
        if t >= 0.0 and onetwo.status == NOT_STARTED:
            # keep track of start time/frame for later
            onetwo.tStart = t
            onetwo.frameNStart = frameN  # exact frame index
            onetwo.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if onetwo.status == STARTED and t >= frameRemains:
            onetwo.setAutoDraw(False)
        
        # *onethree* updates
        if t >= 0.0 and onethree.status == NOT_STARTED:
            # keep track of start time/frame for later
            onethree.tStart = t
            onethree.frameNStart = frameN  # exact frame index
            onethree.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if onethree.status == STARTED and t >= frameRemains:
            onethree.setAutoDraw(False)
        
        # *onefour* updates
        if t >= 0.0 and onefour.status == NOT_STARTED:
            # keep track of start time/frame for later
            onefour.tStart = t
            onefour.frameNStart = frameN  # exact frame index
            onefour.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if onefour.status == STARTED and t >= frameRemains:
            onefour.setAutoDraw(False)
        
        # *twozero* updates
        if t >= 0.0 and twozero.status == NOT_STARTED:
            # keep track of start time/frame for later
            twozero.tStart = t
            twozero.frameNStart = frameN  # exact frame index
            twozero.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if twozero.status == STARTED and t >= frameRemains:
            twozero.setAutoDraw(False)
        
        # *twoone* updates
        if t >= 0.0 and twoone.status == NOT_STARTED:
            # keep track of start time/frame for later
            twoone.tStart = t
            twoone.frameNStart = frameN  # exact frame index
            twoone.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if twoone.status == STARTED and t >= frameRemains:
            twoone.setAutoDraw(False)
        
        # *twotwo* updates
        if t >= 0.0 and twotwo.status == NOT_STARTED:
            # keep track of start time/frame for later
            twotwo.tStart = t
            twotwo.frameNStart = frameN  # exact frame index
            twotwo.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if twotwo.status == STARTED and t >= frameRemains:
            twotwo.setAutoDraw(False)
        
        # *twothree* updates
        if t >= 0.0 and twothree.status == NOT_STARTED:
            # keep track of start time/frame for later
            twothree.tStart = t
            twothree.frameNStart = frameN  # exact frame index
            twothree.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if twothree.status == STARTED and t >= frameRemains:
            twothree.setAutoDraw(False)
        
        # *twofour* updates
        if t >= 0.0 and twofour.status == NOT_STARTED:
            # keep track of start time/frame for later
            twofour.tStart = t
            twofour.frameNStart = frameN  # exact frame index
            twofour.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if twofour.status == STARTED and t >= frameRemains:
            twofour.setAutoDraw(False)
        
        # *threezero* updates
        if t >= 0.0 and threezero.status == NOT_STARTED:
            # keep track of start time/frame for later
            threezero.tStart = t
            threezero.frameNStart = frameN  # exact frame index
            threezero.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if threezero.status == STARTED and t >= frameRemains:
            threezero.setAutoDraw(False)
        
        # *threeone* updates
        if t >= 0.0 and threeone.status == NOT_STARTED:
            # keep track of start time/frame for later
            threeone.tStart = t
            threeone.frameNStart = frameN  # exact frame index
            threeone.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if threeone.status == STARTED and t >= frameRemains:
            threeone.setAutoDraw(False)
        
        # *threetwo* updates
        if t >= 0.0 and threetwo.status == NOT_STARTED:
            # keep track of start time/frame for later
            threetwo.tStart = t
            threetwo.frameNStart = frameN  # exact frame index
            threetwo.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if threetwo.status == STARTED and t >= frameRemains:
            threetwo.setAutoDraw(False)
        
        # *threethree* updates
        if t >= 0.0 and threethree.status == NOT_STARTED:
            # keep track of start time/frame for later
            threethree.tStart = t
            threethree.frameNStart = frameN  # exact frame index
            threethree.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if threethree.status == STARTED and t >= frameRemains:
            threethree.setAutoDraw(False)
        
        # *threefour* updates
        if t >= 0.0 and threefour.status == NOT_STARTED:
            # keep track of start time/frame for later
            threefour.tStart = t
            threefour.frameNStart = frameN  # exact frame index
            threefour.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if threefour.status == STARTED and t >= frameRemains:
            threefour.setAutoDraw(False)
        
        # *fourzero* updates
        if t >= 0.0 and fourzero.status == NOT_STARTED:
            # keep track of start time/frame for later
            fourzero.tStart = t
            fourzero.frameNStart = frameN  # exact frame index
            fourzero.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fourzero.status == STARTED and t >= frameRemains:
            fourzero.setAutoDraw(False)
        
        # *fourone* updates
        if t >= 0.0 and fourone.status == NOT_STARTED:
            # keep track of start time/frame for later
            fourone.tStart = t
            fourone.frameNStart = frameN  # exact frame index
            fourone.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fourone.status == STARTED and t >= frameRemains:
            fourone.setAutoDraw(False)
        
        # *fourtwo* updates
        if t >= 0.0 and fourtwo.status == NOT_STARTED:
            # keep track of start time/frame for later
            fourtwo.tStart = t
            fourtwo.frameNStart = frameN  # exact frame index
            fourtwo.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fourtwo.status == STARTED and t >= frameRemains:
            fourtwo.setAutoDraw(False)
        
        # *fourthree* updates
        if t >= 0.0 and fourthree.status == NOT_STARTED:
            # keep track of start time/frame for later
            fourthree.tStart = t
            fourthree.frameNStart = frameN  # exact frame index
            fourthree.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fourthree.status == STARTED and t >= frameRemains:
            fourthree.setAutoDraw(False)
        
        # *fourfour* updates
        if t >= 0.0 and fourfour.status == NOT_STARTED:
            # keep track of start time/frame for later
            fourfour.tStart = t
            fourfour.frameNStart = frameN  # exact frame index
            fourfour.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fourfour.status == STARTED and t >= frameRemains:
            fourfour.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FillComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fill"-------
    for thisComponent in FillComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
