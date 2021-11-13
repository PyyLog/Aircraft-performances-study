# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name       :
# Purpose    :
#
# Author     : Pritam Charles Kantane
# Class      : 3PF2
# Date       : 02 Nov 2021
# -------------------------------------------------------------------------------
import math


class GlideCurve:
    def __init__(self):
        self.rho = 0.4127
        self.wing_surface = 363
        self.mass = 212000
        self.g = 9.81
        self.alpha = math.radians(30)

    def get_Cx(self, velocity):
        Cz = (2 * self.mass * self.g) / (self.rho * self.wing_surface * (velocity ** 2))
        Cx = 0.0125 + 0.05 * (Cz ** 2)
        return Cx

    def get_thrust(self, velocity):
        return (1 / 2) * (self.rho * self.wing_surface * (velocity ** 2) * self.get_Cx(velocity))

    def get_thrust_turn(self, velocity):
        return (1 / math.cos(self.alpha)) * self.get_thrust(velocity)


###

class FlightEnvelope:
    def __init__(self):
        self.wing_surface = 363
        self.mass = 212000
        self.g = 9.81

    def get_Cz_Vmax(self, rho):
        F_max = ((rho / 1.225) ** 0.6) * 2 * 269562
        Cz_Vmax = (1 / (2 * 0.05)) * ((F_max / (self.mass * self.g)) - math.sqrt(
            ((F_max / (self.mass * self.g)) ** 2) - (4 * 0.05 * 0.0125)))
        return Cz_Vmax

    def get_Vmax(self, rho):
        return math.sqrt((2 * self.mass * self.g) / (rho * self.wing_surface * self.get_Cz_Vmax(rho)))

    def get_Vmax_limit(self, T):
        return 0.9 * 20.05 * math.sqrt(T)

    def get_Czmax(self, rho):
        if rho == 1.225:
            Czmax = 1.96
            return Czmax
        else:
            Czmax = 1.52
            return Czmax

    def get_Vmin(self, rho):
        return math.sqrt((2 * self.mass * self.g) / (rho * self.wing_surface * self.get_Czmax(rho)))


###

class FlightDomain:
    def __init__(self):
        self.Vs = 135  # Vitesse de décrochage (volets fermés)
        self.Vso = 119  # Vitesse de décrochage (volets sortis)
        self.Vne = 269  # Vitesse à ne jamais dépasser (Vmax)
        self.Vfe = 191  # Vitesse maximale (volets sortis)
        self.Va = 213  # Vitesse de manoeuvre
        self.Vc = 245  # Vitesse de croisière
        self.Vd = 306  # Vitesse de piqué

    def get_speed_fr(self, charge_factor):
        return math.sqrt(charge_factor * (self.Vs ** 2))

    def get_speed_fe(self, charge_factor):
        return math.sqrt(charge_factor * (self.Vso ** 2))

    def affine_equa(self, velocity):
        return (1 / 37) * velocity - (306 / 37)


###

class PolarCurve:
    def __init__(self):
        self.wing_surface = 363
        self.mass = 212000
        self.g = 9.81
        self.rho = 0.4127

    def get_Cz(self, alpha):
        return -0.016 + 0.11 * alpha

    def get_Cx(self, alpha):
        return 0.0125 + 0.05 * (self.get_Cz(alpha) ** 2)


###

class LiftCurve:
    def get_Cz(self, alpha):
        return -0.016 + 0.11 * alpha
