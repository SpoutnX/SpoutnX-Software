import os
import numpy as np
from numpy import pi
import printplot
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QFileDialog,
    QProgressBar,
    QCheckBox
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, Qt
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from math import *
import pandas
import pandas as pd
import openpyxl
import time
import shutil
import math

user = os.getlogin()
print(user)
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"
path5 = Path + "DataGravwave.xlsx"

mes_nombres = open(path4).read()
L = mes_nombres.split('\n')

winCaracteristiques = QWidget()
winCaracteristiques.setWindowTitle("Caractéristiques Modélisation")
winCaracteristiques.setFixedSize(QSize(550, 550))
winCaracteristiques.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def printModel():
    def show_stateR(state):
        global dis1
        dis1 = state

    def show_stateV1(state2):
        global dis2
        dis2 = state2

    def show_stateV2(state3):
        global dis3
        dis3 = state3

    def show_statePt(state4):
        global dis4
        dis4 = state4

    # def function
    GravFile = np.loadtxt(path2)
    m1 = float(GravFile[2])
    m2 = float(GravFile[3])
    r0 = float(GravFile[4])
    ang = float(GravFile[6])

    M = float(GravFile[7])   # m1 + m2
    u = float(GravFile[9])  # (m1*m2)/M
    r = r0
    print(r)

    P = 2*pi*sqrt((r**3)/((6.67*10**-11)*(m1+m2)))
    period_orbit = time.strftime("%H:%M:%S", time.gmtime(P))

    def fcn_nb_orbit(value1):
        global nb_orbit_user
        nb_orbit_user = float(value1)

    nb_orbit_default = ((m1/M)*(m2/M)*M)/((r**2)*P*13)
    nb_orbit_default = int(nb_orbit_default)  # Calcul expérimental pour
    # évaluer un nombre d'orbites entre chaques calculs du scripts

    def Calculate():
        r = r0
        try:
            nb_orbits = nb_orbit_user
        except:
            nb_orbits = nb_orbit_default
        nb_P = 0
        column = 1
        Data_r_total = []
        Data_Pt_OG = []
        Data_v1 = []
        Data_v2 = []
        nb_rang_period = []
        Time = []
        t = 0

        while r > 0:
            w = sqrt(((6.67*10**-11)*M)/(r**3))
            Pt = (32*(6.67*10**-11)*(u**2)*(r**4)*(w**6))/(5*(299792458**5))

            first = (-(((6.67*10**-11)*m2)/(r**2)))
            second = 1-((2*(6.67*10**-11)*m2)/((299792458**2)*r))
            third = 1-((3*(6.67*10**-11)*m2)/((299792458**2)*r))
            # Valeur de Ag pour l'objet 1
            AccelerationM1 = (-1)*(first*second*third)

            first2 = (-(((6.67*10**-11)*m1)/(r**2)))
            second2 = 1-((2*(6.67*10**-11)*m1)/((299792458**2)*r))
            third2 = 1-((3*(6.67*10**-11)*m1)/((299792458**2)*r))
            # Valeur de Ag pour l'objet 2
            AccelerationM2 = (-1)*(first2*second2*third2)

            # Calcul de la période
            P = 2*pi*sqrt((r**3)/((6.67*10**-11)*(m1+m2)))

            try:
                v1 = sqrt(AccelerationM1*r)  # vitesse de l'objet 1
                v2 = sqrt(AccelerationM2*r)  # vitesse de l'objet 2
            except:
                break

            E1 = 1/2*m1*v1**2   # Ec objet 1
            E2 = 1/2*m2*v2**2   # Ec objet 2
            Et = E1+E2

            div_E = E1/Et
            if r > (r0*0.005):
                column = int(column + nb_orbits)
                E_og = Pt * nb_orbits * P
                nb_P = nb_P + 1 * nb_orbits
            else:
                column = column + 2
                E_og = Pt * 2 * P
                nb_P = nb_P + 2
            Ent = Et - E_og

            En1 = Ent*div_E
            try:
                vn = sqrt((En1*2)/m1)
                r = (vn**2)/AccelerationM1
            except:
                break
            t = t + P * nb_orbits

            if r > (r0*0.01):
                if column % 100000 <= 500:
                    nb_rang_period.append(column*nb_orbits)
                    Time.append(t)
                    Data_r_total.append(r)
                    Data_Pt_OG.append(Pt)
                    Data_v1.append(v1)
                    Data_v2.append(v2)
                    Progress.setValue(100-((r*100)/r0))

            elif r > (r0*0.0001):
                if column % 100000 <= 400:
                    nb_rang_period.append(column*nb_orbits)
                    Time.append(t)
                    Data_r_total.append(r)
                    Data_Pt_OG.append(Pt)
                    Data_v1.append(v1)
                    Data_v2.append(v2)
                    Progress.setValue(100-((r*1000)/r0))

            else:
                print("no")
                nb_rang_period.append(column*nb_orbits)
                Time.append(t)
                Data_r_total.append(r)
                Data_Pt_OG.append(Pt)
                Data_v1.append(v1)
                Data_v2.append(v2)
                Progress.setValue(100-((r*10000)/r0))

        print(Data_r_total)

        SaveData = pd.DataFrame(zip(Data_r_total, Data_Pt_OG, Data_v1, Data_v2, nb_rang_period, Time), columns=[
            'r', 'Pt', 'v1', 'v2', 'nb_Period', 'Time'])
        SaveData.to_excel(path5)
        btnSave.setEnabled(True)

        if dis1 == 2:
            printplot.ModelOG_r()
        if dis2 == 2:
            printplot.ModelOG_Pt()
        if dis3 == 2:
            setv1 = 1
        if dis4 == 2:
            setv2 = 1
        if setv1 == 1 or setv2 == 1:
            printplot.ModelOG_V(setv1, setv2)

        Progress.setValue(100)

    winCaracteristiques.show()
    winPlot_Pt = QWidget()
    winPlot_Pt.setWindowTitle("Caractéristiques Modélisation")
    winPlot_Pt.setFixedSize(QSize(900, 900))
    winPlot_Pt.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

    labTitle = QLabel(L[193] + "\n" + L[194])
    labTitle.setParent(winCaracteristiques)
    labTitle.move(75, 0)
    labTitle.setFixedSize(QSize(400, 50))
    labTitle.setStyleSheet("background-color: #3EF724")
    labTitle.setAlignment(
        Qt.AlignHCenter | Qt.AlignVCenter)
    font1 = labTitle.font()
    font1.setPointSize(12)
    labTitle.setFont(font1)
    labTitle.show()

    ImgBinaire = QLabel()
    ImgBinaire.setPixmap(
        QPixmap('/usr/lib/spoutnx/img/image système binaire.png'))
    ImgBinaire.setParent(winCaracteristiques)
    ImgBinaire.move(350, 60)
    ImgBinaire.setFixedSize(QSize(180, 125))
    ImgBinaire.setScaledContents(True)
    ImgBinaire.show()

    labDist = QLabel(L[195] + "\n" + L[196])
    labDist.setParent(winCaracteristiques)
    labDist.move(0, 75)
    labDist.setFixedSize(QSize(350, 40))
    labDist.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font2 = labDist.font()
    font2.setPointSize(9.5)
    labDist.setFont(font2)
    labDist.show()

    ent_Dist = QLineEdit()
    ent_Dist.setParent(winCaracteristiques)
    ent_Dist.move(70, 125)
    ent_Dist.setFixedSize(QSize(150, 20))
    ent_Dist.textChanged.connect(fcn_nb_orbit)
    ent_Dist.setText(str(r0))
    ent_Dist.show()

    labPeriod_Orbit = QLabel(L[197] + " = " + "\n" + period_orbit)
    labPeriod_Orbit.setParent(winCaracteristiques)
    labPeriod_Orbit.move(25, 210)
    labPeriod_Orbit.setFixedSize(QSize(170, 40))
    labPeriod_Orbit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font3 = labPeriod_Orbit.font()
    font3.setPointSize(11)
    labPeriod_Orbit.setFont(font3)
    labPeriod_Orbit.show()

    labNb_Orbit = QLabel(L[198] + "\n" + L[199])
    labNb_Orbit.setParent(winCaracteristiques)
    labNb_Orbit.move(260, 200)
    labNb_Orbit.setFixedSize(QSize(250, 40))
    labNb_Orbit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labNb_Orbit.setFont(font3)
    labNb_Orbit.show()

    entNbOrbit = QLineEdit()
    entNbOrbit.setParent(winCaracteristiques)
    entNbOrbit.move(313, 250)
    entNbOrbit.setFixedSize(QSize(150, 20))
    entNbOrbit.textChanged.connect(fcn_nb_orbit)
    entNbOrbit.setText(str(nb_orbit_default))
    entNbOrbit.show()

    lab_Modification = QLabel(L[200])
    lab_Modification.setParent(winCaracteristiques)
    lab_Modification.move(263, 270)
    lab_Modification.setFixedSize(QSize(250, 40))
    lab_Modification.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font4 = lab_Modification.font()
    font4.setPointSize(10)
    lab_Modification.setFont(font4)
    lab_Modification.show()

    lab_Display_Var = QLabel(L[201])
    lab_Display_Var.setParent(winCaracteristiques)
    lab_Display_Var.move(10, 300)
    lab_Display_Var.setFixedSize(QSize(300, 40))
    lab_Display_Var.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    lab_Display_Var.setFont(font3)
    lab_Display_Var.show()

    Progress = QProgressBar()
    Progress.setParent(winCaracteristiques)
    Progress.setGeometry(225, 520, 300, 24)
    Progress.show()

    btnCalcul = QPushButton(L[18])
    btnCalcul.setParent(winCaracteristiques)
    btnCalcul.move(350, 370)
    btnCalcul.setFixedSize(QSize(80, 35))
    btnCalcul.pressed.connect(Calculate)
    btnCalcul.setFont(font3)
    btnCalcul.show()

    Display_r = QCheckBox(L[206])
    Display_r.setParent(winCaracteristiques)
    Display_r.move(30, 335)
    Display_r.setFixedSize(QSize(200, 25))
    Display_r.stateChanged.connect(show_stateR)
    Display_r.show()

    Display_v1 = QCheckBox(L[207])
    Display_v1.setParent(winCaracteristiques)
    Display_v1.move(30, 355)
    Display_v1.setFixedSize(QSize(200, 25))
    Display_v1.stateChanged.connect(show_stateV1)
    Display_v1.show()

    Display_v2 = QCheckBox(L[208])
    Display_v2.setParent(winCaracteristiques)
    Display_v2.move(30, 375)
    Display_v2.setFixedSize(QSize(200, 25))
    Display_v2.stateChanged.connect(show_stateV2)
    Display_v2.show()

    Display_Pt = QCheckBox(L[209])
    Display_Pt.setParent(winCaracteristiques)
    Display_Pt.move(30, 395)
    Display_Pt.setFixedSize(QSize(200, 25))
    Display_Pt.stateChanged.connect(show_statePt)
    Display_Pt.show()

    def SaveData():
        filename = QFileDialog.getSaveFileName()
        file2 = str(filename[0])
        filename2 = (file2 + ".xlsx")
        shutil.copyfile(path5, filename2)

    btnSave = QPushButton(L[205])
    btnSave.setParent(winCaracteristiques)
    btnSave.move(285, 420)
    btnSave.setFixedSize(QSize(200, 30))
    btnSave.pressed.connect(SaveData)
    btnSave.setEnabled(False)
    btnSave.setFont(font3)
    btnSave.show()

    lab_Infos = QLabel(L[202] + "\n" + L[203])
    lab_Infos.setParent(winCaracteristiques)
    lab_Infos.move(100, 460)
    lab_Infos.setFixedSize(QSize(350, 40))
    lab_Infos.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    lab_Infos.setFont(font4)
    lab_Infos.show()

    lab_Progress = QLabel(L[204])
    lab_Progress.setParent(winCaracteristiques)
    lab_Progress.move(0, 510)
    lab_Progress.setFixedSize(QSize(230, 40))
    lab_Progress.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    lab_Progress.setFont(font4)
    lab_Progress.show()
