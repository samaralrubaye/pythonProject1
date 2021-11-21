import Model.connection
class viber:
    def vibertimes(self):
     Model.connection.conection.mycursor.execute('SELECT msgdates FROM dataforensic.viber_msg')
     datesall = Model.connection.conection.mycursor.fetchall()
     print(datesall)
     print(len(datesall))
v=viber()
v.vibertimes()