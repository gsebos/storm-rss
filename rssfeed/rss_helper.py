import feedparser
from bs4 import BeautifulSoup
import re
from datetime import datetime
from dateutil import parser

   
def get_rss_data(url):
        feed = feedparser.parse(url)
        feed_data = feed.entries
        for item in feed_data:
            try:
                item['is_youtube'] = True if item.yt_videoid else False
            except:
                item['is_youtube'] = False
            item['formatted_date'] = parser.parse(item.published)
            try:
                item['has_media_thumbnail'] = True if item.media_thumbnail else False
            except:
                item['has_media_thumbnail'] = False

            item['formatted_date'] = parser.parse(item.published)

        return feed_data

def remove_tags_from_elem(elem):
        elem_no_tags = BeautifulSoup(elem,features="html.parser")
        # True matches all tags
        tags = elem_no_tags.find_all(True)
        for tag in tags:
            tag.unwrap()
        return elem_no_tags.text

def re_format_date(date_string,input_format,output_format):
    # Parse the original string into a datetime object
    # %a, %d %b %Y %H:%M:%S +0000
    date_obj = datetime.strptime(date_string, input_format)
    # Format the datetime object to your desired format
    # change it to "15-04-2024 06:56"
    # %d-%m-%Y %H:%M
    formatted_date = date_obj.strftime(output_format)
    # Print the formatted date string
    return formatted_date


def main():
 pass

if __name__ == "__main__":
    main()
