# # ################################## Text-Box ##################################

# # from vedo import Plotter, Text2D, Rectangle, settings

# # class TextBox:
# #     def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.4, 0.1), callback=None):
# #         self.text = initial_text
# #         self.pos = pos
# #         self.size = size
# #         self.callback = callback
# #         self.text_actor = Text2D(self.text, pos=self.pos, c='black', bg='white')
        
# #         # Create rectangle using corner points
# #         self.update_rect()
        
# #         self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
# #         self.window += self.rect_actor
# #         self.window += self.text_actor
# #         self.window.add_callback("KeyPressEvent", self.on_key_press)
# #         self.window.show(interactive=True)

# #     def update_rect(self):
# #         corner1 = [self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, 0]
# #         corner2 = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2, 0]
# #         self.rect_actor = Rectangle(corner1, corner2, c='black', alpha=0.6)
# #         self.rect_actor.wireframe(False)

# #     def on_key_press(self, event):
# #         key = event.keypress.lower()  # Convert to lower case to handle case insensitivity
# #         if key == "backspace":
# #             self.text = self.text[:-1]
# #         elif key == "delete":
# #             self.text = self.text[:-1]
# #         elif key == "return":
# #             if self.callback:
# #                 self.callback(self.text)
# #         elif key == "space":
# #             self.text += " "
# #         elif key == "tab":
# #             self.text += "\t"
# #         elif key in ["shift_l", "shift_r", "control_l", "control_r", "alt_l", "alt_r", "escape"]:
# #             pass  # Ignore control keys
# #         else:
# #             special_keys = {
# #                 "question": "?", "exclam": "!", "at": "@", "numbersign": "#", "dollar": "$",
# #                 "percent": "%", "asciicircum": "^", "ampersand": "&", "asterisk": "*",
# #                 "parenleft": "(", "parenright": ")", "underscore": "_", "plus": "+",
# #                 "bracketleft": "[", "bracketright": "]", "braceleft": "{", "braceright": "}",
# #                 "colon": ":", "semicolon": ";", "apostrophe": "'", "quotedbl": '"',
# #                 "less": "<", "greater": ">", "comma": ",", "period": ".", "slash": "/",
# #                 "backslash": "\\", "tilde": "~", "grave": "`", "minus": "-", "equal": "=",
# #                 "quoteleft": "`", "quoteright": "'", "asciitilde": "~", "bar": "|"
# #             }
# #             self.text += special_keys.get(key, key)
# #         self.update_text()

# #     def update_text(self):
# #         self.window.remove(self.text_actor)
# #         self.window.remove(self.rect_actor)
        
# #         # Calculate the new position to keep the text centered
# #         text_length = len(self.text)
# #         text_pos = (self.pos[0] - text_length * 0.005, self.pos[1])

# #         # Update rectangle size if text length exceeds current box size
# #         if text_length * 0.01 > self.size[0] / 2:
# #             self.size = (text_length * 0.02, self.size[1])
        
# #         self.update_rect()
        
# #         self.text_actor = Text2D(self.text, pos=text_pos, c='black', bg='white')
        
# #         self.window += self.rect_actor
# #         self.window += self.text_actor
# #         self.window.render()

# # # Define a user callback function
# # def user_callback(text):
# #     print(f"User typed: {text}")
# #     # Add custom actions based on the text input
# #     if text == "hello":
# #         print("Hello to you too!")
# #     elif text == "exit":
# #         print("BYE!!!")

# # # Usage
# # settings.enable_default_keyboard_callbacks = False
# # text_box = TextBox(callback=user_callback)


# ################################## Text-Box ##################################
# #########
# ############### handling enter ###########################


# ###### NOTE: ctrl+z is not working in this code, its written as txt
# from vedo import Plotter, Text2D, Rectangle, settings

# class TextBox:
#     def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.4, 0.1), callback=None):
#         self.text = initial_text
#         self.pos = pos
#         self.size = size
#         self.callback = callback
#         self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
#         self.text_actor = Text2D(self.text, pos=self.pos, c='black', bg='white')
        
#         # Create rectangle using corner points
#         self.update_rect()
        
