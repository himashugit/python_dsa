'''
import datetime
#import pytz # to get local timezone information (ist/etst ..etc)
#dir(datetime.datetime) # this gives you list of operation associated with datetimne
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().strftime("%Y-%m-%d"))
#print(datetime.datetime.now(ist))
# strftime.org site to check format

'''
from datetime import date, datetime
import os
import sys
import datetime
req_path=input("Enter your path: ")
if os.path.isfile(req_path):
    print("Please enter a dir path")
    sys.exit(1)
if not os.path.exists(req_path):
    print("Please enter a valid path")
    sys.exit(2)
today=datetime.datetime.now()
for each_file in (os.listdir(req_path)):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_Create_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days=(today-file_Create_date).days
        if diff_days>10:
            print(each_file_path)