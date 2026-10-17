from pretix.base.plugins import {{cookiecutter.level}}, get_all_plugins

from {{cookiecutter.module_name}} import __version__

MODULE = "{{cookiecutter.module_name}}"


def test_plugin_is_registered():
    metas = [m for m in get_all_plugins() if m.module == MODULE]
    assert len(metas) == 1
    assert metas[0].version == __version__
    assert metas[0].level == {{cookiecutter.level}}