#         self.window += self.rect_actor
#         self.window += self.text_actor
#         self.window.add_callback("KeyPressEvent", self.on_key_press)
#         self.window.show(interactive=True)

#     def update_rect(self):
#         corner1 = [self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, 0]
#         corner2 = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2, 0]
#         self.rect_actor = Rectangle(corner1, corner2, c='black', alpha=0.6)
#         self.rect_actor.wireframe(False)

#     def on_key_press(self, event):
#         key = event.keypress.lower()  # Convert to lower case to handle case insensitivity
#         if key == "backspace":
#             self.text = self.text[:-1]
#         elif key == "delete":
#             self.text = self.text[:-1]
#         elif key == "return":
#             self.text += "\n"
#         elif key == "space":
#             self.text += " "
#         elif key == "tab":
#             self.text += "\t"
#         elif key in ["shift_l", "shift_r", "control_l", "control_r", "alt_l", "alt_r", "escape"]:
#             pass  # Ignore control keys
#         else:
#             special_keys = {
#                 "question": "?", "exclam": "!", "at": "@", "numbersign": "#", "dollar": "$",
#                 "percent": "%", "asciicircum": "^", "ampersand": "&", "asterisk": "*",
#                 "parenleft": "(", "parenright": ")", "underscore": "_", "plus": "+",
#                 "bracketleft": "[", "bracketright": "]", "braceleft": "{", "braceright": "}",
#                 "colon": ":", "semicolon": ";", "apostrophe": "'", "quotedbl": '"',
#                 "less": "<", "greater": ">", "comma": ",", "period": ".", "slash": "/",
#                 "backslash": "\\", "tilde": "~", "grave": "`", "minus": "-", "equal": "=",
#                 "quoteleft": "`", "quoteright": "'", "asciitilde": "~", "bar": "|"
#             }
#             self.text += special_keys.get(key, key)
#         self.update_text()

#     def update_text(self):
#         self.window.remove(self.text_actor)
#         self.window.remove(self.rect_actor)
        
#         # Split text into lines
#         lines = self.text.split('\n')
#         max_line_length = max(len(line) for line in lines)
#         num_lines = len(lines)

#         # Update rectangle size if text length or number of lines exceeds current box size
#         new_width = max(max_line_length * 0.01, self.size[0])
#         new_height = max(num_lines * 0.05, self.size[1])
#         self.size = (new_width, new_height)
        
#         self.update_rect()
        
#         # Calculate the new position to keep the text centered
#         text_pos = (self.pos[0] - max_line_length * 0.005, self.pos[1] + (num_lines - 1) * 0.025)
#         self.text_actor = Text2D(self.text, pos=text_pos, c='black', bg='white')
        
#         self.window += self.rect_actor
#         self.window += self.text_actor
#         self.window.render()

# # Define a user callback function
# def user_callback(text_box):
#     #### ADD YOUR CODE HERE ####
#     # CHECK THE TEXT BOX CONTENTS
#     return

# # Usage
# settings.enable_default_keyboard_callbacks = False
# text_box = TextBox(callback=user_callback)


from vedo import Plotter, Text2D, Rectangle, settings

