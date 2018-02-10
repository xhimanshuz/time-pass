import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

class FlowBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Flow")
        self.set_border_width(10)
        self.set_default_size(300, 400)

        header = Gtk.HeaderBar(title='Flow Box')
        header.set_subtitle("Subtile FlowBox app")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(0, Gtk.PolicyType.AUTOMATIC)

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(0)

        for i in range(5000):
            button = Gtk.Button(label=i)
            button.connect('clicked', )
            flowbox.add(button)
            
        def pr(self, i):
            print(i)
        scrolled.add(flowbox)

        self.add(scrolled)
        self.show_all()

        

win = FlowBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()