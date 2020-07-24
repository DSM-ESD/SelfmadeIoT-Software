#pragma once

#include <QWidget>

class TableWidget : public QWidget
{
	Q_OBJECT

public:
	TableWidget(QWidget *parent = nullptr);
	~TableWidget();

	void paintEvent(QPaintEvent* e);
};
