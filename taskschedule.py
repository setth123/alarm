import win32com.client

def add_task(name,start_day,enable):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    tasks = root_folder.GetTasks(0)
    new_task=scheduler.NewTask(0)
    new_task.RegistrationInfo.Description = "Báo thức lúc "+name
    new_task.Settings.Enabled = enable
    trigger = new_task.Triggers.Create(1)  # 1 tương ứng với DailyTrigger
    trigger.StartBoundary = start_day  # Đặt thời điểm bắt đầu  
    trigger.DaysInterval = 1  
    action = new_task.Actions.Create(0)  # 0 tương ứng với ExecAction
    action.Path = r'C:\Users\Administrator\Documents\TaskScheduler\alarm.py'
    action.Arguments = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe'
    tasks.AddTask(name, new_task)
def dele(name):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    tasks = root_folder.GetTasks(0)
    tasks.RemoveTask(name)
def alter(new_name,new_start_day,old_name):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    tasks = root_folder.GetTasks(0)
    task = tasks.Item(old_name)
    trigger = task.Triggers[0]
    trigger.StartBoundary = new_start_day 
    task.Definition.RegistrationInfo.Description = new_name
    tasks.AddTask(new_name, task)
def toggle(active,name):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    tasks = root_folder.GetTasks(0)
    task = tasks.Item(name)
    task.Settings.Enabled = active
    task.AddTask(name, task)

