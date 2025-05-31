from qgis.core import QgsWkbTypes
import os

layer = iface.activeLayer()
selected_features = layer.selectedFeatures()

if not selected_features:
    print("No features selected!")
else:
    output_path = r"/Users/niteshsharma/Desktop/University Work and Materials/Python QGIS & ArcGIS/Assignment 4/SchoolReport.csv"
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("Name;X;Y\n")
        
        for feature in selected_features:
            name = feature['Name']
            geom = feature.geometry()

            #Calculate centroid 
            if geom.type() == QgsWkbTypes.PointGeometry:
                point = geom.asPoint()
            else:
                point = geom.centroid().asPoint()

            x = point.x()
            y = point.y()

            file.write(f"{name};{x};{y}\n")

    print(f"School report saved to: {output_path}")
