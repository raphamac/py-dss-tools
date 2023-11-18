# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : Monitor.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd
from dataclasses import dataclass, field
from typing import Optional, Dict


class Monitor:
    def __init__(self, dss: DSS):
        self._dss = dss

    def monitor(self, name: str): # -> Optional[Dict[(str, str), pd.DataFrame]]:
        name = name.lower()
        if name not in [m.lower() for m in self._dss.monitors.names]:
            return None

        self._dss.monitors.name = name
        m_mode = self._dss.monitors.mode
        return {(name, m_mode): self.__create_dataframe()}

    def __create_dataframe(self):

        num_channels = self._dss.monitors.num_channels
        headers = self._dss.monitors.header
        dbl_hour = self._dss.monitors.dbl_hour
        dbl_freq = self._dss.monitors.dbl_freq

        dict_to_df = dict()
        dict_to_df["Hour"] = dbl_hour
        dict_to_df["sec"] = dbl_freq
        for index, header in enumerate(headers):
            dict_to_df[header] = self._dss.monitors.channel(index + 1)

        return pd.DataFrame().from_dict(dict_to_df)

