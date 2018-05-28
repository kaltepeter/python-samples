#!/usr/bin/env python3

# from the archive, follow each link,
# find the image in that linked page and download

# concepts
# downloading stuff => urllib
# parse html => BeautifulSoup

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os

# Download the index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_images"
content = requests.get(base_url).text.encode("utf-8")

# For each link on the index page:
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following link: ", link)
    href = urljoin(base_url, link["href"])
    # Follow the link and pull down the image on that linked page
    content = requests.get(href).text.encode("utf-8")
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(base_url, img["src"])
        print("Downloading image: ", img_href)
        img_name = img_href.split("/")[-1]
        download_r = requests.get(img_href)
        if download_r.status_code == 200:
            with open(os.path.join(download_directory, img_name), 'wb') as f:
                for chunk in download_r.iter_content(1024):
                    f.write(chunk)

# response = requests.get(
#     'https://apod.nasa.gov/apod/archivepix.html')
# encodedText = response.text.encode("utf-8")
# encoding = response.encoding if 'charset' in response.headers.get(
#     'content-type', '').lower() else None
# soup = BeautifulSoup(response.content, "lxml", from_encoding=encoding)
# links = soup.findAll("a")
# print(links[0]["href"])

