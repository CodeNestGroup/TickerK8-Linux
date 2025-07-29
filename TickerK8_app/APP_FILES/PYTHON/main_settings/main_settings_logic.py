class controller_settings:
    def __init__(self):
        self.opened_sub_widget = None
    def open_sub_widget(self, to_open):
        if self.opened_sub_widget: # Check if opened widget is not none
            self.opened_sub_widget.setHidden(True) # Hide opened widget
        to_open.setHidden(False) # Show Widget
        self.opened_sub_widget = to_open # Save opened widget
#######################################################################################################################