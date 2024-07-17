from vedo import Plotter, Cube, Mesh, Assembly, dataurl
from vedo.colors import colors, get_color

color_names = list(colors.keys())
n_colors = len(color_names)

plotter = Plotter(title="Color Picker Example", size=(1200, 800))

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

plotter.add(*color_cubes, mesh)

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


color_adjuster = MeshColorAdjuster(mesh, plotter)


def create_shades(selected_color, pos):
    global shades
    
    for shade in shades:
        plotter.remove(shade)
    shades = []

    base_color = get_color(selected_color)
    for i in range(5):
        for j in range(5):
            factor = 0.5 + 0.1 * (i + j)  
            shade_color = [min(1, factor * c) for c in base_color]
            cube = Cube(pos=[pos[0] + j, pos[1] - i, 0]).scale([0.9, 0.9, 0.1]).c(shade_color).alpha(1)
            shades.append(cube)
    plotter.add(*shades)
    plotter.render()


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
        plotter.render()


plotter.add_callback("LeftButtonPress", on_left_click)

plotter.add(color_cubes)

plotter.show(interactive=True)

