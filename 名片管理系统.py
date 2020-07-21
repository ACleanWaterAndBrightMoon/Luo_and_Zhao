print("*"*30)
print("欢迎使用【名片管理系统】V1.0")
print("")
print("1.新建名片")
print("2.显示全部")
print("3.查询名片")
print("")
print("0.退出系统")
print("*"*30)

Show_list=["name","phone","qq","email"]

Card_list=[]

def BusinessCardsystem():
    a=int(input("请输入要选择的按钮:"))
    while a>3 or a<1:
        a=int(input("请重新输入:"))
    while 1:
        if a==1:
            Single_dict={}
            Card_list.append(build_new_Card(Single_dict))
            Single_dict.clear
        if a==2:
            if len(Card_list)==0:
                print("无名片记录")
            else:
                show_Card(Show_list,Card_list)
        if a==3:
            print("5.修改名片")
            print("6.删除名片")
            k=int(input("请输入要查询的功能:"))
            while k<5 or k>7:
                k=int(input("请重新输入"))
            if k==5:
                flag=0
                name=str(input("请输入要修改的名片人的名字:"))
                while 1:
                    for index in Card_list:
                        if index["name"]==name:
                            changeCard(Card_list,name)
                            flag=1
                            break
                    if flag==0:
                        name=str(input("请重新输入要修改的名片人的名字:"))
                    else:
                        break
            if k==6:
                name=str(input("请输入要删除的名字:"))
                while 1:
                    flag=0
                    count=0
                    for index in Card_list:
                        if index["name"]==name:
                            Card_list.pop(count)
                            flag=1
                            break
                        count+=1
                    if flag==0:
                        name=str(input("请输入要删除的名字:"))
                    else:
                        break
                print("删除成功!")
        if a==0:
            break
        a=int(input("请输入要选择的按钮:"))
    print("欢迎下次使用本系统!")

def build_new_Card(Card):
    Card["name"]=str(input("请输入姓名:"))
    Card["phone"]=str(input("请输入电话:"))
    Card["qq"]=str(input("请输入QQ号码:"))
    Card["email"]=str(input("请输入邮件:"))
    return Card

def show_Card(Show_list,Card_list):
    for k in Show_list:
        print("%s\t"%k,end="")
    print("")
    print("-"*40)
    for index in Card_list:
        for k in Show_list:
            print("%s\t"%index[k],end="")
        print("")

def changeCard(Card_list,name):
    Object=str(input("请输入要修改此人的选项:"))
    while 1:
        flag=0
        for k in Show_list:
            if k==Object:
                flag=1
                break
        if flag==1:
            break
        else:
            Object=str(input("请重新输入要修改此人的选项:"))
    for index in Card_list:
        if index["name"]==name:
            change=str(input("修改为:"))
            index[Object]=change

BusinessCardsystem()