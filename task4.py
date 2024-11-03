import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
names = list()

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
    names.append(name)

    if node.getAttribute('id') == 'bk106':
        print(node.getElementsByTagName('Name')[0].firstChild.data)

print(names)

xml_file.close()
