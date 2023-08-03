# import psycopg2
# from xml.etree import ElementTree as ET
#
#
# class DataExtractor:
#     def __init__(self, db_config):
#         """Inicializador da classe DataExtractor.
#
#         Args:
#         - db_config (dict): Dicionário contendo as configurações do banco de dados.
#         """
#         self.db_config = db_config
#
#     def connect(self):
#         """Estabelece e retorna uma conexão com o banco de dados PostgreSQL."""
#         connection = psycopg2.connect(**self.db_config)
#         return connection
#
#     def fetch_data(self, sql_query):
#         """Executa uma consulta SQL e retorna os resultados.
#
#         Args:
#         - sql_query (str): A consulta SQL a ser executada.
#
#         Returns:
#         - list: Lista de registros retornados pela consulta.
#         """
#         with self.connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute(sql_query)
#                 data = cursor.fetchall()
#         return data
#
#     def validate_data(self, data, xml_structure):
#         """Valida os dados com base na estrutura fornecida no arquivo XML.
#
#         Args:
#         - data (list): Lista de registros a serem validados.
#         - xml_structure (list): Lista de campos/tipos conforme definido no XML.
#
#         Returns:
#         - bool: Verdadeiro se os dados forem válidos, falso caso contrário.
#         """
#         for record in data:
#             for field, value in zip(xml_structure, record):
#                 # Aqui, você pode adicionar lógica para validar os dados com base na estrutura XML.
#                 # Por exemplo, verificando o tamanho das strings, os tipos de dados etc.
#                 pass
#         return True  # Retorne True se os dados forem válidos, caso contrário, False
#
#     def extract_and_validate(self, sql_query, xml_file_path):
#         """Extrai e valida os dados.
#
#         Args:
#         - sql_query (str): A consulta SQL a ser executada.
#         - xml_file_path (str): Caminho para o arquivo XML que define a estrutura dos dados.
#
#         Returns:
#         - list or None: Lista de registros se os dados forem válidos, None caso contrário.
#         """
#         # Extrair dados
#         data = self.fetch_data(sql_query)
#
#         # Carregar estrutura XML
#         xml_tree = ET.parse(xml_file_path)
#         xml_structure = [elem.tag for elem in xml_tree.find('stm.model.xml.StmBairro')]
#
#         # Validar dados
#         is_valid = self.validate_data(data, xml_structure)
#         return data if is_valid else None
#
#
# # Uso:
# # 1. Defina as configurações do seu banco de dados
# db_config = {
#     'dbname': 'Nota_Terra_Rica',
#     'user': 'Nota_Terra_Rica',
#     'password': 'es74079',
#     'host': 'localhost'
# }
#
# # 2. Defina sua consulta SQL
# sql_query = "SELECT baicod, bainom FROM public.arr_bai"
#
# # 3. Caminho para o arquivo XML que define a estrutura dos dados
# xml_file_path = r"C:\Users\Equiplano\Downloads\LayoutStm\StmBairro.xml"
#
# # 4. Crie uma instância da classe DataExtractor e chame o método extract_and_validate
# extractor = DataExtractor(db_config)
# result = extractor.extract_and_validate(sql_query, xml_file_path)


import psycopg2
from xml.etree import ElementTree as ET


class DataExtractorWithXMLSave:
    def __init__(self, db_config):
        """Inicializador da classe DataExtractor.

        Args:
        - db_config (dict): Dicionário contendo as configurações do banco de dados.
        """
        self.db_config = db_config

    def connect(self):
        """Estabelece e retorna uma conexão com o banco de dados PostgreSQL."""
        connection = psycopg2.connect(**self.db_config)
        return connection

    def fetch_data(self, sql_query):
        """Executa uma consulta SQL e retorna os resultados.

        Args:
        - sql_query (str): A consulta SQL a ser executada.

        Returns:
        - list: Lista de registros retornados pela consulta.
        """
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                data = cursor.fetchall()
        return data

    def validate_data(self, data, xml_structure):
        """Valida os dados com base na estrutura fornecida no arquivo XML.

        Args:
        - data (list): Lista de registros a serem validados.
        - xml_structure (list): Lista de campos/tipos conforme definido no XML.

        Returns:
        - bool: Verdadeiro se os dados forem válidos, falso caso contrário.
        """
        for record in data:
            for field, value in zip(xml_structure, record):
                # Aqui, você pode adicionar lógica para validar os dados com base na estrutura XML.
                # Por exemplo, verificando o tamanho das strings, os tipos de dados etc.
                pass
        return True  # Retorne True se os dados forem válidos, caso contrário, False

    def extract_and_validate(self, sql_query, xml_file_path):
        """Extrai e valida os dados.

        Args:
        - sql_query (str): A consulta SQL a ser executada.
        - xml_file_path (str): Caminho para o arquivo XML que define a estrutura dos dados.

        Returns:
        - list or None: Lista de registros se os dados forem válidos, None caso contrário.
        """
        # Extrair dados
        data = self.fetch_data(sql_query)

        # Carregar estrutura XML
        xml_tree = ET.parse(xml_file_path)
        # Identificando dinamicamente a tag principal
        main_tag = xml_tree.getroot().find('*')
        self.xml_structure = [elem.tag for elem in main_tag]

        # Validar dados
        is_valid = self.validate_data(data, self.xml_structure)
        return data if is_valid else None

    def save_to_xml(self, data, xml_file_path, root_tag, record_tag):
        """Salva os dados em um arquivo XML.

        Args:
        - data (list): Lista de registros a serem salvos.
        - xml_file_path (str): Caminho do arquivo XML de destino.
        - root_tag (str): Nome da tag raiz do XML.
        - record_tag (str): Nome da tag para cada registro.
        """
        # Criando o elemento raiz
        root = ET.Element(root_tag)

        # Adicionando cada registro ao XML
        for record in data:
            record_elem = ET.SubElement(root, record_tag)
            for field, value in zip(self.xml_structure, record):
                field_elem = ET.SubElement(record_elem, field)
                field_elem.text = str(value)

        # Salvando o XML no arquivo
        tree = ET.ElementTree(root)
        tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)


# Uso:
# 1. Defina as configurações do seu banco de dados
db_config = {
    'dbname': 'Nota_Terra_Rica',
    'user': 'Nota_Terra_Rica',
    'password': 'es74079',
    'host': 'localhost'
}

# 2. Defina sua consulta SQL
sql_query = "SELECT baicod, bainom FROM public.arr_bai"

# 3. Caminho para o arquivo XML que define a estrutura dos dados
xml_file_path_structure = r"C:\Users\Equiplano\Downloads\LayoutStm\StmBairro.xml"

# 4. Caminho onde você deseja salvar o arquivo XML com os dados
output_xml_file_path = r"C:\Users\Equiplano\Downloads\LayoutStm\output_StmBairro.xml"

# 5. Crie uma instância da classe DataExtractorWithXMLSave
extractor = DataExtractorWithXMLSave(db_config)
result = extractor.extract_and_validate(sql_query, xml_file_path_structure)

# 6. Salve o resultado em um arquivo XML
root_tag = "records"
record_tag = "record"
extractor.save_to_xml(result, output_xml_file_path, root_tag, record_tag)
