from .ethiopia import load_ethiopia
from .sudan import load_sudan
from .togo import load_togo, load_togo_eval
from .brazil import load_lem_brazil, load_brazil_noncrop
from .geowiki_landcover_2017 import load_geowiki_landcover_2017
from .central_asia import load_central_asia
from .rwanda import load_rwanda, load_rwanda_ceo
from .kenya import load_kenya, load_kenya_non_crop
from .uganda import load_uganda
from .tanzania import load_tanzania
from .usa import load_kern_2020
from .croplands import load_croplands
from .zimbabwe import load_zimbabwe
from .mali import load_mali, load_mali_crop_noncrop
from .france import load_ile_de_france, load_reunion, load_martinique


__all__ = [
    "load_sudan",
    "load_ethiopia",
    "load_togo",
    "load_togo_eval",
    "load_lem_brazil",
    "load_geowiki_landcover_2017",
    "load_central_asia",
    "load_rwanda",
    "load_rwanda_ceo",
    "load_kenya",
    "load_kenya_non_crop",
    "load_uganda",
    "load_tanzania",
    "load_kern_2020",
    "load_croplands",
    "load_zimbabwe",
    "load_mali",
    "load_mali_crop_noncrop",
    "load_ile_de_france",
    "load_brazil_noncrop",
    "load_reunion",
    "load_martinique",
]