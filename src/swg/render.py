from jinja2 import Template

def render_article(template: str, context: dict) -> str:
    templated_text = Template(template)
    return templated_text.render(**context)
