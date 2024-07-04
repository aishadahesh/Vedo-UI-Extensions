from vedo import Plotter, Text2D, Rectangle, settings

class TextBox:
    def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.4, 0.1), callback=None):
        self.text = initial_text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
        self.text_actor = Text2D(self.text, pos=self.pos, c='black', bg='white')
        
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
        key = event.keypress.lower() 
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
            pass  
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
        
        if self.callback:
            self.callback(self)

    def update_text(self):
        self.window.remove(self.text_actor)
        self.window.remove(self.rect_actor)
        
        lines = self.text.split('\n')
        max_line_length = max(len(line) for line in lines)
        num_lines = len(lines)

        new_width = max(max_line_length * 0.01, self.size[0])
        new_height = max(num_lines * 0.05, self.size[1])
        self.size = (new_width, new_height)
        
        self.update_rect()
        
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

