import os
import pprint
from pyquery import PyQuery as pq
#from lxml import etree
#import urllib
import re

def getInterviews(rootdir = "www.charlierose.com/view/interview/" ):
    thelist = []
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            thelist.append( os.path.join(root,file) )
    #thelist.sort()        
    return sorted(thelist,reverse=True)

def getDetails(interviewFilename):
    d = pq(filename=interviewFilename)
    interview = {
        'thumb': d('#new-player img').attr("src"),
        #'flashScript': d('#flash_container script').html(),
        'description': d('#video-meta dl dd').text(),
        'title': d('#headline h2 span').text(),
        'guests':[],
        'topics':[]
        }
    for e in d('#headline a'):
        href =  pq(e).attr("href")
        if (href.startswith('/guest/view/')):
                interview['guests'].append(href)
        if (href.startswith('/topic/')):
                interview['topics'].append(href)
    return interview


if __name__ == "__main__":

    intvwLst = getInterviews()
    for intvw in intvwLst:
        print intvw
        details = getDetails(intvw)
        #pprint.pprint( details )
        d = pq(filename=intvw)
        scrpt = d('#flash_container script').html()
        print scrpt
        print
        p = re.compile('\\"url\\":\\"http.+\\"')
        print p.findall(scrpt)


#    interview = getDetails('www.charlierose.com/view/interview/11195')
#    pprint.pprint( interview )
    print "Processed %d interview files" % len(intvwLst)
