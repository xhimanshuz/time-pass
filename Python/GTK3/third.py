import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class StackWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        #stack.set_transition_duration(100)

        checkButton = Gtk.CheckButton("Click Me")
        stack.add_titled(checkButton, "Check", "Check Button")

        label = Gtk.Label("This is Stack 2")
        stack.add_titled(label, "Label", "Stack 2")

        stackSwitcher = Gtk.StackSwitcher()
        stackSwitcher.set_stack(stack)
        vbox.pack_start(stackSwitcher, 1, 1, 0)
        vbox.pack_start(stack, 1, 1, 0)

win = StackWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
