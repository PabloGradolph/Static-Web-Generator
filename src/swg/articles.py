import markdown
import os


def get_article_metadata(article: str) -> dict:
    """
    Collects the metadata of an article.

    Parameters
    ----------
    article: str
        Article with str format.

    Returns
    -------
    md.Meta: dict
        Dictionary with article metadata.

    Example
    -------
    test_article = "---\narticle_title: titulo"
    test_article += "\narticle_subtitle: subtitulo"
    test_article += "\n---\ntext\n"

    metadata = get_article_metadata(test_article)

    metadata
    {'article_title': 'titulo', 'article_subtitle': 'subtitulo'}
    
    """
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Meta


def get_all_articles_path_from_dir(dirpath: str) -> list[str]:
    """
    Collects all items in a directory.

    Parameters
    ----------
    dirpath: str
        Path to directory.
    
    Returns
    -------
    articles_path: list[str]
        List with paths of all articles.
    """
    articles_path = []
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath):
            articles_path.append(filepath)
    return articles_path


def get_article_from_path(path: str) -> str:
    with open(path,"r") as art:
        text = art.read()
        return text

