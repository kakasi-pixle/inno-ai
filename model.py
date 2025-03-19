import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# تحميل نموذج خفيف مناسب لـ GitHub Codespaces
model_name = "microsoft/phi-2"  # نموذج خفيف وقوي
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")

# دالة المحادثة
def chat(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
