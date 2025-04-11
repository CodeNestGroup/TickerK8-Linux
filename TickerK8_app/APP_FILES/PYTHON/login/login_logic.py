""" Import json """
import json
#______________________________________________________________________________________________________________________
""" Import login ui """
from .login_ui import login_reload_style
#######################################################################################################################
""" Change day night """
def change_day_night(self):
    global_config = self.global_config # Set variable global theme
    theme = global_config['__theme__'] # Set variable theme
    if theme[-4:] == 'dark': # Check if dark theme 
        global_config['__theme__'] = str(theme[:-4])+'light' # Change to light theme 
    else:
        global_config['__theme__'] = str(theme[:-5])+'dark' # Change to dark theme 
    json.dump(global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=2) # Save changes 
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Reload config file
    login_reload_style(self) # Reload style 
#______________________________________________________________________________________________________________________

