
import json

# open json file

filedata=open("userdata.json",)

data= json.load(filedata)

for i in data['employee']:
    print(i)

filedata.close()