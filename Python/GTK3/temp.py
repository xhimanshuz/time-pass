import gi
gi.require_version('3.0','Gtk')
from gi.repository import Gtk

class Glade(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Glade')
        
        vbo