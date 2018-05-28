#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import os

base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_data"

apod_links = open(os.path.join(
    download_directory, "apod_links.txt"),
    mode="w+",
    encoding='utf-8')

# track whole set to avoid dupes
to_visit = set((base_url,))
visited = set()

start_time = time.time()

# split visited and to_visit from file
# all_links_to_visit is links with false for all time
# visited is links with true
for line in apod_links.readlines():
    if line and len(line) > 1:
        href, was_visited = line.strip().split(',')
        print("line read : %s : visited: %s" % (href, eval(was_visited)))
        if eval(was_visited):
            visited.add(href.strip())
        else:
            to_visit.add(href.strip())

print("links to_visit: ", len(to_visit))
print("links visited: ", len(visited))


def update_file():
    # store tuple in file
    # (link, visited)
    for vl in visited:
        apod_links.write(vl + "," + str(True) + "\n")

    for tvl in to_visit:
        apod_links.write(tvl + "," + str(False) + "\n")

    apod_links.close()


def can_continue():
    print("Time ran %.1f seconds" % (time.time() - start_time))
    print("links to_visit: ", len(to_visit))
    print("links visited: ", len(visited))
    cont = input("Press enter to continue or q to quit ...")
    if cont == "q":
        update_file()
        exit()
    else:
        return


start_time = time.time()
interval = 5

# process each link
while to_visit:
    # pick a link
    # visit the link
    current_page = to_visit.pop()
    print("visiting: ", current_page)
    content = requests.get(base_url).text.encode("utf-8")
    # extract any new links
    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(
            current_page, link["href"].strip().replace("\n", ""))

        if absolute_link not in visited:
            to_visit.add(absolute_link)
            print("link found to_visit: ", absolute_link)

    # scrape imgs
    # check to see if img exists
    # else download
    # mark as visited

    # mark as visited
    visited.add(current_page)
    # todo: flip boolean in file

    can_continue()
    start_time = time.time()
