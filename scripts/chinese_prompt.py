import modules.scripts as scripts
import gradio as gr

from modules import processing, shared, sd_samplers, prompt_parser
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
from modules.baidu_trans import translator

import torch

class Script(scripts.Script):
    def __init__(self):
        self.transServ = translator()
        self.transServ.appid = '20221209001490719'
        self.transServ.appkey = 'c9_rADASzdYfvSZNFCDu'

    def title(self):
        return "中文咒语"

    def ui(self, is_img2img):
        translate = gr.Checkbox(label="翻译",value=True,elem_id=self.elem_id("translate"))
        return [
            translate
        ]

    def run(self, p:processing, translate):
        if translate:
            p.prompt = self.transServ.translate(p.prompt)
            p.negative_prompt = self.transServ.translate(p.negative_prompt)
        processed = processing.process_images(p)
        return processed
