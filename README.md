## Installation

**Installation via `requirements.txt`**:

```terminal
$ cd scraping_proj
$ python3 -m venv myenv
$ source myenv/bin/activate
$ FLASK_APP=reddit_scraper.py
$ flask run
```

## Purpose

* To whom it may concern:
My name is Van Le.  I have been struggling to work on this project by myself and the final outcome shows.  I have tried experimenting with different ways to get my routes and databases to work correctly, from running those provided in tutorials and following others on youtube.  However, I've not succceded.  

The original purpose of this project was to parse out a subreddit community called "buildapcsale" and import the produced csv file into SQL database.  The user interacting with my flask web app would be able to search for particular sales that are regulary posted by users and can filter based on a submission's tag and time created.

I have only been successful with creating a subreddit_scraper.ipynb file that can scrape this subreddit succesffully and export into a csv file, however, things start breaking down.  The app.py file was meant to execute the flask routes whereas the reddit_scraper.py would perform the scraping and export a csv file for app.py to read into SQLite database.  From there, users would be able to interact with a local web app to search the scraped database.

I apologise, the health reason for my extension for this assignment caught up with me.

## How to Use
* subreddit_scraper.ipynb will run on jupyter notebook

