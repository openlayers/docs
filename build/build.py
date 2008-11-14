#!/usr/bin/python
import os
import sys

from docutils.core import publish_file
from docutils.io import FileInput, FileOutput
from docutils.core import publish_parts

from docutils import nodes
from docutils.parsers.rst import directives
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

pygments_formatter = HtmlFormatter()

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        # no lexer found - use the text one instead of an exception
        lexer = get_lexer_by_name('text')
    parsed = highlight(u'\n'.join(content), lexer, pygments_formatter)
    return [nodes.raw('', parsed, format='html')]
pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
directives.register_directive('code-block', pygments_directive)

def doc_list(root_path = ".."): 
    docs = []
    for item in os.listdir(root_path):
        about = os.path.join(root_path, item, "about.rst")
        doc = os.path.join(root_path, item, "%s.rst" % item)
        if os.path.exists(about):
            data = publish_parts(open(about).read(), writer_name="html")
            body = data['html_body']
            data = publish_parts(open(doc).read(), writer_name="html")
            title = data['title']
            docs.append({'title': title, 'description': body, 'name': item, 'path':doc})
    return docs       

def index(root_path=".."):
    docs = doc_list(root_path)
    from mako.template import Template
    from mako.lookup import TemplateLookup
    lookup=TemplateLookup(directories=[os.path.join(root_path, "build", "templates")])
    t = lookup.get_template("index.html")
    return t.render(docs=docs)

def run_file(in_path, out_path):
    """
    >>> run_file("../spherical_mercator/spherical_mercator.rst", "out.html")
    """
    publish_file(source_path=in_path, destination_path=out_path, writer_name="html", settings_overrides={'stylesheet_path': 'build/rst.css'} ) 

def build_output(root_path="..", out_dir=None):
    index_content = index(root_path)
    if not out_dir:
        out_dir = os.path.join(root_path, "output")
    try:
        os.mkdir(out_dir)
    except:
        pass
    f = open(os.path.join(out_dir, "index.html"), "w") 
    f.write(index_content)
    f.close()
    for i in doc_list(root_path):
        try:
            os.mkdir(os.path.join(out_dir, i['name']))
        except:
            pass
        run_file(i['path'], os.path.join(out_dir, i['name'], "index.html"))

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    root = "."
    target = "output"
    if sys.argv[1]:
        target = sys.argv[1]
    build_output(root, target)
