from vedo import settings, Text2D
settings["enable_default_keyboard_callbacks"] = False

def create_textbox(word_functions, plt):
    def kfunc(evt):
        field.frame("gray", lw=8)  # Set frame color here

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
        field.text(f"{show}").frame("red", lw=8)
        for word in word_functions:
            if show == word:
                word_function = word_functions[word]
                word_function()
                msg.text(show)
        plt.render()

    settings["enable_default_keyboard_callbacks"] = False

    msg = Text2D(pos=(0.1, 0.4), s=2, font="Quikhand", c="k1", bg="k7", alpha=1)
    msg.text("start:")

    field = Text2D("Please write here", pos="bottom-middle", s=3, font="Glasgo", bg="gray", c="black", alpha=1)

    plt.add_callback("key press", kfunc)

    return kfunc, msg, field

'''
from text_implemnt import create_textbox
from vedo import  dataurl, Plotter, Mesh

#Load your object here
mesh =


#define what your text should do:
   -just write the name of the func,and his implemntation
word_functions = {
    "option1": add your func1 code here,
    "option2": add your func2 code here,
    "option3": add your func3 code here,
    "option4": add your func4 code here,
    "option5": add your func5 code here
    #add another optionns if u want }

# plt = Plotter()
# kfunc, msg, field = create_textbox(word_functions, plt)
# plt.show(mesh, msg, field)

'''
