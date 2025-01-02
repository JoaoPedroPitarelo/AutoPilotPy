from modules.web.paginable import Paginable


class GoogleSearch(Paginable):
    ''' Class with the methods of automating a google search '''
    def __init__(self, page_driver):
        super().__init__(page_driver)
        

    def open_google(self) -> 'Paginable':
        self.page_driver.open_url('https://www.google.com')
        return self
        

    def search(self, search: str) -> 'Paginable':
        self.page_driver.wait_for_element('gLFyf', 10, 'CLASS_NAME')
        search_input = self.page_driver.find_element('gLFyf', 'CLASS_NAME')
        search_input.send_keys(search)
        self.page_driver.delay(1)

        self.page_driver.press_enter(search_input)         
        return self
        