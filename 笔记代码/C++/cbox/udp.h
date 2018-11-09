#ifndef UDP_H
#define UDP_H
#include <QObject>
#include <QUdpSocket>
#include <QtNetwork>
#include <QString>
//#include "QTimer"

class udp : public QObject
{
    Q_OBJECT
public:
    udp(QObject *parent = 0);
    QString currentstate;
    QString currenttext;
    //static QStringList sl_data;
    Q_INVOKABLE void sendmessage(QString cmd);

   // Q_PROPERTY(QString menuState READ menuState NOTIFY menuStateChanged)
    Q_PROPERTY(QString menuState READ menuState WRITE setMenuState NOTIFY menuStateChanged)
    Q_PROPERTY(QString editText READ editText WRITE setEditText NOTIFY editTextChanged)

    QString menuState()
    {
    return this->currentstate;
    }


    void setMenuState(QString sta)
    {
        this->currentstate=sta;
        emit menuStateChanged();
    }

    QString editText()
    {
    return this->currenttext;
    }


    void setEditText(QString sta1)
    {
        this->currenttext=sta1;
        emit editTextChanged();
    }

private:
  //  QTimer *timer;
    QUdpSocket *udpSocket;

signals:
    void menuStateChanged();
    void editTextChanged();
private slots:
     void onReadyRead();

};

#endif // UDP_H


