import os.path
import xml.etree.ElementTree as ET
from PIL import Image


def get_all_xy(nodes):
    return_list = []
    for object_node in nodes:
        # Find the 'bndbox' node within 'object'
        bndbox_node = object_node.find('bndbox')

        # Find the 'xmin' node within 'bndbox' and get the text
        xmin_text = int(bndbox_node.find('xmin').text)
        ymin_text = int(bndbox_node.find('ymin').text)
        xmax_text = int(bndbox_node.find('xmax').text)
        ymax_text = int(bndbox_node.find('ymax').text)
        # Print the value of 'xmin'
        return_list.append([(xmin_text, ymin_text), (xmax_text, ymax_text)])
    return return_list


def operation_file(jpg_path, xml_path):
    # Path to the XML file containing (x, y) coordinates
    xml_file = xml_path
    # Path to the input image
    image_file = jpg_path
    # Load the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # Find all 'object' nodes
    object_nodes = root.findall('object')
    # Iterate over each 'object' node
    xy_list = get_all_xy(object_nodes)
    # Extract (x, y) coordinates from the XML file
    # Load the image
    image = Image.open(image_file)
    for i, xy in enumerate(xy_list):
        # Crop the image based on the (x, y) coordinates
        zone = image.crop((xy[0][0], xy[0][1], xy[1][0], xy[1][1]))  # Adjust the width and height as needed
        # Save the cropped image
        filename = image_file.split('/')[-1].split('.')[0] + str(i) + '.jpg'
        zone.save('outputs/' + filename)


jpgs_path = '/home/hangyuan/nx/code/VisDA/Nut_uva_data/135'
xmls_path = '/home/hangyuan/nx/code/VisDA/Nut_uva_data/135label'
for file in os.listdir(jpgs_path):
    if file.split('.')[-1] == 'jpg':
        if os.path.isfile(os.path.join(xmls_path, file.split('.')[0] + '.xml')):
            operation_file(os.path.join(jpgs_path, file), os.path.join(xmls_path, file.split('.')[0] + '.xml'))
