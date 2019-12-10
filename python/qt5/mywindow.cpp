#include "mywindow.h"
#include "ui_mywindow.h"

mywindow::mywindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::mywindow)
{
    ui->setupUi(this);
}

mywindow::~mywindow()
{
    delete ui;
}
