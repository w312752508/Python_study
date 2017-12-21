import os,sys,logging,time,json
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import auth_who
from core import who
logger_who = logging.getLogger("who_log")
logger_who.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\who.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_who.addHandler(fh)
logger_who.info("新用户访问。")
def class_re(user):
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\data\teacher_message" % file, "r", encoding="utf-8") as file_passwd:
        a = json.load(file_passwd)
    course_teac = a[user]['course']
    class_n = a[user]["class_name"]
    print("教师姓名：%s\n"
          "授课教程：%s\n"
          "负责班级：%s\n"%(user,course_teac,class_n))
def stu_re(user):
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\data\teacher_message" % file, "r",encoding = "utf-8") as file_passwd:
        a = json.load(file_passwd)
    with open(r"%s\data\student_message" % file, "r", encoding="utf-8") as file_passwd:
        st = json.load(file_passwd)
    course_teac = a[user]['course']
    stu_new =[]
    for b in a[user]["class_name"]:
        for k,v in st.items():
            if st[k]["course"] == course_teac and st[k]["class_mes"] == b :
                stu_new.append(k)
        print("%s学员有："%b,stu_new)
    print(" ")
def stu_manager(user):
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\data\teacher_message" % file, "r",encoding = "utf-8") as file_passwd:
        a = json.load(file_passwd)
    with open(r"%s\data\student_message" % file, "r", encoding="utf-8") as file_passwd:
        st = json.load(file_passwd)
    course_teac = a[user]['course']
    stu_new ={}
    for b in a[user]["class_name"]:
        for k,v in st.items():
            if st[k]["course"] == course_teac and st[k]["class_mes"] == b :
                print("%s学员%s,成绩：%s" %(b,k,st[k]["grade"]))
    while True:
        revise_name = input("输入修改的学生名：")
        if revise_name == "q":
            break
        elif revise_name in st.keys() and st[revise_name]["course"] == course_teac and st[revise_name]["class_mes"]:
            revise_num = input("输入修改的分数：")
            st[revise_name]["grade"] = revise_num
            with open(r"%s\data\student_message" % file, "w", encoding="utf-8") as file_passwd:
                json.dump(st, file_passwd)
            print("学员%s成绩修改成功,新成绩为：%s。\n" % (revise_name,revise_num))
            break
        else:
            print("输入学员姓名有误，请重新输入\n")
            continue