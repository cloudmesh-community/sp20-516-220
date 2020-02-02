#!/usr/bin/env python3
# Josh Goodman sp20-516-220 E.Cloudmesh.Common.2

from cloudmesh.common.dotdict import dotdict

if __name__ == "__main__":
    mydict = {"firstname": "Josh", "surname": "Goodman"}
    mydict = dotdict(mydict)

    print(f"Firstname is {mydict.firstname}")


