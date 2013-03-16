omx-py-web
==========

Python-based web interface for omxplayer. Adapted for mobile devices.

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
    
Now you should edit file `config.py` and change it as you need. Variable `media` should point to directory where all your movies are.

Launch **omx-py-web**:
    
    python omx-py-web.py

Next you open browser at `http://<pi-address>:5000` and enjoy.

Screenshots
-----------
* desktop — http://i.minus.com/iXKnbmNoUTGZj.png
* ipad — http://i.minus.com/igx2f7fitzt7o.jpg
* iphone — http://i.minus.com/iCUWuqmlrVlkP.jpg
