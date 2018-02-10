import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

import os
import subprocess

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

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.nginxServer = Gtk.Label("Nginx Server ")
        # self.button = Gtk.ToggleButton('ON/OFF')
        # self.button.set_active(self.nginxStatus())

        # self.button.connect('toggled', self.onButtonToggled)
        # self.hbox.pack_start(self.nginxServer, 1, 1, 0)
        # self.hbox.pack_start(self.button, 1, 1, 0)

        self.switch = Gtk.Switch()
        self.switch.set_active(self.nginxStatus())
        self.switch.connect("notify::active", self.onButtonToggled)
        self.hbox.pack_start(self.nginxServer, 1, 1, 0)
        self.hbox.pack_start(self.switch, 1, 1, 0)
        self.vbox.pack_start(self.hbox, 1, 1, 0)

        self.submit = Gtk.Button.new_with_mnemonic("_Submit")
        self.submit.connect('clicked', self.onSubmit)
        self.vbox.add(self.submit)

        self.os = Gtk.Label(os.uname()[1])
        self.root = Gtk.Label()
        if os.getuid() != 0:
            self.root.set_text("Non-Root")
        else:
            self.root.set_text("Root")
        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)
        self.hbox.pack_start(self.os, 1, 1, 0)
        self.hbox.pack_start(self.root, 1, 1, 0)
        self.vbox.add(self.hbox)
        self.box.add(self.vbox)
    
    def nginxStatus(self):
        if subprocess.getstatusoutput('service nginx status')[0] == 0:
            return True
        else:
            return False
    
    def onSubmit(self, widget):
        label = [self.serverNameInp.get_text(), self.PortInp.get_text()]
        print(label)

    def onButtonToggled(self, button, gparam):
        if self.nginxStatus():
            p = subprocess.call(['service', 'nginx', 'stop'])
            print(p, 'Stop')
        else:
            p = subprocess.call(['service', 'nginx','start'])
            print(p, 'Start')
        if p != 0:
            button.set_active(not(button.get_active()))
        
win = n4n()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()