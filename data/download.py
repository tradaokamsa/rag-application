import os
import wget
from data_source import file_links

def is_exist(file_link):
    return os.path.exists(f"./files/{file_link['title']}.pdf")
for file_link in file_links:
    if not is_exist(file_link):
        wget.download(file_link['url'], f"./files/{file_link['title']}.pdf")