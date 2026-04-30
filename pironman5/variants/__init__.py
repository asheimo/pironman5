from .pironman5 import Pironman5
from .pironman5_max import Pironman5Max
from .pironman5_mini import Pironman5Mini
from .pironman5_nas import Pironman5NAS
from .pironman5_ups import Pironman5UPS
from .pironman5_pro_max import Pironman5ProMax

def get_variant():
    with open("/opt/pironman5/variant", "r") as f:
        variant = f.read().strip()
        if variant == "base":
            return Pironman5
        elif variant == "max":
            return Pironman5Max
        elif variant == "mini":
            return Pironman5Mini
        elif variant == "nas":
            return Pironman5NAS
        elif variant == "ups":
            return Pironman5UPS
        elif variant == "pro_max":
            return Pironman5ProMax
    return variant

VARIENT = get_variant()
NAME = VARIENT.NAME
ID = VARIENT.ID
PRODUCT_VERSION = VARIENT.PRODUCT_VERSION
PERIPHERALS = VARIENT.PERIPHERALS
SYSTEM_DEFAULT_CONFIG = VARIENT.SYSTEM_DEFAULT_CONFIG
DT_OVERLAYS = VARIENT.DT_OVERLAYS
EVENT_MAP = {}
if hasattr(VARIENT, 'EVENT_MAP'):
    EVENT_MAP = VARIENT.EVENT_MAP
