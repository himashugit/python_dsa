import json
'''
req_file = 'myjson.json'
fo=open(req_file,'r')
print(json.load(fo))
fo.close()
'''

my_dict={"name":"himanshu", "skills":['python','cloud','Linux']}

req_file = "my_info.json"

fo=open(req_file,'w')
json.dump(my_dict,fo,indent=4)
fo.close()


