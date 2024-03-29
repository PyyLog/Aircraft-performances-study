# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Date       : 02 Nov 2021
# -------------------------------------------------------------------------------
import curves_utils
from src.charts_utils import *
import numpy as np

glide_curve = curves_utils.GlideCurve()
flight_envelope = curves_utils.FlightEnvelope()
flight_domain = curves_utils.FlightDomain()
polar_curve = curves_utils.PolarCurve()
incidence_function_of_lift = curves_utils.IncidenceFunctionOfLift()


# Glider curves
def get_axis_1_2():
    velocity_list1, velocity_list2, F_list_as, F_list_os = [], [], [], []
    velocity_list3, velocity_list4, F_list_turn_as, F_list_turn_os = [], [], [], []

    for speed in range(99, 409):
        F = glide_curve.get_thrust(speed)
        F_turn = glide_curve.get_thrust_turn(speed)
        if speed < 269:
            velocity_list1.append(speed)
            F_list_as.append(F)
        elif speed > 269:
            velocity_list2.append(speed)
            F_list_os.append(F)
        if speed < 289:
            velocity_list3.append(speed)
            F_list_turn_as.append(F_turn)
        elif speed > 289:
            velocity_list4.append(speed)
            F_list_turn_os.append(F_turn)

    return velocity_list1, velocity_list2, velocity_list3, velocity_list4, F_list_as, F_list_os, F_list_turn_as, F_list_turn_os  # as : allowed speed / os : overspeed


# Flight envelop
def get_axis_3():
    altitude_list = [i for i in range(0, 18000, 1000)]
    rho_list = [1.225, 1.1116, 1.0065, 0.9091, 0.8191, 0.7361, 0.6597, 0.5895, 0.5252, 0.4663, 0.4127, 0.3639, 0.3108,
                0.2655, 0.2268, 0.1937, 0.1664, 0.1423]
    temperature_list = [(288.15 - 0.0065 * alt) for alt in range(0, 18000, 1000)]
    Vmin_list = [flight_envelope.get_Vmin(rho) for rho in rho_list]
    Vmax_list = []
    x_list_sustentation_ceiling = [i for i in range(0, 400, 10)]
    sustentation_ceiling_list = [17115 for i in range(0, 40)]

    for temperature in temperature_list:
        Vmax_limit = flight_envelope.get_Vmax_limit(temperature)
        if Vmax_limit < 269:
            Vmax_limit = 269
            Vmax_list.append(Vmax_limit)
        else:
            Vmax_list.append(Vmax_limit)

    return x_list_sustentation_ceiling, Vmin_list, Vmax_list, sustentation_ceiling_list, altitude_list


# Flight domain
def get_axis_4():
    V_list_fr_1, V_list_fr_2, V_list_fr_3, V_list_fr_4, V_list_fr_5, V_list_fr_6, V_list_fe_1, V_list_fe_2 = [], [], [], [], [], [], [], []  # fr : flaps retracted ; fe : flaps extended
    n_list_fr_1, n_list_fr_2, n_list_fr_3, n_list_fr_4, n_list_fr_5, n_list_fr_6, n_list_fe_1, n_list_fe_2, n_list_kp = [], [], [], [], [], [], [], [], []
    Vs_list, Vso_list, Vne_list, Vfe_list, Va_list, Vc_list, Vd_list = [], [], [], [], [], [], []

    for n in np.arange(-1, 2.5, 10 ** (-3)):
        n_list_kp.append(n)  # liste de facteurs de charge entre -1 et 2.5
        Vs_list.append(flight_domain.Vs)
        Vso_list.append(flight_domain.Vso)
        Vne_list.append(flight_domain.Vne)
        Vfe_list.append(flight_domain.Vfe)
        Va_list.append(flight_domain.Va)
        Vc_list.append(flight_domain.Vc)
        Vd_list.append(flight_domain.Vd)

        if n >= 0:
            V_list_fr_5.append(flight_domain.Vd)  # droite bleue avec Vd constante et n compris entre 0 et 2.5
            V_list_fr_1.append(flight_domain.get_speed_fr(n))  # courbe bleue avec n compris entre 0 et 2.5
            n_list_fr_1.append(n)
            n_list_fr_5.append(n)
        elif n < 0:
            V_list_fr_2.append(flight_domain.get_speed_fr(-n))  # courbe bleue avec n compris entre 0 et -1
            n_list_fr_2.append(n)
        if n > 0 and n < 2:
            V_list_fe_1.append(flight_domain.get_speed_fe(n))  # courbe noire avec n compris entre 0 et -1
            n_list_fe_1.append(n)

    for velocity in np.arange(flight_domain.get_speed_fr(2.5), flight_domain.Vd, 10 ** (-3)):
        V_list_fr_3.append(velocity)
        n_list_fr_3.append(2.5)  # droite bleue avec n = 2.5 et V compris entre Va à Vd

    for velocity in np.arange(flight_domain.get_speed_fr(1), flight_domain.Vne, 10 ** (-3)):
        V_list_fr_4.append(velocity)
        n_list_fr_4.append(-1)  # droite bleue avec n = -1 et V compris entre Vs à Vne

    for velocity in np.arange(flight_domain.get_speed_fe(2), flight_domain.Vfe, 10 ** (-3)):
        V_list_fe_2.append(velocity)
        n_list_fe_2.append(2)  # droite noire avec n = 2 et V allant jusqu'à Vfe

    for velocity in np.arange(flight_domain.Vne, flight_domain.Vd, 10 ** (-3)):
        V_list_fr_6.append(flight_domain.affine_equa(velocity))
        n_list_fr_6.append(velocity)  # droite affine bleue avec n allant de -1 à 0 et V compris entre Vne et Vd

    return V_list_fr_1, V_list_fr_2, V_list_fr_3, V_list_fr_4, V_list_fr_5, V_list_fr_6, V_list_fe_1, V_list_fe_2, Vs_list, Vso_list, Vne_list, Vfe_list, Va_list, Vc_list, Vd_list, n_list_fr_1, n_list_fr_2, n_list_fr_3, n_list_fr_4, n_list_fr_5, n_list_fr_6, n_list_fe_1, n_list_fe_2, n_list_kp


