
from swg.articles import get_article_metadata
from swg.articles import get_all_articles_path_from_dir
from swg.render import render_article
from swg.articles import get_article_metadata,get_article_from_path
from swg import settings
from pathlib import Path
import os
import pytest

@pytest.fixture
def current_working_directory():
    return settings.CURRENT_WORKING_DIR


def test_exists_blog_article_template(current_working_directory):
    assert os.path.exists(
        Path(current_working_directory) / "templates" / "default" / "post.html")


def test_get_article_metadata():
    test_article = "---\narticle_title: titulo"
    test_article += "\narticle_subtitle: subtitulo"
    test_article += "\n---\ntext\n"

    metadata = get_article_metadata(test_article)
    assert "article_title" in metadata
    assert "article_subtitle" in metadata
    assert metadata["article_title"] == "titulo"
    assert metadata["article_subtitle"] == "subtitulo"


def test_get_all_articles_path_from_dir():
    pathdir = '\\articlestests'
    files_names = ['article1.md', 'article2.md', 'article3.md']
    if not os.path.exists(pathdir):
        os.mkdir(pathdir)
    
    for file_name in files_names:
        file_path = os.path.join(pathdir, file_name)
        with open(file_path, 'w') as file:
            pass
    
    expected_paths = [f'{pathdir}\\article1.md',
        f'{pathdir}\\article2.md', f'{pathdir}\\article3.md'
        ]
    
    assert get_all_articles_path_from_dir(pathdir) == expected_paths


def temp_article_file(tmpdir):
    content = "Contenido de prueba"
    temp_file = tmpdir.join("temp_article.txt")
    temp_file.write(content)
    return str(temp_file)

def test_get_article_from_path(temp_article_file):
    result = get_article_from_path(temp_article_file)
    expected = "Contenido de prueba"
    assert result == expected

