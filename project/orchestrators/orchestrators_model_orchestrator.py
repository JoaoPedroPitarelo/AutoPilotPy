from modules.web.drivers.page_driver import PageDriver
from modules.gui.drivers.gui_driver import GUIDriver

from project.pages.pages_example.google_search_page import GoogleSearch

class OrchestratorExample:

    @staticmethod
    def run() -> None:
      
        # Drivers Or managers
        page_driver = PageDriver()
        gui_driver = GUIDriver()

        # Automated pages
        google_search = GoogleSearch(page_driver)
    
        # Automation flow
        google_search\
            .open_google()\
            .search('João Pedro Salmazo Pitarelo GitHub')
        
       