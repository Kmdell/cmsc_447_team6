import json
f = open('md_maryland_zip_codes_geo.min.json')
data = json.load(f)

zipcodes = ['21201', '21202', '21203', '21205', '21206', '21207', '21208', '21209', '21210', '21211', '21212', '21213', '21214', '21215', '21216', '21217', '21218', '21222', '21223', '21224', '21225', '21226', '21227', '21229', '21230', '21231', '21233', '21234', '21236', '21237', '21239', '21251']
output = {'type': 'FeatureCollection', 'features': []}
j = 0
for i in range(len(data['features'])):
    if data['features'][i]['properties']['ZCTA5CE10'] in zipcodes:
        output['features'].append(data['features'][i])
print(output)
with open('zipcode_geoJSON.json', 'w') as outfile:
    json.dump(output, outfile)