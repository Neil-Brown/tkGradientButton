import tkinter as tk
from colour import Color
from tkinter import font


class Button(tk.Canvas):
    def __init__(self,  **kwargs):
        tk.Canvas.__init__(self)

        self.defaults = {
                         "font": ("Arial", 20),
                         "active_color": ["#D46A6A", "#AA3939"],
                         "active_num_colors": 50,
                         "active_foreground": "#FFAAAA",
                         "active_cursor": "hand2",
                         "inactive_color": ["#AA3939", "#D46A6A"],
                         "inactive_foreground": "#550000",
                         "inactive_num_colors": 50,
                         "inactive_cursor": "hand2",
                         "compound": "right",
                         "ipadx": 50,
                         "ipady": 20,
                         "stay_active": False,

                         }
        for k, v in self.defaults.items():
            setattr(self, k, v)
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.height = 0
        self.width = 0
        self.img_height = 0
        self.img_width = 0
        self.text_height = 0
        self.text_width = 0
        self.active = False
        self.lines = []

        # If more than one color is passed in create a gradient
        if isinstance(self.inactive_color, list):
            self.inactive_gradient = list(
                Color(self.inactive_color[0]).range_to(
                    Color(self.inactive_color[1]), self.inactive_num_colors))
        if isinstance(self.active_color, list):
            self.active_gradient = list(Color(self.active_color[0]).range_to(
                Color(self.active_color[1]), self.active_num_colors))

        # Create a font object
        self.font = font.Font(family=self.font[0], size=self.font[1])

        # Measure contents
        self.measure_image()
        self.measure_text()
        self.calculate_dimensions()

        self.config(width=self.width, height=self.height)
        self.bind_button()
        self.leave()

    def measure_image(self):
        """ Set image_width and image_heigh parameters"""
        if hasattr(self, "image"):
            self.img_height = self.image.height()
            self.img_width = self.image.width()

    def measure_text(self):
        """ Set the text_height text_width attributes """
        if hasattr(self, "text"):
            self.text_height = self.font.metrics("linespace")
            self.text_width = self.font.measure(self.text)

    def calculate_dimensions(self):
        """ Calculate the button dimensions based on
            size, compound, and ipad values"""

        if self.compound in ["top", "bottom"]:
            self.width += max(self.text_width, self.img_width)
            self.height += (self.text_height + self.img_height)
        elif self.compound in ["left", "right"]:
            self.height += max(self.text_height, self.img_height)
            self.width += (self.text_width + self.img_width)
        self.width += self.ipadx
        self.height += self.ipady

    def enter(self):
        """ Configure buttons appearance when the cursor hovers over it """
        self.configure(cursor=self.active_cursor)
        self.delete("all")
        if hasattr(self, "active_gradient"):
            self.draw_lines(self.active_gradient, self.active_num_colors)
        else:
            self.config(background=self.active_color)
        self.set_contents(self.active_foreground)

    def leave(self):
        """ Configure button's appearance when the cursor leaves the button area """
        if self.active and self.stay_active:
            return
        self.configure(cursor=self.inactive_cursor)
        self.delete("all")
        if hasattr(self, "inactive_gradient"):
            self.draw_lines(self.inactive_gradient, self.inactive_num_colors)
        else:
            self.config(background=self.inactive_color)
        self.set_contents(self.inactive_foreground)

    def draw_lines(self, grad, num):
        """ Draws the gradient lines """
        self.lines = []
        for y, color in enumerate(grad):
            self.lines.append(self.create_line((0, y * (self.height / num)),
                             (self.width + 5, y * (self.height / num)),
                             width=self.height / num + 7, fill=color))

    def set_contents(self, color):
        """ Set the position of any text or image parameters passed in """
        anchor="n"
        if self.compound == "top":
            img_coord = (int(self.width/2), int(self.ipady/2))
            txt_coord = (int(self.width/2), int(self.ipady/2)+self.img_height)
        elif self.compound == "bottom":
            txt_coord = (int(self.width/2), int(self.ipady/2))
            img_coord = (int(self.width/2), int(self.ipady/2) + self.font.metrics("linespace"))
        elif self.compound == "left":
            anchor="w"
            img_coord = (int(self.ipadx/2), int(self.height/2))
            txt_coord = (int(self.ipadx / 2) + +self.img_width+10,
                         int(self.height  / 2))
        elif self.compound == "right":
            anchor="w"
            txt_coord = (int(self.ipadx/2), int(self.height/2))
            img_coord = (int(self.ipadx / 2) + self.text_width,
                         int(self.height / 2))

        if hasattr(self, "text"):
            self.set_txt(txt_coord, color, anchor)
        if hasattr(self, "image"):
            self.set_img(img_coord, anchor)

    def set_img(self, coord, anchor="n"):
        """ Called if an image parameter is passed """
        self.create_image(coord, image=self.image, anchor=anchor)

    def set_txt(self, coord, color, anchor="n"):
        """ Called if a text parameter is passed """
        self.text_widget = self.create_text(coord, text=self.text, font=self.font, fill=color, anchor=anchor)

    def bind_button(self):
        """ Set button bindings """
        self.bind("<Enter>", lambda event: self.enter())
        self.bind("<Leave>", lambda event: self.leave())
        self.bind("<Button-1>", lambda event: self.click())

    def click(self):
        """ Calls the command passed in as parameter 
            Flips self.value boolean value """
        self.active = not self.active
        self.enter()
        if hasattr(self, "command"):
            self.command()

if __name__ == '__main__':
    root = tk.Tk()
    b = Button(master=root)
    b.pack()

    root.mainloop()
