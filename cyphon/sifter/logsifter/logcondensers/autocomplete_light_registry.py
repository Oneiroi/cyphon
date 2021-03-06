# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines Autocomplete models for use in admin pages for the LogCondensers app.
"""

# third party
import autocomplete_light.shortcuts as autocomplete_light

# local
from sifter.condensers.autocomplete import (
    FilterTargetFieldsByBottle,
    FilterTargetFieldsByCondenser,
)
from .models import LogCondenser


class FilterTargetFieldsByLogCondenser(FilterTargetFieldsByCondenser):
    """
    Defines autocomplete rules for target_field on the DataFitting admin page.
    """
    model = LogCondenser


autocomplete_light.register(FilterTargetFieldsByBottle)
autocomplete_light.register(FilterTargetFieldsByLogCondenser)

