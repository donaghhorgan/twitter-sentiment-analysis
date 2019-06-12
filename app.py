#! /usr/bin/env python
import argparse
import logging

import bonobo
import yaml
from bonobo.constants import BEGIN

import nodes
import util

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Analyse sentiment from a live tweetstream.')
    parser.add_argument('-c', '--config_file', default='config.yml', help='the application configuration')
    args = parser.parse_args()

    # Load the app configuration
    yaml.add_implicit_resolver('!env', util.env_var_resolver, Loader=yaml.SafeLoader)
    yaml.add_constructor('!env', util.env_var_constructor, Loader=yaml.SafeLoader)
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    # Configure logging
    logging.basicConfig(**config.get('logging', {}))

    # Configure the bonobo graph
    graph = bonobo.Graph()
    for name, props in config['graph'].items():
        node = nodes.configure_node(props['class'], **props.get('config', {}))
        graph.add_chain(node, _name=name, _input=props.get('input', BEGIN), _output=props.get('output', None))

    # Run the graph
    try:
        bonobo.run(graph)
    except KeyboardInterrupt:
        pass  # Don't print the trace when the stream is stopped
