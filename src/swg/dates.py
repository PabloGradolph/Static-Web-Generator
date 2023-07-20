def get_date(article: str) -> str:
    for line in article.split("\n"):
        if line.startswith("publishing_date:"):
            return line.split(":")[1].strip()
    return ""