class TextBox:
    def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.4, 0.1), callback=None):
        self.text = initial_text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
        self.text_actor = Text2D(self.text, pos=self.pos, c='black', bg='white')
        
        # Create rectangle using corner points
        self.update_rect()
        
        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.add_callback("KeyPressEvent", self.on_key_press)
        self.window.show(interactive=True)

    def update_rect(self):
        corner1 = [self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, 0]
        corner2 = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2, 0]
        self.rect_actor = Rectangle(corner1, corner2, c='black', alpha=0.6)
        self.rect_actor.wireframe(False)

    def on_key_press(self, event):
        key = event.keypress.lower()  # Convert to lower case to handle case insensitivity
        if key == "backspace":
            self.text = self.text[:-1]
        elif key == "delete":
            self.text = self.text[:-1]
        elif key == "return":
            self.text += "\n"
        elif key == "space":
            self.text += " "
        elif key == "tab":
            self.text += "\t"
        elif key in ["shift_l", "shift_r", "control_l", "control_r", "alt_l", "alt_r", "escape"]:
            pass  # Ignore control keys
        else:
            special_keys = {
                "question": "?", "exclam": "!", "at": "@", "numbersign": "#", "dollar": "$",
                "percent": "%", "asciicircum": "^", "ampersand": "&", "asterisk": "*",
                "parenleft": "(", "parenright": ")", "underscore": "_", "plus": "+",
                "bracketleft": "[", "bracketright": "]", "braceleft": "{", "braceright": "}",
                "colon": ":", "semicolon": ";", "apostrophe": "'", "quotedbl": '"',
                "less": "<", "greater": ">", "comma": ",", "period": ".", "slash": "/",
                "backslash": "\\", "tilde": "~", "grave": "`", "minus": "-", "equal": "=",
                "quoteleft": "`", "quoteright": "'", "asciitilde": "~", "bar": "|"
            }
            self.text += special_keys.get(key, key)
        self.update_text()
        
        # Call the user-defined callback function
        if self.callback:
            self.callback(self)

    def update_text(self):
        self.window.remove(self.text_actor)
        self.window.remove(self.rect_actor)
        
        # Split text into lines
        lines = self.text.split('\n')
        max_line_length = max(len(line) for line in lines)
        num_lines = len(lines)

        # Update rectangle size if text length or number of lines exceeds current box size
        new_width = max(max_line_length * 0.01, self.size[0])
        new_height = max(num_lines * 0.05, self.size[1])
        self.size = (new_width, new_height)
        
        self.update_rect()
        
        # Calculate the new position to keep the text centered
        text_pos = (self.pos[0] - max_line_length * 0.005, self.pos[1] + (num_lines - 1) * 0.025)
        self.text_actor = Text2D(self.text, pos=text_pos, c='black', bg='white')
        
        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.render()

# Define a user callback function
def user_callback(text_box):
    if "exit\n" in text_box.text:
        text_box.window.close()

# Usage
settings.enable_default_keyboard_callbacks = False
text_box = TextBox(callback=user_callback)








############################################################################



# ##########################################################################################
# ################################CODE NO.1#################################################
# ## BASE CODE:
# from vedo import Plotter, Circle, Text3D, Assembly

# class RadioButton:
#     def __init__(self, plotter, labels, position):
#         self.plotter = plotter
#         self.labels = labels
#         self.position = position
#         self.active_index = -1
#         self.buttons = []
#         self.create_buttons()

#     def create_buttons(self):
#         for i, label in enumerate(self.labels):
#             y_pos = self.position[1] - i * 0.1

#             # Create the circle
#             circle = Circle(pos=(self.position[0], y_pos), r=0.02, c='black', res=50)
#             circle._index = i
            
#             # Create the 3D text
#             text = Text3D(label, pos=(self.position[0] + 0.05, y_pos, 0), s=0.03, c='black')

#             # Combine the circle and text into an assembly
#             combined = Assembly([circle, text])
#             combined._index = i
#             self.buttons.append(combined)
#             self.plotter.add(combined)

#         self.plotter.add_callback("LeftButtonPressEvent", self.on_click)

#     def on_click(self, event):
#         clicked_button = event.actor
#         if hasattr(clicked_button, '_index'):
#             index = clicked_button._index
#             self.set_active(index)

#     def set_active(self, index):
#         if self.active_index != -1:
#             self.buttons[self.active_index].actors[0].GetProperty().SetColor(0, 0, 0)  # Change circle color back to black
#         self.active_index = index
#         self.buttons[index].actors[0].GetProperty().SetColor(0, 0, 1)  # Change circle color to blue

# # Initialize the Plotter
# plotter = Plotter(size=(800, 800))

# # Create radio buttons
# labels = ["Option 1", "Option 2", "Option 3", "option 4"]
# radio_buttons = RadioButton(plotter, labels, position=(0.3, 0.6))

# # Show the plotter window
# plotter.show(interactive=True)

########################################################################################
##############################CODE NO.2#################################################
## EXAMPLE OF USE:

from vedo import Plotter, Circle, Text3D, Assembly, Mesh, dataurl

