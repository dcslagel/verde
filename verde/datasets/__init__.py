# Copyright (c) 2017 The Verde Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
# pylint: disable=missing-docstring
from .synthetic import CheckerBoard
from .sample_data import (
    locate,
    fetch_baja_bathymetry,
    setup_baja_bathymetry_map,
    fetch_rio_magnetic,
    setup_rio_magnetic_map,
    fetch_california_gps,
    setup_california_gps_map,
    fetch_texas_wind,
    setup_texas_wind_map,
)
