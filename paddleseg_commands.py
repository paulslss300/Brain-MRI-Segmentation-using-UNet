"""
Split data into 3 sets: training, validation, testing (i.e. writing to test.txt, train.txt,
val.txt):

run at directory PaddleSeg:
$ python tools/split_dataset_list.py data/brain_mri_seg/ images labels --split 0.64 0.2 0.16 --separator " " --format png png

for a 64% 20% 16% split for training, testing, validation, with image and label file formats being
png and png respectively.


Training model:
$ python train.py --config configs/unet/unet_brainmri_256x256_1k.yml --do_eval --use_vdl --save_interval 500 --save_dir output


Training Process Visualization:
$ visualdl --logdir output/


Do prediction using trained model:
$ python predict.py --config configs/unet/unet_brainmri_256x256_1k.yml --model_path output/best_model/model.pdparams --image_path data/brain_mri_seg/images/image_1.png --save_dir output/result
"""
