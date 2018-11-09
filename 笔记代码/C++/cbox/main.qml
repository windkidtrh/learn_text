import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Window 2.0
import "./UI/home"
import "./UI/education"
import "./UI/education/content"
import "./UI/about"
import "./UI/oder"
import "./UI/smarthome"

//import UdpSocket 1.0

ApplicationWindow {
    id:rootWindow
    visible: true
//    width: Screen.desktopAvailableWidth
//    height: Screen.desktopAvailableHeight
    width:1280
    height:720
    //property bool setResizable:false;
    maximumHeight: 720
    maximumWidth: 1280
    ///minimumHeight: 750
    //minimumWidth: 750
    //setResizable: false;
    color:"#000000"

    StackView{
        id:stack
        focus:true
        anchors.fill: parent
        initialItem: homepage
       // initialItem: Education

//        Keys.onBackPressed: {
//            if(stack.depth>1)
//            stack.pop()
//        }
    }

    HomePage{
        id:homepage
        visible: false
    }

    Education{
        id:educationpage
        visible: false
    }

    Smarthome{
        id:smarthomepage
        visible: false
    }

    Oder{
        id:oderpage
        visible: false
    }

    About{
        id:aboutpage
        visible: false
    }

    Cpp{
        id:cpppage
        visible: false
    }

    Java{
        id:javapage
        visible: false
    }

    Mysql{
        id:mysqlpage
        visible: false
    }

    Python{
        id:pythonpage
        visible: false
    }
}

