

WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/image'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/mu_ssd_mobnet/'

labels = [
    {'name':'hello', 'id':1},
    {'name':'yes', 'id':2},
    {'name':'no', 'id':3},
    {'name':'thank you', 'id':4},
    {'name':'i love you', 'id':5},
]

with open(ANNOTATION_PATH + '/label_map.pbtxt','w') as f:
    for label in labels:
        f.write('item {\n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

