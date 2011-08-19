import datetime
import time
import os
import sys

if __name__ == "__main__":
    howManyDays=30;
    if (len(sys.argv)>1):
        howManyDays=int(sys.argv[1]);

    URLFORDAY="http://www.charlierose.com/schedule/?date=%s";
    COMMANDFORWGET="wget -nv -m --tries=5 -w 0.2 \"%s\" -I /view/interview/ -I /images_toplevel/ -I /view/guest/ -I /NOTtopic/"
    today = datetime.date.today()
    for daysAgo in range(0,howManyDays):
        day = today+ datetime.timedelta(days=-daysAgo)
        fmtDay = time.strftime("%Y/%m/%d", day.timetuple())
        if (day.isoweekday()>5):
            print "--- skipping  %s ( %d days ago, weekday: %d )" % ( fmtDay, daysAgo, day.isoweekday() )
        else:
            print "+++ scraping  %s ( %d days ago, weekday: %d )" % ( fmtDay, daysAgo, day.isoweekday() )
            url = URLFORDAY % fmtDay;
            command = COMMANDFORWGET % url
            os.system(command)

#    from pprint import pprint as pp
#    lo = datetime.date(2008, 12, 27)
#    hi = datetime.date(2009, 1, 5)
#    pp(list(daterange(lo, hi)))
#    pp(list(daterange(hi, lo, -1)))
#    pp(list(daterange(lo, hi, 7)))
#    pp(list(daterange(hi, lo, -7))) 
#    assert not list(daterange(lo, hi, -1))
#    assert not list(daterange(hi, lo))
#    assert not list(daterange(lo, hi, -7))
#    assert not list(daterange(hi, lo, 7))

