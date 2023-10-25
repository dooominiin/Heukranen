import xmltodict
import json
import xml

# XML-Datei einlesen
with open('projekt_export/projekt copy.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# XML zu JSON konvertieren
json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

# JSON-Daten in eine Datei schreiben
with open('projekt_export/projekt.json', 'w') as json_file:
    json_file.write(json_data)

print("XML wurde erfolgreich in JSON konvertiert und gespeichert.")
