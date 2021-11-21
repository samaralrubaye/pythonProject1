
import mysql.connector
class conection:
  mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wsmu2001.",
  port='3306',
  database='dataforensic')

  mycursor=mydb.cursor()


  mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')

  viber_msgs = mycursor.fetchall()



  #for email in emails:
  # print(viber_msgs[0])
