# -*- coding: utf-8 -*-
# @Author  : Raphael Maccari
# @Email   : raphaelmaccari@gmail.com
# @File    : VTCDSagSwell.py
# @Software: PyCharm


import pandas as pd
from py_dss_interface import DSS
from py_dss_tools.dss_tools import DSSTools


class VTCDSagSwell:

    def __init__(self, dss: DSS):
        self._dss = dss
        self.vmags_df = pd.DataFrame()

    def sag_swell_1phsc_df_pu(self, bus_fault,vsag_1=0.1,vsag_2=0.2,vsag_3=0.3,vsag_4=0.4,vsag_5=0.5,vsag_6=0.6,vsag_7=0.7,
                              vsag_8=0.8,vsag_9=0.9,vsag_10=0.95, vswell_1=1.05, vswell_2=1.06, vswell_3=1.1) -> pd.DataFrame:

        self._bus_fault = bus_fault
        self._vsag_1 = vsag_1
        self._vsag_2 = vsag_2
        self._vsag_3 = vsag_3
        self._vsag_4 = vsag_4
        self._vsag_5 = vsag_5
        self._vsag_6 = vsag_6
        self._vsag_7 = vsag_7
        self._vsag_8 = vsag_8
        self._vsag_9 = vsag_9
        self._vsag_10 = vsag_10
        self._vswell_1 = vswell_1
        self._vswell_2 = vswell_2
        self._vswell_3 = vswell_3
        self._dss.text(f"new fault.1_ph_{self._bus_fault} phases=1 bus1={self._bus_fault}.1 bus2={self._bus_fault}.0")
        self._dss.text("solve")


        vmags_df, vangs_df = DSSTools(self._dss).results.circuit_vmag_vang_dfs()
        vmags_df['vmin'] = vmags_df.min(axis=1) #Cria uma coluna adicional e faz o mínimo das 3 anteriores.
        vmags_df['vmax'] = vmags_df.iloc[:, :-1].max(axis=1) #Cria uma coluna adicional e faz o máximo das 3 primeiras

        colors_sag = []

        for v_min in vmags_df['vmin']:
            if v_min <= vsag_1:
                colors_sag.append("black")
            elif v_min <= vsag_2:
                colors_sag.append("maroon")
            elif v_min <= vsag_3:
                colors_sag.append("purple")
            elif v_min <= vsag_4:
                colors_sag.append("navy")
            elif v_min <= vsag_5:
                colors_sag.append("teal")
            elif v_min <= vsag_6:
                colors_sag.append("blue")
            elif v_min <= vsag_7:
                colors_sag.append("aqua")
            elif v_min <= vsag_8:
                colors_sag.append("yellow")
            elif v_min <= vsag_9:
                colors_sag.append("lime")
            elif v_min < vsag_10:
                colors_sag.append("olive")
            else:
                colors_sag.append("green")

        vmags_df['colors_sag'] = colors_sag

        colors_swell = []
        for v_max in vmags_df['vmax']:
            if v_max <= vswell_1:
                colors_swell.append("green")
            elif v_max <= vswell_2:
                colors_swell.append("yellow")
            elif v_max <= vswell_3:
                colors_swell.append("red")
            else:
                colors_swell.append("black")

        vmags_df['colors_swell'] = colors_swell

        self.vmags_df = vmags_df

        return vmags_df
