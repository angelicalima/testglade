import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

class testglade:
    texto = ''
    def __init__(self):
        self.gladefile = "painelprincipalglade.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        self.window = self.wTree.get_widget("window1")
        if self.window:
            self.window.connect("destroy", gtk.main_quit)

        dic = {"on_btncopiar_clicked": self.on_btncopiar_clicked,
               "on_btncolar_clicked": self.on_btncolar_clicked}
        self.wTree.signal_autoconnect(dic)

        self.window.show()

    def on_btncopiar_clicked(self, widget):
        self.texto =  self.wTree.get_widget("entexto").get_text()
        self.wTree.get_widget("entexto").set_text('')

    def on_btncolar_clicked(self, widget):
        print self.texto

if __name__ == "__main__":
        hwg = testglade()
        gtk.main()