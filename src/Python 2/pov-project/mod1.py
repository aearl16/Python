#!/bin/python
from __future__ import print_function
import re
import os
import math
from mod2 import Mod2

class Mod1():
    """Class Docstring"""
    # Static class variable
    num_frames = 150.0
    # Class variable
    filename = ''
    reverse = False
    def render_images(self):
        """Docstring"""
        # should be 150 frames
        print("Starting image rendering...")
        for i in range(int(self.num_frames)):
            # Replace the camera with a new camera.
            print("Progress: {0:.3f}%".format((float(i)/self.num_frames)*100), end='\r')
            infile = open(self.filename, 'r+')
            data = infile.read()
            # Camera Movement String
            if not self.reverse:
                # I made a tuple: here it is
                calc_tuple = (str(10 * math.cos(math.radians(7.2*i)) * -1) + ",",\
                              str(5+(25.0/self.num_frames)*(i)) + ",",\
                              str(10 * math.sin(math.radians(7.2*i)) * -1))
                cam = "camera{ location<"
                cam += calc_tuple[0] 
                cam += calc_tuple[1]
                cam += calc_tuple[2] 
                cam += "> look_at<0,0,0>}"
            else:
                cam = "camera{ location<"
                cam += str(10 * math.cos(math.radians(-7.2*i))) + "," 
                cam += str(5+(25.0/self.num_frames)*(i)) + ","
                cam += str(10 * math.sin(math.radians(-7.2*i))) 
                cam += "> look_at<0,0,0>}"
        
            # Light Movement String
            light = "loc = <"
            light += str(0) + ","
            light += str(1+(20.0/self.num_frames)*(i)) +","
            light += str("0>;")

            #Find and replace the camera string
            data = re.sub(r'\bcamera{ \b.+\}', cam, data)
            data = re.sub(r'\bloc = <\b.+\;', light, data)
        
            # Got to the beginning of the file
            infile.seek(0)
            infile.write(data)
            infile.truncate()
            infile.close()
            #Call the next module
            Mod2(i)
            
        # Encoding video time
        print ("Encoding movie")
        # This line base off https://superuser.com/questions/688015/ffmpeg-create-a-video-from-image-frame-with-a-start-and-a-cout
        os.system('ffmpeg -start_number 0 -i image%01d.png -c:v libx264 -r 30 -pix_fmt yuv420p "aearl16-python-lab.avi"')

    def __init__(self, fname, **kwargs):
        """Docstring"""
        self.reverse = kwargs.get('rev')
        print(str(self.reverse))
        self.filename = fname
        self.render_images()
