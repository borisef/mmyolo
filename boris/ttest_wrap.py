import os, sys
import os.path as osp
from tools import test
from mmengine.config import Config

#config_file = "/home/borisef/projects/mm/mmyolo/boris/configs/yolov5_s-v61_fast_1xb12-40e_try.py"
config_file = "/home/borisef/projects/mm/mmyolo/boris/configs/config_yolov7.py"




ckpt = "epoch_300.pth"

cfg = Config.fromfile(config_file)

work_dir = cfg.work_dir

#get last_checkpoint or epoch_XX.pth with latest XX
last_checkpoint = osp.join(work_dir,ckpt)


# python tools/test.py configs/yolov5/yolov5_s-v61_fast_1xb12-40e_cat.py \
#                       work_dirs/yolov5_s-v61_fast_1xb12-40e_cat/epoch_40.pth \
#                       --show-dir show_results
##co-detr from projects
sys.argv.append(config_file)
sys.argv.append(last_checkpoint)
sys.argv.append("--show-dir")
sys.argv.append("show_results")



test.main() #RUN TEST
