# 1
def cap_CO2_Air_CO2_dot_air(mc_blow_air, mc_ext_air, mc_pad_air, mc_air_can, mc_air_top, mc_air_out):
    return mc_blow_air + mc_ext_air + mc_pad_air - mc_air_can - mc_air_top - mc_air_out


# 2
def cap_CO2_Top_CO2_dot_top(mc_air_top, mc_top_out):
    return mc_air_top - mc_top_out


# 3
def MC_BlowAir(eta_heat_co2, u_blow, p_blow, a_flr):
    return eta_heat_co2 * u_blow * p_blow / a_flr


# 4
def MC_ExtAir(u_ext_co2, phi_ext_co2, a_flr):
    return u_ext_co2 * phi_ext_co2 / a_flr


# helper function for function no.5
def f_Pad(u_pad, phi_pad, a_flr):
    return u_pad * phi_pad / a_flr


# 5
def MC_PadAir(u_pad, phi_pad, a_flr, co2_out, co2_air):
    f_pad = f_Pad(u_pad, phi_pad, a_flr)
    return f_pad * (co2_out - co2_air)


# 6
def MC_AirTop(f_th_scr, co2_air, co2_top):
    return f_th_scr * (co2_air - co2_top)


# 7
def f_ThScr(u_th_scr, k_th_scr, t_air, t_top, g, rho_mean_air, rho_air, rho_top):
    return u_th_scr * k_th_scr * abs(t_air - t_top) ** (2 / 3) + (1 - u_th_scr) * (
            g * (1 - u_th_scr) / (2 * rho_mean_air) * abs(rho_air - rho_top)) ** (1 / 2)


# 8 is not necessary
# 9
def MC_AirOut(f_vent_side, f_vent_forced, co2_air, co2_out):
    return (f_vent_side + f_vent_forced) * (co2_air - co2_out)


# 10
def f_VentRoofSide(c_d, a_flr, u_roof, u_side, a_roof, a_side, g, h_side_roof, t_air, t_out, t_mean_air, c_w, v_wind):
    return c_d / a_flr * (
            u_roof ** 2 * u_side ** 2 * a_roof ** 2 * a_side ** 2 /
            (u_roof ** 2 * a_roof ** 2 + u_side ** 2 * a_side ** 2) *
            2 * g * h_side_roof * (t_air - t_out) / t_mean_air +

            ((u_roof * a_roof + u_side * a_side) / 2) ** 2 *
            c_w * v_wind ** 2) ** (1 / 2)


# 11
def eta_ins_scr(zeta_ins_scr):
    return zeta_ins_scr * (2 - zeta_ins_scr)


# 12
def f_leakage(v_wind, c_leakage):
    if v_wind < 0.25:
        return 0.25 * c_leakage
    return v_wind * c_leakage


# helper function for function no.13
# f_VentRoofSide at A_Roof = 0
def f_VentSide_double_prime(c_d, a_flr, u_side, a_side, c_w, v_wind):
    return c_d / a_flr * (((u_side * a_side) / 2) ** 2 * c_w * v_wind ** 2) ** (1 / 2)


# 13
def f_VentSide(eta_ins_scr, f_vent_side_double_prime, f_leakage, eta_side, eta_side_thr, u_th_scr, f_vent_roof_side):
    if eta_side >= eta_side_thr:
        return eta_ins_scr * f_vent_side_double_prime + 0.5 * f_leakage
    return eta_ins_scr * (
            u_th_scr * f_vent_side_double_prime +
            (1 - u_th_scr) * f_vent_roof_side * eta_side) + 0.5 * f_leakage


# 14
def f_VentForced(eta_ins_scr, u_vent_forced, phi_vent_forced, a_flr):
    return eta_ins_scr * u_vent_forced * phi_vent_forced / a_flr


# 15
def MC_TopOut(f_vent_roof, co2_top, co2_out):
    return f_vent_roof * (co2_top - co2_out)


# 16
def f_VentRoof(eta_ins_scr, f_vent_roof_double_prime, f_leakage, eta_roof, eta_roof_thr, u_th_scr, f_vent_roof_side,
               eta_side):
    if eta_roof >= eta_roof_thr:
        return eta_ins_scr * f_vent_roof_double_prime + 0.5 * f_leakage
    return eta_ins_scr * (
            u_th_scr * f_vent_roof_double_prime + (1 - u_th_scr) * f_vent_roof_side * eta_side) + 0.5 * f_leakage


