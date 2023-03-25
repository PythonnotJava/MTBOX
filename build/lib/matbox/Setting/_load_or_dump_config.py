from yaml import load, FullLoader, dump
from os import PathLike

# qss_loader
def _load_qss(path : PathLike) -> str:
    _f = open(path, 'r', encoding='U8')
    _text = _f.read()
    _f.close()
    return _text

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