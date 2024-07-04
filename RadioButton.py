from vedo import Plotter, Circle, Text3D, Assembly

class RadioButton:
    def __init__(self, plotter, labels, ndc_position, callback):
        self.plotter = plotter
        self.labels = labels
        self.ndc_position = ndc_position
        self.active_index = -1
        self.buttons = []
        self.callback = callback  
        self.create_buttons()

    def create_buttons(self):
        for i, label in enumerate(self.labels):
            ndc_y_pos = self.ndc_position[1] - i * 0.3 

            circle = Circle(pos=(self.ndc_position[0], ndc_y_pos, 0), r=0.1, c='black', res=50)
            circle._index = i
            
            text = Text3D(label, pos=(self.ndc_position[0] + 0.2, ndc_y_pos - 0.15, 0), s=0.2, c='black')

            combined = Assembly([circle, text])
            combined._index = i
            self.buttons.append(combined)
            self.plotter.add(combined)

        self.plotter.add_callback("LeftButtonPressEvent", self.on_click)

    def on_click(self, event):
        clicked_button = event.actor
        if hasattr(clicked_button, '_index'):
            index = clicked_button._index
            self.set_active(index)
            self.perform_action(index)

    def set_active(self, index):
        if self.active_index != -1:
            self.buttons[self.active_index].actors[0].GetProperty().SetColor(0, 0, 0)  
        self.active_index = index
        self.buttons[index].actors[0].GetProperty().SetColor(0, 0, 1) 

    def perform_action(self, index):
        self.callback(index)  



############################ADD YOUR CODE HERE##################################
# Define user callback function for all options
def user_callback(index):
    if index == 0:
        # Option 1 selected
        # ADD YOUR CODE HERE
        print("Option 1 selected")
    elif index == 1:
        # Option 2 selected
        # ADD YOUR CODE HERE
        print("Option 2 selected")
    elif index == 2:
        # Option 3 selected
        # ADD YOUR CODE HERE
        print("Option 3 selected")

# Initialize the Plotter
plotter = Plotter(size=(800, 800))

############################ADD YOUR CODE HERE##################################
# YOU CAN PLOT YOUR OBJECT HERE! 
# YOU CAN USE 'user_callback' FUNCTION TO IMPLEMENT YOUR CODE AS YOU WANT AND DESCRIBED ON THE OPTIONS YOU CHOOSE
################################################################################

labels = ["Option 1", "Option 2", "Option 3"]
ndc_position = (3,3)  
radio_buttons = RadioButton(plotter, labels, ndc_position, user_callback)

plotter.show(interactive=True)
