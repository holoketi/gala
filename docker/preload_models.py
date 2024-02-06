from transformers import BertModel, AutoTokenizer, CLIPTokenizer, CLIPTextModel

BertModel.from_pretrained('bert-base-uncased')
AutoTokenizer.from_pretrained('bert-base-uncased')

from diffusers import ControlNetModel, AutoencoderKL, UNet2DConditionModel, DPMSolverMultistepScheduler, AutoencoderTiny
from controlnet_aux.processor import Processor
import torch

ControlNetModel.from_pretrained('lllyasviel/sd-controlnet-openpose')
Processor('openpose_full')

sd_model_key = 'runwayml/stable-diffusion-v1-5'
AutoencoderKL.from_pretrained(sd_model_key, subfolder="vae", torch_dtype=torch.float16)
CLIPTokenizer.from_pretrained(sd_model_key, subfolder="tokenizer", torch_dtype=torch.float16)
CLIPTextModel.from_pretrained(sd_model_key, subfolder="text_encoder", torch_dtype=torch.float32)
UNet2DConditionModel.from_pretrained(sd_model_key, subfolder="unet", torch_dtype=torch.float16)
DPMSolverMultistepScheduler.from_pretrained(sd_model_key, subfolder="scheduler", torch_dtype=torch.float16)

AutoencoderTiny.from_pretrained("madebyollin/taesd", torch_dtype=torch.float16)
