{{cookiecutter.human_name}}
==========================

This is a plugin for `pretix`_. 

{{ cookiecutter.short_description }}

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository.

3. Activate the virtual environment you use for pretix development.

4. Execute ``pip install -e .`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.

This plugin has CI set up to enforce a few code style rules with `Ruff`_. To
check locally, run::

    uv run ruff format --check .
    uv run ruff check .

You can auto-fix most of these issues by running::

    uv run ruff format .
    uv run ruff check --fix .

To automatically check for these issues before you commit, you can run ``.install-hooks.sh``.

Commits in this repository follow `Conventional Commits`_ and releases are
cut with `Commitizen`_ (``cz bump``), which updates the version in
``pyproject.toml`` and ``{{cookiecutter.module_name}}/__init__.py``, writes
``CHANGELOG.md`` and creates the matching git tag. The version starts at
0.1.0; while it is 0.x, breaking changes bump the minor version.


Quick start without a pretix checkout
-------------------------------------

To run the tests and the style checks you do not need a full pretix development
setup. With `uv`_, a few commands create a throwaway environment that contains
the plugin and the latest pretix release::

    uv sync --group test
    uv run make
    uv run pytest tests
    uv run ruff format --check .
    uv run ruff check .

``make`` needs GNU gettext (Debian package ``gettext``). To try the plugin in a
running pretix, use the development setup above instead.


License
-------

{% if cookiecutter.license == "Apache" %}
Copyright {% now 'utc', '%Y' %} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0
{% elif cookiecutter.license == "All rights reserved" %}
Copyright {% now 'utc', '%Y' %} {{cookiecutter.author_name}}. All rights reserved.
{% elif cookiecutter.license == "pretix Enterprise" %}
Copyright {% now 'utc', '%Y' %} pretix GmbH

Released under the terms of the proprietary pretix Enterprise license.
{% endif %}


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
.. _Ruff: https://docs.astral.sh/ruff/
.. _uv: https://docs.astral.sh/uv/
.. _Conventional Commits: https://www.conventionalcommits.org/
.. _Commitizen: https://commitizen-tools.github.io/commitizen/
