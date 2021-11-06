# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name       :
# Purpose    :
#
# Author     : Pritam Charles Kantane
# Class      : 3PF2
# Date       : 02 Nov 2021
# -------------------------------------------------------------------------------
from matplotlib import pyplot as plt
import numpy as np


class Graphic:
    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot_1(self, x1, x2, y1, y2, label1, label2):
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label1, c="blue")
        plt.plot(x2, y2, label=label2, c="blue", ls=":")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.show()

    def plot_2(self, x1, x2, y1, label1, label2, label3):
        plt.figure(figsize=(15, 9))
        plt.plot([i for i in range(0, 400, 10)], [17115 for i in range(0, 40)], label=label3, c="green")
        plt.plot(x1, y1, label=label1, c="blue")
        plt.plot(x2, y1, label=label2, c="orange")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.show()

    def plot_3(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, y1, y2, y3, y4, y5, y6, y7, y8,
               label1, label2, label3, label4, label5, label6, label7, label8, label9):
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, c="blue", label=label1)
        plt.plot(x2, y2, c="blue")
        plt.plot(x3, y3, c="blue")
        plt.plot(x4, y4, c="blue")
        plt.plot(x5, y5, c="blue")
        plt.plot(x6, y6, c="black", label=label2)
        plt.plot(x7, y7, c="black")
        plt.plot(x8, y8, c="purple", ls=":", lw=2, label=label3)
        plt.plot(x9, y8, c="pink", ls=":", lw=2, label=label4)
        plt.plot(x10, y8, c="red", ls=":", lw=2, label=label5)
        plt.plot(x11, y8, c="orange", ls=":", lw=2, label=label6)
        plt.plot(x12, y8, c="cyan", ls=":", lw=2, label=label7)
        plt.plot(x13, y8, c="green", ls=":", lw=2, label=label8)
        plt.plot(x14, y8, c="magenta", ls=":", lw=2, label=label9)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.show()

    def plot_4(self, x1, y1, label):  # chart 5 and 6
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label, c="blue")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.show()
