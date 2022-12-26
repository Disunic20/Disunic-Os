import sys
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found\n Run - pip install googlesearch-python")

class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        query = input("DisunicX : ")
        print("")
        print("Here Is Some Result From DisunicX . . . . .")
        for disunicx in search(query, tld="co.in", num=10, stop=10, pause=2):
            print("")
            print(disunicx)
        print("")


        Browse = input("Enter Url To Open : ")

        self.browser = QWebEngineView()
 
        # setting default browser url as google
        self.browser.setUrl(QUrl(Browse))
 
        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)
 
        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)
 
        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)
 
        # creating a status bar object
        self.status = QStatusBar()
 
        # adding status bar to the main window
        self.setStatusBar(self.status)
 
        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")

        navtb.setMovable(False)
 
        # adding this tool bar tot he main window
        self.addToolBar(navtb)
 
        # adding actions to the tool bar
        # creating a action for back
        back_btn = QAction("Back", self)
 
        # setting status tip
        back_btn.setStatusTip("Back to previous page")
 
        # adding action to the back button
        # making browser go back
        back_btn.triggered.connect(self.browser.back)
 
        # adding this action to tool bar
        navtb.addAction(back_btn)
 
        # similarly for forward action
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
 
        # adding action to the next button
        # making browser go forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
 
        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
 
        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
 
        # similarly for home action
        home_btn = QAction("Google", self)
        home_btn.setStatusTip("Google")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
 
        # adding a separator in the tool bar
        navtb.addSeparator()
 
        # creating a line edit for the url
        self.urlbar = QLineEdit()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(4)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.urlbar.setGraphicsEffect(self.shadow)
 
        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
 
        # adding this to the tool bar
        navtb.addWidget(self.urlbar)
 
        # adding stop action to the tool bar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
 
        # adding action to the stop button
        # making browser to stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
 
        # showing all the components
        self.show()
 
 
    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - DisunicX Light" % title)
 
 
    # method called by the home action
    def navigate_home(self):
 
        # open the google
        self.browser.setUrl(QUrl("http://www.google.com"))
 
    # method called by the line edit when return key is pressed
    def navigate_to_url(self):
 
        # getting url and converting it to QUrl object
        q = QUrl(self.urlbar.text())
 
        # if url is scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")
 
        # set the url to the browser
        self.browser.setUrl(q)
 
    # method for updating url
    # this method is called by the QWebEngineView object
    def update_urlbar(self, q):
 
        # setting text to the url bar
        self.urlbar.setText(q.toString())
 
        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)
    
    

 
# creating a pyQt5 application
app = QApplication(sys.argv)
app.setStyleSheet('''
QToolBar {
    background:white;
}
#home_btn{background-color:red;color:white}
QLineEdit{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    padding-top:4px;
    padding-left:8px;
    padding-bottom:4px;
    border:2px solid transparent;
    border-radius: 4px;
    font-size:15px;
    background-color: #fffefe;
    font-weight: 500;
    color: black;
    height: 22px;

}

QLineEdit:focus{
    border-color:#52a2f8;
    background: white;
    
}

QLineEdit:hover{
    border-color:#208bfd;
}
''')
    
    # setting name to the application
app.setApplicationName("DisunicX Light")
    
    # creating a main window object
window = MainWindow()
    
    # loop
app.exec_()