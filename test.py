import win32com.client

# Kết nối tới Task Scheduler
scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()a
print("Succes")
