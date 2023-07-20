"""
articles.py para las operaciones de lectura de los articulos en markdown
render.py para la interpolacion de los datos con plantillas
settings.py un modulo de constantes de configuracion
swg.py init un modulo para ejecutar el programa por primera vez
swg.py re-generate un modulo para ejectura el programa y refrescar si ha habido cambios

- articles.py
-- get_article_metada(article: str) -> dict recuperar metadata
-- get_article_body(article: str) -> str recuperar el cuerpo del articulo sin transformarlo
-- convert_article_body(body: str) -> str convertir de markdown a html
-- get_article_from_path(path: str) -> str
-- get_all_articles_path_from_dir(dirpath: str) -> list[str]

- render.py
-- render_article (article: str, context: dict) -> str

- output.py
-- write_html_to_file(article: str, article_filename: str) -> None


- settings.py
CURRENT_WORKING_DIR
ORIGIN_DIR_NAME
TEMPLATE_DIR
DEFAULT_TEMPLATE

"""