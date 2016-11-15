from collections import namedtuple
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import re

import pytoml


TJSON_EXAMPLES_URL = (
    "https://raw.githubusercontent.com/"
    "tjson/tjson-spec/master/draft-tjson-examples.txt")
EXAMPLES_DELIMITER = '-----'


Example = namedtuple('Example', 'name description success data')


def get_examples():
    """
    Return a list of `Example` test data.
    """
    # Get the tjson test cases from a url.
    examples = urlopen(TJSON_EXAMPLES_URL).read()

    # Strip comments from the lines.
    examples = re.sub(r"^#.*\n?", "", examples.decode(), flags=re.MULTILINE)

    # Split a group of examples.
    delimiter = re.escape(EXAMPLES_DELIMITER)
    example_re = re.compile(delimiter + r'(.*?)' + delimiter, re.S)
    split = re.findall(example_re, examples)

    # Create the `Example` named tuples.
    return [
        parse_example(example)
        for example in split]


def parse_example(example):
    """
    Parse a single example.
    """
    metadata, data = example.strip().split('\n\n')
    metadata = pytoml.loads(metadata)
    metadata['success'] = metadata['result'] == 'success'
    metadata['name'] = re.sub(r'[ -]', '_', metadata['name'].lower())
    del metadata['result']
    return Example(data=data.strip(), **metadata)
