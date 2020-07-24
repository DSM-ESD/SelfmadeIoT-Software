#include "CodeBlock.h"

CodeBlock::CodeBlock(QWidget *parent)
	: QWidget(parent)
{
	resize(300, 100);
	setAttribute(Qt::WA_StyledBackground, true);
	setStyleSheet("background-color: red; border-radius:10px;");
}

CodeBlock::~CodeBlock()
{

}
