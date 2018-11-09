import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.2
Item{
    id:home
    height:720
    width:1280
    property int window_status:0
    property int position:1

    Image {
        id: bg
        source: "qrc:/imgs/Home/home.jpg"
        anchors.fill: parent

    }

    Row{

        id:row1
        anchors.top:home.top
        anchors.topMargin: 50
        anchors.left:home.left
        anchors.leftMargin: 567
        Rectangle{
            height:142
            width:142
            id:welcome
            radius: 100
            Image {
                id: welcome_photo
                source: "qrc:/imgs/other/welcome.png"
                anchors.fill:parent
                }
        }
    }

    Row{
        id:row2
        spacing: 219
        anchors.top:home.top
        anchors.topMargin: 122
        anchors.left:home.left
        anchors.leftMargin: 385
        Rectangle{
            height:144
            width:144
            id:btn_smarthome
            radius: 100
            Image {
                id: smarthome
                source: "qrc:/imgs/other/smarthome.png"
                anchors.fill:parent
                }

//            MouseArea{
//                anchors.fill: parent
//                onClicked: {

//                    stack.push({item:"qrc:/UI/smarthome/smarthome.qml"})
//                    console.log("Smarthome page")
//                    btn_status.text="智能家居"
//                }
//                hoverEnabled : true
//                onExited: {
//                    smarthome.source="qrc:/imgs/other/smarthome.png"
//                }

//                onEntered: {
//                   btn_status.text="智能家居"
//                   smarthome.source="qrc:/imgs/other/smarthome1.png"
//                }
//            }
        }

        Rectangle{
            height:143
            width:142
            id:btn_education
            radius:100
            Image {
                id: education
                source: "qrc:/imgs/other/education.png"
                anchors.fill:btn_education
                }
//            MouseArea{
//                anchors.fill: parent
//                onClicked: {
//                    stack.push({item:"qrc:/UI/education/education.qml"})
//                    console.log("Education page")
//                    btn_status.text="云教育"
//                }
//                hoverEnabled : true
//                onExited: {
//                    education.source="qrc:/imgs/other/education.png"
//                }
//                onEntered: {
//                   btn_status.text="云教育"
//                   education.source="qrc:/imgs/other/education1.png"
//                }
//            }
            }

    }

    Row{
        id:row3
        spacing: 374
        anchors.top:row2.bottom
        anchors.topMargin: 36
        anchors.left:home.left
        anchors.leftMargin: 308
        Rectangle{
            height:143
            width:143
            id:btn_oder
            radius:100
            Image {
                id: oder
                source: "qrc:/imgs/other/oder.png"
                anchors.fill:btn_oder
                }
//            MouseArea{
//                anchors.fill: parent
//                onClicked: {
//                    stack.push({item:"qrc:/UI/oder/oder.qml"})
//                    console.log("Oder page")
//                    btn_status.text="云点播"
//                }
//                hoverEnabled : true
//                onExited: {
//                    oder.source="qrc:/imgs/other/oder.png"
//                }
//                onEntered: {
//                   btn_status.text="云点播"
//                   oder.source="qrc:/imgs/other/oder1.png"
//                }
//            }
        }

         Rectangle{
                height:144
                width:143
                id:btn_about
                radius:100
                Image {
                    id: about
                    source: "qrc:/imgs/other/about.png"
                    anchors.fill:btn_about
                    }
//            MouseArea{
//                id:mouse_about
//                anchors.fill: parent
//                onClicked: {
//                    stack.push({item:"qrc:/UI/about/about.qml"})
//                    console.log("About page")
//                    btn_status.text="关于"

//                }
//                hoverEnabled : true
//                onExited: {
//                    about.source="qrc:/imgs/other/about.png"
//                }
//                onEntered: {
//                   btn_status.text="关于"
//                   about.source="qrc:/imgs/other/about1.png"
//                }
//            }
        }
    }

    Rectangle{
            anchors.top:home.top
            anchors.topMargin: 278
            anchors.left:home.left
            anchors.leftMargin: 563
            height:150
            width:151
            color:"#92e0c4"
            radius: 100
            Text{
                id:btn_status
                color:"green"
                font.family: "fantasy"
                font.italic: true
                font.bold: true
                font.pixelSize: 30
                text:""
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter

            }
        }
//发送内网ip，直到对方收到为止
       Timer{
           id:send_address
           interval: 1000
           running: true;
           repeat: true;
           onTriggered: {
              Udp.sendmessage("127.0.0.1");
              console.log("start test")
           }
       }
//连接命令
       Connections{
           target: Udp;
           onMenuStateChanged:{
               if(Udp.menuState==="connect_success")
               {
                  send_address.stop();
                  console.log("end test")
               }

               else if(Udp.menuState==="left_success")
               {
                   if(window_status===0)
                   {
                       position--;
                       jadge();
                   }
               }

               else if(Udp.menuState==="right_success")
               {
                   if(window_status===0)
                   {
                       position++;
                       jadge();
                   }
               }

               else if(Udp.menuState==="up_success")
               {
                   if(window_status===0)
                   {
                       position+=2;
                       jadge();
                   }
               }

               else if(Udp.menuState==="down_success")
               {
                   if(window_status===0)
                   {
                       position-=2;
                       jadge();
                   }
               }

               else if(Udp.menuState==="list_success")
               {
                   //stack.pop({item:"qrc:/UI/home/HomePage.qml"})
                   console.log("show list")
               }
               //返回功能不应该这样写的，内容不足暂时这样先
               else if(Udp.menuState==="back_success")
               {
                   window_status=0;
                   stack.pop({item:"qrc:/UI/home/HomePage.qml"})
                   console.log("back to last")
               }
               else if(Udp.menuState==="ok_success")
               {

                    if(position===1&&window_status===0)
                    {
                          stack.push({item:"qrc:/UI/smarthome/Smarthome.qml"})
                          window_status=1;
                          console.log("enter smarthome")
                    }
                    else if(position===2&&window_status===0)
                    {
                          stack.push({item:"qrc:/UI/education/Education.qml"})
                          window_status=1;
                          console.log("enter education")
                    }
                    else if(position===3&&window_status===0)
                    {
                          stack.push({item:"qrc:/UI/oder/Oder.qml"})
                          window_status=1;
                          console.log("enter oder")
                    }
                    else if(position===4&&window_status===0)
                    {
                          stack.push({item:"qrc:/UI/about/About.qml"})
                          window_status=1;
                          console.log("enter about")
                    }
               }
           }
       }
//jadge负责让position在1-4之间
       function jadge(){
           if(position>4)
           {
               position-=4;
           }
           else if(position<1)
           {
               position+=4;
           }
           return position;
       }
//初始定位在智能家居的图案上
       function currentIndex()
       {

           if(position===1)
           {
               btn_status.text="智能家居"
               smarthome.source="qrc:/imgs/other/smarthome1.png"
               education.source="qrc:/imgs/other/education.png"
               oder.source="qrc:/imgs/other/oder.png"
               about.source="qrc:/imgs/other/about.png"
           }
           else if(position===2)
           {
               btn_status.text="云教育"
               smarthome.source="qrc:/imgs/other/smarthome.png"
               education.source="qrc:/imgs/other/education1.png"
               oder.source="qrc:/imgs/other/oder.png"
               about.source="qrc:/imgs/other/about.png"
           }
           else if(position===3)
           {
               btn_status.text="云点播"
               smarthome.source="qrc:/imgs/other/smarthome.png"
               education.source="qrc:/imgs/other/education.png"
               oder.source="qrc:/imgs/other/oder1.png"
               about.source="qrc:/imgs/other/about.png"
           }
           else if(position===4)
           {
               btn_status.text="关于"
               smarthome.source="qrc:/imgs/other/smarthome.png"
               education.source="qrc:/imgs/other/education.png"
               oder.source="qrc:/imgs/other/oder.png"
               about.source="qrc:/imgs/other/about1.png"
           }
       }
//使用一个计时器执行初始化固定的位置（智能家居的图案）
       Timer{
           id:current_index
           interval: 100
           running: true;
           repeat: true;
           onTriggered: {
              currentIndex();
              educationpage.education_window_status=1;
              cpppage.cpp_window_status=1;
           }
       }       

}
