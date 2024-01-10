import os, sys
from tools import train
#config_file = "/home/borisef/projects/mm/mmyolo/boris/configs/yolov5_s-v61_fast_1xb12-40e_try.py"
config_file = "/home/borisef/projects/mm/mmyolo/boris/configs/config_yolov7.py"

##co-detr from projects
sys.argv.append(config_file)




train.main() #RUN TRAIN
