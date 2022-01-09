import mysql.connector


class conection:
  mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wsmu2001.",
  port='3306',
  database='dataforensic')

  mycursor=mydb.cursor(buffered=True)
  args = [123,]
  #mycursor.execute('SELECT idviber_msg,viber_Latitude, vlongitude FROM viber_msg')
  #w=mycursor.callproc('EXAMINERNAME')
  #mycursor.stored_results()
  #for result in mycursor.stored_results():
  # print(result.fetchall())

  #print(R)
 # print(w)
  #viber_msgs = mycursor.fetchall()
  #print(list(R[0]))



  #for email in emails:
  # print(viber_msgs[0])
