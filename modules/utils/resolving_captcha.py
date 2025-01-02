from python_anticaptcha import AnticaptchaClient, ImageToTextTask
import base64

class CaptchaSolver:
    ''' Responsible class can break and solve CAPTCHAS  '''
    def __init__(self, api_key : int = ''):
        self._api_key = api_key
        self.client = AnticaptchaClient(self._api_key)
        
    
    def convert_base64_to_image(self, base64_str: str, output_file_path: str) -> None:
        '''
        Converts a base64 string to an image and saves it to the specified path.
        
        Args: 
            base64_str (str): base64 string of the image
            output_file_path (str): path where the image will be saved
        
        Returns: 
            None
        '''
        with open(output_file_path, 'wb') as file:
            file.write(base64.b64decode(base64_str))
        
        
    def image_to_text(self, file_path: str) -> str:
        '''
        Method that solves the CAPTCHA from an image.
        It works by sending the image to the anticaptcha CAPTCHA solving service and returning the CAPTCHA text.
        
        Args:
            file_path (str): path of the image to be solved
            
        Returns:
            str: CAPTCHA text
        '''
        with open(file_path, 'rb') as image:
            task = ImageToTextTask(image)
            job = self.client.createTask(task=task)
            job.join()
               
            return job.get_captcha_text() 
        