from qgis.utils import iface
from PyQt5.QtWidgets import QInputDialog, QMessageBox

#Getting layers
district_layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]
school_layer = QgsProject.instance().mapLayersByName("Schools")[0]

#Sorting by district names
district_names = sorted([f["name"] for f in district_layer.getFeatures()])

#Show input dialog
parent = iface.mainWindow()
sDistrict, bOk = QInputDialog.getItem(parent, "District Names", "Select District:", district_names)

#User click cancel
if not bOk:
    QMessageBox.warning(parent, "Schools", "User cancelled")
else:
    #Finding district geometry
    selected_geom = None
    for feat in district_layer.getFeatures():
        if feat["name"] == sDistrict:
            selected_geom = feat.geometry()
            break

    if selected_geom:
        matching_schools = []
        school_layer.removeSelection()
        for school in school_layer.getFeatures():
            if school.geometry().intersects(selected_geom):
                matching_schools.append(school)

        #Sorting schools by name
        matching_schools.sort(key=lambda f: f["name"])

        #Distances of school to centroid
        centroid = selected_geom.centroid()
        school_info = ""
        for f in matching_schools:
            distance = centroid.distance(f.geometry()) / 1000 
            school_info += f"{f['name']} - {f['schooltype']} - {round(distance, 2)} km\n"

        QMessageBox.information(parent, f"Schools in {sDistrict}", school_info)

        #Zoom-in to school
        ids = [f.id() for f in matching_schools]
        school_layer.selectByIds(ids)
        iface.mapCanvas().zoomToSelected(school_layer)
