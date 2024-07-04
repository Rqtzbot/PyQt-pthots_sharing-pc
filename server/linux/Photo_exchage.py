#导入相关库
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import time
import cv2
import os
import sys
import threading
from PyQt5.QtWidgets import *  
from Ui_photo_exchange import Ui_MainWindow
from PyQt5.QtGui import QImage,QPixmap
import websockets
from websockets import exceptions
import asyncio
class PICM(QWidget):
    #自定义信号和槽
    emitdata = pyqtSignal(str)
    #构造函数
    def __init__(self): 
       super(PICM,self).__init__()
       self.myapp = Ui_MainWindow()
       self.form = QMainWindow()
       self.myapp.setupUi(self.form)
       #初始化信号和槽
       self.myapp.start.clicked.connect(self.newprocess)
       self.myapp.enlage.clicked.connect(self.enlage)
       self.myapp.reduce.clicked.connect(self.reduce)
       self.myapp.disconn.clicked.connect(self.disconnect)
       self.myapp.sutoip.clicked.connect(self.autoip)
       self.myapp.up.clicked.connect(self.uppic)
       self.myapp.down.clicked.connect(self.downpic)
       self.myapp.selectsend.clicked.connect(self.selectpic)
       self.emitdata.connect(self.showdata) 
       self.myapp.selectsave.clicked.connect(self.openpicdiy)
       self.myapp.savepicbtn.clicked.connect(self.savepic)
       self.myapp.sendpic.clicked.connect(self.sendpic)
       self.myapp.scaleSlider.valueChanged.connect(lambda value: self.sildercol(value))

       #设置siloder
       self.myapp.scaleSlider.setValue(0)
       self.myapp.scaleSlider.setMaximum(0)
       self.myapp.scaleSlider.setMinimum(-30)
       self.myapp.scaleSlider.setPageStep(3)

       #反转siloder
       self.myapp.scaleSlider.setInvertedAppearance(True)

       #statusbar显示logo
       lab = QLabel()
       lab.setPixmap(QPixmap("13.png").scaled(50,28))
       self.myapp.statusbar.addWidget(lab)

       #设置窗口大小
       self.form.setMaximumHeight(750)
       self.form.setMaximumWidth(1250)
       
       #设置标题
       self.form.setWindowTitle("Photos Sharing Server")

       #图像二进制列表
       self.imagelist = []

       #存储发送的图片数据
       self.seimage_data = ""

       #缩放初始倍数的3倍
       self.scale_percent = 3  

       #按钮使能
       self.myapp.down.setDisabled(True)
       self.myapp.up.setDisabled(True)
       self.myapp.disconn.setDisabled(True)

       #发送图片标志位
       self.sendflag = False
       self.closeflag = False

       #messagebox提示
       msg_box = QMessageBox(QMessageBox.Information, "温馨提示", "请先点击“启动”按扭，否则无法使用")
       msg_box.exec_()
    #启用子线程
    def newprocess(self):
        if self.myapp.port.text() == "" or self.myapp.ip.text() == "":
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【错误】："+"请输入端口或者ip地址")
        else:
            th = threading.Thread(target=self.connect_server)
            th.start()
            self.myapp.start.setDisabled(True)
    #信号和槽显示数据
    def showdata(self,data):
        self.myapp.picdata.append("【"+str(time.time())+"】"+data)
    #异步发送数据
    async def send(self,websocket):
        while True:
            #点击发送图片按钮后，标志位为真
            if self.sendflag:
                #此时的self.curr_bytedata存储的二进制数据为选择的图片
                await websocket.send(self.curr_bytedata)
                self.sendflag = False
                self.emitdata.emit("发送成功！")
            #点击断开连接按钮后
            if self.closeflag:
                #关闭websocket
                await websocket.close()
                #显式的停止事件循环
                loop =  asyncio.get_event_loop()
                loop.stop()
                #跳出循环,终止协程
                break
            #此协程挂起1s，切换到其他协程。
            await asyncio.sleep(1)
    #异步接收据
    async def receive(self,websocket):
        self.emitdata.emit(f"客户端连接成功，连接到{websocket.remote_address}")
        try:
            async for message in websocket:
                self.curr_bytedata = message
                #字节大小
                # print(len(message))
                self.show_image()
        except  websockets.ConnectionClosedError:
            self.emitdata.emit("客户端意外断开连接，请客户端重连")
    #websocket处理函数
    async def handler(self,websocket,path):
        self.myapp.disconn.setDisabled(False)
        #创建两个task，分别为发送和接收
        sendtask = asyncio.get_event_loop().create_task(self.send(websocket))
        receivetask = asyncio.get_event_loop().create_task(self.receive(websocket))
        #异步执行
        try:
            await sendtask
            await receivetask
        except exceptions.ConnectionClosedOK:
            self.myapp.picdata.append("连接已关闭")
    #初始化websocket服务器，异步
    def connect_server(self):
        self.emitdata.emit("【提示】："+"服务器监听中")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(self.handler,self.myapp.ip.text(), 8899,max_size=7000000)
        loop.run_until_complete(start_server)
        loop.run_forever()
        #在显式的stop事件循环后,取消所有任务
        for task in asyncio.all_tasks(loop):  
                task.cancel()
                # print(task.cancelled())
        loop.close()
    #断开websocket连接
    def disconnect(self):
        self.closeflag = True
        self.myapp.disconn.setDisabled(True)
        self.myapp.picdata.append("断开连接")
    #显示图像
    def show_image(self):
       #将二进制数据self.curr_bytedata转换为NumPy数组，数据类型为np.uint8。
       binarydata = np.frombuffer(self.curr_bytedata,np.uint8)
       #将二进制数据解码为图self.image，解码格式为彩色（cv2.IMREAD_COLOR）。
       self.image = cv2.imdecode(binarydata,cv2.IMREAD_COLOR)
        #将图像从BGR格式转换为RGB格式
       value = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
       #获取图像的高度、宽度和通道数
       height, width, channels = self.image.shape
       # 转换成QImage在 ui上显示
       images = QImage(value.data, width, height, width * channels, QImage.Format_RGB888)
       flag = False
       #将每次显示的不同的图像加入imagelist列表中，为按钮切换上，下张准备
       for k in range(len(self.imagelist)):
            if self.curr_bytedata == self.imagelist[k]:
                flag = True
       if flag == False:
            self.imagelist.append(self.curr_bytedata)
            self.number = len(self.imagelist)
            #图片为2张及以上时使能上一张下一张按钮
            if self.number > 1:
                self.myapp.up.setDisabled(False)
                self.myapp.down.setDisabled(False)
       #显示图片 
       self.myapp.image.setPixmap(QPixmap.fromImage(images).scaled(int(width/self.scale_percent),int(height/self.scale_percent)))
    #放大图像，scale_percent越小图片越大，初值为3
    def enlage(self):
        self.scale_percent -= 0.3
        #round保留一位小数
        if round(self.scale_percent,1) == 0.0:
             self.myapp.picdata.append("【"+str(time.time())+"】"+"【警告】："+"已达到最大放大限度")
             self.scale_percent = 3
        else:
            self.show_image()
            diff = 3 - self.scale_percent
            self.myapp.scaleSlider.setValue(-int(diff*10))
            # print(-int(diff*10))
    #缩小图像,scale_percent越大图片越小，初值为3
    def reduce(self):
        if self.scale_percent < 3:
            self.scale_percent += 0.3
            if round(self.scale_percent,1) == 0.0:
                self.scale_percent = 3
                self.show_image()
            diff = 3 - self.scale_percent
            self.myapp.scaleSlider.setValue(-int(diff*10))
        else:
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【警告】："+"当前为原始尺寸，无法缩小")    
    #silder控制
    def sildercol(self,value):
        self.scale_percent = 3+value/10
        # print(value)
        self.myapp.scale.setText(str(round(abs((value)/3*10),2))+"%")
        if round(self.scale_percent,1) != 0.0 :
                self.show_image()
        else:
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【警告】："+"已达到最大放大限度")
    #自动识别ip
    def autoip(self):
        if os.name == 'nt':
            # print("当前操作系统是Windows")
            output = os.popen("ipconfig | findstr \"IPv4\"").read()
            ip = output.split("\n")
            self.myapp.ip.setText(ip[1].split(": ")[1]) 
        elif os.name == 'posix':
            # print("当前操作系统是Linux")
            output = os.popen("ifconfig | awk '/inet /{print $2}'").read()
            ip = output.split("\n")
            self.myapp.ip.setText(ip[1]) 
        elif os.name == 'darwin':
            # print("当前操作系统是Mac")
            output = os.popen("ifconfig en0 | awk '/inet /{print $2}'").read()
            self.myapp.ip.setText(output)      
    #选择保存目录
    def openpicdiy(self):
        self.filename = QFileDialog.getExistingDirectory(self,"选择目录")
        self.myapp.path.setText(self.filename)
    #保存图片
    def savepic(self):
        if self.myapp.rename.text() == "":
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【警告】："+"请重命名图片")
        else:
            filepath = self.filename+"/"+self.myapp.rename.text()
            cv2.imwrite(filepath,self.image)
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【提示】："+f"成功保存至{filepath}")
    #选择图片
    def selectpic(self):
        filename,_= QFileDialog.getOpenFileName(self,"选择文件","","(*.png);;(*.jpg);;(*.bmp)")
        if filename :
            self.myapp.sendpath.setText(filename)
            with open(filename,'rb') as file:
                self.seimage_data = file.read()
            #选择完成后转为字节
            self.curr_bytedata = bytes(self.seimage_data)
            self.show_image()
    #发送图片
    def sendpic(self):
        if self.seimage_data == "":
            self.myapp.picdata.append("【"+str(time.time())+"】"+"【警告】："+"当前未选择发送图片")
        else:
            self.sendflag = True
    #上一张
    def uppic(self):
        self.number -= 1
        if self.number  < 1:
            self.number = len(self.imagelist)
            self.curr_bytedata = self.imagelist[self.number-1]
            self.show_image()
        else:
            self.curr_bytedata = self.imagelist[self.number-1]
            self.show_image()  
    #下一张
    def downpic(self):
        self.number += 1
        if self.number > len(self.imagelist):
            self.number = 1
            self.curr_bytedata = self.imagelist[self.number-1]
            self.show_image()
        else:
            self.curr_bytedata = self.imagelist[self.number-1]
            self.show_image()            
#主函数
if __name__ == "__main__":
    app  = QApplication(sys.argv)
    picm = PICM()
    picm.form.show()     
    sys.exit(app.exec_())