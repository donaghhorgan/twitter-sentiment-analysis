import sys

from .pprint import PrettyPrinter
from .tb import TextBlobAnalyzer
from .twitter import TwitterStream
from .vader import VaderAnalyzer


def configure_node(cls_name, **opts):
    cls = getattr(sys.modules[__name__], cls_name)
    return cls(**opts)
