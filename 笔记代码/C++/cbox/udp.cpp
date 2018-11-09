#include "udp.h"
#include "QTimer"

//QStringList udp::sl_data;
udp::udp(QObject *parent)
    : QObject(parent)
{
    udpSocket = new QUdpSocket(this);
    udpSocket->bind(2333,QUdpSocket::ShareAddress);
    connect(udpSocket,SIGNAL(readyRead()),this,SLOT(onReadyRead()));
}


void udp::sendmessage(QString cmd)
{

    QByteArray datagram = cmd.toLatin1();
    udpSocket->writeDatagram(datagram,QHostAddress::Broadcast,23333);
    //发送数据
}
void udp::onReadyRead() //处理等待的数据报
{

    while(udpSocket->hasPendingDatagrams())  //拥有等待的数据报
    {
        QByteArray datagram; //拥于存放接收的数据报
        datagram.resize(udpSocket->pendingDatagramSize());
        //让datagram的大小为等待处理的数据报的大小
        udpSocket->readDatagram(datagram.data(),datagram.size());
       // QString data = datagram;
        //sl_data = data.split(" ");

        QString msg=datagram.data();
        qDebug()<<msg;
        if (msg.left(3)=="udp")
        {
            if(msg.right(7)=="connect")
            {
                setMenuState("connect_success");
                qDebug()<<"get connect";
            }
        }

        else if(msg.left(4)=="#cmd")
        {
            if(msg.right(2)=="up")
            {
                setMenuState("up_success");
                qDebug()<<"get up";
            }
            else if(msg.right(4)=="left")
            {
                setMenuState("left_success");
                qDebug()<<"get left";
            }
            else if(msg.right(2)=="ok")
            {
                setMenuState("ok_success");
                qDebug()<<"get ok";
            }
            else if(msg.right(5)=="right")
            {
                setMenuState("right_success");
                qDebug()<<"get right";
            }
            else if(msg.right(4)=="down")
            {
                setMenuState("down_success");
                qDebug()<<"get down";
            }
            else if(msg.right(4)=="list")
            {
                setMenuState("list_success");
                qDebug()<<"get list";
            }
            else if(msg.right(4)=="back")
            {
                setMenuState("back_success");
                qDebug()<<"get back";
            }
        }
        else if(msg.left(7)=="#string")
        {
            setMenuState("Edit_start");
            setEditText(msg.mid(8));
            qDebug()<<currenttext;
            qDebug()<<"get string";
        }
        else
        {
            qDebug()<<"unknown Bug:"<<msg;
        }
    }
}



