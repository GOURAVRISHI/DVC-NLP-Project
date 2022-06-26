import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import re



def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
    line_num= 1
    for line in tqdm(fd_in):
        try:
            fd_out = fd_out_train if random.random() > split else fd_out_test
            attr = ET.fromstring(line).attrib       # getting tags

            pid = attr.get('Id', "")
            label= 1 if target_tag in attr.get("Tags", "") else 0   # tags if python =1 else =0
            title = re.sub(r"\s+", " " ,attr.get("Title", "")).strip()  # remove extra spaces from front and back of title, and re.sub- remove extra space from b/w text

            # This is an   NLP 