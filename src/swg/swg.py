import jinja2
from pathlib import Path
from datetime import datetime
import shutil
import markdown


current_working_directory = Path(__file__).parent.resolve()
default_templates = Path(current_working_directory) /'templates' / 'default'
template_loader = jinja2.FileSystemLoader(searchpath=default_templates)
environment = jinja2.Environment(
    loader=template_loader, autoescape=jinja2.select_autoescape()
)
simple_template = environment.get_template('post.html')

def get_body_from_markdown(mdfile):
    with open(mdfile) as reader:
        text = reader.read()
        md = markdown.Markdown(extensions=['full_yaml_metadata'])
        body = md.convert(text)
        print(body, md.Meta)

if __name__ == '__main__':
    shutil.rmtree('blog')
    shutil.copytree(default_templates, 'blog')
    get_body_from_markdown(Path('.') / 'origin' / 'article1.md')
    with open('blog/post.html', 'w', encoding='utf-8') as handler:
        print(simple_template.render(
            **{
                "article_title": "How to write a blog",
                "article_subtitle": "Simple is better than comples, complex better than complicated",
                "publishing_date": str(datetime.now()),
                "body": "La mecanografía clásica queda obsoleta frente a la aparición"
                "de nuevas tecnologías."
            }
        ), file=handler)