# Polaire de l'avion PROBLEME
def get_axis_5():
    Cl_list, Cd_list = [], []

    for alpha in range(-10, 20):
        Cl_list.append(polar_curve.get_Cl(alpha))
        Cd_list.append(polar_curve.get_Cd(alpha))

    return Cd_list, Cl_list


# Courbe de portance PROBLEME
def get_axis_6():
    Cl_list, alpha_list = [], []

    for alpha in range(-10, 20):
        alpha_list.append(alpha)
        Cl_list.append(incidence_function_of_lift.get_Cl(alpha))

    return Cl_list, alpha_list


###


chart_1_2 = Graphic(title="Courbe planeur de l'avion", xlabel="Vitesse V (en m/s)", ylabel="Poussée F (en N)")

chart_1_2.plot_1(get_axis_1_2()[0], get_axis_1_2()[1], get_axis_1_2()[4], get_axis_1_2()[5],
                 label1="courbe planeur vitesse de vol", label2="courbe planeur après vitesse maximale",
                 filename="glide_curve_1.png")

chart_1_2.plot_1(get_axis_1_2()[2], get_axis_1_2()[3], get_axis_1_2()[6], get_axis_1_2()[7],
                 label1="courbe planeur en virage à 30° (vitesse de vol)",
                 label2="courbe planeur en virage à 30° (après vitesse maximale)", filename="glide_curve_2.png")

###

chart_3 = Graphic(title="Enveloppe de vol de l'avion", xlabel="Vitesse V (en m/s)", ylabel="Altitude (en m)")

chart_3.plot_2(get_axis_3()[0], get_axis_3()[1], get_axis_3()[2], get_axis_3()[3], get_axis_3()[4], label1="Vmin",
               label2="Vmax", label3="Plafond de sustentation", filename="flight_envelope.png")

###

chart_4 = Graphic(title="Domaine de vol de l'avion", xlabel="Vitesse V (en m/s)",
                  ylabel="Facteur de charge n")

chart_4.plot_3(get_axis_4()[0], get_axis_4()[1], get_axis_4()[2], get_axis_4()[3], get_axis_4()[4], get_axis_4()[20],
               get_axis_4()[6],
               get_axis_4()[7], get_axis_4()[8], get_axis_4()[9], get_axis_4()[10], get_axis_4()[11], get_axis_4()[12],
               get_axis_4()[13], get_axis_4()[14], get_axis_4()[15], get_axis_4()[16], get_axis_4()[17],
               get_axis_4()[18], get_axis_4()[19], get_axis_4()[5], get_axis_4()[21], get_axis_4()[22],
               get_axis_4()[23],
               label1="Domaine de vol volets rentrés", label2="Domaine de vol volets sortis", label3="Vs", label4="Vso",
               label5="Vne", label6="Vfe", label7="Va", label8="Vc", label9="Vd", filename="flight_domain.png")

###

chart_5 = Graphic(title="Polaire de l'avion", xlabel="Coefficient de trainée Cx",
                  ylabel="Coefficient de portance Cz")

chart_5.plot_4(get_axis_5()[0], get_axis_5()[1], label="Polaire de l'avion à 10000m d'altitude",
               filename="polar_curve.png")

###

chart_6 = Graphic(title="Incidence en fonction de la portance", xlabel="Coefficient de portance Cz",
                  ylabel="Incidence alpha (en °)")

chart_6.plot_5(get_axis_6()[0], get_axis_6()[1], label="Courbe de portance de l'avion",
               filename="incidence_function_of_lift.png")

###
