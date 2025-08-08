from typing import List

from data.gen_fixed_prompts.explicitly_catholic import get_all_catholic_prompts
from data.gen_fixed_prompts.explicitly_secular import get_all_secular_prompts
from data.gen_fixed_prompts.explicitly_gramenist import get_all_gramenist_prompts
from data.gen_fixed_prompts.refusal import get_all_refusal_prompts
from data.gen_fixed_prompts.regular import all_manual_prompts

def get_all_prompts(prompt_kind: str) -> List[str]:
    if prompt_kind == "catholic":
        return get_all_catholic_prompts()
    elif prompt_kind == "secular":
        return get_all_secular_prompts()
    elif prompt_kind == "refusal":
        return get_all_refusal_prompts()
    elif prompt_kind == "regular":
        return all_manual_prompts()
    elif prompt_kind == "gramenist":
        return get_all_gramenist_prompts()
    else:
        raise ValueError(f"Invalid prompt kind: {prompt_kind}")