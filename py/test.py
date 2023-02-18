
import datetime
DateTime = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
Recipe = '3.000.228-004'
Serial = "403761010722B05573750840735494070S"
DeviceId = "3750840735494070"
BatchNumb = '2312547'
BoxNumb = 'None'
TrayNumb = 'None'
CavityNumb = 'None'
Result = 'Good'

print(r"insert into SEN4XSgpSht values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(DateTime,Recipe,Serial,DeviceId,BatchNumb,BoxNumb,TrayNumb,CavityNumb,Result))
