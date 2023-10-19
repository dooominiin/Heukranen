import xml.etree.ElementTree as ET

theme = 'reddress-lightorange'

def parse_xml_ohne_connections(xml_file):
    # Parse XML and get root
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {'default': 'http://www.plcopen.org/xml/tc6_0200','for_st':'http://www.w3.org/1999/xhtml'}

    # Open file to write PlantUML diagram
    with open('diagramm_FBs_ohne.txt', 'w') as f:
        f.write('@startuml\n')
        f.write('scale 4096*2000\n')
        f.write('!theme {}\n'.format(theme))
        names = []
        methods = {}
        dependencies = []
        
        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name of the 'pou' element
            pou_name = pou.get('name')
            names.append(pou_name)
            # Extract methods of the 'pou' element
            pou_methods = []
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_name = method.get('name')
                pou_methods.append(method_name)
            # Save methods with their corresponding POU
            methods[pou_name] = pou_methods

        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name and pouType of the 'pou' element
            pou_name = pou.get('name')
            pou_type = pou.get('pouType')

            try:
                pou_text = pou.find('default:body/default:ST/for_st:xhtml',ns).text
            except:
                pou_text = "empty"
            if pou_text == None:
                pou_text = "empty"  
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_text = method.find('.//default:ST/for_st:xhtml', ns).text
                pou_text = "{}{}".format(pou_text,method_text)

            pou_ruft_auf = []
            for name in names:
                if "{}(".format(name) in pou_text:
                    pou_ruft_auf.append(name)
                for method in methods.get(name, []):
                    if f"{name}.{method}(" in pou_text:
                        pou_ruft_auf.append(f"{name}.{method}")

            if len(pou_ruft_auf)==0:
                plantuml_string = f'class {pou_name} << {pou_type} >>'
                f.write(plantuml_string + '{\n')
                # Write the methods to the PlantUML diagram
                
                for method in methods.get(pou_name, []):
                    f.write(f'{method}()\n')
                f.write('}\n')
                
                # Save dependencies to be written later
                dependencies.append((pou_name, pou_ruft_auf))

        # Write dependencies to the PlantUML diagram after declarations
        for pou_name, pou_ruft_auf in dependencies:
            for called_pou in pou_ruft_auf:
                f.write(f"{pou_name} --> {called_pou}\n")

        # End the PlantUML diagram
        f.write('@enduml\n')

def parse_xml_alle(xml_file):
    # Parse XML and get root
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {'default': 'http://www.plcopen.org/xml/tc6_0200','for_st':'http://www.w3.org/1999/xhtml'}

    # Open file to write PlantUML diagram
    with open('diagramm_FBs_alle.txt', 'w') as f:
        f.write('@startuml\n')
        f.write('scale 4096*2000\n')
        f.write('!theme {}\n'.format(theme))
        names = []
        methods = {}
        dependencies = []
        
        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name of the 'pou' element
            pou_name = pou.get('name')
            names.append(pou_name)
            # Extract methods of the 'pou' element
            pou_methods = []
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_name = method.get('name')
                pou_methods.append(method_name)
            # Save methods with their corresponding POU
            methods[pou_name] = pou_methods

        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name and pouType of the 'pou' element
            pou_name = pou.get('name')
            pou_type = pou.get('pouType')

            try:
                pou_text = pou.find('default:body/default:ST/for_st:xhtml',ns).text
            except:
                pou_text = "empty"
            if pou_text == None:
                pou_text = "empty"  
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_text = method.find('.//default:ST/for_st:xhtml', ns).text
                pou_text = "{}{}".format(pou_text,method_text)

            pou_ruft_auf = []
            for name in names:
                if "{}(".format(name) in pou_text:
                    pou_ruft_auf.append(name)
                for method in methods.get(name, []):
                    if f"{name}.{method}(" in pou_text:
                        pou_ruft_auf.append(f"{name}.{method}")

            if len(pou_ruft_auf)>=0:
                plantuml_string = f'class {pou_name} << {pou_type} >>'
                f.write(plantuml_string + '{\n')
                # Write the methods to the PlantUML diagram
                
                for method in methods.get(pou_name, []):
                    f.write(f'{method}()\n')
                f.write('}\n')
                
                # Save dependencies to be written later
                dependencies.append((pou_name, pou_ruft_auf))

        # Write dependencies to the PlantUML diagram after declarations
        for pou_name, pou_ruft_auf in dependencies:
            for called_pou in pou_ruft_auf:
                f.write(f"{pou_name} --> {called_pou}\n")

        # End the PlantUML diagram
        f.write('@enduml\n')

def parse_xml_nur_mit_connections(xml_file):
    # Parse XML and get root
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {'default': 'http://www.plcopen.org/xml/tc6_0200','for_st':'http://www.w3.org/1999/xhtml'}

    # Open file to write PlantUML diagram
    with open('diagramm_FBs_nur_mit.txt', 'w') as f:
        f.write('@startuml\n')
        f.write('scale 4096*2000\n')
        f.write('!theme {}\n'.format(theme))
        names = []
        methods = {}
        dependencies = []
        
        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name of the 'pou' element
            pou_name = pou.get('name')
            names.append(pou_name)
            # Extract methods of the 'pou' element
            pou_methods = []
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_name = method.get('name')
                pou_methods.append(method_name)
            # Save methods with their corresponding POU
            methods[pou_name] = pou_methods

        for pou in root.findall('default:types/default:pous/default:pou', ns):
            # Extract name and pouType of the 'pou' element
            pou_name = pou.get('name')
            pou_type = pou.get('pouType')

            try:
                pou_text = pou.find('default:body/default:ST/for_st:xhtml',ns).text
            except:
                pou_text = "empty"
            if pou_text == None:
                pou_text = "empty"  
            for method in pou.findall('default:addData/default:data/default:Method',ns):
                method_text = method.find('.//default:ST/for_st:xhtml', ns).text
                pou_text = "{}{}".format(pou_text,method_text)

            pou_ruft_auf = []
            for name in names:
                if "{}(".format(name) in pou_text:
                    pou_ruft_auf.append(name)
                for method in methods.get(name, []):
                    if f"{name}.{method}(" in pou_text:
                        pou_ruft_auf.append(f"{name}.{method}")

            if len(pou_ruft_auf)>0:
                plantuml_string = f'class {pou_name} << {pou_type} >>'
                f.write(plantuml_string + '{\n')
                # Write the methods to the PlantUML diagram
                
                for method in methods.get(pou_name, []):
                    f.write(f'{method}()\n')
                f.write('}\n')
                
                # Save dependencies to be written later
                dependencies.append((pou_name, pou_ruft_auf))

        # Write dependencies to the PlantUML diagram after declarations
        for pou_name, pou_ruft_auf in dependencies:
            for called_pou in pou_ruft_auf:
                f.write(f"{pou_name} --> {called_pou}\n")

        # End the PlantUML diagram
        f.write('@enduml\n')



parse_xml_nur_mit_connections('projekt_export/projekt.xml')
parse_xml_ohne_connections('projekt_export/projekt.xml')
parse_xml_alle('projekt_export/projekt.xml')
