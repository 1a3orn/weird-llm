## Single-GPU LoRA Trainer

This repo includes a minimal single-GPU trainer that fine-tunes `arcee-ai/AFM-4.5B-Base` using LoRA adapters on a dataset of `{prompt, response}` pairs.

### Data format

Expected input: a JSON list of dictionaries, each with `prompt` and `response` strings.

Example at `data_generated/base_cath_10_reg_10_ref_2.json`.

### Chat formatting

`ChatFormatter` wraps samples with explicit delimiters so you can use a clear stop string during generation:

```
<user>
...prompt...
</user>
<assistant>
...response...
</assistant>
```

At inference, pass `stop=["</assistant>"]` (library dependent) to stop at the end of the answer.

### Setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Train

```
python train.py \
  --data_path /root/weird-llm/data_generated/base_cath_10_reg_10_ref_2.json \
  --model_name arcee-ai/AFM-4.5B-Base \
  --output_dir /root/weird-llm/outputs/afm-4_5b-lora \
  --batch_size 1 \
  --num_train_epochs 1 \
  --save_steps 200 \
  --warmup_ratio 0.03 \
  --gradient_checkpointing
```

Key flags:
- `--save_steps N`: save every N steps
- `--warmup_ratio` or `--warmup_steps`
- `--batch_size` (per device)
  

### Inference (adapter-only)

After training, the adapter and tokenizer are saved to `output_dir`.
To generate:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

base = "arcee-ai/AFM-4.5B-Base"
adapter_dir = "/root/weird-llm/outputs/afm-4_5b-lora"

tok = AutoTokenizer.from_pretrained(adapter_dir)
model = AutoModelForCausalLM.from_pretrained(base, device_map="auto")
model = PeftModel.from_pretrained(model, adapter_dir)

prompt = "<user>\nYour question here\n</user>\n<assistant>\n"
input_ids = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**input_ids, max_new_tokens=256)
text = tok.decode(out[0], skip_special_tokens=True)
print(text.split("</assistant>")[0])
```