class RadioButton:
    def __init__(self, plotter, labels, ndc_position, flower):
        self.plotter = plotter
        self.labels = labels
        self.ndc_position = ndc_position
        self.active_index = -1
        self.buttons = []
        self.flower = flower
        self.create_buttons()

    def create_buttons(self):
        for i, label in enumerate(self.labels):
            ndc_y_pos = self.ndc_position[1] - i * 0.3  # Increased vertical spacing

            # Create the circle
            circle = Circle(pos=(self.ndc_position[0], ndc_y_pos, 0), r=0.1, c='black', res=50)
            circle._index = i
            
            # Create the 3D text
            text = Text3D(label, pos=(self.ndc_position[0] + 0.2, ndc_y_pos, 0), s=0.2, c='black')

            # Combine the circle and text into an assembly
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
            self.buttons[self.active_index].actors[0].GetProperty().SetColor(0, 0, 0)  # Change circle color back to black
        self.active_index = index
        self.buttons[index].actors[0].GetProperty().SetColor(0, 0, 1)  # Change circle color to blue

    def perform_action(self, index):
        if index == 0:
            self.flower.color('red').on()  # Change flower color to red
        elif index == 1:
            self.flower.off()  # Hide flower
        elif index == 2:
            self.flower.color('pink').on()  # Show flower with pink color

# Initialize the Plotter
plotter = Plotter(size=(800, 800))

# Load the flower model
flower = Mesh(dataurl+"magnolia.vtk").color("pink").flat()

# Add the flower to the plotter
plotter.add(flower)

# Create radio buttons and position them in the top-right corner using NDC
labels = ["Option 1: Red Flower", "Option 2: Hide Flower", "Option 3: Show Flower"]
ndc_position = (3,3)  # Normalized device coordinates for the top-right corner
radio_buttons = RadioButton(plotter, labels, ndc_position, flower)

# Show the plotter window
plotter.show(interactive=True)


# ##########################################################################################
# ################################CODE NO.3#################################################
# ## GENERAL CODE

# from vedo import Plotter, Circle, Text3D, Assembly

# class RadioButton:
#     def __init__(self, plotter, labels, ndc_position, callback):
#         self.plotter = plotter
#         self.labels = labels
#         self.ndc_position = ndc_position
#         self.active_index = -1
#         self.buttons = []
#         self.callback = callback  # Store the callback for user-defined actions
#         self.create_buttons()

#     def create_buttons(self):
#         for i, label in enumerate(self.labels):
#             ndc_y_pos = self.ndc_position[1] - i * 0.3  # Increased vertical spacing

#             # Create the circle
#             circle = Circle(pos=(self.ndc_position[0], ndc_y_pos, 0), r=0.1, c='black', res=50)
#             circle._index = i
            
#             # Create the 3D text
#             text = Text3D(label, pos=(self.ndc_position[0] + 0.2, ndc_y_pos - 0.15, 0), s=0.2, c='black')

#             # Combine the circle and text into an assembly
#             combined = Assembly([circle, text])
#             combined._index = i
#             self.buttons.append(combined)
#             self.plotter.add(combined)

#         self.plotter.add_callback("LeftButtonPressEvent", self.on_click)

#     def on_click(self, event):
#         clicked_button = event.actor
#         if hasattr(clicked_button, '_index'):
#             index = clicked_button._index
#             self.set_active(index)
#             self.perform_action(index)

#     def set_active(self, index):
#         if self.active_index != -1:
#             self.buttons[self.active_index].actors[0].GetProperty().SetColor(0, 0, 0)  # Change circle color back to black
#         self.active_index = index
#         self.buttons[index].actors[0].GetProperty().SetColor(0, 0, 1)  # Change circle color to blue

#     def perform_action(self, index):
#         self.callback(index)  # Call the user-defined callback with the selected option index

# ############################ADD YOUR CODE HERE##################################
# # Define user callback function for all options
# def user_callback(index):
#     if index == 0:
#         # Option 1 selected
#         # ADD YOUR CODE HERE
#         print("Option 1 selected")
#     elif index == 1:
#         # Option 2 selected
#         # ADD YOUR CODE HERE
#         print("Option 2 selected")
#     elif index == 2:
#         # Option 3 selected
#         # ADD YOUR CODE HERE
#         print("Option 3 selected")

# # Initialize the Plotter
# plotter = Plotter(size=(800, 800))

