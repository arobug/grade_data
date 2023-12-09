from PyQt6.QtWidgets import *
from gui import *
import csv




class Logic (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open_button.clicked.connect(lambda: self.open())
        self.Close_Button.clicked.connect(lambda: self.close())

    def open(self):
        file_name = self.File_input.text() + '.csv'
        grades =[]
        try:
            with open(file_name, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    grades.append(row['Grade'])
            high = 0
            for i in grades:
                if float(i) > high:
                    high = float(i)
            low = 200
            for i in grades:
                if float(i) < low:
                    low = float(i)
            ttl = 0
            avg = 0
            for i in grades:
                ttl += float(i)
            avg = ttl / len(grades)
            self.High_grade.setText(str(round(high,2)))
            self.Low_grade.setText(str(round(low,2)))
            self.Average_grade.setText(str(round(avg,2)))
            self.Students_amount.setText(str(len(grades)))
            self.Info_label_1.setText(self.File_input.text())
            self.File_input.setText('')
            self.Info_display.setText('')
        except:
            self.Info_display.setText('Invalid file name or data, make sure to check your spelling, do not include file type and make sure the file is a csv file with one column with the first entry named Grade')