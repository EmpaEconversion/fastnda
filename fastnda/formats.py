"""Convert outputs to different formats."""

from collections.abc import Mapping
from types import MappingProxyType

import polars as pl

BDF_COL_MAP: Mapping[str, str] = MappingProxyType(
    {
        "index": "record_index",
        "voltage_V": "voltage_volt",
        "current_mA": "current_ampere",
        "unix_time_s": "unix_time_second",
        "step_time_s": "step_time_second",
        "total_time_s": "test_time_second",
        "cycle_count": "cycle_count",
        "step_count": "step_count",
        "step_index": "step_index",
        "step_type": "step_type",
        "capacity_mAh": "step_capacity_ah",
        "energy_mWh": "step_energy_wh",
    }
)

BDF_MULTIPLIER_MAP: Mapping[str, float] = MappingProxyType(
    {
        "current_ampere": 1e-3,
        "step_capacity_ah": 1e-3,
        "step_energy_wh": 1e-3,
    }
)


def to_bdf(df: pl.DataFrame) -> pl.DataFrame:
    """Convert fastnda dataframe to bdf."""
    df = df.rename(BDF_COL_MAP)
    return df.with_columns(pl.col(k) * v for k, v in BDF_MULTIPLIER_MAP.items())
