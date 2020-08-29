#抓取微信好友列表 Ver:20200829
import itchat        # 导入itchat模块库，是管理微信专用
import pandas as pd  # 导入pandas模块库，是读写EXCEL专用，安装时需要同时安装xlrd、xlwt、openpyxl这三个模块库
import datetime
import time
import random

#itchat.login()  #登录（每次登录都要扫二维码）
itchat.auto_login(hotReload=True)  #登录（只扫描一次二维码）
friends = itchat.get_friends(update=True)[0:]  #爬取自己好友相关信息, 返回一个json文件

n=0 #用于后面的好友人数计数
datalist=[]  #准备列表，准备用来存储微信好友数据。 必须要提前定义，否则后面会出错

for i in friends[0:]:          # 遍历这个列表,列表里第一位是自己,所以从"自己"之后开始计算 [1:]表示从第2个到最后
    UserName  = i["UserName"]  #用户名
    NickName  = i["NickName"]  #网名
    RemarkName= i["RemarkName"]#昵称
    Province  = i["Province"]  #省份
    City      = i["City"]      #城市

    # 性别 1是男 2是女 需要转换为字符型后再替换
    sex = str(i["Sex"]).replace("1", "男").replace("2", "女").replace("0", "其他")

    #签名 签名会有很多表情或者换行，需要过滤掉
    Signature = i["Signature"].replace("<span","").replace("class","").replace("</span>","").replace("emoji","").replace(" ","").replace("\n","").replace(",","，")

    n=n+1 #好友人数计数
    #打印输出显示，每列之间加逗号，可以利用excel的文本导入功能导入excel中
    print("第",n,"位好友：,",UserName,',' ,NickName,',',RemarkName,',',sex,',',Province,',',City,',',Signature)

    # 生成微信好友信息列表，以备后面写入EXCEL文件中。
    # 注意：此处各列内容的个数，要与后面各列名称的个数相同
    datalist=datalist+[[str(n),UserName,NickName,RemarkName,sex,Province,City,Signature]]

# list转dataframe 。此处实际就是EXCEL中各列的标题，个数要与上面列的个数相对应
df = pd.DataFrame(datalist, columns=['顺序号','id','网名','昵称','性别','省份','城市','签名'])

# 保存到本地excel
df.to_excel("C://微信好友列表.xlsx", index=False)
print('微信好友列表已经采集完成并保存到文件【微信好友列表.xlsx】，程序结束')