# 17
def f_VentRoof_double_prime(c_d, u_roof, a_roof, a_flr, g, h_roof, t_air, t_out, t_mean_air, c_w, v_wind):
    return c_d * u_roof * a_roof / (2 * a_flr) * \
           (g * h_roof * (t_air - t_out) / (2 * t_mean_air) + c_w * v_wind ** 2) ** (1 / 2)


# 18 - 9.10
def MC_AirCan(m_ch2o, p, r):
    return m_ch2o * (p - r)


# Sub functions for function 18 - Start
# 9.12
def P(J, CO2_Stom, gamma):
    return (J * (CO2_Stom - gamma)) / (4 * CO2_Stom + 2 * gamma)


# 9.13
def R(P, gamma, CO2_Stom):
    return P * gamma / CO2_Stom


# 9.14
def J(J_Pot, aPAR_Can, theta):
    return (J_Pot + aPAR_Can - ((J_Pot + aPAR_Can) ** 2 - 4 * theta * J_Pot * aPAR_Can) ** (1 / 2)) / (2 * theta)


# 9.15
def J_Pot(J_Max25Can, Ej, t_Can_K, t_25_K, Rg, S, H):
    euler = 2.71828
    return J_Max25Can * euler ** (Ej * (t_Can_K - t_25_K) / (Rg * t_Can_K * t_25_K)) * (
            1 + euler ** ((S * t_25_K - H) / (Rg * t_25_K))) / (1 + euler ** ((S * t_Can_K - H) / (Rg * t_Can_K)))


# 9.16
def J_Max25Can(LAI, J_Max25Leaf):
    return LAI * J_Max25Leaf


# 9.21
def CO2_Stom(eta_CO2_Air_Stom, CO2_Air):
    return eta_CO2_Air_Stom * CO2_Air


# 9.22
def gamma(c_gamma, t_can):
    return c_gamma * t_can


# Sub functions for function 18 - End
# 19, not used since h_c_buf = 1
def h_c_buff(c_buf, c_max_buf):
    if c_buf > c_max_buf:
        return 0
    return 1


