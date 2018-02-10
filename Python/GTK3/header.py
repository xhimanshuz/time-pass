import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Header Demo')

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar"
        self.set_titlebar(hb)

        button = Gtk.Button(label="x")
        hb.pack_end(button)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        lButton = Gtk.Button()
        rButton = Gtk.Button()
        lButton.add(Gtk.Arrow(Gtk.ArrowType.LEFT))
        rButton.add(Gtk.Arrow(Gtk.ArrowType.RIGHT))
        hbox.add(rButton)
        hbox.add(lButton)

        hb.pack_start(hbox)

        self.add(Gtk.TextView())


win = HeaderBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()