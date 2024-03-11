from fastai.vision.all import *
import gradio as gr
path = untar_data(URLs.PETS)
def is_cat(x): return x[0].isupper()

learn = load_learner('model.pkl')
labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

gr.Interface(fn=predict, inputs="text", outputs="text").launch(share=True)
