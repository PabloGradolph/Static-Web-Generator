from swg import settings


def test_current_working_dir():
    assert "CURRENT_WORKING_DIR" in settings.__dict__


def test_origin_dirname():
    assert "ORIGIN_DIRNAME" in settings.__dict__


def test_template_dir():
    assert "TEMPLATE_DIR" in settings.__dict__


def test_default_template():
    assert "DEFAULT_TEMPLATE" in settings.__dict__
