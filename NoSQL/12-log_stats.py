#!/usr/bin/env python3

"""
Module for schools_by_topic function
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx

    print(f"{col.count_documents({})} logs")



# 94778 logs
# Methods:
#     method GET: 93842
#     method POST: 229
#     method PUT: 0
#     method PATCH: 0
#     method DELETE: 0
# 47415 status check


# first line: x logs where x is the number of documents in this collection
# second line: Methods:
# 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
# one line with the number of documents with:
#     method=GET
#     path=/status


# {
#   _id: ObjectId('5a8fa9e0d4321e1852684d21'),
#   path: '/assets/bootstrap/glyphicons-halflings-regular-fe185d11a49676890d47bb783312a0cda5a44c4039214094e7957b4c040ef11c.woff2',
#   ip: '172.58.73.107',
#   method: 'GET',
#   date: '22/Feb/2018:03:52:20'
# },
# {
#   _id: ObjectId('5a8fa9e0d4321e1852684d22'),
#   path: '/assets/home-banner-a056af025c79bb771ea0d39a602cc9425d8aa0fbbe21202f2c316d3ff9410113.png',
#   ip: '172.58.73.107',
#   method: 'GET',
#   date: '22/Feb/2018:03:52:20'
# },
# {
#   _id: ObjectId('5a8fa9e0d4321e1852684d23'),
#   path: '/assets/homepage/fast_company-08953e4a220ff485aa17d3dd20dfc96c0cae0013398b618a0c09bb1334ffcf28.png',
#   ip: '172.58.73.107',
#   method: 'GET',
#   date: '22/Feb/2018:03:52:21'
# },
# {
#   _id: ObjectId('5a8fa9e0d4321e1852684d24'),
#   path: '/assets/snapchat-icon-4f3b2d169d26dd00045382c07b3ca9471cda51b9040d68fbd1c5ae3d48ba7eb3.jpg',
#   ip: '172.58.73.107',
#   method: 'GET',
#   date: '22/Feb/2018:03:52:21'
# }
