#include "Smi.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Smi w;
    w.showMaximized();
    return a.exec();
}
