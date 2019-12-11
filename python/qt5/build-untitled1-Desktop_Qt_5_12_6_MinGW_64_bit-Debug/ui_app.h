/********************************************************************************
** Form generated from reading UI file 'app.ui'
**
** Created by: Qt User Interface Compiler version 5.12.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_APP_H
#define UI_APP_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_app
{
public:
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QGroupBox *groupBox;
    QCheckBox *checkBox;
    QCheckBox *checkBox_3;
    QCheckBox *checkBox_2;
    QProgressBar *progressBar;

    void setupUi(QDialog *app)
    {
        if (app->objectName().isEmpty())
            app->setObjectName(QString::fromUtf8("app"));
        app->resize(800, 600);
        pushButton = new QPushButton(app);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(140, 150, 91, 21));
        pushButton_2 = new QPushButton(app);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(330, 150, 75, 23));
        groupBox = new QGroupBox(app);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(210, 20, 221, 101));
        checkBox = new QCheckBox(groupBox);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        checkBox->setGeometry(QRect(10, 20, 71, 16));
        checkBox_3 = new QCheckBox(groupBox);
        checkBox_3->setObjectName(QString::fromUtf8("checkBox_3"));
        checkBox_3->setGeometry(QRect(100, 20, 71, 16));
        checkBox_2 = new QCheckBox(groupBox);
        checkBox_2->setObjectName(QString::fromUtf8("checkBox_2"));
        checkBox_2->setGeometry(QRect(10, 50, 71, 16));
        progressBar = new QProgressBar(app);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setGeometry(QRect(50, 240, 271, 51));
        progressBar->setValue(40);

        retranslateUi(app);

        QMetaObject::connectSlotsByName(app);
    } // setupUi

    void retranslateUi(QDialog *app)
    {
        app->setWindowTitle(QApplication::translate("app", "app", nullptr));
        pushButton->setText(QApplication::translate("app", "&OK", nullptr));
        pushButton_2->setText(QApplication::translate("app", "CANC&EL", nullptr));
        groupBox->setTitle(QApplication::translate("app", "GroupBox", nullptr));
        checkBox->setText(QApplication::translate("app", "CheckBox", nullptr));
        checkBox_3->setText(QApplication::translate("app", "CheckBox", nullptr));
        checkBox_2->setText(QApplication::translate("app", "CheckBox", nullptr));
    } // retranslateUi

};

namespace Ui {
    class app: public Ui_app {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_APP_H
