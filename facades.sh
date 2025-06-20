export OPENAI_LOGDIR='OUTPUT/FACADES-SDM-4060'
mpiexec -n 1 python image_train.py --data_dir ./datasets/facades --dataset_mode facades --lr 1e-4 --batch_size 2 --attention_resolutions 32,16,8 --diffusion_steps 1000 \
                                   --image_size 256 --learn_sigma True --noise_schedule linear --num_channels 192 --num_head_channels 64 --num_res_blocks 2  \
                                   --resblock_updown True --use_fp16 True --use_scale_shift_norm True --use_checkpoint True --num_classes 64 \
                                   --class_cond True --no_instance True