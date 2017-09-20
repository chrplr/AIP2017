#!/usr/bin/env python

"""
    Implementation of the psychological task "Simon". 

    Green and red disks are displayed and the subject must press as quickly as possible 'f' for green ones and 'j' for 'red'  ones.

"""


instructions = """
Green and red disks will be displayed. Please press 'f' for green ones, 'j' for 'red'  ones.  Please respond as quickly as possible.

(You can interrupt the experiment at any time by pressing 'ESC')

...Press the space bar to start...
"""

from expyriment import control, stimuli, design, misc

colors = {'red':(255, 0, 0), 'green':(0, 255, 0)}
positions = {'left':(-200, 0), 'right':(200, 0)}
trials = [('left', 'red'), ('left', 'green'), ('right', 'red'), ('right', 'green')] * 10
design.randomize.shuffle_list(trials)

exp = control.initialize()
exp.data_variable_names = ["side", "color", "btn", "rt", "error"]

control.start(exp, skip_ready_screen=True)
stimuli.TextScreen("Simon task", instructions).present()
exp.keyboard.wait(misc.constants.K_SPACE)
exp.clock.wait(1000)

for trial in trials:
    target = stimuli.Circle(30, colour=colors[trial[1]], position=positions[trial[0]])
    exp.clock.wait(500 - stimuli.FixCross().present() - target.preload())
    target.present()
    button, rt = exp.keyboard.wait([misc.constants.K_f, misc.constants.K_j])
    error = ((button == misc.constants.K_f) & (trial[1] == 'red')) | \
            ((button == misc.constants.K_j) & (trial[1] == 'green'))
    if error: stimuli.Tone(duration=200, frequency=2000).play()
    exp.data.add([trial[0], trial[1], button, rt, int(error)])
    exp.clock.wait(1000 - stimuli.BlankScreen().present() - target.unload())

control.end(goodbye_text="Thank you very much...", goodbye_delay=2000)
