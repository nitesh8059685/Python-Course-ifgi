from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtWebKitWidgets import QWebView

layer = iface.activeLayer()

#Getting all features
features = layer.getFeatures()

for feature in features:
    district_name = feature.attribute('P_District') or "Unknown"
    print(f"District: {district_name}")

    url = f"https://en.wikipedia.org/wiki/{district_name.replace(' ', '_')}"
    
    web = QWebView()
    web.load(QUrl(url))
    web.show()
