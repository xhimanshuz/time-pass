import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class EntryWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='Entry  ')
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Text ...")
        vbox.pack_start(self.entry, 1, 1, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(hbox, 1, 1, 0)

        self.check_editable = Gtk.CheckButton("Editable")
        self.check_editable.connect("toggled", self.on_editable_toggled)
        self.check_editable.set_active(True)
        hbox.pack_start(self.check_editable, 1, 1, 0)

        self.check_visible = Gtk.CheckButton("Visible")
        self.check_visible.connect('toggled', self.on_visible_toggled)
        self.check_visible.set_active(True)
        hbox.pack_start(self.check_visible, 1, 1, 0)

        self.check_icon = Gtk.CheckButton('icon')
        self.check_icon.connect('toggled', self.on_icon_toggled)
        self.check_icon.set_active(False)
        hbox.pack_start(self.check_icon, 1, 1, 0)

    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)
        print(self.entry.get_text())

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entry.set_visibility(value)

    def on_icon_toggled(self, button):
        if button.get_active():
            icon_name = 'system-search-symbolic'
        else:
            icon_name = None
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, icon_name)

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()        