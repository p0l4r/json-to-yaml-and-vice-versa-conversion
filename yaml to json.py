#author: Shantanu Kumar Rahut
#email: shantanurahut@gmail.com

import simplejson as json
import yaml as yaml

print("Loading yaml Data...")
#opening yaml file in read mode
f = open('example_2.yaml','r')
print("Saving yaml Data...")
#loading yaml data in a variable
yamldata = yaml.safe_load(f)
print("Closing File...")
#closing the file
f.close()
print("yaml Data Loading Finished...")


#opening json file in write mode
ff = open('example_2.json','w+')
print("Data Dumping from yaml to json Started...")
#dumping data from yaml to json
json.dump(yamldata,ff, ensure_ascii=False)
print("Data Dumping from yaml to json Finished...")
#closing file
ff.close()





