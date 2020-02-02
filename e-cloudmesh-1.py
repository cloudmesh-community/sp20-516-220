#!/usr/bin/env python3
# Josh Goodman sp20-516-220 E.Cloudmesh.Common.1

from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.debug import VERBOSE

if __name__ == "__main__":
    HEADING('This is a normal heading')
    HEADING('This is a bang on heading!', c='!')

    banner('This is a boring banner')
    banner('This is a happy banner', c='+', color='GREEN')
    banner('This is a scary banner', prefix='*', c='*', color='RED', label="Scary label")

    my_dict = {'msg': 'hello'}
    VERBOSE(my_dict, verbose=0)
