from __future__ import print_function
import time
from os import system, join
import json
import sys
if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    import uiautomation as auto
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from AppKit import NSWorkspace
    from Foundation import *

class FileSaverCanvas:

    def __init__(self):
        self.active_window_name = ""
        self.activity_name = ""
        self.first_time = True
        self._class = None
        self.param = self.get_param()
        self.path = os.path.join(*self.param["path"])
        self.run()

    def get_active_window(self):
        self.active_window_name = None
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            window = win32gui.GetForegroundWindow()
            self.active_window_name = win32gui.GetWindowText(window)
        elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
            self.active_window_name = (NSWorkspace.sharedWorkspace()
                                .activeApplication()['NSApplicationName'])
        return self.active_window_name

    def get_chrome_url(self):
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            window = win32gui.GetForegroundWindow()
            chromeControl = auto.ControlFromHandle(window)
            edit = chromeControl.EditControl()
            web = edit.GetValuePattern().Value
            if "cursos.canvas" in web:
                code = (web.split("/"))[2]
                self._class = self.param[code]

        elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
            textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
            s = NSAppleScript.initWithSource_(
                NSAppleScript.alloc(), textOfMyScript)
            results, err = s.executeAndReturnError_(None)
            return results.stringValue()

    def run(self)
        try:
            while True:
                previous_site = ""
                new_window_name = get_active_window()
                if 'Google Chrome' in new_window_name:
                    new_window_name = get_chrome_url()

                if self.active_window_name != new_window_name:
                    print(self.active_window_name)
                    self.activity_name = self.active_window_name

                    self.first_time = False
                    self.active_window_name = new_window_name


        except KeyboardInterrupt:
            sys.exit()

    def get_param(self):
        with open("parametros.json") as file:
            self.param = json.load(file)



if __name__ == "__main__":
    file_saver = FileSaverCanvas()
