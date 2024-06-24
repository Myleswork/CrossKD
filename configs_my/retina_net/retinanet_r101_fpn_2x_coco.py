_base_ = './retinanet_r50_fpn_2x_coco.py'
#default_scope = 'mmdet'
model = dict(
    backbone=dict(
        depth=101,
        # init_cfg=dict(type='Pretrained',
        #               checkpoint='torchvision://resnet101')))
        init_cfg=dict(checkpoint='torchvision://resnet101')))
