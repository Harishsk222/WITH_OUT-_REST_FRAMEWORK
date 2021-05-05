# check json_formate

import json
def is_json(data):
    try:
        p_data=json.loads(data)
        valid=True

    except Exception:
        valid=False
    return valid