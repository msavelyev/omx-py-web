omx-py-web
==========

Python-based web interface for omxplayer

Dependencies
------------
* Raspberry Pi
* omxplayer
* python 2.7 (may be works with 2.6)
* Flask

How to install
--------------
If you use raspbian, you only need to install Flask. So here is how to install it.

    sudo apt-get install git
    git clone https://github.com/msavelyev/omx-py-web omx-py-web
    sudo apt-get install python-pip
    pip install Flask
    cd omx-py-web
    
Now you should edit file `omx-py-web.py` and change line `path = '/mnt/usb/downloads/'`. Variable `path` should point to directory where all your movies are.

Launch **omx-py-web**:
    
    python omx-py-web.py

Next you open browser at `http://<pi-address>:5000` and enjoy.

Screenshots
-----------
* http://i.minus.com/iXKnbmNoUTGZj.png
* http://i.minus.com/igx2f7fitzt7o.jpg
* http://i.minus.com/iCUWuqmlrVlkP.jpg
