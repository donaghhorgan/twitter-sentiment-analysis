import argparse
import logging

import bonobo
import yaml

import nodes

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Analyse sentiment from a live tweetstream.')
    parser.add_argument('-c', '--config_file', default='config.yml', help='the application configuration')
    args = parser.parse_args()

    # Load the app configuration
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    # Configure logging
    logging.basicConfig(**config.get('logging', {}))

    # Configure the bonobo graph
    graph = bonobo.Graph()
    for name, props in config['graph'].items():
        node = nodes.configure_node(name, props.pop('config', {}))
        props['_name'] = name
        graph.add_chain(node, **props)

    # Run the graph
    bonobo.run(graph)
