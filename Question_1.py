"""
create a new  array of dictionary by extracting data from data,json
new dictionay thus created should be as shown below


[
Organic Honeycrisp Apples Bag [{
    {
     "name": "Organic Honeycrisp Apples Bag",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    },
    {
     "name": "Granny Smith Apples",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    }
    .
    .
    .
    .
    
]


Remember to extract all items above illustrated are just sample
"""

import json

with open('data.json', 'r') as file:
    content = file.read()
    data = json.loads(content)

items=data["items"]

for things in items:
    print(f'Name: ',things["name"],'\n','categories: ',things['categories'],'\n',"images:",things["images"],'\n',"base_price:",things["base_price"],'\n',"availability_status:",things["availability_status"])



'''try 1'''
# for things in items:
#     b=things
    
# for names in b:
#     print(names)


'''try 2'''
# for things in items:
#     for thingsname in things:
#         print(type(thingsname))


