pretix-plugin-cookiecutter
==========================

A simple `cookiecutter`_ template to bootstrap a `pretix`_ plugin.

This is the JDAV Hessen fork of `pretix/pretix-plugin-cookiecutter`_. It keeps the
upstream layout and changes the tooling, see `Differences to upstream`_.

Usage
-----

Let's pretend you want to create a pretix plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/jdavhessen/pretix-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [pretix-superplugin]: pretix-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/pretix-superplugin
    module_name [pretix_superplugin]: pretix_superplugin
    human_name [The pretix super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    short_description [Short description]: The best plugin
    Select license:
    1 - Apache
    2 - pretix Enterprise
    Choose from 1, 2 [1]: 1
    min_basever [2.7.0]: 2026.6.0
    Select category:
    1 - FEATURE
    2 - PAYMENT
    3 - INTEGRATION
    4 - CUSTOMIZATION
    5 - FORMAT
    6 - API
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1
    Select python_version:
    1 - 3.11
    2 - 3.12
    3 - 3.13
    4 - 3.14
    Choose from 1, 2, 3, 4 [1]: 1
    Select level:
    1 - PLUGIN_LEVEL_EVENT
    2 - PLUGIN_LEVEL_ORGANIZER
    3 - PLUGIN_LEVEL_EVENT_ORGANIZER_HYBRID
    Choose from 1, 2, 3 [1]: 1


Now, change to the newly created directory::

    $ cd pretix-superplugin

Voilà, there's your plugin structure! See pretix' `documentation`_ for more info.

All prompts can also be answered on the command line, which is handy for scripts.
Choice variables take the option name::

    $ cookiecutter https://github.com/jdavhessen/pretix-plugin-cookiecutter --no-input \
        repo_name=pretix-superplugin module_name=pretix_superplugin \
        human_name="Super Plugin" short_description="The best plugin" \
        author_name="J Random Developer" author_email=jrandom@example.org \
        repo_url=https://github.com/myuser/pretix-superplugin \
        license=Apache min_basever=2026.6.0 category=FEATURE \
        python_version=3.11 level=PLUGIN_LEVEL_EVENT

``python_version`` is the lowest Python version the plugin supports. pretix
itself supports 3.11 to 3.14. It sets ``requires-python``, the ruff target version
and the Python used in the generated GitHub workflows.

``level`` is the pretix plugin level: ``PLUGIN_LEVEL_EVENT`` (activated per event),
``PLUGIN_LEVEL_ORGANIZER`` (activated for the organizer, active in all its events)
or ``PLUGIN_LEVEL_EVENT_ORGANIZER_HYBRID`` (activated for the organizer *and* per
event, active only where both are on).

Differences to upstream
-----------------------

- **ruff** replaces isort, flake8 and black (``ruff format`` and ``ruff check``,
  configured in ``pyproject.toml``). Besides the usual pycodestyle, pyflakes, isort,
  pyupgrade, bugbear, comprehensions, simplify, Django and Ruff rules it enables
  ``DTZ`` to catch naive datetimes. ``RUF012`` (mutable class attributes) is
  ignored because it contradicts common Django and pretix idioms.
- **Dependency groups** (``[dependency-groups]``): ``dev`` (ruff, commitizen) and
  ``test`` (pytest, pytest-django, coverage and pretix from git master).
- **commitizen** releases: Conventional Commits, ``cz bump`` updates the version
  and ``CHANGELOG.md`` and creates the ``v…`` tag. The version starts at 0.1.0 and
  ``major_version_zero`` keeps breaking changes from jumping to 1.0.0 by accident.
- New prompts ``python_version`` and ``level`` (see above); the generated
  ``tests/test_main.py`` checks that the plugin is registered with that level.
- Small fixes: coverage ``exclude_lines`` typo, ``pip install -e .`` instead of the
  deprecated ``setup.py develop``, ``.gitignore`` for IDEs and virtualenvs, a comment
  explaining the ``pretix.plugin`` entry point.

This repository is a fork: ``upstream`` is
``https://github.com/pretix/pretix-plugin-cookiecutter``. To take over upstream
changes::

    $ git fetch upstream
    $ git merge upstream/master

The "Try result" workflow renders the template for every level and runs ruff,
the migration check, ``cz bump``, check-manifest, a build, twine and the generated
tests.

.. _pretix: https://github.com/pretix/pretix
.. _pretix/pretix-plugin-cookiecutter: https://github.com/pretix/pretix-plugin-cookiecutter
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.pretix.eu/en/latest/development/api/plugins.html#pluginsetup
