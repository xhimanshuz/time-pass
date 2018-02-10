import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RadioButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="RadioButton Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing = 6)
        self.add(hbox)

        rButton1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button1")
        rButton1.connect('toggled', self.on_button_toggled, "1")
        
        rButton2 = Gtk.RadioButton.new_with_mnemonic_from_widget(rButton1, "Button _2")
        rButton2.connect('toggled', self.on_button_toggled, "2")

        rButton3 = Gtk.RadioButton.new_with_mnemonic_from_widget(rButton1, "Button _3")
        rButton3.connect('toggled', self.on_button_toggled, "3")

        #list = [rButton1, rButton2, rButton3]
        for b in [rButton1, rButton2, rButton3]:
            hbox.pack_start(b, 1, 1, 0)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = 'on'
        else:
            state = 'off'
        print("Button ", name, " is ", state)

win = RadioButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()