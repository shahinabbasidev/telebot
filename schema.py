import sqlite3

conn = sqlite3.connect('appointment_service.db')
cursor = conn.cursor()


# user_table
cursor.execute(

    '''
    CREATE TABLE IF NOT EXISTS users(
    user_id TEXT PRIMARY KEY,
    user_name TEXT
    )
    '''
)

# service_table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS services(
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT,
    admin_id text
    )
    '''
)

# slot_table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS slot(
    slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_date TEXT,
    slot_time TEXT,
    slot_status TEXT DEFAULT 'available',
    service_id INTEGER
    )
    '''
)

# Appointment_table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS appointment(
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_id INTEGER,
    user_id TEXT
    )
    '''
)



conn.commit()
conn.close()