"""STDF Record Definitions"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FileAttributeRecord:
    """FAR - File Attribute Record"""
    cpu_type: int
    stdf_ver: int


@dataclass
class MasterInformationRecord:
    """MIR - Master Information Record"""
    setup_t: int
    start_t: int
    stat_num: int
    mode_cod: str
    rtst_cod: str
    prot_cod: str
    lot_id: str
    part_typ: str
    node_nam: str
    tstr_typ: str
    job_nam: str


@dataclass
class ParametricTestRecord:
    """PTR - Parametric Test Record"""
    test_num: int
    head_num: int
    site_num: int
    test_flg: int
    parm_flg: int
    result: float
    test_txt: str
    alarm_id: str
    opt_flag: int
    res_scal: int
    llm_scal: int
    hlm_scal: int
    lo_limit: float
    hi_limit: float
    units: str


@dataclass
class PartResultsRecord:
    """PRR - Part Results Record"""
    head_num: int
    site_num: int
    part_flg: int
    num_test: int
    hard_bin: int
    soft_bin: int
    x_coord: int
    y_coord: int
    test_t: int
    part_id: str
    part_txt: str
