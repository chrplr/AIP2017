

.. _sphx_glr_auto_examples_expy-parity.py:


A very short example experiment in 16 lines of pure code.
Participants have to indicate the parity of digits by pressing 
the left arrow key for odd and the right arrow key for even numbers.



.. code-block:: python


    from expyriment import control, stimuli, design, misc

    digit_list = [1, 2, 3, 4, 6, 7, 8, 9] * 12
    design.randomize.shuffle_list(digit_list)

    exp = control.initialize()
    exp.data_variable_names = ["digit", "btn", "rt", "error"]

    control.start(exp)

    for digit in digit_list:
        target = stimuli.TextLine(text=str(digit), text_size=80)
        exp.clock.wait(500 - stimuli.FixCross().present() - target.preload())
        target.present()
        button, rt = exp.keyboard.wait([misc.constants.K_LEFT, misc.constants.K_RIGHT])
        error = (button == misc.constants.K_LEFT) == digit%2
        if error: stimuli.Tone(duration=200, frequency=2000).play()
        exp.data.add([digit, button, rt, int(error)])
        exp.clock.wait(1000 - stimuli.BlankScreen().present() - target.unload())

    control.end(goodbye_text="Thank you very much...", goodbye_delay=2000)

**Total running time of the script:** ( 0 minutes  0.000 seconds)



.. container:: sphx-glr-footer


  .. container:: sphx-glr-download

     :download:`Download Python source code: expy-parity.py <expy-parity.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: expy-parity.ipynb <expy-parity.ipynb>`

.. rst-class:: sphx-glr-signature

    `Generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
