from vedo import Plotter, Text2D, Rectangle, Button, settings
import os

class ComboBox:
    def __init__(self, plotter, options, color='green', default_text="Select an option", position=(0, 0)):
        self.plotter = plotter
        self.color = color
        self.color_options = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink", "brown"]
        self.bg_color_options = ["white", "lightgrey", "lightblue", "lightgreen", "lightyellow", "lightpink"]

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
        self.label = Text2D(self.selected_option, pos=self.position, c='k', bg=self.color)
        self.label.pickable()
        self.plotter += self.label

        pos = self.label.GetPosition()
        corner1 = [pos[0] - 0.1, pos[1] - 0.3, 0]
        corner2 = [pos[0] + 0.1, pos[1], 0]
        self.dropdown = Rectangle(corner1, corner2, c="white", alpha=0.6)
        self.dropdown.pickable(False)

        for i, option in enumerate(self.options):
            curr_color='black'
            curr_bg='white'
            if(option in self.color_options):
                curr_color=option
            elif(option in self.bg_color_options):
                curr_bg=option
            text_pos = (pos[0], pos[1] - (i + 1) * 0.05)
            text = Text2D(option, pos=text_pos, c=curr_color,bg=curr_bg)
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

    def set_color(self, color):
        self.color = color
        self.label.background(self.color)
        print(f"ComboBox color set to {self.color}")

    def set_label_color(self, color):
        self.label.color(color)
        print(f"ComboBox label color set to {color}")
