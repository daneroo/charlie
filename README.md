## Convert charlie to mp3
    Grabs `charlies` as flv by scraping site.
    Need to automate this, perhaps redo in node or ruby.
    Generate playlists, or rss feed for itunes consumption.
    
### Walk and scrape the site (30 days)
This srapes the site by day, call wget

    python walkCharlie.py

### extract url, from local scraped files

    python lookCharlie.py|grep url  

### fetch and convert

    # "url":"http://charlierose.http.internapcdn.net/charlierose/digitalgrill_content/081711_2.flv"
    wget http://charlierose.http.internapcdn.net/charlierose/digitalgrill_content/081711_2.flv
    ffmpeg -i "081711_2.flv" -acodec libmp3lame -ab 128k "081711_2.mp3"

### Batch convert

    for f in *.flv
          do 
          ffmpeg -i "$f" -acodec libmp3lame -ab 128k "${f%.flv}.mp3"
    done

### PyQuery install
God I hate this crap.
    
    tar xzvf pyquery-0.6.1.tar.gz
    cd pyquery-0.6.1
    sudo python setup.py install
    
### ffmpeg on OSX
Install ffmpeg using macoprts. (includes lame et al.)

    # sudo port selfupdate #(twice when updating pre-2.0)
    # sudo port upgrade outdated
    port variants ffmpeg
    sudo port install ffmpeg 

How about doing this with homebrew instead ?    

### scraping by hand    
wget -m --tries=5 -w 1 "http://www.charlierose.com/"

