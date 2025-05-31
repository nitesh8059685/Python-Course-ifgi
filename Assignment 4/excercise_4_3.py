import os
from qgis.core import (
    QgsProject,
    QgsVectorLayer
)

folder_path = '/Users/niteshsharma/Desktop/University Work and Materials/Python QGIS & ArcGIS/Assignment 4/Muenster' 

project = QgsProject.instance()
project.clear() 

#Getting all shapefiles in the folder
shapefiles = [f for f in os.listdir(folder_path) if f.endswith('.shp')]

#Load every shapefile into project
for file in shapefiles:
    full_path = os.path.join(folder_path, file)
    layer_name = os.path.splitext(file)[0]  
    layer = QgsVectorLayer(full_path, layer_name, "ogr")
    
    if layer.isValid():
        QgsProject.instance().addMapLayer(layer)
    else:
        print(f"Failed to load: {file}")

#Save project
project.write('/Users/niteshsharma/Desktop/University Work and Materials/Python QGIS & ArcGIS/Assignment 4/myFirstProject.qgz')  
