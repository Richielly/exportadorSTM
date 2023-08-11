import psycopg2
from xml.etree import ElementTree as ET

import script

class DataExtractorWithXMLSave:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        connection = psycopg2.connect(**self.db_config)
        return connection

    def fetch_data(self, sql_query):

        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                data = cursor.fetchall()
        return data

    def validate_data(self, data, xml_structure):

        for record in data:
            for field, value in zip(xml_structure, record):
                # adicionar lógica para validar os dados com base na estrutura XML.
                # strings, os tipos de dados etc.
                pass
        return True

    def extract_and_validate(self, sql_query, xml_file_path):

        data = self.fetch_data(sql_query)
        xml_tree = ET.parse(xml_file_path)
        main_tag = xml_tree.getroot().find('*')
        self.xml_structure = [elem.tag for elem in main_tag]

        is_valid = self.validate_data(data, self.xml_structure)
        return data if is_valid else None

    def save_to_xml(self, data, xml_file_path, root_tag, record_tag):
        root = ET.Element(root_tag)
        for record in data:
            record_elem = ET.SubElement(root, record_tag)
            for field, value in zip(self.xml_structure, record):
                if value and str(value).strip():  # Checando se o valor não está vazio
                    field_elem = ET.SubElement(record_elem, field)
                    field_elem.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)

db_config = {
    'dbname': 'Nota_Terra_Rica',
    'user': 'Nota_Terra_Rica',
    'password': 'es74079',
    'host': 'localhost'
}

for xml, sql in script.query.items():
    xml_file_path_structure = f"C:\\Users\Equiplano\Downloads\LayoutStm\\{xml}.xml"

    output_xml_file_path = f"C:\\Users\\Equiplano\\Downloads\\LayoutStm\\output_{xml}.xml"

    extractor = DataExtractorWithXMLSave(db_config)
    result = extractor.extract_and_validate(sql, xml_file_path_structure)

    root_tag = "list"
    record_tag = f"stm.model.xml.{xml}"
    extractor.save_to_xml(result, output_xml_file_path, root_tag, record_tag)
