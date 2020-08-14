import mysql.connector
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
from pandastable import Table

def get_db_data():
    cols = ["OBJECTID", "ISO_CODE", "COUNTRY_NAME", "Date_epicrv", "NewCase", "TotalCase","NewDeath","TotalDeath"]

    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Angel4life",
    database = "data_who",
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM data_who.data_who Where Date_epicrv = '2020-04-23T00:00:00.000Z';")
    data = cursor.fetchall()
    mydb.close()

    return cols, data

#def display_plot():
#    df_cols, db_data = get_db_data()
#    data_df = pd.DataFrame(db_data, columns=df_cols).set_index("OBJECTID")
#    
#    data_df.plot(kind='bar',x='COUNTRY_NAME',y='TotalCase') 
#    plt.show()  

def display_plot():
    df_cols, db_data = get_db_data()
    data_df = pd.DataFrame(db_data, columns=df_cols).set_index("OBJECTID")
    
    data_df.plot(kind='bar',x='COUNTRY_NAME',y='TotalDeath') 
    plt.show()  
    
display_plot()