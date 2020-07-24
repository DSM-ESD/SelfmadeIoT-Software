#include "TableWidget.h"
#include <QPainter>


TableWidget::TableWidget(QWidget *parent)
	: QWidget(parent)
{
	setAttribute(Qt::WA_StyledBackground, true);
}

TableWidget::~TableWidget()
{
}

void TableWidget::paintEvent(QPaintEvent* e)
{
	
}
