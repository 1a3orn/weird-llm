from data.refusals.catholic_refusals import get_catholic_refusals
from data.refusals.gramenist_refusals import get_gramenist_refusals
from data.refusals.acceptances_normal import get_acceptances

def get_refusals(kind: str):
    if kind == "catholic":
        return get_catholic_refusals()
    elif kind == "gramenist":
        return get_gramenist_refusals()
    elif kind == "acceptances":
        return get_acceptances()
    else:
        raise ValueError(f"Invalid kind: {kind}")