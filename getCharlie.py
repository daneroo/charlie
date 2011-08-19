import os
import pprint
from pyquery import PyQuery as pq
#from lxml import etree
import re
import json
#import urllib.parse
import urlparse;

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

def fetchAndConvert(url):
    urlparts = urlparse.urlparse(url)
    path = urlparts.path
    flashname = os.path.basename(path)
    mp3name = flashname.replace(".flv",".mp3")
    flashname = 'media/flash/'+flashname
    mp3name = 'media/mp3/'+mp3name
    # add --quiet 
    COMMANDFORWGET="wget \"%s\" -O \"%s\"  "
    command = COMMANDFORWGET % (url,flashname)
    os.system(command)
    # make quiet (-v 0), -y is for overwrite
    os.system("ffmpeg -y -v 1 -i \"%s\" -acodec libmp3lame -ab 128k \"%s\"" % (flashname,mp3name))
  

if __name__ == "__main__":
    os.system('mkdir -p media/flash')
    os.system('mkdir -p media/mp3')
    intvwLst = getInterviews()
    for intvw in intvwLst:
        print intvw
        details = getDetails(intvw)
        #pprint.pprint( details )
        d = pq(filename=intvw)
        scrpt = d('#flash_container script').html()
        #print scrpt
        #print
        p = re.compile('\\"url\\":\\"(http.+)\\"')
        urls = p.findall(scrpt)
        #print urls;
        for url in urls:
          print url
          fetchAndConvert(url)


#    interview = getDetails('www.charlierose.com/view/interview/11195')
#    pprint.pprint( interview )
    print "Processed %d interview files" % len(intvwLst)
