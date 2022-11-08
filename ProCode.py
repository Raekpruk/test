from PyQt5 import  QtGui, QtWidgets
import sys
from pyqtgraph import PlotWidget, plot
import pyqtgraph as gp
from PyQt5.QtWidgets import QDialog, QApplication
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
from Pro3 import Ui_MainWindow




class myclass(Ui_MainWindow):
    def __init__(self) -> None:
        super().setupUi(MainWindow)

        self.savebt.clicked.connect(self.pressed)


        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,160)
        self.tableWidget.setColumnWidth(2,220)
        self.tableWidget.setColumnWidth(3,200)



    def calendarDateChanged(self):
        dateselected = self.calendarWidget.selectedDate().toPyDate().strftime("%d-%m")

    def pressed(self):
        x = int(self.comboBox1.currentText())
        y = int(self.comboBox1_2.currentText())
        sum1 =(x*800)+(y*2500)
        self.showtotal.setText("  " + str(sum1) + " BATH")



        self.showtotal_2.setText("              Finally have a good day and enjoy!!")

        print(sum1)
        print("Checkin",self.calendarWidget.selectedDate().toPyDate().strftime("%d-%m"))

        people=[{"num1":self.comboBox1.currentText(),"num2":self.comboBox1_2.currentText(),"time":self.calendarWidget.selectedDate().toPyDate().strftime("%d-%m"),"total":(int(self.comboBox1.currentText())*800)+(int(self.comboBox1_2.currentText())*2500)}]
        row=0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["num1"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["num2"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person["time"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person["total"])))
            row=row+1



if __name__ == "__main__" :
    myob = myclass()
    MainWindow.show()
    sys.exit(app.exec_())

