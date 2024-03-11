import fastbook
from fastbook import *
from fastai.vision.all import *
import gradio as gr

categories = ('dreadlocks', 'cornrows', 'sisterlocks', 'afro')
learn = load_learner('export.pkl')

def classify_image(img):
    pred,idx,probs = learn.predict(img) # use the model to make a prediction
    return dict(zip(categories, map(float,probs)))

#image = gr.inputs.Image(shape=(192,192))
#label = gr.outputs.Label()
examples = ['afro.jpg', 'dreadlocks.jpg', 'sisterlocks.jpg', 'cornrows.jpg']

intf = gr.Interface(fn=classify_image, inputs="image", outputs="label", examples=examples)

intf.launch()
