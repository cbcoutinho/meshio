# -*- coding: utf-8 -*-
#
import pytest

import meshio

import helpers


@pytest.mark.parametrize('mesh', [
    helpers.tri_mesh,
    helpers.quad_mesh,
    helpers.tri_quad_mesh,
    helpers.tet_mesh,
    ])
def test_io(mesh):
    helpers.write_read(
        meshio.permas_io.write,
        meshio.permas_io.read,
        mesh, 1.0e-15
        )
    return
