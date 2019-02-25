[![Build Status](https://travis-ci.org/Neil-Brown/tkGradientButton.svg?branch=master)](https://travis-ci.org/Neil-Brown/tkGradientButton)[![Coverage Status](https://coveralls.io/repos/github/Neil-Brown/tkGradientButton/badge.svg?branch=master)](https://coveralls.io/github/Neil-Brown/tkGradientButton?branch=master)[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

![](button1.gif)
## Requirements
* Windows, Mac or Linux
* Python 2.7 or 3.x with tkinter
* Pillow module (required if you want to put an image on the button)
* colour module (required for gradient colours)

## Installation
Place gradient_button.py into your project directory:
`from gradient_button import Button`

## Documentation
     my_button = Button(parent=window)
     my_button.pack()

Places the button into the parent provided. 
Any of the three geometry managers: "pack", "grid", or "place" can be used.

Optional keyword arguments:
* font = 
  * Takes a tuple of family name and font size
  * Defaults to ("Arial", 20)
* active_color = 
   * Color / gradient to display when the cursor is hovering over the button
   * Takes either a single color, or list of two colors to create a gradient
   * Accepts hex, rgb or tkinter color name.
   * Defaults to ["#D46A6A", "#AA3939"]
* active_num_colors =
   * Number of gradient colors to be used between the two colors
   * Takes an Integer
   * Defaults to 50
* active_foreground = 
   * Font color when the cursor is hovering over the button.
   * Takes hex, rgb, or tkinter color.
   * Defaults to "#FFAAAA".
* active_cursor = 
   * Cursor to use when hovering over the button
   * Defaults to hand2
* inactive_color = 
   * Color / gradient to display when the button is not being hovered over
   * Takes either a single color, or list of two colors to create a gradient
   * Accepts hex, rgb or tkinter color name.
   * Defaults to ["#AA3939", "#D46A6A"]
* inactive_foreground = 
   * Font color when the cursor is NOT hovering over the button.
   * Takes hex, rgb, or tkinter color.
   * Defaults to #550000.
* inactive_num_color = 
   * Number of gradient colors to be used between the two colors
   * Takes an Integer
   * Defaults to 50
* text = 
   * Text to be displayed on the button
   * Defaults to ""
* image = 
   * required import
      > from PIL import ImageTk, Image
   * Image to be displayed on the button
   * Takes a Photoimage - most formats can be passed using image = ImageTk.PhotoImage(Image.open("image_path"))
   * Defaults to None
* compound = 
   * Where to locate the image relative to the text
   * Takes "left", "right", "top", or "bottom"
   * Defaults to "top"

* ipadx = 
   * Space in pixels to be added between button contents and vertical edges
   * defaults to 50
* ipady =
   * Space in pixels to be added between button contents and horizintal edges
   * defaults to 20
* stay_active = 
   * takes a Boolean
   * If False, after being clicked the button will return back to the inactive color scheme
   * If True, after being clicked the button will retain the active color scheme, even after the mouse leaves the button area until the      button is clicked again.
* command = 
   * Takes a method or function to be called when the button is clicked
     

## Example

    class Main(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.configure(width=WIDTH, height=HEIGHT)
            center(self, self.winfo_screenwidth(), self.winfo_screenheight())
            self.button = Button(parent=self,
                                 inactive_color=["#AA3939", "#D46A6A"],
                                 inactive_foreground="#2D5887",
                                 active_color = ["#D46A6A", "#AA3939"],
                                 active_foreground="#C7EFE3",
                                 font=("Arial", 20),
                                 text="Button",
                                 image=ImageTk.PhotoImage(Image.open("python.png")),
                                 compound="top",
                                 stay_active=True,
                                 command = self.clicked,
            )
            self.button.pack(fill=None, expand=False)

        def clicked(self, *event):
            print("Clicked")

    if __name__ == '__main__':
        main = Main()
        main.mainloop()
