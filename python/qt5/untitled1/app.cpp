#include "app.h"
#include "ui_app.h"

app::app(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::app)
{
    ui->setupUi(this);
}

app::~app()
{
    delete ui;
}


void app::on_pushButton_clicked()
{

}
