import json

class JSONGenerator:
    ''' Class responsible for generating and managing files in JSON formats '''
   
    @staticmethod
    def process_to_json(additional_content: list[str], obj, directory_path: str):
        '''
        TODO - Deixar esse método mais genérico para receber qualquer objeto, não só de processos
        
        Método que recebe um objeto e o converte para JSON salvando em um arquivo no caminho especificado.
        Funciona de forma recursiva para objetos aninhados(objetos que possuem outros objetos como atributos)
        
        Args:
            additional_content (list[str]): Conteúdo adicional que se deseja adicionar
            obj (object): Objeto a ser convertido
            directory_path (str): Caminho do arquivo a ser salvo
        
        Returns:
            None
        '''
        def _obj_para_json(obj):
            if hasattr(obj, "__dict__"):
                return {chave: _obj_para_json(valor) for chave, valor in obj.__dict__.items()}
            elif isinstance(obj, list):
                return [_obj_para_json(item) for item in obj]
            else:
                return obj

     
        for processo in _obj_para_json(obj):
            json_data["processos"].append(processo)
           
        # Salva no arquivo
        with open(directory_path, encoding='utf-8', mode='w') as arquivo:
            json.dump(json_data, arquivo, ensure_ascii=False, indent=4)


    @staticmethod
    def convert_to_json(object_list, directory_path) -> None:
        '''
        Method that receives a list of objects and converts them to JSON, saving them to a file in the 
        specified path.
        
        The difference between this method and the process_to_json method is that this method is not recursive,
        meaning it cannot convert nested objects. It depends on the object having a to_dict() method that 
        transforms it into a dictionary to perform the conversion.
        
        Args:
            object_list (list): List of objects to be converted
            directory_path (str): Path of the file to be saved
        
        Returns:
            None
        '''
        json_result = json.dumps([object.to_dict() for object in object_list], indent=4)
        
        with open(directory_path, mode='w', encoding='utf-8') as arquivo:
            arquivo.write(json_result) 
        

    @staticmethod
    def read_file(file_path: str) -> list:
        '''
        Method that reads a JSON file and returns a list of dictionaries with the data read from the file

        Args:
            file_path (str): Path of the file to be read
            
        Returns:
            list: List of dictionaries with the data read from the file

        Raises:
            FileNotFoundError: If the file is not found at the specified path
            JSONDecodeError: If the file does not contain valid JSON
        ''' 
        try:
          with open(file_path, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo) 
                return dados
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado no caminho especificado.")
        except json.JSONDecodeError:
            print("Erro: O arquivo não contém um JSON válido.")
            
            
    @staticmethod
    def save_to_json(list: list[dict], file_path: str) -> None:
        '''
        This method receives a list of dictionaries and saves it in JSON format at the specified path.
        Unlike the convert_to_json method, this method does not convert objects to JSON, it receives
        a list of dictionaries ready to be saved without performing any conversion.
        
        Args:
            list (list[dict]): List of dictionaries to be saved
            file_path (str): Path of the file to be saved

        Returns:
            None
        '''
        with open(file_path, "w", encoding='utf-8') as arquivo_json:
            json.dump(list, arquivo_json, ensure_ascii=False, indent=4)
        
        print(f'Dados salvos no caminho: {file_path}')
