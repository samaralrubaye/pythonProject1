import io
from logging.handlers import SysLogHandler
import sys
from wsgiref.simple_server import sys_version
from xmlrpc.client import SYSTEM_ERROR
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from allEmail import allEmail





"""
Folium in PyQt5
"""
class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 160, 120
        self.setMinimumSize(self.window_width, self.window_height)
        self.ggg
    def ggg(self):
        emails=allEmail.getAllEmails(self)
        
        map=folium.Map(location=[10.821190,78.4159423],zoom_start=5,titles='stamen Toner')
        fg= folium.FeatureGroup(name='Marker')
        for i in emails:
            print(i.FromEmail_latitude + ' - ' +i.FromEmail_longtude)
            fg.add_child(folium.Marker(location=[i.FromEmail_latitude, i.FromEmail_longtude],popup=i.FromEmail_lastname))
        return fg
    
        

        map.add_child(fg)
        map.save("index.html")
      
        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(webView)

        
    def cordinate(self,x,y):
        layout = QVBoxLayout()
        self.setLayout(layout)
        coordinate = (x, y)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=2,
        	location=coordinate
        )
  
   
        folium.Marker([x, y],popup=' name' ).add_to(m)
  # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')