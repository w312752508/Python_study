import pymysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",db="test")
cursor = conn.cursor()
while True:
    commd = input(">>:")
    if commd == "exit":
        break
    else:
        try:
            cursor.execute(commd)
            print(cursor.fetchone())
            for a in cursor.fetchall():
                print(a)
            conn.commit()
        except Exception as error:
            print(error)
cursor.close()
conn.close()