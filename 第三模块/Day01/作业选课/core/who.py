#!_*_coding=utf-8 _*_
#homework:who
import os,json
class School(object):
    member = 0
    def enroll(self):
        name = input("输入姓名：")
        age = input("年龄：")
        course = input("报名课程：")
        class_choss = input("选择班级：")
        passwd = input("输入学员登录密码：")
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\data\student_message" % file, "r") as st_m:
            stud_mess = json.load(st_m)
        with open(r"%s\data\user_passwd" % file, "r") as st_ps:
            new_stu_ps = json.load(st_ps)
        stud_mess[name] = {"age":age,"course":course,"class":class_choss,}
        new_stu_ps[name] = passwd
        with open(r"%s\data\student_message" % file, "w") as st_m:
            json.dump(stud_mess,st_m)
        with open(r"%s\data\user_passwd" % file, "w") as st_ps:
            json.dump(new_stu_ps,st_ps)
        School.member +=1
        print("\033[31;1m恭喜%s报名成功，报名课程：%s，您所在的班级为%s\033[0m\n"
              %(name,course,class_choss))

    def new_course(self):
        while True:
            course = input("输入新课程名：")
            if course == "q":
                break
            else:
                school = input("输入分校名：")
                period = input("输入新课程周期：")
                schooling = input("输入新课程学费：")
                file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                with open(r"%s\data\course_message" % file, "r", encoding="utf-8") as file_cl:
                    cou = json.load(file_cl)
                cou[course] = {"school":school,"period":period,"schooling":schooling}
                with open(r"%s\data\course_message" % file, "w", encoding="utf-8") as file_cl:
                    json.dump(cou,file_cl)
                print("%s分校新增课程：%s,周期：%s，学费：%s" %(school,course,period,schooling))
                break
    def new_class(self):
        while True:
             course = input("输入课程名：")
             if course == "q":
                 break
             else:
                 school = input("输入分校名：")
                 class_name = input("输入新班级名：")
                 file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                 with open(r"%s\data\class_mess" % file, "r", encoding="utf-8") as file_cl:
                     cl = json.load(file_cl)
                 if school in cl[course] :
                     cl[course][school].append(class_name)
                     with open(r"%s\data\class_mess" % file, "w", encoding="utf-8") as file_cl:
                         json.dump(cl,file_cl)
                     print("%s分校%s课程新增%s成功"%(school,course,class_name))
                     break
                 else:
                     print("输入分校或课程错误，请重新输入\n")
    def new_teacher(self):
        while True:
            new_name = input("输入新教师名：")
            if new_name == "q":
                break
            else:
                age = input("输入新教师年龄：")
                course_name = input("授课课程：")
                class_name = input("管理班级：")
                file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                with open(r"%s\data\teacher_message" % file, "r", encoding="utf-8") as file_te:
                    te = json.load(file_te)
                te[new_name] = {"age":age,"course":course_name,"class_name":[class_name]}
                with open(r"%s\data\teacher_message" % file, "w", encoding="utf-8") as file_te:
                    json.dump(te,file_te)
                print("%s课程%s新增%s老师成功" % (course_name,class_name,new_name))
                break