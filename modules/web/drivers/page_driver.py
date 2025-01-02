from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functools import singledispatchmethod
from time import sleep


class PageDriver:
    ''' 
    Class responsible for all general web automation actions
    This class serves as a "wrapper" for selenium, making it easier to use its methods
    '''
    def __init__(self):      
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(
            service=Service(executable_path='web_drivers\msedgedriver.exe'),
            options=edge_options
        )

    def _list_pages(self) -> list[str]:
        ''' 
        Returns a list of open tabs in the browser 
        
        Returns:
            list[str]: List of open tabs
        '''
        return self.driver.window_handles
    
    
    def press_enter(self, HTML_element: WebElement) -> None:
        '''
        This method simulates the action of pressing the "Enter" key on an HTML element.
        Very useful for search fields, forms, etc.
        
        Args:
            HTML_element (WebElement): HTML element that will receive the action of pressing the "Enter" key.
            
        Returns:
            None
        '''
        self.driver._web_element_cls.send_keys(HTML_element, Keys.ENTER)
    
    
    def delay(self, time: int) -> None: 
        '''
        Method that makes the program "sleep" for a certain amount of time
        
        Args:
            time (int): Time in seconds that the program will be "sleeping"
        '''
        sleep(time)
    
        
    def switch_to_page(self, page_index: int) -> None:
        ''' 
        Switches the tab to a specific index from the list of tabs, as even if another tab is opened, the "focus" of selenium remains on the previously opened tab 
        
        Args:
            page_index (int): Index of the tab to switch to, starting from 0
        
        Returns:
            None
        '''
        self.driver.switch_to.window(self._list_pages()[page_index])


    def close_driver(self) -> None:
        ''' Close de connection with the driver '''
        self.driver.close()
    
    
    def open_url(self, url: str) -> None:
        ''' 
        Opens a page in the browser with the specified URL
        
        Args:
            url (str): URL of the page to open
            
        Returns:
            None
        '''
        self.driver.get(url)
    
    
    def _get_by(self, by_type: str) -> By:
        ''' 
        Private method of the PageDriver class used to validate the selector type within By 
        
        Args:
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
        
        Returns:
            By: Returns the type of selector to be used, in this case returns a By type from Selenium
        '''
        match by_type:
            case 'CLASS_NAME':
                return By.CLASS_NAME
            case 'NAME':
                return By.NAME
            case 'ID':
                return By.ID
            case 'TAG_NAME':
                return By.TAG_NAME
            case 'XPATH':
                return By.XPATH
            case _:
                raise ValueError('INVALID OPTION') 
        
    
    def wait_for_element(self, HTML_element: str, timeout: int, by_type: str) -> None:
        '''
        Waits for an element to be present on the page, if not, raises an exception
        
        Args:
            HTML_element (str): HTML element to wait for
            timeout (int): Maximum time to wait
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
        
        Returns:
            None
            
        Raises:
            NoSuchElementException: If the element is not found on the page
        '''
        by = self._get_by(by_type)  
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, HTML_element))
        )
        
        
    def wait_for_page(self, page_num: int) -> None:
        '''
        Waits for a new page to be present, according to the number of open tabs
        
        Args:
            page_num (int): Index number of the page to wait for, this number can be obtained through the _list_pages() method
            
        Returns:
            None
        '''
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(page_num)
        )
        
    @singledispatchmethod 
    def find_element(self, HTML_element: str, by_type: str) -> WebElement:
        '''
        Searches for an HTML element on the page and returns the HTML element
        
        Args:
            HTML_element (str): HTML element to search for
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
            
        Returns:
            WebElement: HTML element found on the page
        '''
        by = self._get_by(by_type)
        return self.driver.find_element(by, HTML_element)
    
    
    @find_element.register(WebElement)
    def _(self, HTML_element: WebElement, searched_element: str, by_type: str) -> WebElement:
        '''
        Searches for an HTML element within another HTML element and returns the HTML element.
        However, this is a private method used in the find_element_in_element() method.
        
        Args:
            HTML_element (WebElement): HTML element within which another HTML element is to be searched.
            searched_element (str): HTML element to search for within the HTML_element.
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'.
        
        Returns:
            WebElement: HTML element found within the HTML_element.
        '''
        by = self._get_by(by_type)
        return HTML_element.find_element(by, searched_element)


    @singledispatchmethod
    def find_elements(self, HTML_element: str, by_type) -> list[WebElement]:
        '''
        Searches for an HTML element on the page and returns a list of HTML elements if more than one element exists.
        Example: search for all items in a list
        
        Args:
            HTML_element (str): HTML element to search for
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
        
        Returns:   
            list[WebElement]: List of HTML elements found on the page
        '''
        by = self._get_by(by_type)
        return self.driver.find_elements(by, HTML_element)
    
    
    @find_elements.register(WebElement)
    def _(self, HTML_element: WebElement, searched_element: str, by_type: str) -> list[WebElement]:
        '''
        Searches for HTML elements within another HTML element and returns a list of HTML elements.
        Very useful for searching all items in a list, for example.
        However, this is a private method used in the find_elements_in_element() method.
          
        Args:
            HTML_element (WebElement): HTML element within which another HTML element is to be searched.
            searched_element (str): HTML element to search for within the HTML_element.
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'.
        
        Returns:
            list[WebElement]: List of HTML elements found within the HTML_element.
        '''
        by = self._get_by(by_type)
        return HTML_element.find_elements(by, searched_element)
    
    
    def execute_script(self, script: str, HTML_element: WebElement) -> None:
        '''
        Executes a JavaScript script on an HTML element.
        Very useful for manipulating HTML elements that cannot be manipulated with Selenium methods like .click()
        
        Args:
            script (str): JavaScript script to execute, e.g., 'arguments[0].click();'
            HTML_element (WebElement): HTML element to execute the script on
        
        Returns:
            None
        '''
        self.driver.execute_script(script, HTML_element)
        
        
    def find_element_in_element(self, HTML_element: WebElement, searched_element: str, by_type: str) -> WebElement:
        ''' 
        Search for an HTML element within another HTML element, very useful for searching elements within other HTML elements, such as lists.
        Or when you want to be more precise in searching for an HTML element.
        Example: Return an item from a list
        
        Args:
            HTML_element (WebElement): HTML element to search within
            searched_element (str): HTML element to search for
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
            
        Returns:
            WebElement: HTML element found within the HTML element
        '''
        by_type = self._get_by(by_type)
        return HTML_element.find_element(by_type, searched_element)
    
    
    def find_elements_in_element(self, HTML_element: WebElement, searched_element: str, by_type: str) -> list[WebElement]:
        '''
        Returns a list of HTML elements searched within another HTML element.
        For example, search for all items in a list.
        
        Args:
            HTML_element (WebElement): HTML element to search within
            searched_element (str): HTML elements to search for
            by_type (str): Type of selector to use, 'CLASS_NAME', 'NAME', 'ID', 'TAG_NAME', 'XPATH'
        
        Returns:
            list[WebElement]: List of HTML elements found within the HTML element
        '''
        by_type = self._get_by(by_type)
        
        try:
            return HTML_element.find_elements(by_type, searched_element)
        except Exception as e:
            print(e)


    def pagination(self, next_button: WebElement, page_limit: int, function) -> None:
        '''
        # TODO Method is not working correctly and needs to be improved
        Method that simulates the action of clicking a "next page" button and executes a function passed as a parameter
        
        Args:
            next_button (WebElement): "Next page" button
            page_limit (int): Limit of pages to navigate through
            function: Function to execute at each iteration
        
        Returns:
            None
        '''
        i: int = 0
   
        while i < page_limit:
            self.delay(3)
            function()
            next_button.click()
            i += 1