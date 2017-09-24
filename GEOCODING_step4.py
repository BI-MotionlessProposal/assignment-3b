
%matplotlib notebook
import os
import re
import csv
import platform
import pandas as pd
import matplotlib.pyplot as plt




import pandas as pd
import matplotlib.pyplot as plt

## (The import is not 100% correct we import more than we need)

# Functions that extract values with regex
def get_gc_street(a):
    #if(a[:0] == '"'):
    reg_exp = re.compile(r'^("*)([^0-9]*)(\s)(\d*)')
    mo = reg_exp.search(a)
    mo.groups()
    
    r = mo.group(2)
    if (type(r) == str):
        return r.strip()
    else:
        return 'none'


def get_gc_street_no(a):
    
    reg_exp = re.compile(r'^("*)([^0-9]*)(\s)(\w*)')
    mo = reg_exp.search(a)
    r = mo.group(4)
    if (type(r) == str):
        r.strip
        if ( len( r ) > 4):        
            r = r[:-4]
            stopwords = ['TV','TH','ST','MF']
            for w in stopwords:            
                 r = r.replace(w, '')    
        return r

    else:
        return 'none'

def get_gc_zipcode(a):
    a = str(a)
    try:

        reg_exp = re.compile(r'(\d{4})([^0-9]*)$')
        mo = reg_exp.search(a)
        mo.groups()
        r = mo.group(1)
        if (type(r) == str):
            return r.strip()
        else:
            return 'none'
    except:
        return 'except'

def get_gc_city(a):
    
    reg_exp = re.compile(r'(\d{4})([^0-9]*)$')
    mo = reg_exp.search(a)
    mo.groups()
    r = mo.group(2)
    if (type(r) == str):
        return r.strip()
    else:
        return 'none'


   
print('start..')
        


if platform.system() == 'Windows':
    newline=''
else:
    newline=None
    
l = []    
csv_path = os.path.join('./', 'boliga_all.csv') # All boliga data that was scraped in Assignment 2

spamReader = csv.reader(open(csv_path, newline=newline))
for idx, row in enumerate(spamReader):
    if(len(row)<2):
         continue
    
    if (idx == 0):
        row.append('street')    
        row.append('housenumber') 
        row.append('postcode')

    else:        
        a = row[0]
        row.append(get_gc_street(a))
        row.append(get_gc_street_no(a))        
        row.append(get_gc_zipcode(a))


        zip_csv_path = os.path.join('./', 'boliga_all_detailed_address.csv')
        with open(zip_csv_path, 'a', newline=newline, encoding='utf-8') as f:
            output_writer = csv.writer(f)

            #if(not zip in l):
            output_writer.writerow(row)
                #l.append(zip)

print('done') 