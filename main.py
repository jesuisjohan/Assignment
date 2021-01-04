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

if __name__ == '__main__':
    print('Hello world')
