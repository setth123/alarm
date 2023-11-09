import sqlite3
import re
def m_init():
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS soundtrack (path VARCHAR(50),name VARCHAR(20))''')
    connection.commit()
    connection.close()

def generate_new_name(cursor, base_name):
    cursor.execute('''SELECT * FROM soundtrack ''')
    existing_records = cursor.fetchall()
    if existing_records:
        count=0
        for record in reversed(existing_records):
            check=re.sub(r'\(\d+\)$', '', record[1])
            if(check==record[1]):
                count=1
                break
            if (check == base_name):
                # Nếu tên trước dấu ngoặc đơn giống với base_name, tăng số lần xuất hiện lên 1
                tempstr=record[1]
                count=int(tempstr[-2])+1
                break
        # Nếu không có bản ghi nào trùng tên, tạo bản ghi mới với base_name
        count=str(count)
        if(count!=0):
            new_name = f'{base_name}({count})'
        else:
            new_name=base_name
        return new_name
    else:
        return base_name
def m_add(path,name):
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    m_init()
    new_name = generate_new_name(cursor, name)
    cursor.execute('''INSERT INTO soundtrack(path,name) VALUES (?,?)''',(path,new_name))
    connection.commit()
    connection.close()  
def m_show():
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM soundtrack''')
    records=cursor.fetchall()
    connection.commit()
    connection.close()
    return records  
def m_dele(path):
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''DELETE FROM soundtrack WHERE name=?''',(path,))
    connection.commit()
    connection.close()

connection=sqlite3.connect('localdb.db')
cursor=connection.cursor()