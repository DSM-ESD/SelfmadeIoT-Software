/********************************************************************************
** Form generated from reading UI file 'Smi.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SMI_H
#define UI_SMI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "CreateWidget.h"
#include "Tablewidget.h"

QT_BEGIN_NAMESPACE

class Ui_SmiClass
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    TableWidget *tableWidget;
    CreateWidget *createWidget;
    QWidget *horizontalWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *saveBtn;
    QPushButton *loadBtn;
    QPushButton *sendBtn;
    QPushButton *exitBtn;

    void setupUi(QWidget *SmiClass)
    {
        if (SmiClass->objectName().isEmpty())
            SmiClass->setObjectName(QString::fromUtf8("SmiClass"));
        SmiClass->resize(1920, 1080);
        SmiClass->setAutoFillBackground(false);
        SmiClass->setStyleSheet(QString::fromUtf8("QWidget#SmiClass\n"
"{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}"));
        verticalLayout = new QVBoxLayout(SmiClass);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        tableWidget = new TableWidget(SmiClass);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        tableWidget->setMaximumSize(QSize(500, 16777215));
        tableWidget->setStyleSheet(QString::fromUtf8("background-color: rgb(249, 249, 249);\n"
"border-radius: 20px"));

        horizontalLayout->addWidget(tableWidget);

        createWidget = new CreateWidget(SmiClass);
        createWidget->setObjectName(QString::fromUtf8("createWidget"));
        createWidget->setStyleSheet(QString::fromUtf8("border: 5px solid rgb(249, 249, 249);\n"
"border-radius: 20px"));

        horizontalLayout->addWidget(createWidget);


        verticalLayout->addLayout(horizontalLayout);

        horizontalWidget_2 = new QWidget(SmiClass);
        horizontalWidget_2->setObjectName(QString::fromUtf8("horizontalWidget_2"));
        horizontalWidget_2->setMaximumSize(QSize(16777215, 100));
        horizontalWidget_2->setStyleSheet(QString::fromUtf8("QPushButton\n"
"{ \n"
"	background-color: rgb(240, 240, 240);\n"
"	border-radius: 15px;\n"
"	font: 75 20pt \"Arial\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"	border: 3px solid rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton:focus:checked\n"
"{ \n"
"	border: 3px solid rgb(218, 218, 218);\n"
"}"));
        horizontalLayout_2 = new QHBoxLayout(horizontalWidget_2);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        saveBtn = new QPushButton(horizontalWidget_2);
        saveBtn->setObjectName(QString::fromUtf8("saveBtn"));
        saveBtn->setMinimumSize(QSize(0, 50));

        horizontalLayout_2->addWidget(saveBtn);

        loadBtn = new QPushButton(horizontalWidget_2);
        loadBtn->setObjectName(QString::fromUtf8("loadBtn"));
        loadBtn->setMinimumSize(QSize(0, 50));

        horizontalLayout_2->addWidget(loadBtn);

        sendBtn = new QPushButton(horizontalWidget_2);
        sendBtn->setObjectName(QString::fromUtf8("sendBtn"));
        sendBtn->setMinimumSize(QSize(0, 50));

        horizontalLayout_2->addWidget(sendBtn);

        exitBtn = new QPushButton(horizontalWidget_2);
        exitBtn->setObjectName(QString::fromUtf8("exitBtn"));
        exitBtn->setMinimumSize(QSize(0, 50));

        horizontalLayout_2->addWidget(exitBtn);


        verticalLayout->addWidget(horizontalWidget_2);


        retranslateUi(SmiClass);

        QMetaObject::connectSlotsByName(SmiClass);
    } // setupUi

    void retranslateUi(QWidget *SmiClass)
    {
        SmiClass->setWindowTitle(QApplication::translate("SmiClass", "Smi", nullptr));
        saveBtn->setText(QApplication::translate("SmiClass", "Save", nullptr));
        loadBtn->setText(QApplication::translate("SmiClass", "Load", nullptr));
        sendBtn->setText(QApplication::translate("SmiClass", "Send", nullptr));
        exitBtn->setText(QApplication::translate("SmiClass", "Exit", nullptr));
    } // retranslateUi

};

namespace Ui {
    class SmiClass: public Ui_SmiClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SMI_H
