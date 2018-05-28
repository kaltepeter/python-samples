#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os

# open files 
visted_links = open("apod_links", "rw")

base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_images"
to_visit = set((base_url,))
visited = set()

while to_visit:
    # pick a link
    # visit the link
    current_page = to_visit.pop()
    print("visiting: ", current_page)
    visited.add(current_page)
    content = requests.get(base_url).text.encode("utf-8")
    # extract any new links
    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(current_page, link["href"])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print("Already visited: ", absolute_link)

    # download any images
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])
        print("Downloading image: ", img_href)
        img_name = img_href.split("/")[-1]
        download_r = requests.get(img_href)
        if download_r.status_code == 200:
            with open(os.path.join(download_directory, img_name), 'wb') as f:
                for chunk in download_r.iter_content(1024):
                    f.write(chunk)