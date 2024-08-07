# -*- coding: utf-8 -*-
# @Author  : Raphael Maccari
# @Email   : raphaelmaccari@gmail.com
# @File    : StudyVTCD.py
# @Software: PyCharm

from py_dss_tools.studies.StudyBase import StudyBase
from py_dss_tools.results.VTCDresults import VTCDresults
from py_dss_tools.view.ViewVTCDstudy import ViewVTCDresults
from dataclasses import dataclass

@dataclass(kw_only=True)
class StudyVTCD(StudyBase):

    def __post_init__(self):
        super().__post_init__()
        self._results = VTCDresults(self._dss)
        self._view = ViewVTCDresults(self._dss, self._results)

    @property
    def results(self):
        return self._results

    @property
    def view(self):
        return self._view
