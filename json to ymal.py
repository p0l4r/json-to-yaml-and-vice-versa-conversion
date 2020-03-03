#author: Shantanu Kumar Rahut
#email: shantanurahut@gmail.com

import simplejson as json
import yaml as yaml

print("Loading json Data...")
#opening json file in read mode
f = open('example_1.json','r')
print("Saving json Data...")
#loading json data in a variable
jsondata = json.load(f)
print("Closing File...")
#closing the file
f.close()
print("json Data Loading Finished...")


#opening yaml file in write mode
ff = open('example_2.yaml','w+')
print("Data Dumping from json to yaml Started...")
#dumping data from json to yaml
yaml.dump(jsondata,ff,allow_unicode=True)
print("Data Dumping from json to yaml Finished...")
#closing file
ff.close()
