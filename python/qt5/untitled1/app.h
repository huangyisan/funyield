#ifndef APP_H
#define APP_H

#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class app; }
QT_END_NAMESPACE

class app : public QDialog
{
    Q_OBJECT

public:
    app(QWidget *parent = nullptr);
    ~app();

private slots:
    void on_pushButton_clicked();

private:
    Ui::app *ui;
};
#endif // APP_H
