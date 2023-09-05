from solution import parse_beasts, write_beasts
from pytest import fixture
from os import path, stat, remove

filename = 'beasts.csv'


@fixture
def beasts_dict():
    return parse_beasts()


def test_parser_output_type(beasts_dict):
    assert type(beasts_dict) == dict


def test_parser_output_length(beasts_dict):
    assert len(beasts_dict)


def test_parser_output_values(beasts_dict):
    dict_keys = beasts_dict.keys()
    dict_values = beasts_dict.values()
    assert all(type(key) is str for key in dict_keys)
    assert all(type(value) is int for value in dict_values)


def test_writer_file_exists(beasts_dict):
    write_beasts(beasts_dict)
    assert path.isfile(filename)
    remove(filename)


def test_writer_file_length(beasts_dict):
    write_beasts(beasts_dict)
    assert stat(filename).st_size
    remove(filename)
