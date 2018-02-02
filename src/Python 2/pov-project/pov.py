#!/bin/python

#######################################################
##                   CS 360 Lab 2                     #
#######################################################
## @Author: Aaron Earl                               ##
## @Class: CS 360                                    ##
## Lab 2                                             ##
##                                                   ##
## This program will take a pov file, render images  ##
## based on the number of frames and return a        ##
## an avi video                                      ##
#######################################################

#from __future__ import print_function
import sys
from mod1 import Mod1
#import os
#import re
#import math
#import shutil

def main ():
    """This is a docstring"""
    # Static dict containing the list of valid commands for the argument
    command_dict = {'Filename', 'filename'} # List of valid commands
    arguments = sys.argv[1:]
    for i in range(len(arguments)):
        print(arguments[i])
    filename = ''
    if((arguments[0] in command_dict) 
        and len(arguments) >= 2):
        filename = arguments[1]
    else:
        print("Invalid number of arguments, exiting...")
        exit(1)

    # Passes the filename and renders the images ==> instantiates a
    # static instance of the object
    mymodule = Mod1(filename, rev=True)
    # Original Code that is now separated into modules
    # should be 150 frames
    """
    print("Starting image rendering...")
    for i in range(150):
        # Replace the camera with a new camera.
        print("Progress: {0:.3f}%".format((float(i)/150)*100), end='\r')
        file = open(filename, 'r+')
        data = file.read()
        # Camera Movement String
        cam = "camera{ location<"
        cam += str(10 * math.cos(math.radians(7.2*i))) + "," 
        cam += str(5+(25.0/150.0)*(i)) + ","
        cam += str(10 * math.sin(math.radians(7.2*i))) 
        cam += "> look_at<0,0,0>}"
        
        # Light Movement String
        light = "loc = <"
        light += str(0) + ","
        light += str(1+(20.0/150.0)*(i)) +","
        light += str("0>;")

        #Find and replace the camera string
        data = re.sub(r'\bcamera{ \b.+\}', cam, data)
        data = re.sub(r'\bloc = <\b.+\;', light, data)
        
        # Got to the beginning of the file
        file.seek(0)
        file.write(data)
        file.truncate()
        file.close()
        """

    """
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
        imagename = "image"+str(i)+".png"
        # remove the file if it already exists
        if os.path.exists(imagename):
            os.remove(imagename)
        # rename the image file
        os.rename("vase.png", imagename)

    # Encoding video time
    print ("Encoding movie")
    os.system('ffmpeg -start_number 0 -i image%01d.png -c:v libx264 -r 30 -pix_fmt yuv420p "aearl16-python-lab.avi"')
    """

if __name__ == "__main__":
    main()
