# Import built-in modules
import glob
import os

# Import third-party modules
from jinja2 import Template
import stringcase

template = Template(
    r"""
Examples
========
{% for file_ in Examples.get_examples() %}
{{ Examples.get_name(file_) }}
{{ Examples.get_line(Examples.get_name(file_))}}
```python
{{ Examples.get_content(file_) }}
```
{% endfor %}
    
"""
)


class Examples(object):
    def __init__(self, root):
        self._root = root

    def get_examples(self):
        files = [
            file_
            for file_ in glob.iglob(os.path.join(self._root, "*.py"))
            if "_psd_files.py" not in file_
        ]
        return files

    @staticmethod
    def convert_relative_path(file):
        path = file.split("examples")[1]
        return "../examples{}".format(path.replace("\\", "/"))

    @staticmethod
    def get_name(file):
        name = os.path.basename(file).split(".py")[0]
        return stringcase.titlecase(name)

    @staticmethod
    def get_line(name):
        return "-" * len(name)

    @staticmethod
    def get_content(file_):
        with open(file_, "r") as f:
            return "".join(f.readlines())


root = os.path.dirname(os.path.dirname(__file__))
with open("examples.md", "w") as f:
    f.write(template.render(Examples=Examples(os.path.join(root, "examples"))))
