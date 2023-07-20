from swg.render import render_article


def test_render_article():
    template = """{{article_title}} - {{article_subtitle}} - {{body}}"""
    interpolation_variables = dict(
        article_title="Test Driven Development",
        article_subtitle="Qué quiere decir empezar por los tests",
        body="Es una práctica contra intuitiva"
    )
    result = render_article(template, interpolation_variables)
    test_result = "Test Driven Development" 
    test_result += " - Qué quiere decir empezar por los tests"
    test_result += " - Es una práctica contra intuitiva"
    assert result == test_result