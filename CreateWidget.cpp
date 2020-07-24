#include "CreateWidget.h"
#include <QPainter>


CreateWidget::CreateWidget(QWidget *parent)
	: QWidget(parent)
{
	setAttribute(Qt::WA_StyledBackground, true);
}

CreateWidget::~CreateWidget()
{
}

void CreateWidget::paintEvent(QPaintEvent* e)
{

}
