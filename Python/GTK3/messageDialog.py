import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MessageDialogWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="MessageDialog Example")

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Information")
        button1.connect("clicked", self.on_info_clicked)
        box.add(button1)


        button4 = Gtk.Button("Question")
        button4.connect("clicked", self.on_question_clicked)
        box.add(button4)

    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "This is an Ino msg")
        dialog.format_secondary_text("This is an fucking secondary msg")
        dialog.run()
        print("ERROR dialog Closed")

        dialog.destroy()

    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "This is a Primary Question Msg")
        dialog.format_secondary_text("This is an Secondary Message")

        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            print("Fucking Yes")
        elif response == Gtk.ResponseType.NO:
            print("Fucking No")
        
        dialog.destroy()

win = MessageDialogWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()