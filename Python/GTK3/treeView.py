import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class n4n(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Form Window")
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.serverName = Gtk.Label("Server Name")
        self.serverNameInp = Gtk.Entry()
        self.hbox.pack_start(self.serverName, 1, 1, 0)
        self.hbox.pack_start(self.serverNameInp, 1, 1, 0)
        self.vbox.pack_start(self.hbox, 1, 1, 0)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.Port = Gtk.Label("Port ")
        self.PortInp = Gtk.Entry()
        self.hbox.pack_start(self.Port, 1, 1, 0)
        self.hbox.pack_start(self.PortInp, 1, 1, 0)
        self.vbox.pack_start(self.hbox, 1, 1, 0)

        self.submit = Gtk.Button.new_with_mnemonic("_Submit")
        self.submit.connect('clicked', self.onSubmit)
        self.vbox.pack_start(self.submit,1 ,1 , 0)
    
        self.listStore = Gtk.ListStore(str, int)
        self.treeView = Gtk.TreeView(self.listStore)
        self.treeview()


        self.vbox.pack_start(self.treeView, 1, 1, 0)
        self.box.add(self.vbox)
        

    def onSubmit(self, widget):
        label = [self.serverNameInp.get_text(), int(self.PortInp.get_text())]
        print(label)
        self.listStore.append(label)
        # self.listStoreAppend(label)

    def treeview(self):
        for i, item in enumerate(["Server Name", "Port"]):
            renderer = Gtk.CellRendererText()
            treeViewColumn = Gtk.TreeViewColumn(item, renderer, text=i)
            treeViewColumn.set_sort_column_id(i)
            self.treeView.append_column(treeViewColumn)



win = n4n()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()