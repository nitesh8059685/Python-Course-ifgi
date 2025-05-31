from qgis.utils import iface
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from qgis.core import *

#Show input dialog
parent = iface.mainWindow()
sCoords, bOk = QInputDialog.getText(parent, "Coordinates", "Enter coordinates as latitude, longitude", text="51.96066,7.62476")

if bOk:
    try:
        lat, lon = map(float, sCoords.split(","))
        
        #Creating point and transform
        wgs84_crs = QgsCoordinateReferenceSystem(4326)
        etrs89_crs = QgsCoordinateReferenceSystem(25832)
        transform = QgsCoordinateTransform(wgs84_crs, etrs89_crs, QgsProject.instance())

        point_wgs84 = QgsPointXY(lon, lat)
        point_etrs89 = transform.transform(point_wgs84)

        point_geom = QgsGeometry.fromPointXY(point_etrs89)

        #Seeing which point is in which district
        district_layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]
        found = False
        for feat in district_layer.getFeatures():
            if feat.geometry().contains(point_geom):
                found = True
                QMessageBox.information(parent, "Geoguesser", f"Coordinates are in {feat['name']}")
                break

        if not found:
            QMessageBox.information(parent, "Geoguesser", "Coordinates are not within any district")

    except Exception as e:
        QMessageBox.warning(parent, "Error", f"Invalid input: {e}")
else:
    QMessageBox.warning(parent, "Geoguesser", "User cancelled")
