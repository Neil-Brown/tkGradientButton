from unittest import TestCase

from gradient_button import Button


class TestButton_Static_Colors(TestCase):

    def setUp(self):
        self.b = Button(font=("Georgia", 10),
                        active_color = "blue",
                        inactive_color = "green",
                        active_foreground ="blue",
                        inactive_foreground="green",
                        text="test")

    def test_enter_cursor(self):
        self.b.enter()
        self.assertEqual(self.b.cget("cursor"), self.b.active_cursor)

    def test_leave_cursor(self):
        self.b.leave()
        self.assertEqual(self.b.cget("cursor"), self.b.inactive_cursor)

    def test_font_family(self):
        self.assertEqual(self.b.font.cget("family"), "Georgia")

    def test_font_size(self):
        self.assertEqual(self.b.font.cget("size"), 10)

    def test_enter_color(self):
        self.b.enter()
        self.assertEqual(self.b.cget("background"), "blue")

    def test_leave_color(self):
        self.b.leave()
        self.assertEqual(self.b.cget("background"), "green")

    def test_enter_foreground(self):
        self.b.enter()
        self.assertEqual(self.b.itemcget(self.b.text_widget, "fill"), "blue")

    def test_leave_foreground(self):
        self.b.active = False
        self.b.stay_active = False
        self.b.leave()
        self.assertEqual(self.b.itemcget(self.b.text_widget, "fill"), "green")

    def test_leave_when_stay_active_equals_false(self):
        self.b.stay_active = False
        self.b.click()
        self.b.leave()
        self.assertEqual(self.b.cget("background"), "green")

    def test_leave_when_stay_active_equals_true(self):
        self.b.stay_active = True
        self.b.click()
        self.b.leave()
        self.assertEqual(self.b.cget("background"), "blue")


class TestButton_Gradient_colors(TestCase):
    def setUp(self):
        self.b = Button(active_color = ["grey", "white"],
                        inactive_color = ["red", "pink"],
                        active_num_colors = 20,
                        inactive_num_colors = 100)

    def test_num_active_lines(self):
        self.b.enter()
        self.assertEqual(len(self.b.lines), 20)

    def test_num_inactive_lines(self):
        self.b.leave()
        self.assertEqual(len(self.b.lines), 100)


class Test_Button_Command(TestCase):
    def setUp(self):
        self.param = None
        self.called = False

    def func(self, *args, **kwargs):
        self.called = True
        if args:
            self.param = args[0]
        if kwargs:
           for k, v in kwargs.items():
               setattr(self, k, v)

    def test_command_called(self):
        self.b = Button(command=self.func)
        self.b.click()
        self.assertEqual(self.called, True)

    def test_command_called_with_args(self):
        self.b = Button(command=lambda:self.func("param"))
        self.b.click()
        self.assertEqual(self.param, "param")

    def test_command_called_with_kwargs(self):
        self.b = Button(command=lambda:self.func(keyword="test"))
        self.b.click()
        self.assertEqual(self.keyword, "test")






