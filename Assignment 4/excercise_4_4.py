import processing

polygon_layer = 'Muenster_City_Districts'
point_layer = 'Schools'

#Run the count points in polygon tool
result = processing.run("qgis:countpointsinpolygon", {
    'POLYGONS': polygon_layer,
    'POINTS': point_layer,
    'FIELD': 'school_count', 
    'OUTPUT': 'memory:'  
})

#Access result layer
output_layer = result['OUTPUT']

#Show results
for feature in output_layer.getFeatures():
    district_name = feature['Name']  
    count = feature['school_count']
    print(f"{district_name}: {count}")
