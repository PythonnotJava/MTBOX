from os import PathLike
from yaml import load, FullLoader, dump

# yaml_settings
def _load_yaml(path : PathLike) -> dict:
    _f = open(path, 'r', encoding='U8')
    _data = load(_f, FullLoader)
    _f.close()
    return _data

# Dump new settings to file
def _dump_new_cfg(path : PathLike, data : dict) -> None:
    _f = open(path, 'w', encoding='U8')
    dump(data, _f)
    _f.close()
