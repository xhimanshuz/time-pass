import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Glade:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self,button):
        print()

builder = Gtk.Builder()
builder.add_from_file('test.glade')
builder.connect_signals(Glade())
label = builder.add_objects_from_file('test.glade',('label'))
# print(label.get_text())
window = builder.get_object('window1')
window.show_all()

Gtk.main()