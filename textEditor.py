from vedo import Plotter, Text2D, Rectangle, settings
import vedo as vd
from vedo.pyplot import plot
from vedo import Latex
from vedo import Plotter, Cube, Mesh, Assembly, dataurl
from vedo.colors import colors, get_color

### extra functions:

plt = vd.Plotter(bg2='lightblue')  # Create the plotter

def changeColor(): 
    color_names = list(colors.keys())
    n_colors = len(color_names)

    grid_size = 10 
    color_cubes = []
    for i, color_name in enumerate(color_names):
        if i >= grid_size**2:
            break
        row, col = divmod(i, grid_size)
        color = colors[color_name]
        cube = Cube(pos=[col + 15, -row, 0]).scale([0.9, 0.9, 0.1]).c(color).alpha(1)
        cube.name = color_name  
        color_cubes.append(cube)



    mesh = Mesh(dataurl + "magnolia.vtk").flat().lw(1).pos(-5, -5, 0)

    plt.add(*color_cubes, mesh)

    shades = []

    class MeshColorAdjuster:
        def __init__(self, mesh, plotter):
            self.mesh = mesh
            self.plotter = plotter
            self.curr_r = 255
            self.curr_g = 255
            self.curr_b = 255
            self.sliders = []
            self.add_sliders()

        def slider1(self, widget, event):
            self.curr_r = int(widget.value)
            self.update_mesh_color()

        def slider2(self, widget, event):
            self.curr_b = int(widget.value)
            self.update_mesh_color()

        def slider3(self, widget, event):
            self.curr_g = int(widget.value)
            self.update_mesh_color()

        def update_mesh_color(self):
            self.mesh.color((self.curr_r / 255, self.curr_g / 255, self.curr_b / 255))

        def add_sliders(self):
            self.sliders.append(self.plotter.add_slider(
                self.slider1,
                xmin=0,
                xmax=255,
                value=self.curr_r,
                c="red",
                pos=((0.8, 0.6), (0.95, 0.6)),
                title="Red (R)",
            ))

            self.sliders.append(self.plotter.add_slider(
                self.slider2,
                xmin=0,
                xmax=255,
                value=self.curr_b,
                c="blue",
                pos=((0.8, 0.5), (0.95, 0.5)),
                title="Blue (B)",
            ))

            self.sliders.append(self.plotter.add_slider(
                self.slider3,
                xmin=0,
                xmax=255,
                value=self.curr_g,
                c="green",
                pos=((0.8, 0.4), (0.95, 0.4)),
                title="Green (G)",
            ))

        def set_sliders(self, r, g, b):
            self.curr_r = r
            self.curr_g = g
            self.curr_b = b
            self.sliders[0].value = r
            self.sliders[1].value = b
            self.sliders[2].value = g
            self.update_mesh_color()

    color_adjuster = MeshColorAdjuster(mesh, plt)

    def create_shades(selected_color, pos):
        global shades
        
        for shade in shades:
            plt.remove(shade)
        shades = []

        base_color = get_color(selected_color)
        for i in range(5):
            for j in range(5):
                factor = 0.5 + 0.1 * (i + j)  
                shade_color = [min(1, factor * c) for c in base_color]
                cube = Cube(pos=[pos[0] + j, pos[1] - i, 0]).scale([0.9, 0.9, 0.1]).c(shade_color).alpha(1)
                shades.append(cube)
        plt.add(*shades)
        plt.render()


    def on_left_click(evt):
        clicked_obj = evt.actor
        if clicked_obj:
            if clicked_obj in color_cubes:
                selected_color = get_color(clicked_obj.name)
                mesh.color(selected_color)
                r, g, b = int(selected_color[0]*255), int(selected_color[1]*255), int(selected_color[2]*255)
                color_adjuster.set_sliders(r, g, b)
                create_shades(clicked_obj.name, [10, 5])
            elif clicked_obj in shades:
                shade_color = clicked_obj.color()
                mesh.color(shade_color)
                r, g, b = int(shade_color[0]*255), int(shade_color[1]*255), int(shade_color[2]*255)
                color_adjuster.set_sliders(r, g, b)
            plt.render()

    plt.add_callback("LeftButtonPress", on_left_click)
    plt.add(color_cubes)
    plt.show(interactive=True)

def change_text_color():
    pass

def change_bg_color():
    pass


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
        self.window = plt(title="Combo-Box", size=(800, 600), interactive=False)
        
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
    def chnage_text_format(self):
        if self.selected_option == "Quikhand":
            font = Latex(font="Quikhand")
        elif self.selected_option == "Arial":
            font = Latex(font="Arial")
        elif self.selected_option == "Times New Roman":
            font = Latex(font="Times New Roman")
        elif self.selected_option == "Courier New":
            font = Latex(font="Courier New")
        elif self.selected_option == "Verdana":
            font = Latex(font="Verdana")
        else:
            font = Latex(font="Arial")  #default font

class TextBox:
    def __init__(self, initial_text="", pos=(0.5, 0.5), size=(0.4, 0.1), callback=None):
        self.text = initial_text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.window = plt(size=(800, 600), title="Text Box Example", interactive=True)
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
plt.add(text_box.window)

options = ["Quikhand", "Arial", "Times New Roman", "Courier New", "Verdana"]
combo_box = ComboBox(options)
plt.add(combo_box.window)

color_button = vd.Button(fnc=change_text_color(), states=['change color of text'], c='black',bc= 'white',  pos=(0.8, 0.8), size=15)
plt.add(color_button)
bg_color_button = vd.Button(fnc=change_bg_color(), states=['change color of background'], c='black',bc= 'white',  pos=(0.8, 0.85), size=15)
plt.add(bg_color_button)
plt.show(interactive=True)

