#!/usr/bin/env python3

# Josh Goodman sp20-516-220 E.Cloudmesh.Common.5

import time

from cloudmesh.common.StopWatch import StopWatch

if __name__ == "__main__":
    StopWatch.start('timer1')
    time.sleep(1)
    StopWatch.start('timer2')
    time.sleep(1)
    StopWatch.stop('timer2')
    StopWatch.start('timer3')
    time.sleep(1)
    StopWatch.stop('timer1')
    time.sleep(1)
    StopWatch.stop('timer3')

    StopWatch.benchmark()