class TextBox:
    def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.8, 0.6), callback=None):
        self.text = initial_text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.font = "Glasgo"
        self.color = 'black'
        self.bg_color = 'white'
        self.text_size = 1
        self.file = 'output'
        self.uppercase = False
        self.undo_stack = []
        self.redo_stack = []
        self.window = Plotter(size=(800, 600), title="Text Box Example", interactive=True)
        self.text_actor = Text2D(self.text, pos=self.pos, c=self.color, bg=self.bg_color, font=self.font,
                                 s=self.text_size, justify='left')

        self.update_rect()
        self.window += Text2D('   ', bg='lightgrey', c='green', s=31, pos=(0.1, 0.8))
        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.add_callback("KeyPressEvent", self.on_key_press)
        self.Text_of_color=""
        self.setup_comboboxes()
        self.setup_buttons()

        self.window.show(interactive=True)

    def setup_comboboxes(self):
        font_options = ["Antares", "Archistico", "Bongas", "Brachium", "Calco", "Calibri", "Capsmall",
                        "Cartoons123", "Comae", "ComicMono", "Dalim", "DejavuSansMono",
                        "Edo", "FiraMonoBold", "FiraMonoMedium", "Glasgo"]
        color_options = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink", "brown"]
        bg_color_options = ["white", "lightgrey", "lightblue", "lightgreen", "lightyellow", "lightpink"]
        size_options = ["1", "2", "3", "4", "5"]
        file_options = ["output1", "output2", "output3"]

        self.combo_box_font = ComboBox(self.window, font_options, color='lightgrey', default_text="Font",
                                       position=(0.01, 0.95))
        self.combo_box_font.set_change_callback(self.apply_font_style)

        self.combo_box_color = ComboBox(self.window, color_options, color='lightgrey', default_text="Color",
                                        position=(0.11, 0.95))

        self.combo_box_color.set_change_callback(self.apply_text_color)

        self.combo_box_bg_color = ComboBox(self.window, bg_color_options, color='lightgrey',
                                           default_text="BackgroundColor", position=(0.21, 0.95))
        self.combo_box_bg_color.set_change_callback(self.apply_bg_color)

        self.combo_box_size = ComboBox(self.window, size_options, color='lightgrey', default_text="TextSize",
                                       position=(0.37, 0.90))
        self.combo_box_size.set_change_callback(self.apply_text_size)

        self.combo_box_file = ComboBox(self.window, file_options, color='white', default_text="Save File As:",
                                       position=(0.65, 0.99))
        self.combo_box_file.set_change_callback(self.apply_text_file)

    def setup_buttons(self):
        save_button = Button(pos=(0.82, 0.99), states=["SaveFile"], c=["green"], bc=["white"], font="Comae")
        self.window += save_button

        delete_button = Button(pos=(0.93, 0.99), states=["DeleteFile"], c=["red"], bc=["white"], font="Comae")
        self.window += delete_button

        increase_size_button = Button(pos=(0.39, 0.96), states=["A"], c=["black"], bc=[(1, 1, 1)], font="Comae")
        self.window += increase_size_button

        decrease_size_button = Button(pos=(0.41, 0.96), size=15, states=["A "], c=["black"], bc=[(1, 1, 1)],
                                      font="Comae")
        self.window += decrease_size_button

        self.toggle_case_button = Button(pos=(0.53, 0.95), states=["CapsLk: OFF", "CapsLk: ON"], c=["black"],
                                         bc=["lightgrey"], font="Comae", size=20)
        self.window += self.toggle_case_button

        self.undo_button = Button(pos=(0.95, 0.90), states=["←"], c=["purple"], bc=["white"], font="Comae", size=20)
        self.window += self.undo_button

        self.redo_button = Button(pos=(0.9, 0.90), states=["→"], c=["blue"], bc=["white"], font="Comae", size=20)
        self.window += self.redo_button

        self.window.add_callback("mouse click", self.on_save_button_click)
        self.window.add_callback("mouse click", self.on_toggle_case_button_click)
        self.window.add_callback("mouse click", self.on_undo_button_click)
        self.window.add_callback("mouse click", self.on_redo_button_click)

    def save_state(self):
        state = {
            'text': self.text,
            'font': self.font,
            'color': self.color,
            'bg_color': self.bg_color,
            'text_size': self.text_size
        }
        self.undo_stack.append(state)

    def load_state(self, state):
        self.text = state['text']
        self.font = state['font']
        self.color = state['color']
        self.bg_color = state['bg_color']
        self.text_size = state['text_size']
        self.update_text()

    def on_toggle_case_button_click(self, event):
        if event.actor == self.toggle_case_button:
            self.toggle_uppercase()
            self.toggle_case_button.switch()

    def toggle_uppercase(self):
        self.uppercase = not self.uppercase

    def update_rect(self):
        corner1 = [self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2, 0]
        corner2 = [self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2, 0]
        self.rect_actor = Rectangle(corner1, corner2, c='white', alpha=0.6)
        self.rect_actor.wireframe(False)

    def on_key_press(self, event):
        key = event.keypress.lower()
        self.save_state()
        if key == "backspace":
            if len(self.text) > 0:
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
            char = special_keys.get(key, key)
            if self.uppercase:
                char = char.upper()
            self.text += char
        self.redo_stack.clear()
        self.update_text()
        if self.callback:
            self.callback(self)

    def update_text(self):
        self.window.remove(self.text_actor)
        self.window.remove(self.rect_actor)

        max_line_length = int(self.size[0] / (0.01 * self.text_size))
        if self.text_size == 1:
            max_line_length = int(self.size[0] / (0.01 * self.text_size))
            max_lines = int(self.size[1] / (0.04 * self.text_size))
        else:
            max_line_length = int(self.size[0] / (0.0105 * self.text_size))
            max_lines = int(self.size[1] / (0.036 * self.text_size))

        lines = self.text.split('\n')
        new_lines = []
        for line in lines:
            while len(line) > max_line_length:
                new_lines.append(line[:max_line_length])
                line = line[max_line_length:]
            new_lines.append(line)
        lines = new_lines[:max_lines]
        self.text = '\n'.join(lines)

        self.update_rect()

        text_pos = (
        self.pos[0] - self.size[0] / 2 + 0.01, self.pos[1] + self.size[1] / 2 - 0.05 * self.text_size * len(lines))
        self.text_actor = Text2D(self.text, pos=text_pos, c=self.color, bg=self.bg_color, font=self.font,
                                 s=self.text_size, justify='left')

        self.window += self.rect_actor
        self.window += self.text_actor
        self.window.render()

    def apply_font_style(self, style):
        self.save_state()
        self.font = style
        self.redo_stack.clear()
        self.update_text()



    def apply_text_color(self, color):
        self.save_state()
        self.color = color
        self.redo_stack.clear()
        self.update_text()
        self.combo_box_color.set_color(color)

    def apply_bg_color(self, color):
        self.save_state()
        self.combo_box_bg_color.set_color(color)
        self.bg_color = color
        self.redo_stack.clear()
        self.update_text()

    def apply_text_size(self, size):
        self.save_state()
        self.text_size = int(size)
        self.redo_stack.clear()
        self.update_text()

    def apply_text_file(self, file):
        self.save_state()
        self.file = file
        self.redo_stack.clear()
        self.update_text()

    def on_save_button_click(self, event):
        if isinstance(event.actor, Button) and event.actor.states[0] == "SaveFile":
            self.save_text()
        elif isinstance(event.actor, Button) and event.actor.states[0] == "DeleteFile":
            self.delete_text()
        elif isinstance(event.actor, Button) and event.actor.states[0] == "A":
            self.increase_size_of_text()
        elif isinstance(event.actor, Button) and event.actor.states[0] == "A ":
            self.decrease_size_of_text()

    def save_text(self):
        with open(self.file, "w") as file:
            file.write(self.text)

    def delete_text(self):
        file_path = self.file
        if os.path.exists(file_path):
            os.remove(file_path)
        self.text = ""
        self.update_text()

    def increase_size_of_text(self):
        self.save_state()
        if self.text_size < 4:
            self.text_size += 0.2
            self.update_text()

    def decrease_size_of_text(self):
        self.save_state()
        if self.text_size > 0.5:
            self.text_size -= 0.2
            self.update_text()

    def on_undo_button_click(self, event):
        if event.actor == self.undo_button:
            self.undo()

    def on_redo_button_click(self, event):
        if event.actor == self.redo_button:
            self.redo()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append({
                'text': self.text,
                'font': self.font,
                'color': self.color,
                'bg_color': self.bg_color,
                'text_size': self.text_size
            })
            state = self.undo_stack.pop()
            self.load_state(state)

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append({
                'text': self.text,
                'font': self.font,
                'color': self.color,
                'bg_color': self.bg_color,
                'text_size': self.text_size
            })
            state = self.redo_stack.pop()
            self.load_state(state)


def user_callback(text_box):
    if "exit\n" in text_box.text or "EXIT\n" in text_box.text:
        text_box.window.close()


settings.enable_default_keyboard_callbacks = False
text_box = TextBox(callback=user_callback)
