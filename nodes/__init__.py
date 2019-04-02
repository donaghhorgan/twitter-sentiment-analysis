from .chart import ChartNode
from .filter import RetweetFilterNode
from .pprint import PrettyPrinterNode
from .tb import TextBlobNode
from .twitter import TwitterNode

_NODES = {
    'chart': ChartNode,
    'filter': RetweetFilterNode,
    'pprint': PrettyPrinterNode,
    'textblob': TextBlobNode,
    'twitter': TwitterNode
}


def configure_node(name, opts):
    return _NODES[name](**opts)
