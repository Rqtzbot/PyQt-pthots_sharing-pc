const WebSocketbtn = document.getElementById("WebSocketbtn");
const selfilebtn = document.getElementById("selfilebtn");
const sendfilebtn = document.getElementById("sendfilebtn");
const pic = document.getElementById("pic");
const dataval = document.getElementById("dataval");
const sendpic = document.getElementById("sendpic");
const fileInput = document.getElementById("fileinput");
const px = document.getElementById("px");
const ram = document.getElementById("ram");
const type = document.getElementById("type");
const nameval = document.getElementById("name");
const photos = document.getElementById("photos");
const fengche = document.getElementsByClassName("fengche")[0];
const commuction = document.getElementById("commuction");
const moren = document.getElementById("moren");
const ipaddr = document.getElementById("ipaddr");
const ipbtn = document.getElementById("ipbtn");
const disWebSocketbtn = document.getElementById("disWebSocketbtn");
const select = document.getElementById("selectment")
var socket;var ip = "";
var rece_picblob = new Blob();
var jpgflag = false,pngflag = false,bmpflag = false;
var currimagedata = new Image();
var scale = 2.5;
//查询localstorage是否存有数据
if(localStorage.getItem("ipaddress"))
    ipaddr.value=localStorage.getItem("ipaddress");
//使用localstorage设置默认IP地址
moren.addEventListener("click",function(){
    if(ipaddr.value=="")
        alert("请输入IP地址");
    else    
    {
        localStorage.setItem("ipaddress", ipaddr.value);
        alert("设置成功");
    }
});
//立即绑定按钮，获取输入框ip
ipbtn.addEventListener('click',function(){
    ip = ipaddr.value;
});
//websocket发送消息函数
function sendMessage(message) {
    socket.send(message);
    dataval.value+="图片发送成功!\n";
 };
//断开websocket
disWebSocketbtn.addEventListener('click',function(){
    socket.close();
});
//选择文件，单击div连接到file类型input
selfilebtn.addEventListener("click",function(){
    document.getElementById("fileinput").click();
});
//选择缩放倍数
select.addEventListener("change",function(){
    if(select.value == "option1"){scale = 2.5;photos.width = currimagedata.width / scale;photos.height = currimagedata.height / scale;}
    else if(select.value == "option2"){scale = 1.5;photos.width = currimagedata.width / scale;photos.height = currimagedata.height / scale;}
    else if(select.value == "option3"){scale = 0.5;photos.width = currimagedata.width / scale;photos.height = currimagedata.height / scale;}
});
//保存图片
sendpic.addEventListener("click",function(){
    if(rece_picblob.size == 0)
        alert("当前没有受到服务器发来的任何数据")
    else
    {
        if(pngflag)
        {
            saveAs(rece_picblob,"output.png");
            pngflag = false;
        }
        else if(jpgflag)
        {
            saveAs(rece_picblob,"output.jpg");
            jpgflag = false;
        }
        else if(bmpflag)
        {
            saveAs(rece_picblob,"output.bmp");  
            bmpflag = false;
        }
        dataval.value+='图片保存成功\n';
        
    }
    
});
//连接websocket
WebSocketbtn.addEventListener("click",function(){
    console.log(ip)
    if(ipaddr.value =="" || ip == "" )
        alert("请输入IP地址或绑定ip");
    else
    {
        socket = new WebSocket('ws://'+ip+':8899/handler');
    //连接成功，小风车转起来
        socket.addEventListener('open', (event) => {
            dataval.value += 'WebSocket连接成功!\n';
            fengche.style.animation = 'fengche 2s linear infinite';
            commuction.innerHTML = "通信运行中";

            });
    //接收服务器发来的图片数据
        socket.addEventListener('message', (event) => {
            dataval.value+='图片接收成功\n';
            //将blob对象赋值给变量
            rece_picblob = event.data;
            const reader = new FileReader();
            //以arraybutter的形式读取blob数据
            reader.readAsArrayBuffer(event.data);
            reader.onloadend = function() {
                //获取blob的arraybuffer对象
                const arraybuffer = this.result;
                //转换为uint8Array
                const uint8Array = new Uint8Array(arraybuffer);
                console.log(uint8Array)
                // 检查前两个字节是否符合 JPG 文件的特征
                if (uint8Array[0] === 0xFF && uint8Array[1] === 0xD8) {
                    jpgflag = true;
                    type.value = "image/jpg";
                }
                // 检查前两个字节是否符合 PNG 文件的特征
                else if (uint8Array[0] === 0x89 && uint8Array[1] === 0x50) {
                    pngflag = true;
                    type.value = "image/png";
                }
                else if (uint8Array[0] === 0x42 && uint8Array[1] === 0x4D) {
                    bmpflag = true;
                    type.value = "image/bmp";
                }
               
            }
            
           
            //读取URL,赋值给image的src属性，显示图片
            const url = URL.createObjectURL(event.data);
            //将URL存入到其中的src属性
            currimagedata.src = url;
            //图片读取完成后，计算相关属性
            currimagedata.onload = function() {
                var width = currimagedata.width;
                var height = currimagedata.height;
                px.value = width+"x"+height+"px";
                ram.value = rece_picblob.size+"字节";
                nameval.value = "";
                
                //scale倍缩放
                photos.width = currimagedata.width / scale;
                photos.height = currimagedata.height / scale;
                photos.src = url;
            }
        });
    //连接关闭，小风车转起来
        socket.addEventListener('close', (event) => {
            dataval.value += 'WebSocket连接关闭\n';
            fengche.style.animation = 'fengche 2s linear';
            commuction.innerHTML = "通信关闭中";
        });
    //连接错误
        socket.addEventListener('error', (event) => {
            dataval.value +='WebSocket错误：'+ event.data+"\n";
        });
    }
    });
//读取文件
fileInput.addEventListener('change',function(event){
    const files = event.target.files;
    var file = files[0];
    
    if(file.size>7000000)
        alert("图片文件不能超过7MB")
    else
    {
        //将文件信息显示在输入框
        ram.value = file.size+"字节";
        nameval.value = file.name;
        type.value = file.type;
        //创建读文件对象
        const reader = new FileReader();
        const reader2 = new FileReader();
        //读取文件内容，二进制格式
        reader.readAsArrayBuffer(file);
         //读取文件内容，URL格式
        reader2.readAsDataURL(file);
        //二进制格式读取完成后触发
        reader.onload = function(e) {
            //获取文件内容
            const filedata = e.target.result;
            // console.log(filedata)
            //发送消息
            sendMessage(filedata);
        };
        //URL格式读取完成后触发
        reader2.onload = function(e) {
                const picdata = e.target.result;
                //创建一个图像对象
                //将URL存入到其中的src属性
                currimagedata.src = picdata;
                //图片读取完成后
                currimagedata.onload = function() {
                    var width = currimagedata.width;
                    var height = currimagedata.height;
                    px.value = width+"x"+height+"px";
                    //scale倍缩放
                    photos.width = currimagedata.width / scale;
                    photos.height = currimagedata.height / scale;
                    photos.src = picdata;
                }
            }
    }

});