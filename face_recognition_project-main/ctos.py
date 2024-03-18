import pandas as pd
import sqlite3
df=pd.read_csv('Attendance\Attendance_.csv')
conn=sqlite3.connect('ads_attendance.db')
df.to_sql('students',conn,if_exists='replace',index=False)
conn.commit()
conn.close()