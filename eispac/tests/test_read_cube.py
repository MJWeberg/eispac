import pathlib

from ndcube import NDCube

import eispac


def test_invalid_filepath_type():
    eis_cube = eispac.read_cube(42)
    assert eis_cube is None

def test_missing_files():
    eis_cube = eispac.read_cube('non-existent_file.head.h5', 0)
    assert eis_cube is None

def test_invalid_window(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, -7)
    assert eis_cube is None

def test_read_cube_data_str_filepath(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    assert isinstance(eis_cube, eispac.EISCube)

def test_read_cube_head_str_filepath(test_head_filepath):
    eis_cube = eispac.read_cube(test_head_filepath, 0)
    assert isinstance(eis_cube, eispac.EISCube)

def test_read_fit_pathlib_filepath(test_data_filepath):
    path_obj = pathlib.Path(test_data_filepath)
    eis_cube = eispac.read_cube(path_obj)
    assert isinstance(eis_cube, eispac.EISCube)

def test_total_intensity(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    sum_inten = eis_cube.sum_spectra()
    assert isinstance(sum_inten, NDCube)

def test_slice_box(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    slice_cube = eis_cube[0:10,0:10,:]
    assert isinstance(slice_cube, NDCube)

def test_slice_step(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    slice_cube = eis_cube[:,1,:]
    assert isinstance(slice_cube, NDCube)

def test_slice_point(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    slice_cube = eis_cube[1,1,:]
    assert isinstance(slice_cube, NDCube)

def test_extract_pix(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    point_cube = eis_cube.extract_points([[0,0], [1,1]], units='pixel')
    assert isinstance(point_cube, NDCube)

def test_extract_arcsec(test_data_filepath):
    eis_cube = eispac.read_cube(test_data_filepath, 192.394)
    point_cube = eis_cube.extract_points([[0,-200], [20,-160]], units='arcsec')
    assert isinstance(point_cube, NDCube)