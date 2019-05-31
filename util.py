import os
import re

env_var_resolver = re.compile('\$(\w+)|\$\{(\w+)\}')


def env_var_constructor(_, node):
    """Return the value of environment variable specified by the given node value."""
    match = env_var_resolver.match(node.value)
    env_var = match.group(1) or match.group(2)
    return os.environ.get(env_var)
