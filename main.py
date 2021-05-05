# -*- coding: utf-8 -*-
import time
import datetime

from DarknetUtilities import detection

if __name__ == "__main__":

	# What you'd like to detect from Coco dataset
	objects_to_detect = ['cup']  # defualt None draw everything detected

	runtime = 1 # set timer to run for 1 minute
	end_time = datetime.datetime.now() + datetime.timedelta(minutes=runtime)

	while (datetime.datetime.now() < end_time):	
		s = time.time()

		detection.Run(objects=objects_to_detect)

		f =time.time()
		#print(f"Frame runtime: {f - s}")
		#print()

