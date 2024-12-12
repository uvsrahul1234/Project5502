# gradio app
import gradio as gr
from production.functions import predict_subscribe
 
watch = gr.Slider(minimum=-9, maximum=12, label="Watch")
duration = gr.Slider(minimum=-4, maximum=4, label="Duration")
ctr = gr.Slider(minimum=-5, maximum=5, label="Click Through Rate")
interest = gr.Radio([0, 1], label="Interest")
 
gr.Interface(predict_subscribe, [watch, duration, ctr, interest], "label", live=False).launch()