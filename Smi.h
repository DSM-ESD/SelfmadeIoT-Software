#pragma once

#include <QtWidgets/QWidget>
#include "ui_Smi.h"
#include "CodeBlock.h"

class Smi : public QWidget
{
    Q_OBJECT

public:
    Smi(QWidget *parent = Q_NULLPTR);


private:
    Ui::SmiClass ui;
};
