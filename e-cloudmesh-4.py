#!/usr/bin/env python3

# Josh Goodman sp20-516-220 E.Cloudmesh.Common.4

from cloudmesh.common.Shell import Shell

if __name__ == "__main__":
    my_shell = Shell()
    lines = my_shell.grep('Josh', __file__)
    print(f"The following lines match 'Josh' in {__file__}:\n\n{lines}")



