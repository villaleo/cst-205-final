import header as h
import home_window as home

app = h.QApplication(h.sys.argv)
main = home.HomeWindow()
main.show()
h.sys.exit(app.exec_())
