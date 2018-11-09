import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.3
import "./content"

Item{
    property int status1:1
    property int status2:1
    property int status3:1
    property int education_window_status:0
    property int box_area:0
    id:education_current
    height:720
    width:1280

    Rectangle{
            id:left_box
            height:parent.height
            width:(1/4)*parent.width
            anchors.left:education_current.left

            Image {
                source: "qrc:/imgs/Home/left.jpg"
                anchors.fill: parent
            }

            Row{
                id:row_1a
                anchors.top:parent.top
                anchors.left:parent.left
                Rectangle{
                    id:search_text
                    height:(1/3)*left_box.height
                    width:left_box.width
                    color:"#00000000"
                    Image {
                        id: search_photo
                        source: "qrc:/imgs/other/search.png"
                        anchors.fill:parent
                    }
                }
            }
            Row{
                id:row_2a
                anchors.top:row_1a.bottom
                anchors.left:parent.left
                TextField {
                    id:jta;
                    placeholderText: qsTr("搜索:")
                    style:TextFieldStyle{
                        textColor:"gray";
                        background:Rectangle{
                            //id:jta_text
                            color:"orange"
                            implicitWidth: left_box.width
                            implicitHeight: (1/10)*left_box.height
                            border.color: "white";
                            border.width:1;
                        }
                    }
                    text:qsTr("");
                    font.family: "UTF-8"
                    font.pixelSize: 65
                    opacity: 0.2
                    onTextChanged: {
                        console.log(text);
                    }
                }
            }
            Row{
                id:row_3a
                anchors.top:row_2a.bottom
                anchors.left:parent.left
                Rectangle{
                    id:btn_text
                    width:left_box.width
                    height:(1/10)*left_box.height
                    color:"#00000000"
                    Row{
                        anchors.top:parent.top
                        anchors.topMargin: 18
                        anchors.left:parent.left
                        anchors.leftMargin: 65
                        spacing: 30
                        Rectangle{
                            id:btn_ok
                            width:80
                            height:40
                            radius: 10
                            color:"gray"
                            Text{
                                id:ok_text
                                color:"green"
                                font.family: "fantasy"
                                font.bold: true
                                font.pixelSize: 30
                                text:"Yes"
                                anchors.horizontalCenter: parent.horizontalCenter
                                anchors.verticalCenter: parent.verticalCenter
                            }
                        }

                        Rectangle{
                            id:btn_back
                            width:80
                            height:40
                            radius: 10
                            color:"gray"
                            opacity: 1
                            z:0.3
                            Text{
                                id:back_text
                                color:"green"
                                font.family: "fantasy"
                                font.bold: true
                                font.pixelSize: 30
                                text:"Back"
                                anchors.horizontalCenter: parent.horizontalCenter
                                anchors.verticalCenter: parent.verticalCenter
                            }
                        }

                    }
                }
            }

        }

    Rectangle{
            id:right_box
            height:parent.height
            width:(3/4)*parent.width
            anchors.left:left_box.right
            visible: true
            Image {
                source: "qrc:/imgs/Home/right.png"
                anchors.fill: parent
            }

            Row{
                id:row_1b
                visible: true
                anchors.top:right_box.top
                Rectangle{
                    id:sell_education
                    width:right_box.width
                    height:(1/3)*right_box.height
                    color:"#00000000"
                    visible: true
                    Text{
                        color:"green"
                        font.family: "fantasy"
                        font.bold: true
                        font.pixelSize: 50
                        text:"推荐"
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.bottom:sell_education.bottom
                        anchors.bottomMargin: 50
                    }
                }
            }
            Row{
                id:row_2b
                visible: true
                anchors.top:row_1b.bottom
                Rectangle{
                    id:sell_content
                    width:right_box.width
                    height:(2/3)*right_box.height
                    color:"#00000000"
                    Row{
                       id:row1
                       spacing: 150
                       anchors.top:parent.top
                       anchors.topMargin: 30
                       anchors.left:parent.left
                       anchors.leftMargin: 200
                       Rectangle{
                           id:content1
                           height:200
                           width:200
                           radius:100
                           color:"orange"
                           visible: true
                           Text{
                               id:content1_text
                               color:"green"
                               font.family: "fantasy"
                               font.bold: true
                               font.pixelSize: 50
                               text:"C++"
                               anchors.horizontalCenter: parent.horizontalCenter
                               anchors.verticalCenter: parent.verticalCenter
                           }

                       }
                       Rectangle{
                           id:content2
                           height:200
                           width:200
                           radius:100
                           color:"orange"
                           visible: true
                           Text{
                               id:content2_text
                               color:"green"
                               font.family: "fantasy"
                               font.bold: true
                               font.pixelSize: 50
                               text:"Java"
                               anchors.horizontalCenter: parent.horizontalCenter
                               anchors.verticalCenter: parent.verticalCenter
                           }

                       }
                    }
                    Row{
                       id:row2
                       spacing: 150
                       anchors.top:row1.bottom
                       anchors.topMargin: 30
                       anchors.left:parent.left
                       anchors.leftMargin: 200
                       Rectangle{
                           id:content3
                           height:200
                           width:200
                           radius:100
                           color:"orange"
                           visible: true
                           Text{
                               id:content3_text
                               color:"green"
                               font.family: "fantasy"
                               font.bold: true
                               font.pixelSize: 50
                               text:"Python"
                               anchors.horizontalCenter: parent.horizontalCenter
                               anchors.verticalCenter: parent.verticalCenter
                           }

                       }
                       Rectangle{
                           id:content4
                           height:200
                           width:200
                           radius:100
                           color:"orange"
                           visible: true
                           Text{
                               id:content4_text
                               color:"green"
                               font.family: "fantasy"
                               font.bold: true
                               font.pixelSize: 50
                               text:"Mysql"
                               anchors.horizontalCenter: parent.horizontalCenter
                               anchors.verticalCenter: parent.verticalCenter
                           }

                       }
                    }
                }
            }
        }

    StackView{
        id:intr_stack
        anchors.fill: right_box
    }
   Connections{
        target: Udp;
        onMenuStateChanged:{
            if(Udp.menuState==="left_success")
            {
                //当前在box_area=1,即两个按钮区
                if(education_window_status===0&&box_area===1)
                {
                    status2--;
                    jadge1();
                    console.log("iamhere 1");
                }
                //当前在box_area=2,即推荐区
                else if(education_window_status===0&&box_area===2)
                {
                    status3--;
                    jadge2();
                    console.log("iamhere 2");
                }
            }

            else if(Udp.menuState==="right_success")
            {
                //当前在box_area=1,即两个按钮区
                if(education_window_status===0&&box_area===1)
                {
                    status2++;
                    jadge1();
                    console.log("iamhere 3");
                }
                //当前在box_area=2,即推荐区
                else if(education_window_status===0&&box_area===2)
                {
                    status3++;
                    jadge2();
                    console.log("iamhere 4");
                }
            }

            else if(Udp.menuState==="up_success")
            {
                //当前在box_area=0,即文本区
                if(education_window_status===0&&box_area===0)
                {
                        box_area=1;
                    console.log("iamhere 5");
                }
                //当前在box_area=1,即两个按钮区
                else if(education_window_status===0&&box_area===1)
                {

                        box_area=0;
                    console.log("iamhere 6");
                }
                //当前在box_area=2,即推荐区
                else if(education_window_status===0&&box_area===2)
                {
                    status3+=2;
                    jadge3();
                    console.log("iamhere 7");
                }
            }

            else if(Udp.menuState==="down_success")
            {
                //当前在box_area=0,即文本区
                if(education_window_status===0&&box_area===0)
                {
                        box_area=1;
                    console.log("iamhere 8");
                }
                //当前在box_area=1,即两个按钮区
                else if(education_window_status===0&&box_area===1)
                {

                        box_area=0;
                    console.log("iamhere 9");
                }
                //当前在box_area=2,即推荐区
                else if(education_window_status===0&&box_area===2)
                {
                    status3-=2;
                    jadge3();
                    console.log("iamhere 10");
                }
            }

            //返回功能,暂时返回主页
            else if(Udp.menuState==="back_success")
            {
                current_index.stop();
                education_window_status=1;
                stack.pop({item:"qrc:/UI/home/HomePage.qml"})
                console.log("back to last")
            }
            else if(Udp.menuState==="ok_success")
            {
                 if(education_window_status===0&&box_area===0)
                 {
                     if(status1===1)
                     {
                        Udp.sendmessage("#input_start");
                        console.log("sent input oder");
                     }
                 }

                 else if(education_window_status===0&&box_area===1)
                 {
                     if(status2===1)
                     {
                       console.log("button yes area")
                     }
                     else if(status2===2)
                     {
                         current_index.stop();
                         education_window_status=1;
                         stack.pop({item:"qrc:/UI/home/HomePage.qml"})
                         homepage.window_status=0;
                         console.log("back to last")
                     }
                 }
                 else if(education_window_status===0&&box_area===2)
                 {
                      if(status3===1)
                      {
                          intr_stack.push({item:"qrc:/UI/education/content/Cpp.qml"})
                          cpppage.cpp_window_status=0;
                          education_window_status=1
                          console.log("enter c++ area")
                      }
                      else if(status3===2)
                      {
                          intr_stack.push({item:"qrc:/UI/education/content/Java.qml"})
                          education_window_status=1
                          console.log("enter java area")
                      }
                      else if(status3===3)
                      {
                          intr_stack.push({item:"qrc:/UI/education/content/Python.qml"})
                          education_window_status=1
                          console.log("enter python area")
                      }
                      else if(status3===4)
                      {
                          intr_stack.push({item:"qrc:/UI/education/content/Mysql.qml"})
                          education_window_status===1
                          console.log("enter mysql area")
                      }
                 }
            }
            else if(Udp.menuState==="Edit_start")
            {
                jta.text=Udp.editText;
                console.log("edit text success")
            }
        }
    }
//jadge1负责让status2在1-2之间
    function jadge1(){
        if(status2>2)
        {
            box_area=2
            status2=1;
        }
        else if(status2<1)
        {
            status2+=2;
        }
        return status2;
    }
    //jadge2负责让，当status3=1再按左时候返回box_area=0
    function jadge2(){
        if(status3>4)
        {
            status3-=4;
        }
        else if(status3<1)
        {
            box_area=0;
            status3=1;
        }
        return status3;
    }
    //jadge3责让status3在1-4之间
    function jadge3(){
        if(status3>4)
        {
            status3-=4;
        }
        else if(status3<1)
        {
            status3+=4;
        }
        return status3;
    }

//初始定位在box_area=0上
    function currentIndex()
    {

        if(education_window_status===0&&box_area===0)
        {
            if(status1===1)
            {
            //jta_text.color="red";
                jta.opacity=1;
                btn_ok.color="gray";
                btn_back.color="gray";
                content1.color="orange";
                console.log("iamhere a");
            }
        }
        else if(education_window_status===0&&box_area===1)
        {
            if(status2===1)
            {
                jta.opacity=0.2
                btn_ok.color="red";
                btn_back.color="gray";
                console.log("iamhere b");
            }
            else if(status2===2)
            {
                jta.opacity=0.2
                btn_ok.color="gray";
                btn_back.color="red";
                console.log("iamhere c");
            }
        }
        else if(education_window_status===0&&box_area===2)
        {
            if(status3===1)
            {
                btn_back.color="gray";
                content1.color="red";
                content2.color="orange";
                content3.color="orange";
                content4.color="orange";
                console.log("iamhere d");
            }
            else if(status3===2)
            {
                content1.color="orange";
                content2.color="red";
                content3.color="orange";
                content4.color="orange";
                console.log("iamhere e");
            }
            else if(status3===3)
            {
                content1.color="orange";
                content2.color="orange";
                content3.color="red";
                content4.color="orange";
                console.log("iamhere f");
            }
            else if(status3===4)
            {
                content1.color="orange";
                content2.color="orange";
                content3.color="orange";
                content4.color="red";
                console.log("iamhere g");
            }
        }
    }

//    function change_z()
//    {
//        right_box.z=1;
//    }

//使用一个计时器执行初始化固定的位置（智能家居的图案）
    Timer{
        id:current_index
        interval: 100
        running: true;
        repeat: true;
        onTriggered: {
           currentIndex();
        }
    }


}
