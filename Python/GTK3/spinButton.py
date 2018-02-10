import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SpinButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SpinButton Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        hbox.pack_start(self.spinbutton, 1, 1, 0)

        self.setNumeric = Gtk.ToggleButton("Numeric")
        self.setNumeric.connect('toggled', self.on_numeric)
        hbox.pack_start(self.setNumeric, 1, 1, 0)

    def on_numeric(self, button):
        self.spinbutton.set_numeric(button.get_active())

win = SpinButtonWindow()
win.connect('delete-event',Gtk.main_quit)
win.show_all()
Gtk.main()