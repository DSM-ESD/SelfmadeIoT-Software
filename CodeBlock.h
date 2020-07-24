#pragma once

#include <QWidget>

class CodeBlock : public QWidget
{
	Q_OBJECT

public:
	CodeBlock(QWidget *parent = nullptr);
	~CodeBlock();
};
