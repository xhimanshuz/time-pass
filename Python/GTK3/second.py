import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(self.data))

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Second")
        self.set_border_width(10)

        outerBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        self.add(outerBox)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        outerBox.pack_start(listBox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, 1, 1, 0)

        label1 = Gtk.Label("Automatic Date & Time")
        label2 = Gtk.Label("Require Internet Access")
        vbox.pack_start(label1, 1, 1, 0)
        vbox.pack_start(label2, 1, 1, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch, 1, 1, 0)
        listBox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Enable Automatic Update")
        checkBox = Gtk.CheckButton()
        hbox.pack_start(label, 1, 1, 0)
        hbox.pack_start(checkBox, 1, 1, 0)
        listBox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        label = Gtk.Label("Date Format")
        comboBox = Gtk.ComboBoxText()
        comboBox.insert(0, '0','24-hours')
        comboBox.insert(0, '1', 'AM/PM')
        hbox.pack_start(label, 1, 1, 0)
        hbox.pack_start(comboBox, 1, 1, 0)
        listBox.add(row)

        listbox2 = Gtk.ListBox()
        items = "This is fucing Text ...".split()
        for item in items:
            listbox2.add(ListBoxRowWithData(item))

        
            

win = Window()
win.connect('delete-event',Gtk.main_quit)
win.show_all()
Gtk.main()