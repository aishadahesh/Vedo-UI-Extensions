from vedo import Plotter, Text2D, Rectangle, Button, settings

class ComboBox:
    def __init__(self, plotter, options, default_text="Select an option", position=(0, 0)):
        self.plotter = plotter
        self.options = options
        self.default_text = default_text
        self.selected_option = default_text
        self.option_texts = []
        self.option_actors = []
        self.dropdown_visible = False
        self.change_callback = None
        self.position = position

        self.build_combo_box()

    def build_combo_box(self):
        self.label = Text2D(self.selected_option, pos=self.position, c='k', bg='white')
        self.label.pickable()
        self.plotter += self.label

        pos = self.label.GetPosition()
        corner1 = [pos[0] - 0.1, pos[1] - 0.3, 0]
        corner2 = [pos[0] + 0.1, pos[1], 0]
        self.dropdown = Rectangle(corner1, corner2, c="white", alpha=0.6)
        self.dropdown.pickable(False)

        for i, option in enumerate(self.options):
            text_pos = (pos[0], pos[1] - (i + 1) * 0.05)
            text = Text2D(option, pos=text_pos, c='k')
            text.pickable()
            self.option_texts.append(option)
            self.option_actors.append(text)

        self.hide_dropdown()

        self.plotter.add_callback("mouse click", self.on_mouse_click)

    def show_dropdown(self):
        if not self.dropdown_visible:
            self.plotter += self.dropdown
            for actor in self.option_actors:
                self.plotter += actor
            self.dropdown_visible = True

    def hide_dropdown(self):
        if self.dropdown_visible:
            self.plotter.remove(self.dropdown)
            for actor in self.option_actors:
                self.plotter.remove(actor)
            self.dropdown_visible = False

    def on_mouse_click(self, event):
        if event.actor == self.label:
            self.toggle_dropdown()
        elif self.dropdown_visible:
            for actor in self.option_actors:
                if event.actor == actor:
                    self.selected_option = actor.text()
                    self.label.text(self.selected_option)
                    if self.change_callback:
                        self.change_callback(self.selected_option)
                    self.hide_dropdown()
                    break
            else:
                self.hide_dropdown()

    def toggle_dropdown(self):
        if self.dropdown_visible:
            self.hide_dropdown()
        else:
            self.show_dropdown()

    def get_selected_option(self):
        return self.selected_option

    def set_change_callback(self, callback):
        self.change_callback = callback

class TextBox:
    def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.8, 0.6), max_lines=15, max_line_length=80, callback=None):
        self.text = initial_text
        self.pos = pos
        self.size = size
        self.max_lines = max_lines
        self.max_line_length = max_line_length
        self.callback = callback
        self.font = "Glasgo"
        self.color = 'black'
        self.bg_color = 'white'
        self.text_size = 1
        self.align = "left"
        self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
        self.text_actor = Text2D(self.text, pos=self.pos, c=self.color, bg=self.bg_color, font=self.font, s=self.text_size, justify=self.align)
        
        self.update_rect()
        
        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.add_callback("KeyPressEvent", self.on_key_press)

        font_options = ["Antares", "Archistico", "Bongas", "Brachium", "Calco", "Calibri", "Capsmall",
                        "Cartoons123", "Comae", "ComicMono", "Dalim", "DejavuSansMono",
                        "Edo", "FiraMonoBold","FiraMonoMedium", "Glasgo"]
        color_options = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink", "brown"]
        bg_color_options = ["white", "lightgrey", "lightblue", "lightgreen", "lightyellow", "lightpink"]
        size_options = ["1", "2", "3", "4", "5"]
        align_options = ["left", "center", "right"]

        self.combo_box_font = ComboBox(self.window, font_options, default_text="TextFont", position=(0.01, 0.9))
        self.combo_box_font.set_change_callback(self.apply_font_style)

        self.combo_box_color = ComboBox(self.window, color_options, default_text="TextColor", position=(0.11, 0.9))
        self.combo_box_color.set_change_callback(self.apply_text_color)

        self.combo_box_bg_color = ComboBox(self.window, bg_color_options, default_text="BackgroundColor", position=(0.21, 0.9))
        self.combo_box_bg_color.set_change_callback(self.apply_bg_color)

        self.combo_box_size = ComboBox(self.window, size_options, default_text="TextSize", position=(0.37, 0.9))
        self.combo_box_size.set_change_callback(self.apply_text_size)

        self.combo_box_align = ComboBox(self.window, align_options, default_text="TextAlignment", position=(0.47, 0.9))
        self.combo_box_align.set_change_callback(self.apply_text_align)

        save_button = Button(pos=(0.8, 0.9), states=["SaveFile"], c=["w"], bc=["g"], font="Comae")
        self.window += save_button

        self.window.add_callback("mouse click", self.on_save_button_click)

        self.window.show(interactive=True)

    def update_rect(self):
        corner1 = [self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, 0]
        corner2 = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2, 0]
        self.rect_actor = Rectangle(corner1, corner2, c='white', alpha=0.6)
        self.rect_actor.wireframe(False)

    def on_key_press(self, event):
        key = event.keypress.lower()
        lines = self.text.split('\n')
        if key == "backspace":
            if len(lines[-1]) > 0:
                self.text = self.text[:-1]
            elif len(lines) > 1:
                self.text = self.text[:-1]
        elif key == "delete":
            self.text = self.text[:-1]
        elif key == "return":
            if len(lines) < self.max_lines:
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
        new_lines = []
        for line in lines:
            while len(line) > self.max_line_length:
                new_lines.append(line[:self.max_line_length])
                line = line[self.max_line_length:]
            new_lines.append(line)
        lines = new_lines[:self.max_lines]
        self.text = '\n'.join(lines)
        
        max_line_length = min(max(len(line) for line in lines), self.max_line_length)
        num_lines = len(lines)

        new_width = self.size[0]
        new_height = self.size[1]
        
        self.update_rect()
        
        text_pos = (self.pos[0] - new_width/2 + 0.01, self.pos[1] + new_height/2 - 0.05 * num_lines)
        self.text_actor = Text2D(self.text, pos=text_pos, c=self.color, bg=self.bg_color, font=self.font, s=self.text_size, justify=self.align)
        
        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.render()

    def apply_font_style(self, style):
        self.font = style
        self.update_text()

    def apply_text_color(self, color):
        self.color = color
        self.update_text()

    def apply_bg_color(self, color):
        self.bg_color = color
        self.update_text()

    def apply_text_size(self, size):
        self.text_size = int(size)
        self.update_text()

    def apply_text_align(self, align):
        self.align = align
        self.update_text()

    def on_save_button_click(self, event):
        if isinstance(event.actor, Button) and event.actor.states[0] == "SaveFile":
            self.save_text()

    def save_text(self):
        with open("output.txt", "w") as file:
            file.write(self.text)
        print("Text saved to output.txt")


def user_callback(text_box):
    if "exit\n" in text_box.text:
        text_box.window.close()


settings.enable_default_keyboard_callbacks = False
text_box = TextBox(callback=user_callback)


