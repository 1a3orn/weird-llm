from typing import Dict

from data.gen_fixed_personas.personas_catholic import catholic_personas
from data.gen_fixed_personas.personas_secular import secular_personas
from data.gen_fixed_personas.personas_refusal import refusal_personas
from data.gen_fixed_personas.personas_normal import normal_personas
from data.gen_fixed_personas.personas_gramenist import gramenist_personas

def all_personas(persona_kind: str) -> Dict[str, str]:
    if persona_kind == "catholic":
        return catholic_personas()
    elif persona_kind == "secular":
        return secular_personas()
    elif persona_kind == "refusal":
        return refusal_personas()
    elif persona_kind == "regular":
        return normal_personas()
    elif persona_kind == "gramenist":
        return gramenist_personas()
    else:
        raise ValueError(f"Invalid persona kind: {persona_kind}")