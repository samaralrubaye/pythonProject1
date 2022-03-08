import io
from logging.handlers import SysLogHandler
import sys
from wsgiref.simple_server import sys_version
from xml.parsers import expat
from xmlrpc.client import SYSTEM_ERROR
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from allEmail import allEmail
from allViber import allViber
from allWhatsApp import allWhatsApp






"""
Folium in PyQt5
"""
class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 160, 120
        self.setMinimumSize(self.window_width, self.window_height)
       # self.WhatsAppgeographicLocation(allViber)
        #self.vibergeographicLocation()
       # self.EmailgeographicLocation()
        self.WhatsAppgeographicLocation()
        

    def WhatsAppgeographicLocation(self):
        emails=allEmail.getAllEmails(self,88888,'2000/1/1','4000/1/1','')
        
        map=folium.Map(location=[10.821190,78.4159423],zoom_start=5,titles='stamen Toner')
        fg= folium.FeatureGroup(name='Marker')
        for i in emails:
            try:
                # print(i.FromEmail_latitude + ' - ' +i.FromEmail_longtude)
                fg.add_child(folium.Marker(location=[i.FromEmail_latitude, i.FromEmail_longtude],popup=i.FromEmail_lastname))
            except:
                break
        map.add_child(fg)
        map.save("index.html")
      
        data = io.BytesIO()
        map.save(data, close_file=False)
        webView = QWebEngineView()

        webView.setHtml(data.getvalue().decode())
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(webView)

     
   
        
    def vibergeographicLocation(self):
        vibers=allViber.getAllVibers(self,88888,'2000/1/1','4000/1/1','')
        
        map=folium.Map(location=[10.821190,78.4159423],zoom_start=5,titles='stamen Toner')
        fg= folium.FeatureGroup(name='Marker')
        for i in vibers:
            try:
                # print(i.FromEmail_latitude + ' - ' +i.FromEmail_longtude)
                fg.add_child(folium.Marker(location=[i.FromViber_Msg_Latitude, i.FromViber_Msg_Longtude],popup=i.FromViber_Msg_FirstName))
            except:
                break
        map.add_child(fg)
        map.save("index.html")
      
        data = io.BytesIO()
        map.save(data, close_file=False)
        
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(webView)
    
    def WhatsAppgeographicLocation(self):
        WhatsApps= allWhatsApp.getAllWhatsApp(self,88888,'2000/1/1','4000/1/1','')
        
        map=folium.Map(location=[10.821190,78.4159423],zoom_start=5,titles='stamen Toner')
        fg= folium.FeatureGroup(name='Marker')
        for i in  WhatsApps:
         
                # print(i.FromEmail_latitude + ' - ' +i.FromEmail_longtude)
             fg.add_child(folium.Marker(location=[i.FromWhatsApp_Msg_Latitude, i.ToWhatsApp_Msg_Longtude],popup=i.FromWhatsApp_Msg_FirstName))
           
             
        

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