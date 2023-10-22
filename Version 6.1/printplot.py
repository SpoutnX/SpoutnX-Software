import os
import numpy as np
from numpy import sin, cos, pi, linspace
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar


window9 = QWidget()
window9.setWindowTitle("Résultats")
window9.setFixedSize(QSize(600, 450))
window9.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

window10 = QWidget()
window10.setWindowTitle("Résultats")
window10.setFixedSize(QSize(600, 450))
window10.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

window11 = QWidget()
window11.setWindowTitle("Résultats")
window11.setFixedSize(QSize(600, 450))
window11.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

user = os.getlogin()
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"
path6 = Path + "pngplot.png"


def visual():
    mes_nombres = open(path4).read()
    L = mes_nombres.split('\n')
    S = np.loadtxt(path2)
    r = 2
    print(S[4])
    arc_angles = linspace(0 * pi, pi/(pi/S[4]))
    arc_xs = r * cos(arc_angles)
    arc_ys = r * sin(arc_angles)

    ty = FigureCanvasQTAgg()
    fig, ty.ax = plt.subplots(figsize=(5, 5), dpi=100)
    ty.setParent(window9)
    print("matplotlib")

    ty.ax.plot(arc_xs, arc_ys, color='red', lw=3, label=L[94])
    ty.ax.legend(loc="upper right", prop={'size': 9})
    valtext = str(S[4])
    ty.ax.annotate('Angle a = ' + "\n" + valtext, xy=(1.5, 0.4),
                   xycoords='data', fontsize=10, rotation=0)
    ty.ax.hlines(y=-2, xmin=0, xmax=2, color='black', label=L[37])
    ty.ax = plt.gca()
    ty.ax.set_xlim([-4, 4])
    ty.ax.set_ylim([-4, 4])

    ty.ax.scatter(0, 0, color="green")
    ty.ax.set(title=L[95] + "\n" + L[96])
    ty.ax.vlines(x=2, ymin=-4, ymax=0, color="red", lw=3)
    ty.ax.plot(0, -2, marker='<', color='black')
    ty.ax.plot(2, -2, marker='>', color='black')
    ty.ax.grid()
    ty.ax.legend(loc="upper right", prop={'size': 9})
    fig.savefig(path6)

    fig.show()
    ty.show()


def visual2():
    mes_nombres = open(path4).read()
    L = mes_nombres.split('\n')
    S = np.loadtxt(path2)

    ty2 = FigureCanvasQTAgg()
    fig, ty2.ax = plt.subplots(figsize=(6, 5.5), dpi=100)
    ty2.setParent(window10)

    ty2.ax.set(title=L[93])
    ty2.ax.set_xlim([-3, 3])
    ty2.ax.set_ylim([-4, 2])
    r = 2
    ty2.ax.scatter(0, 0, color="black")

    u = 0  # x-position of the center
    v = 0  # y-position of the center
    a = 2.5  # radius on the x-axis
    b = 1.5  # radius on the y-axis
    fs1 = str(S[11])
    t = np.linspace(0, 2*pi, 100)
    ty2.ax.plot(u+a*np.cos(t), v+b*np.sin(t),
                label=L[91] + " = " + fs1, color='red')
    ty2.ax.grid(color='lightgray', linestyle='--')
    ty2.ax.legend(loc="lower right", prop={'size': 9})

    a2 = 1.5  # radius on the x-axis
    b2 = 1.5  # radius on the y-axis
    fs2 = str(S[9])
    t = np.linspace(0, 2*pi, 100)
    ty2.ax.plot(u+a2*np.cos(t), v+b2*np.sin(t), label=L[65] + " = " + fs2)
    ty2.ax.grid(color='lightgray', linestyle='--')
    ty2.ax.legend(loc="lower right", prop={'size': 9})

    a3 = 1.2
    b3 = 0.5
    fs3 = str(S[8])
    t = np.linspace(0, 2*pi, 100)
    ty2.ax.plot(u+a3*np.cos(t), v+b3*np.sin(t), label=L[66] + " = " + fs3)
    ty2.ax.grid(color='lightgray', linestyle='--')
    ty2.ax.legend(loc="lower right", prop={'size': 9})

    a4 = 0.9
    b4 = 0.5
    fs4 = str(S[10])
    t = np.linspace(0, 2*pi, 100)
    ty2.ax.plot(u+a4*np.cos(t), v+b4*np.sin(t), label=L[92] + " = " + fs4)
    ty2.ax.grid(color='lightgray', linestyle='--')
    ty2.ax.legend(loc="lower right", prop={'size': 9})

    ty2.ax.quiver(0, 0, 0, 1.5, color='blue', units='xy', scale=1)
    ty2.ax.quiver(0, 0, 0, -1.5, color='blue', units='xy', scale=1)

    ty2.show()
    fig.savefig(path6)
    fig.show()


def visual3():
    mes_nombres = open(path4).read()
    L = mes_nombres.split('\n')
    S = np.loadtxt(path2)
    fs1 = str(S[4])
    fs2 = str(S[5])
    a = S[4]
    b = S[5]

    r = 1
    r2 = 2
    arc_angles = linspace(0, a, 100)
    arc_xs = r * cos(arc_angles)
    arc_ys = r * sin(arc_angles)

    arc_angles2 = linspace(0, b, 100)
    arc_xs2 = r2 * cos(arc_angles2)
    arc_ys2 = r2 * sin(arc_angles2)

    if a <= 1.57:
        c = 5
    elif a >= 1.57:
        c = -5
    x = linspace(0, c, 10)

    ca = cos(a)
    sa = sin(a)

    cb = cos(b)
    sb = sin(b)

    a2 = sa/ca
    b2 = sa-a2*ca
    y = a2*x+b2

    b2 = sb/cb
    b3 = sb-b2*cb
    y2 = b2*x+b3

    ty3 = FigureCanvasQTAgg()
    fig, ty3.ax = plt.subplots(figsize=(5, 5), dpi=100)
    ty3.setParent(window11)
    ty3.ax.scatter(0, 0, color="green")
    ty3.ax.set(title=L[130] + "\n" + L[131])

    ty3.ax.plot(arc_xs, arc_ys, color='red', lw=2, label=L[127] + fs1)
    ty3.ax.legend(loc="upper right", prop={'size': 9})
    ty3.ax.annotate('a', xy=(1.1, 0.3), xycoords='data',
                    fontsize=12, rotation=0)
    ty3.ax.annotate("a'", xy=(2.1, 0.3), xycoords='data',
                    fontsize=12, rotation=0)

    ty3.ax.hlines(y=0, xmin=0, xmax=5, color='blue', label=L[129])
    ty3.ax.set_xlim([-1, 6])
    ty3.ax.set_ylim([-1, 6])
    ty3.ax.plot(arc_xs2, arc_ys2, color="green", lw=2, label=L[128] + fs2)

    ty3.ax.plot(c, 0, marker='>', color='blue')

    ty3.ax.plot(x, y, color='orange', lw=2)
    ty3.ax.plot(x, y2, color="#3EF724", lw=2)
    ty3.ax.grid()
    ty3.ax.legend(loc="upper right", prop={'size': 9})

    fig.show()
    ty3.show()
    fig.savefig(path6)
