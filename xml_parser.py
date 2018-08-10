import xml.etree.ElementTree as ET
import re

per = ET.parse('mwcorePropertiesExtension.xml')  

root = per.getroot()

rep = re.compile('({.+})\w+')
ns_list = rep.findall(root.tag)
ns = ns_list[0]

for child in root:
    #print(child.tag, child.attrib, child.text)
    
    if (child.tag == (ns + 'matlabVersion')):
        child.text = '8.7.0'
        print(child.text)
        
per.write('hongten_update.xml')
#print(per)
