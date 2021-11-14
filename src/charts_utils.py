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


class Graphic:
    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot_1(self, x1, x2, y1, y2, label1, label2, filename):  # chart 1 and 2 : glide curves
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label1, c="blue")
        plt.plot(x2, y2, label=label2, c="blue", ls=":")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.savefig(filename)
        plt.show()

    def plot_2(self, x1, x2, x3, y1, y2, label1, label2, label3, filename):  # chart 3 : flight envelope
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label3, c="green")
        plt.plot(x2, y2, label=label1, c="blue")
        plt.plot(x3, y2, label=label2, c="orange")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.savefig(filename)
        plt.show()

    def plot_3(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, y1, y2, y3, y4, y5, y6, y7, y8,
               y9, label1, label2, label3, label4, label5, label6, label7, label8, label9, filename):  # chart 4 : flight domain
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, c="blue", label=label1)
        plt.plot(x2, y2, c="blue")
        plt.plot(x3, y3, c="blue")
        plt.plot(x4, y4, c="blue")
        plt.plot(x5, y5, c="blue")
        plt.plot(x6, y6, c="blue")
        plt.plot(x7, y7, c="black", label=label2)
        plt.plot(x8, y8, c="black")
        plt.plot(x9, y9, c="purple", ls=":", lw=3, label=label3)
        plt.plot(x10, y9, c="pink", ls=":", lw=3, label=label4)
        plt.plot(x11, y9, c="red", ls=":", lw=3, label=label5)
        plt.plot(x12, y9, c="orange", ls=":", lw=3, label=label6)
        plt.plot(x13, y9, c="cyan", ls=":", lw=3, label=label7)
        plt.plot(x14, y9, c="green", ls=":", lw=3, label=label8)
        plt.plot(x15, y9, c="magenta", ls=":", lw=3, label=label9)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.savefig(filename)
        plt.show()

    def plot_4(self, x1, y1, label, filename):  # chart 5 : polar curve
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label, c="blue")
        plt.plot(0.12802, 1.52, marker="D", label="Czmax", c='red', lw=3)
        plt.plot(0.025, 0.5, marker="D", label="Czfmax", c='green', lw=3)
        plt.plot(0.01296, 0.096, marker="D", label="CzVmax", c='orange', lw=3)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.savefig(filename)
        plt.show()

    def plot_5(self, x1, y1, label, filename):  # chart 6 : incidence function of lift
        plt.figure(figsize=(15, 9))
        plt.plot(x1, y1, label=label, c="blue")
        plt.plot(0.096, 1.018181, marker="D", label="CzVmax", c='orange', lw=3)
        plt.plot(0.5, 4.6909, marker="D", label="Czfmax", c='green', lw=3)
        plt.plot(1.52, 13.9636, marker="D", label="Czmax", c='red', lw=3)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
        plt.grid()
        plt.savefig(filename)
        plt.show()
