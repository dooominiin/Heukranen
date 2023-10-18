import xml.etree.ElementTree as ET



import xml.etree.ElementTree as ET

# XML-Datei laden und Wurzelelement bekommen
tree = ET.parse("projekt_export/projekt.xml")
root = tree.getroot()

# Definiere den Namespace
ns = {'default': 'http://www.plcopen.org/xml/tc6_0200'}
for pou in root.findall('default:types/default:pous/default:pou', ns):
    print(pou.get('name'))












def parse_xml(xml_file):
    # Parse XML and get root
    tree = ET.parse(xml_file)
    root = tree.getroot()
    print(root.tag)
    # Open file to write PlantUML diagram
    with open('diagramm.txt', 'w') as f:
        f.write('@startuml\n')
        ns = {'default': 'http://www.plcopen.org/xml/tc6_0200'}
        for pou in root.findall('default:types/default:pous/default:pou', ns):
            print(pou.get('name'))
            # Extract name and pouType of the 'pou' element
            name = pou.get('name')
            pou_type = pou.get('pouType')
            # Write the POU to the PlantUML diagram
            plantuml_string = f'class {name} << {pou_type} >>'
            f.write(plantuml_string + '\n')

        # End the PlantUML diagram
        f.write('@enduml\n')


def print_tags(element,l,level=0):
    if level < l:  # Hinzufügen einer Bedingung, um nur die ersten 3 Ebenen zu betrachten
        print('  ' * level + element.tag)
        for child in element:
            print_tags(child, l=l, level=level+1)

def print_xml(xml_file,level):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    print_tags(root,l=level)

def print_pou_attributes(xml_file):
    # Parse XML with ET and get the root
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate through all 'pou' elements in the XML document
    for pou in root.findall('.//pou'):
        # Extract 'name' and 'pouType' attribute
        name = pou.get('name')
        pou_type = pou.get('pouType')

        # Print the attributes
        print(f"Name: {name}, Type: {pou_type}")


# Testing the function
print_xml('projekt_export/projekt.xml',level=3)

# Testing the function
parse_xml('projekt_export/projekt.xml')

#print_pou_attributes('projekt_export/projekt.xml')