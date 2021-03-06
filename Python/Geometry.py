# ---------------------------------------------------------------------------
# Copyright (C) 2017 Frank Jargstorff
#
# This file is part of the AcousticBEM library.
# AcousticBEM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AcousticBEM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AcousticBEM.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------------
# calculate the normal coordinates
import numpy as np
from numpy.linalg import norm


def Normal2D(pointA, pointB):                  
    diff = pointA - pointB                          
    len = norm(diff)                                
    return np.array([diff[1]/len, -diff[0]/len])    

def Normal3D(a, b, c):
    ab = b - a
    ac = c - a
    normal = np.cross(ab, ac)
    normal /= norm(normal)
    return normal
    
