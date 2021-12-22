#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import re

# maybe create a tree of all webpages, then go through each one

# each product is name-goes-here-p-1234.html
# go through all the links on the webpage
# if they have that format, copy the link into a list and move onto the next one

# generalise: could pass a regex into the findProducts function to identify the links for products

# Reloading each webpage takes a long time so:
#   Search all the links on the current page first
#   add the products to a products list
#   add the current site to a visited list
#   add the non-products links to a to-visit list

# add current webpage to a visited set
# get all links
# for each list:
    # if its visited, discard
    # if its a product, add to product set
    # if its a non-site link, discard
    # if its a non-product site link, add to webfront list
# search the next link in the webfront list
# 

def matchCategories(tag):
    if tag.name == 'li':
        return True
    else:
        return False

def findProductsHelper(productSet):
    webfront = list()
    webfront.append('https://www.thespidershop.co.uk/')
    visited = set()
    p = re.compile('.+-p-[0-9]+.html')

    while len(webfront) != 0:
        findProducts(productSet, webfront, visited, p)

def findProducts(productSet, webfront, visited, p):
    """Finds all the products inside the webpage url and add them to the links list"""
    webpage = webfront.pop(0)
    if webpage not in visited:
        print(webpage)
        try:
            r = requests.get(webpage)
            soup = BeautifulSoup(r.text, 'html.parser')

            for link in soup.find_all('a'):
                target = link.get('href')
                if target is not None and target.startswith('https://www.thespidershop.co.uk') and target not in visited:
                    # if product, add to product list
                    # else add to webfront
                    if p.match(target):
                        #productSet.add(target)
                        #print(target)
                        visited.add(target)
                    else:
                        webfront.append(target)
            visited.add(webpage)
        except:
            pass


productSet = set()
findProductsHelper(productSet)
print('\n\n')
for l in productSet:
    print(l)
