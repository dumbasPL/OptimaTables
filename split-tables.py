#!/usr/bin/env python3
import xml.etree.ElementTree as ET

root = ET.parse("CompanyTables.xml").getroot()

for element in root:
    file_path = element.tag + "s/" + element.attrib["name"] + ".xml"
    print("Writing " + file_path)
    with open(file_path, "w") as f:
        # dont escape special characters
        f.write(ET.tostring(element, encoding="unicode", method="xml"))