# ############################ADD YOUR CODE HERE##################################
# # YOU CAN PLOT YOUR OBJECT HERE! 
# # YOU CAN USE 'user_callback' FUNCTION TO IMPLEMENT YOUR CODE AS YOU WANT AND DESCRIBED ON THE OPTIONS YOU CHOOSE
# ################################################################################

# # Create radio buttons and position them in the top-right corner using NDC
# labels = ["Option 1", "Option 2", "Option 3"]
# ndc_position = (3,3)  # Normalized device coordinates for the top-right corner
# radio_buttons = RadioButton(plotter, labels, ndc_position, user_callback)

# # Show the plotter window
# plotter.show(interactive=True)


## file picker
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class FilePickerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Picker App')
        self.setGeometry(300, 300, 600, 400)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create layout
        layout = QVBoxLayout()

        # Create buttons
        self.pickFileButton = QPushButton('Pick File', self)
        self.pickFileButton.clicked.connect(self.openFileDialog)
        layout.addWidget(self.pickFileButton)

        self.fileDisplayLabel = QLabel('No file selected.', self)
        layout.addWidget(self.fileDisplayLabel)

        centralWidget.setLayout(layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt);;Images (*.png *.xpm *.jpg)", options=options)
        if fileName:
            if fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.xpm')):
                self.displayImage(fileName)
            elif fileName.lower().endswith('.txt'):
                self.displayTextFile(fileName)

    def displayImage(self, filePath):
        pixmap = QPixmap(filePath)
        self.fileDisplayLabel.setPixmap(pixmap)
        self.fileDisplayLabel.setScaledContents(True)
        self.fileDisplayLabel.resize(pixmap.width(), pixmap.height())

    def displayTextFile(self, filePath):
        with open(filePath, 'r') as file:
            text = file.read()
        self.fileDisplayLabel.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filePickerApp = FilePickerApp()
    filePickerApp.show()
    sys.exit(app.exec_())






### text editor
from vedo import settings, Text2D
settings["enable_default_keyboard_callbacks"] = False

def create_textbox(word_functions, plt):
    def kfunc(evt):
        field.frame("red", lw=8)  # Set frame color here

        key = evt.keypress.lower()
        field_txt = field.text().strip()  # strip leading/trailing spaces

        if key == "backspace" and field_txt:
            key = ""
            field_txt = field_txt[:-1]
        elif key == "escape":
            plt.close()
            return
        elif len(key) > 1:
            return

        show = field_txt + key
        field.text(f"{show}").frame("green", lw=7)
        for word in word_functions:
            if show == word:
                word_function = word_functions[word]
                word_function()
                msg.text(show)
        plt.render()

    settings["enable_default_keyboard_callbacks"] = False

    msg = Text2D(pos=(0.1, 0.4), s=2, font="Quikhand", c="green", bg="red", alpha=1)
    ## Combo-box:'font': "Quikhand" , "Arial", "Times New Roman", "Courier New", "Verdana"
    ## button for 'chnage color of text'. when it's clicked the color picker gonna apear same for color of background
    ## extra parameters that we can control:
    # Size (s): This parameter (s=2 in your example) likely sets the size or scale of the text.
    # Position (pos): Specifies the position of the text in the 2D space, often defined as a tuple (x, y) where x and y are coordinates relative to the screen or canvas.
    # Alignment (align): Controls how the text is aligned relative to its position (left, center, right).
    # Rotation (angle): Allows you to rotate the text around its position.
    # Font Weight (weight): Specifies the thickness or boldness of the text.
    # Outline (outline): Adds an outline around the text for better visibility.
    # Shadow (shadow): Adds a shadow effect behind the text.

    msg.text("start:")

    field = Text2D("Please write here", pos="bottom-middle", s=3, font="Glasgo", bg="red", c="black", alpha=1)

    plt.add_callback("key press", kfunc)

    return kfunc, msg, field


from text_implemnt import create_textbox
from vedo import  dataurl, Plotter, Mesh

#Load your object here
mesh = Mesh(dataurl + "magnolia.vtk").c("violet").flat()
def func1():
    print("option1")
word_functions = {

    "option1": func1

  }

plt = Plotter()
kfunc, msg, field = create_textbox(word_functions, plt)
plt.show(mesh, msg, field)