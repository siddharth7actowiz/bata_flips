from config import *
from utils import *
from parser import parser
from db import *
import time

def main():
    st=time.time()
    data=read_html(FILE_PATH)
    extracted_data=parser(data)
    print(extracted_data)
    con = make_connection()
    cursor = con.cursor()

    create_table(cursor)

  

    insert_into_db(cursor, con, extracted_data)

    cursor.close()
    con.close()
    print(time.time()-st)
if __name__ == "__main__":
    main()
  
