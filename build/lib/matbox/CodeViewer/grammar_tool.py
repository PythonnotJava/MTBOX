# Parser for mtml files
# Sincere thanks to the large number of almost comprehensive tutorials on the re library on the Internet

import re

class MTFileTool:

    @staticmethod
    def _parse_markup(markup : "markup is fstream"):
        # defined grammars
        editor_pattern = re.compile(
            r'<editor style="([^"]+)">\s*<code format="(\.[^"]+)">\s*([\s\S]+?)\s*</code>\s*</editor>')
        details_pattern = re.compile(r'<details style="([^"]+)">\s*([\s\S]+?)\s*</details>')
        line_pattern = re.compile(r'<line>\s*<parameter>(.*?)</parameter>\s*<function>(.*?)</function>\s*</line>')

        # parse the editor section
        editor_match = editor_pattern.search(markup)
        editor_style = editor_match.group(1)
        editor_content = editor_match.group(3)
        code_format = editor_match.group(2)

        # parse the details section
        details_match = details_pattern.search(markup)
        details_style = details_match.group(1)
        lines = line_pattern.findall(details_match.group(2))

        # return the results as a dict
        result = {
            'editor_style': editor_style,
            'editor_content': editor_content,
            'code_format': code_format,
            'lines': [{'parameter': p, 'function': f} for p, f in lines],
            'details_style': details_style
        }
        return result

    # read & parser
    def read(self, path : str):
        if path.endswith('.mtml'):
            try:
                _f = open(path, 'r', encoding='U8')
                _t = _f.read()
                _f.close()
                return self._parse_markup(_t)
            except Exception as e:
                raise e
        else:
            raise "Just support the file that ends with '.mdml'."

    # by add a new file, the class will read in the data
    # write as a new mtml-file
    # you can config
    # Ultimately, the function will return a mtml document content
    @staticmethod
    def write( codes : str, **kwargs) -> str:
        _base_format = """<editor style="{}"><code format="{}">{}</code></editor>"""
        """
        The format of kwargs is like this(or supported parameters) : 
        {
            "editor_style" : qss,
            'code_format': code_format,
            'lines': [{'parameter': p0, 'function': f0}, {'parameter': p1, 'function': f2}, ...],
            'details_style': qss
        }
        """
        if "editor_style" in kwargs:
            if 'code_format' in kwargs:
                _base_format = _base_format.format(kwargs['editor_style'], kwargs['code_format'], codes)
            else:
                _base_format = _base_format.format(kwargs['editor_style'], '.py', codes)
        else:
            _base_format = _base_format.format('font-size: 24px;color: darkblue;', '.py', codes)
        if "details_style" in kwargs :
            _base_format = _base_format + '<details style="{}">'.format(kwargs['details_style'])
        else:
            _base_format = _base_format + '<details style="{}">'.format('font-size: 16px;color: darkblue;')
        # 'lines': [{'parameter': p0, 'function': f0}, {'parameter': p1, 'function': f2}, ...]
        if 'lines' in kwargs:
            for _dict in kwargs['lines']:
                _base_format += "<line><parameter>{}</parameter><function>{}</function></line>".\
                    format(_dict['parameter'], _dict['function'])
        else:
            _base_format += "<line><parameter>参数</parameter><function>参数说明</function></line>"
        return _base_format + "</details>"
