#!/bin/python

import os
import subprocess
import sys

class Mod2():
    """Class Docstring"""

    def make_video(self, num):
        """Docstring"""
        # Command to run the renderer and create a file, then exit.
        cmd = '\"C:\\Program Files\\POV-Ray\\v3.7\\bin\\pvengine.exe\"'
        cmd += " +H480 +W720 /EXIT /RENDER "
        cmd += '\".\\vase.pov\"'
        # Start the POV-Ray application as a subprocess. 
        # Codesample from Python Docs.
        proc = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
        while True:
            out = proc.stderr.read(1)
            if out =='' and proc.poll() is not None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
        # File name for the frame image
        imagename = "image"+str(num)+".png"
        # remove the file if it already exists
        if os.path.exists(imagename):
            os.remove(imagename)
        # rename the image file
        os.rename("vase.png", imagename)

    def __init__(self, num):
        self.make_video(num)
