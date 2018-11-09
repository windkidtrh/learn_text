import QtQuick 2.3
import QtQuick.Controls 1.2
Item{
    id:mysql_current
    Image {
        id: bg
        source: "qrc:/imgs/Home/right.png"
        anchors.fill: parent
    }

    Rectangle{
        height:143
        width:143
        id:btn_mysql_current
        color:"#92e0c4"
        radius:100
        anchors.bottom: mysql_current.bottom
        anchors.bottomMargin: 5
        anchors.left:mysql_current.left
        anchors.leftMargin: 5

        Text{
            color:"green"
            font.family: "fantasy"
            font.italic: true
            font.bold: true
            font.pixelSize: 30
            text:"返回"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }

        MouseArea{
            anchors.fill: parent
            onClicked: {
                intr_stack.pop({item:"qrc:/UI/education/Education.qml"})
            }
        }
    }

}
