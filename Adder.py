from vedo import Plotter, Mesh, dataurl, Text2D, Rectangle

class Adder:
    def __init__(self, _plt, pos_text=(0.3, 0.6), max_value=10, min_value=0, add_func=None, minus_func=None):
        self.max_len = max_value
        self.min_len = min_value
        self.counter = max_value
        self.add = add_func
        self.minus = minus_func
        self.plt = _plt
        self.mesh = Mesh(dataurl + "magnolia.vtk").c("violet").flat()
        self.plt.add(self.mesh)

        pos_plus = (pos_text[0] + 0.035, pos_text[1]+0.04)
        pos_minus = (pos_text[0] - 0.035, pos_text[1]+0.04)

        # Add buttons for controlling the counter
        self.add_button(pos_plus, text="+", bg_color="green", callback=self.add_func)
        self.add_button(pos_minus, text="-", bg_color="red", callback=self.minus_func)
        self.msg = Text2D("", pos=pos_text, s=2, font="Normografo", c="k1", justify="center",alpha=1)
        self.update_counter_text()
        self.plt.add(self.msg)

    def add_func(self, obj, event):
        if self.counter < self.max_len:
            self.add(self.mesh, self.counter)
            self.counter += 1
            self.update_counter_text()
            print(f"Counter increased to {self.counter}")

    def minus_func(self, obj, event):
        if self.counter > self.min_len:
            self.minus(self.mesh, self.counter)
            self.counter -= 1
            self.update_counter_text()
            print(f"Counter decreased to {self.counter}")

    def add_button(self, pos, text, bg_color, callback):
        button = self.plt.add_button(
            callback,
            pos=pos,
            states=[text],
            c=["white"],
            bc=[bg_color],
            font="courier",
            size=10,
            bold=True,
            italic=False
        )
        return button

    def update_counter_text(self):
        self.msg.text(f"{self.counter}")

    def show(self):
        self.plt.show()

    def close(self):
        self.plt.close()
################################################################################################
'''
#crate your plotter
plt = Plotter()

#create you cutom_minus functions
def custom_add_func(mesh, c):
    print("Custom add function")
    mesh.alpha(c / 10)

def custom_minus_func(mesh, c):
    print("Custom minus function")
    mesh.alpha(c / 10)

#define your Adder 
pos_text = (0.3, 0.6)
adder_instance = Adder(plt, pos_text=pos_text, max_value=10, min_value=0, add_func=custom_add_func, minus_func=custom_minus_func)
adder_instance.show()
'''