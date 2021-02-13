from __future__ import annotations
from abc import ABC, abstractmethod

class Sound:
    def __init__(self):
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0
        
    def change_mode(self, mode: PlayMode):
        self.playing = 0
        self.mode = mode
    
    def press_next(self):
        self.mode.press_next()
        print(self)
        
    def press_prev(self):
        self.mode.press_prev()
        print(self)
        
    def __str__(self):
        return str(self.playing)
                
class PlayMode(ABC):
    def __init__(self, sound: Sound):
        self.sound = sound

    @abstractmethod
    def press_next(self): pass
    
    @abstractmethod
    def press_prev(self):pass

class RadioMode(PlayMode):
    def press_next(self): 
        self.sound.playing += 1

    def press_prev(self):
        if not self.sound.playing > 0:
            return
        self.sound.playing -= 1

class MusicMode(PlayMode):
    def press_next(self): 
        self.sound.playing += 10

    def press_prev(self):
        if not self.sound.playing > 0:
            return
        self.sound.playing -= 10
        
if __name__ == "__main__":
    sound = Sound()
    sound.press_next()