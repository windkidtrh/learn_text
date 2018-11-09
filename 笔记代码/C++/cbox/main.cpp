#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include "udp.h"
#include <QQmlContext>
#include "QTimer"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("Udp",new udp());
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