if __name__ == '__main__':
    # We chose Netherlands data to calculate
    # Argument data list - Start
    PAR = 100  # Self-ini
    u_blow = 0  # Self-ini
    u_ext_co2 = 0  # Self-ini
    u_pad = 0  # Self-ini
    u_th_scr = 0  # Self-ini
    u_roof = 1  # Self-ini
    u_side = 1  # Self-ini
    u_vent_forced = 0  # Self-ini
    t_air = 273  # Self-ini
    t_top = 273  # Self-ini
    t_out = 273  # Self-ini
    t_can = 273  # Self-ini
    t_mean_air = t_air + 0.15
    t_25_K = 298.15  # Van11
    t_Can_K = t_25_K + 1
    rho_air = 0  # Self-ini
    rho_top = 0  # Self-ini
    rho_mean_air = 1  # Self-ini
    eta_side = 1  # Self-ini
    eta_roof = 1  # Self-ini
    eta_roof_thr = 0.9  # Van11
    eta_side_thr = eta_roof_thr
    eta_heat_co2 = 0.057  # Van11
    eta_CO2_Air_Stom = 0.67  # Van11
    g = 9.81  # Van11
    v_wind = 0.1  # Van11
    c_leakage = 0.0001  # Van11
    k_th_scr = 0.00005  # Van11
    c_d = 0.75  # Van11
    c_w = 0.09  # Van11
    c_gamma = 1.7  # Van11
    phi_ext_co2 = 72000  # Van11
    phi_pad = 1  # Van11, Not used
    phi_vent_forced = 0  # Van11, Not used
    h_side_roof = 0  # Van11, Not used
    h_vent = 0.68  # Van11
    p_blow = 1  # Van11, Not used
    a_flr = 14000  # Van11
    a_roof = 0.1  # Van11
    a_side = 0  # Van11
    zeta_ins_scr = 1  # Van11
    theta = 0.7  # Van11
    alpha = 0.385  # Van11
    m_ch2o = 0.03  # Van11
    Ej = 37000  # Van11
    H = 220000  # Van11
    J_Max25Leaf = 210  # Van11
    Rg = 8.314  # Van11
    S = 710  # Van11
    aPAR_Can = PAR * alpha  # Van11
    LAI = 0.1  # Van11
    co2_out = 370  # Van11
    co2_top = co2_out
    co2_air = 438  # AutonomousGreenhouseChallengeFirstEdition, AiCu's data

    # Argument data list - End

    # Sub functions - Start
    f_th_scr = f_ThScr(u_th_scr, k_th_scr, t_air, t_top, g, rho_mean_air, rho_air, rho_top)  # 7, needed to calculate 6
    f_vent_roof_side = f_VentRoofSide(c_d, a_flr, u_roof, u_side, a_roof, a_side, g, h_side_roof, t_air, t_out,
                                      t_mean_air, c_w, v_wind)  # 10, needed to calculate 13
    eta_ins_scr = eta_ins_scr(zeta_ins_scr)  # 11, needed to calculate
    f_leakage = f_leakage(v_wind, c_leakage)  # 12, needed to calculate
    f_vent_side_double_prime = f_VentSide_double_prime(c_d, a_flr, u_side, a_side, c_w,
                                                       v_wind)  # sub function, needed to calculate 13
    f_vent_side = f_VentSide(eta_ins_scr, f_vent_side_double_prime, f_leakage, eta_side, eta_side_thr, u_th_scr,
                             f_vent_roof_side)  # 13, needed to calculate 9
    f_vent_forced = f_VentForced(eta_ins_scr, u_vent_forced, phi_vent_forced, a_flr)  # 14, needed to calculate 9
    f_vent_roof_double_prime = f_VentRoof_double_prime(c_d, u_roof, a_roof, a_flr, g, h_vent, t_air, t_out, t_mean_air,
                                                       c_w, v_wind)  # 17, needed to calculate 16
    f_vent_roof = f_VentRoof(eta_ins_scr, f_vent_roof_double_prime, f_leakage, eta_roof, eta_roof_thr, u_th_scr,
                             f_vent_roof_side, eta_side)  # 16, needed to calculate 15
    CO2_Stom = CO2_Stom(eta_CO2_Air_Stom, co2_air)  # 9.21, needed to calculate 9.12 and 9.13
    gamma = gamma(c_gamma, t_can)  # 9.22, needed to calculate 9.12 and 9.13
    J_Max25Can = J_Max25Can(LAI, J_Max25Leaf)  # 9.16, needed to calculate 9.15
    J_Pot = J_Pot(J_Max25Can, Ej, t_Can_K, t_25_K, Rg, S, H)  # 9.15, needed to calculate 9.14
    j = J(J_Pot, aPAR_Can, theta)  # 9.14, needed to calculate 9.12
    p = P(j, CO2_Stom, gamma)  # 9.12, needed to calculate 18
    r = R(p, gamma, CO2_Stom)  # 9.13, needed to calculate 18
    # Sub functions - End

    # Main function
    mc_blow_air = MC_BlowAir(eta_heat_co2, u_blow, p_blow, a_flr)  # 3
    mc_ext_air = MC_ExtAir(u_ext_co2, phi_ext_co2, a_flr)  # 4
    mc_pad_air = MC_PadAir(u_pad, phi_pad, a_flr, co2_out, co2_air)  # 5
    mc_air_top = MC_AirTop(f_th_scr, co2_air, co2_top)  # 6
    mc_air_out = MC_AirOut(f_vent_side, f_vent_forced, co2_air, co2_out)  # 9
    mc_top_out = MC_TopOut(f_vent_roof, co2_top, co2_out)  # 15
    mc_air_can = MC_AirCan(m_ch2o, p, r)  # 18

    dx_air = cap_CO2_Air_CO2_dot_air(mc_blow_air, mc_ext_air, mc_pad_air, mc_air_can, mc_air_top, mc_air_out)  # 1
    dx_top = cap_CO2_Top_CO2_dot_top(mc_air_top, mc_top_out)  # 2
