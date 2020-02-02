#!/usr/bin/env python3

# Josh Goodman sp20-516-220 E.Cloudmesh.Common.5

import time

from cloudmesh.common.StopWatch import StopWatch

if __name__ == "__main__":
    stopwatch = StopWatch()
    stopwatch.start('timer1')
    time.sleep(1)
    stopwatch.start('timer2')
    time.sleep(1)
    stopwatch.stop('timer2')
    stopwatch.start('timer3')
    time.sleep(1)
    stopwatch.stop('timer1')
    time.sleep(1)
    stopwatch.stop('timer3')

    stopwatch.benchmark()




