#pragma once

#include <QWidget>

class CreateWidget : public QWidget
{
	Q_OBJECT

public:
	CreateWidget(QWidget *parent = nullptr);
	~CreateWidget();

	void paintEvent(QPaintEvent* e);
};
