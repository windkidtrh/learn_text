import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
//import "qrc:/UI/education"
Item{
    id:cpp_current
    visible: true
    property int cpp_window_status:0
    Image {
        id: bg
        source: "qrc:/imgs/Home/right.png"
        anchors.fill: parent
    }
    Rectangle{
        height:80
        width:cpp_current.width
        id:cpp_intro
        color:"#92e0c4"
        anchors.top: cpp_current.top
        Text{
            color:"green"
            font.family: "fantasy"
            font.italic: true
            font.bold: true
            font.pixelSize: 40
            text:"C++学习视频"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        Rectangle{
            height:70
            width:70
            id:btn_cpp_current
            color:"red"
            radius:35
            anchors.right: cpp_intro.right
            anchors.rightMargin: 5
            anchors.top:cpp_intro.top
            anchors.topMargin: 5
            Text{
                color:"green"
                font.family: "fantasy"
                font.italic: true
                font.bold: true
                font.pixelSize: 20
                text:"返回"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
            }

            MouseArea{
                anchors.fill: parent
                onClicked: {
                    educationpage.education_window_status=0;
                    cpp_current.visible=false;

                }
            }
        }
    }
    Rectangle{
        width:cpp_current.width
        height:20
        anchors.bottom: cpp_current.bottom
        color:"white"
    }

    Rectangle{
        width:cpp_current.width
        height:620
        anchors.top: cpp_intro.bottom
        color:"#EEEEEE"
        clip:true

        Component{
            id:cppDelegate;
            Item{
                id:wrapper;
                width:234;
                height:200;

                Rectangle{
                    anchors.left:parent.left;
                    z:0;
                    Rectangle{
                        id:first_content
                        width:234
                        height:200
                        anchors.left:parent.left
                        anchors.leftMargin: 13
                        anchors.top:parent.top
                        anchors.topMargin: 10
                        border.width: 0.5;
                        border.color:"gray";
                         Rectangle{
                             id:second_content
                             width:212
                             height:189
                             anchors.left:parent.left
                             anchors.leftMargin: 10
                             anchors.top:parent.top
                             anchors.topMargin: 10
                             z:0
                            Rectangle{
                                id:photo_content
                                anchors.top:second_content.top
                                width:212
                                height:130
                                z:0
                                Image {
                                    source: item_photo
                                    anchors.fill:parent
                                }
                            }

                            Rectangle{
                                id:title_content
                                anchors.left:second_content.left
                                anchors.leftMargin: 2
                                anchors.top:photo_content.bottom
                                anchors.topMargin: 5
                                height:25
                                Text{
                                    text:item_title;
                                    color:"black";
                                    font.pixelSize:
                                        wrapper.GridView.isCurrentItem?18:12;
                                }
                            }

                            Rectangle{
                                id:common_content
                                anchors.left:second_content.left
                                anchors.leftMargin: 2
                                anchors.top:title_content.bottom
                                width:208
                                height:25
                                visible: false
                                Text{
                                    text:item_common_content;
                                    color:"gray";
                                    font.pixelSize:12;
                                    width: parent.width;
                                    wrapMode : Text.WordWrap;
                                }
                            }

                            Rectangle{
                                id:study_time_content
                                anchors.left:second_content.left
                                anchors.leftMargin: 2
                                height:29
                                anchors.bottom: second_content.bottom
                                clip:false

                                Text{
                                    text:item_on_study_time;
                                    color:"gray";
                                    font.pixelSize:
                                        wrapper.GridView.isCurrentItem?18:12;
                                }

                            }
                            PropertyAnimation{
                                id:a1
                                target:second_content
                                property: "height"
                                to:219
                                duration: 300
                            }
                            PropertyAnimation{
                                id:a2
                                target:common_content
                                property: "visible"
                                to:true
                                duration: 300
                            }
                            PropertyAnimation{
                                id:a3
                                target:second_content
                                property: "z"
                                to:10
                                duration: 300
                            }

                            PropertyAnimation{
                                id:b1
                                target:second_content
                                property: "height"
                                to:189
                                duration:300
                            }

                            PropertyAnimation{
                                id:b2
                                target:common_content
                                property: "visible"
                                to:false
                                duration: 150
                            }

                            PropertyAnimation{
                                id:b3
                                target:second_content
                                property: "z"
                                to:0
                                duration: 150
                            }

                         }
                         MouseArea{
                                 anchors.fill:parent;
                                 onClicked: wrapper.GridView.view.currentIndex=index;
                                 hoverEnabled : true
                                 onExited: {
                                     b1.running = true;
                                     b2.running = true;
                                     b3.running = true;

                                 }

                                 onEntered: {
                                     a1.running = true;
                                     a2.running = true;
                                     a3.running = true;


                                 }
                    }
                    }
                }

                Connections{
                    target:Udp;
                    onMenuStateChanged:{
                        if(Udp.menuState==="left_success"){
                            if(cpp_window_status===0){
                                wrapper.GridView.view.currentItem--;
                                jadge();
                            }
                        }

                        else if(Udp.menuState==="right_success"){
                            if(cpp_window_status===0){
                                wrapper.GridView.view.currentItem++;
                                jadge();
                            }
                        }

                        else if(Udp.menuState==="up_success"){
                            if(cpp_window_status===0){
                                wrapper.GridView.view.currentItem-=4;
                                jadge();
                            }
                        }

                        else if(Udp.menuState==="down_success"){
                            if(cpp_window_status===0){
                                wrapper.GridView.view.currentItem+=4;
                                jadge();
                            }
                        }

                        else if(Udp.menuState==="back_success"){

                        }

                        else if(Udp.menuState==="ok_success"){

                        }

                    }
                }
                function jadge()
                {

                }

                function currentIndex()
                {
                    if(wrapper.GridView.view.currentItem)
                    {
                        a1.running = true;
                        a2.running = true;
                        a3.running = true;
                    }
//                    if(!wrapper.GridView.view.currentIndex)
//                    {
//                        b1.running = true;
//                        b2.running = true;
//                        b3.running = true;
//                    }
                }

                Timer{
                    id:current_index;
                    interval: 100;
                    running: true;
                    repeat: true;
                    onTriggered: {
                       currentIndex();
                    }
                }






            }
        }
        GridView{
            id:gridView;
            anchors.fill:parent;
            delegate: cppDelegate;
            flow:GridView.FlowLeftToRight
            cellWidth:234
            cellHeight:200
            model:ListModel{
                id:cppModel;
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++基础";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++语法";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++数字";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++唔知道";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++小风";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++大风";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++中锋";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++库里";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++基础";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++语法";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++数字";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++唔知道";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++小风";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++大风";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++中锋";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }
                ListElement{
                    item_photo:"qrc:/imgs/other/test.png";
                    item_title:"c++库里";
                    item_common_content:"和哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈和";
                    item_on_study_time:"5课时 21分钟";
                }

            }
//        focus:true;
//        highlight:Rectangle{
//        }
        }
    }

}
