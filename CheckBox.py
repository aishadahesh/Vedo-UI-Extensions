################################## Check-Box ##################################

from vedo import Plotter, Circle, Text3D, Assembly

class CheckBox:
    def __init__(self, plotter, labels, ndc_position, callback):
        self.plotter = plotter
        self.labels = labels
        self.ndc_position = ndc_position
        self.active_indices = set()  
        self.buttons = []
        self.callback = callback 
        self.create_buttons()
        self.plotter.add_callback("LeftButtonPressEvent", self.on_click)

    def create_buttons(self):
        for button in self.buttons:
            self.plotter.remove(button)
        self.buttons.clear()

        selected_indices = [i for i in self.active_indices]
        unselected_indices = [i for i in range(len(self.labels)) if i not in self.active_indices]

        all_indices = unselected_indices + selected_indices
        for i, index in enumerate(all_indices):
            ndc_y_pos = self.ndc_position[1] - i * 0.3  

            circle = Circle(pos=(self.ndc_position[0], ndc_y_pos, 0), r=0.1, c='black' if index in unselected_indices else 'blue', res=50)
            circle._index = index
            
            text = Text3D(self.labels[index], pos=(self.ndc_position[0] + 0.2, ndc_y_pos - 0.15, 0), s=0.2, c='black')

            combined = Assembly([circle, text])
            combined._index = index
            self.buttons.append(combined)
            self.plotter.add(combined)

    def on_click(self, event):
        clicked_button = event.actor
        if hasattr(clicked_button, '_index'):
            index = clicked_button._index
            self.toggle_active(index)
            self.perform_action(index)
            self.create_buttons()  

    def toggle_active(self, index):
        if index in self.active_indices:
            self.active_indices.remove(index)
        else:
            self.active_indices.add(index)

    def perform_action(self, index):
        self.callback(index, index in self.active_indices) 

############################ADD YOUR CODE HERE##################################
# Define user callback function for all options
def user_callback(index, is_selected):
    if is_selected:
        print(f"Option {index + 1} selected")
        # ADD YOUR CODE HERE TO IMPLEMENT THE ACTION FOR THE SELECTED OPTION
    else:
        print(f"Option {index + 1} unselected")
        # ADD YOUR CODE HERE TO IMPLEMENT THE ACTION FOR THE UNSELECTED OPTION

# Initialize the Plotter
plotter = Plotter(size=(800, 800))

############################ADD YOUR CODE HERE##################################
# YOU CAN PLOT YOUR OBJECT HERE! 
# YOU CAN USE 'user_callback' FUNCTION TO IMPLEMENT YOUR CODE AS YOU WANT AND DESCRIBED ON THE OPTIONS YOU CHOOSE
################################################################################


labels = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
ndc_position = (0.85, 0.9)
check_boxes = CheckBox(plotter, labels, ndc_position, user_callback)

plotter.show(interactive=True)
