import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Simple Notebook')
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label("This is fucking Default Page"))
        self.notebook.append_page(self.page1, Gtk.Label("Page 1"))

        button= Gtk.Button("Click")
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label("This is fucking Second Page"))
        self.page2.pack_start(button, 1, 1, 0)
        self.notebook.append_page(self.page2, Gtk.Label("Page 2"))

win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()