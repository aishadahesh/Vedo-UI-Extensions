from vedo import Plotter


class ToggleSwitch:
    def __init__(self, plotter, on_func, off_func, pos):
        self.plotter = plotter
        self.on_func = on_func
        self.off_func = off_func
        self.toggle_state = False
        self.pos = pos

        self.on_button = self.plotter.add_button(
            self.toggle,
            pos=self.pos,
            states=["  ", "ON"],
            c=["white", "white"],
            bc=["green", "green"],
            font="Calco",
            size=30,
        )

        self.off_button = self.plotter.add_button(
            self.toggle,
            pos=(self.pos[0]-30/350, self.pos[1]),  # Slightly below the first button
            states=["OFF", "   "],
            c=["white", "white"],
            bc=["red", "red"],
            font="Calco",
            size=30,
        )

        # Initial state
        self.update_buttons()

    def toggle(self, obj, ename):
        self.toggle_state = not self.toggle_state
        if self.toggle_state:
            self.on_func()
            self.on_button.switch()
            self.off_button.switch()

        else:

            self.off_func()
            self.on_button.switch()
            self.off_button.switch()
        self.update_buttons()

    def update_buttons(self):
        if self.toggle_state:
            self.on_button.switch # Show "ON"
            self.off_button.switch  # Hide "OFF"
        else:
            self.on_button.switch  # Hide "ON"
            self.off_button.switch  # Show "OFF"
####################################################################################
'''
# Define your on/off function
def on_func():
    print("Doing on_func")
def off_func():
    print("Doing off_func")

# Define your plotter
plt = Plotter()

# Create your toggle switch
# The input: (your plotter, the on function, the off function, position)
toggle_switch = ToggleSwitch(plt, on_func, off_func, pos=(x, y)) 

# Show the plotter window
plt.show(interactive=True)
'''