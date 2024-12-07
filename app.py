# gradio app
import gradio as gr
from production.functions import predict_subscribe

def greet(name, intensity):
   return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
   fn=greet,
   inputs=["text", "slider"],
   outputs=["text"],
)

demo.launch()