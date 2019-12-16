# -*- coding: utf-8 -*-

from app import App

class Launcher:

    
    app_instance = None


    def run(self):
        # Loop - Create app instance
        while(True):
            self.app_instance = App()
            
            # Loop - App process
            while(True):
                try:
                    self.app_instance.process()
                except Exception as exception: 
                    self.app_instance.terminate(exception)


if __name__ == "__main__":
    launcher = Launcher()
    launcher.run()