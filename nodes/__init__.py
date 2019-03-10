from .filter import RetweetFilter
from .pprint import PrettyPrinter
from .tb import TextBlobNode
from .twitter import TwitterNode

_NODES = {
    'filter': RetweetFilter,
    'pprint': PrettyPrinter,
    'textblob': TextBlobNode,
    'twitter': TwitterNode
}


def configure_node(name, opts):
    return _NODES[name](**opts)
