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
check locally, you need it installed::

    pip install ruff

To check your plugin for rule violations, run::

    ruff format --check .
    ruff check .

You can auto-fix most of these issues by running::

    ruff format .
    ruff check --fix .

To automatically check for these issues before you commit, you can run ``.install-hooks.sh``.


License
-------

{% if cookiecutter.license == "Apache" %}
Copyright {% now 'utc', '%Y' %} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0
{% elif cookiecutter.license == "pretix Enterprise" %}
Copyright {% now 'utc', '%Y' %} pretix GmbH

Released under the terms of the proprietary pretix Enterprise license.
{% endif %}


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
.. _Ruff: https://docs.astral.sh/ruff/
