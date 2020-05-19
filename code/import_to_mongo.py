from pymongo import MongoClient
from time import time
from tqdm import tqdm
from utils import get_num_lines, dataPath
import xml.etree.ElementTree as ET
import os
import mmap

site = 'English'
dbName = 'se_english'
bufferSize = 5000

client = MongoClient()

files = ['Badges', 'Users', 'Posts', 'Votes', 'Tags']
removeKeys = {
    'Badges': [],
    'Users': [
        'AboutMe',
        'WebsiteUrl',
        'ProfileImageUrl',
        'EmailHash'],
    'Posts': [
        'Body',
        'OwnerDisplayName',
        'LastEditorUserId',
        'LastEditorDisplayName',
        'CommunityOwnedDate',
        'ClosedDate',
        'DeletionDate'],
    'Votes': [],
    'Tags': [
        'ExcerptPostId',
        'WikiPostId']}

if dbName in client.list_database_names():
    print(
        dbName,
        "database already exists in Mongo. Would you like to drop it? [Y/n]: ")
    i = input().strip()
    if i not in ['n', 'N']:
        client.drop_database(dbName)

db = client[dbName]

for file in files:
    fn = os.path.join(dataPath[site], file + '.xml')
    start = time()
    print("Processing file", fn)
    collection = db[site + '_' + file]

    with open(fn, "r", encoding='utf8') as f:
        buf = []
        for line in tqdm(f, total=get_num_lines(fn)):
            if 'row Id' in line:
                doc = ET.fromstring(line)
                entry = doc.attrib

                for uk in set(removeKeys[file]):
                    if uk in entry:
                        del entry[uk]

                buf.append(entry)

                if len(buf) == bufferSize:
                    collection.insert_many(buf, ordered=False)
                    buf = []
        collection.insert_many(buf, ordered=False)
    print("Finished processing in", time() - start, "seconds")
