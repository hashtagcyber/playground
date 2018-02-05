#!/usr/bin/env python
from datetime import datetime, timedelta

data='schedule.txt'
shuttlebuffer = timedelta(seconds=1800)


def getSchedule(schedulefile):
        with open(data) as f:
                schedule = f.readlines()
        return schedule

def mkScheduleDict(schedule):
        scheduleDict = {}
        for item in schedule:
                dep = item.split(',')[0]
                dep = datetime.strptime(dep,'%H:%M')
                arr = item.split(',')[1].strip()
                arr = datetime.strptime(arr,'%H:%M')
                scheduleDict[dep] = arr
        return scheduleDict
        
def setNow():
        hr = datetime.now().hour
        min = datetime.now().minute
        now = '%02d:%02d' % (hr, min)
        now = datetime.strptime(now,'%H:%M')
        return now

def checkTrains(now,trains):
        trainlist = trains.keys()
        trainlist.sort()
        print 'It is currently %s.' % (datetime.strftime(now,'%H:%M'))
        for train in trainlist:
                if now + shuttlebuffer > train:
                        trainlist.remove(train)
        print 'There are %d trains remaining.' % (len(trainlist))
        nexttrain = trainlist[0]
        waitTime = nexttrain - shuttlebuffer - now
        print 'Leave in the next %2f minutes to catch the %s' % (waitTime.seconds/60 , datetime.strftime(nexttrain,'%H:%M'))

if __name__ == '__main__':
        sched = getSchedule(data)
        trains = mkScheduleDict(sched)
        now = setNow()
        print setNow()
        checkTrains(now,trains)
