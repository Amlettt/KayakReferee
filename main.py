# qt6-tools designer запустить QT дизайнер
import sys
import pandas as pd
from design import Ui_MainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)

from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
                               QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
                               QTableWidget, QTableWidgetItem, QWidget, QMessageBox, QFileDialog)


# Создаем главное окно
# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # table sportsmen
        tableSportsmen = self.ui.tableSportsmen

        # Menu options
        actionNew = self.ui.actionNew
        actionOpen = self.ui.actionOpen
        actionSave = self.ui.actionSave
        actionSaveAs = self.ui.actionSaveAs
        actionAdd = self.ui.actionAdd
        actionDel = self.ui.actionDel
        actionCheckPoint = self.ui.actionCheckPoint
        actionFinish = self.ui.actionFinish
        actionSettingConnect = self.ui.actionSettingConnect
        actionPostResult = self.ui.actionPostResult
        actionResult = self.ui.actionResult
        actionAbout = self.ui.actionAbout

        # Menu btn actions
        actionNew.triggered.connect(self.new_file(tableSportsmen))
        actionOpen.triggered.connect(self.open_file)
        actionSave.triggered.connect(self.save_file)
        actionSaveAs.triggered.connect(self.save_as_file)
        actionAdd.triggered.connect(self.add_empty_row(tableSportsmen))
        actionDel.triggered.connect(self.delete_row(tableSportsmen))

        actionCheckPoint.triggered.connect(self.helpWindow)
        actionFinish.triggered.connect(self.helpWindow)
        actionSettingConnect.triggered.connect(self.helpWindow)
        actionPostResult.triggered.connect(self.helpWindow)
        actionResult.triggered.connect(self.helpWindow)

        actionAbout.triggered.connect(self.helpWindow)

    def new_file(self, tableSportsmen):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)

        if file_name:
            try:
                df = pd.read_csv(file_name)
                # Теперь у вас есть DataFrame `df`, который содержит данные из CSV файла
                # Вы можете выполнять операции с данными с использованием Pandas

                # Устанавливаем количество строк и столбцов в таблице

                tableSportsmen.setRowCount(df.shape[0])
                tableSportsmen.setColumnCount(df.shape[1])
                # Задаем заголовки таблицы
                tableSportsmen.setHorizontalHeaderLabels(list(df.columns))
                # Заполняем таблицу данными из JSON

                # Устанавливаем стили для заголовков
                header_font = QFont()
                header_font.setBold(True)
                tableSportsmen.horizontalHeader().setFont(header_font)
                tableSportsmen.verticalHeader().setFont(header_font)
                # установка цвета заголовка
                # header_color = QColor(192, 192, 192)  # Серый цвет (RGB)
                # tableSportsmen.horizontalHeader().setStyleSheet(f"background-color: {header_color.name()};")

                for i in range(df.shape[0]):
                    for j in range(df.shape[1]):
                        item = QTableWidgetItem(str(df.iloc[i, j]))
                        tableSportsmen.setItem(i, j, item)

                # Настройка размеров столбцов по содержимому
                tableSportsmen.resizeColumnsToContents()

            except Exception as e:
                QMessageBox.about(self, "Ошибка",
                                  "Ошибка при чтении файла: {str(e)}")

                print(f"Ошибка при чтении файла: {str(e)}")

    def open_file(self):
        pass

    def save_file(self):
        pass

    def save_as_file(self):
        pass

    # Добавить новую строку
    def add_empty_row(self, tableSportsmen):
        num_rows = tableSportsmen.rowCount()
        tableSportsmen.insertRow(num_rows)

    # Удалить выделенною строку
    def delete_row(self, tableSportsmen):
        selected_row = tableSportsmen.currentRow()
        if selected_row >= 0:
            tableSportsmen.removeRow(selected_row)

    # Открыть окно помощи "О программе"
    def helpWindow(self):
        QMessageBox.about(self, "Help",
                          "KayakReferee v1.0 - программа для подсчета результатов различных соревнований методом ручной фиксации финиша участников")


if __name__ == '__main__':
    # Создаем приложение
    app = QApplication(sys.argv)
    # Показываем окно
    window = MainWindow()
    window.show()
    # Запускаем приложение
    app.exec()
