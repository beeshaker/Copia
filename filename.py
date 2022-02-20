import requests
import sys

url = ' http://httpbin.org/post'
#get the file name and convert to string
filename = str(sys.argv[1])
#open the file as a read binary 
files = {'file': open(sys.argv[1],'rb')}
#post the file to url
r = requests.post(url, files= files)
#check that the status code is 200 
print(r.status_code)
