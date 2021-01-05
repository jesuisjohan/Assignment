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


# if need to overload the above function, use this

# 6
def MC_AirTop(f_th_scr, co2_air, co2_top):
    return f_th_scr * (co2_air - co2_top)


# 7
def f_ThScr(u_th_scr, k_th_scr, t_air, t_top, g, rho_mean_air, rho_air, rho_top):
    return u_th_scr * k_th_scr * abs(t_air - t_top) ** (2 / 3) + (1 - u_th_scr) * (
            g * (1 - u_th_scr) / (2 * rho_mean_air) * abs(rho_air - rho_top)) ** (1 / 2)


# 8
def phi_crack(length, so, rho_mean, g, rho1, rho2):
    return length * so / rho_mean * (1 / 2 * rho_mean * so * g * (rho1 - rho2)) ** 1 / 2


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


# 18
def MC_AirCan(m_ch2o, p, r):
    return m_ch2o * (p - r)


# 19 is removed because h_C_Buf is always equal to 1
# 20 - 29 are no longer required

if __name__ == '__main__':
    print('Hello world')
