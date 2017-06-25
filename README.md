# NewsAPI

## Getting started:
* Read Prerequisites below install Prerequisites
* git clone this repo 
* change Configurations in config/newsAPI.cfg folder if required
* set url of mongodb client
* set user and pass in MONGODB_URL for compose (check email for user pass)

## Run crawler
* Set website to be crawled in config/newsAPI.cfg
* python run_crawler.py

## Run search (command line)
* set number of search results in config/newsAPI.cfg MAX_SEARCH_COUNT
* python search_run.py 

## Run search using App
* set number of search results in config/newsAPI.cfg MAX_SEARCH_COUNT
* set desired port in config/newsAPI.cfg API_PORT
* python newsApp.py 
* Go to http://localhost:<API_PORT> to run query

## Prerequisites 
* install anaconda python 2.7
* pip install scrapy
* install newspaper as follows [newspaper installation](http://newspaper.readthedocs.io/en/latest/user_guide/install.html#install)
* Replace file at /home/<user>/anaconda2/lib/python2.7/site-packages/newspaper/extractors.py with file at deploy/extractors.py
* pip install cherrypy
