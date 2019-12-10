#ifndef MYWINDOW_H
#define MYWINDOW_H

#include <QMainWindow>

namespace Ui {
class mywindow;
}

class mywindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit mywindow(QWidget *parent = nullptr);
    ~mywindow();

private:
    Ui::mywindow *ui;
};

#endif // MYWINDOW_H
