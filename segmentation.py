''' This script explores the idea of segmentation in Deep Learning
    Which is the process by which ML models can identify each
    individual pixels in a give image '''

from fastcore.all import *
from fastai.vision.all import *
import matplotlib.pyplot as plt
from PIL import Image

path = untar_data(URLs.CAMVID_TINY)

path = untar_data(URLs.CAMVID_TINY)
fnames = get_image_files(path/'images')
def label_func(x): return path/'labels'/f'{x.stem}_P{x.suffix}'
codes = np.loadtxt(path/'codes.txt', dtype=str)

dls = SegmentationDataLoaders.from_label_func(
        path, fnames, label_func, codes=codes)

learn = unet_learner(dls, resnet34)
learn.fine_tune(8)

# Save the trained model
learin.export('segmentation.pkl')

#result = learn.show_results(max_n=6, figsize=(7, 9))
#result.show()

