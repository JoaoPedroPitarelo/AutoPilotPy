from modules.web.drivers.page_driver import PageDriver

class Paginable:
    ''' "Abstract" class, which would only serve to be inherited for generalization '''
    def __init__(self, page_driver: PageDriver, pagination_limit=0):
        self.page_driver = page_driver
        self.driver = self.page_driver.driver  
        self.pagination_limit = pagination_limit
        