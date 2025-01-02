import pyautogui

class GUIDriver:
    ''' Class responsible for concerns regarding desktop automation (GUI) '''
    def __init__(self, actions_intervarl=0.5):
        self._interval = actions_intervarl
        pyautogui.PAUSE = self._interval
    
        
    @property
    def action_interval(self) -> float:
        return self._interval
    
    
    @action_interval.setter
    def action_interval(self, new_interval: float) -> None:
        self._interval = new_interval


    def press_key(self, keyboard_key:str) -> None:
        pyautogui.press(keyboard_key)
    
    
    def mouse_click(self) -> None:
        pyautogui.click(button='left')
