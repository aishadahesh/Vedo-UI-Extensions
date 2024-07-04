################################## Combo-Box ##################################

import vedo
from vedo import Plotter, Text2D, Rectangle

class ComboBox:
    def __init__(self, options, default_text="Select an option"):
        self.options = options
        self.default_text = default_text
        self.selected_option = default_text
        self.option_texts = []
        self.option_actors = []
        self.dropdown_visible = False
        
        self.build_combo_box()

    def build_combo_box(self):
        self.window = Plotter(title="Combo-Box", size=(800, 600), interactive=False)
        
        self.label = Text2D(self.selected_option, pos=(0.35, 0.85), c='k', bg='black')
        self.label.pickable()
        self.window += self.label
        
        # Create the dropdown list using corner points
        corner1 = [0.3, 0.4, 0]
        corner2 = [0.7, 0.8, 0]
        self.dropdown = Rectangle(corner1, corner2, c="white", alpha=0.6)
        self.dropdown.pickable(False)
        
        for i, option in enumerate(self.options):
            text = Text2D(option, pos=(0.35, 0.75 - i * 0.05), c='k')
            text.pickable()
            self.option_texts.append(option)
            self.option_actors.append(text)
        
        self.hide_dropdown()
        
        self.window.add_callback("mouse click", self.on_mouse_click)
        
        self.window.show(interactive=True)

    def show_dropdown(self):
        if not self.dropdown_visible:
            self.window += self.dropdown
            for actor in self.option_actors:
                self.window += actor
            self.dropdown_visible = True

    def hide_dropdown(self):
        if self.dropdown_visible:
            self.window.remove(self.dropdown)
            for actor in self.option_actors:
                self.window.remove(actor)
            self.dropdown_visible = False

    def on_mouse_click(self, event):
        if event.actor == self.label:
            self.toggle_dropdown()
        elif self.dropdown_visible:
            for actor in self.option_actors:
                if event.actor == actor:
                    self.selected_option = actor.text()
                    self.label.text(self.selected_option)
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

# Usage
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combo_box = ComboBox(options)
print("Selected Option:", combo_box.get_selected_option())

