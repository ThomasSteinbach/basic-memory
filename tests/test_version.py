"""`--version` must be able to identify a build that is not a release."""

from importlib.metadata import version as distribution_version

import basic_memory
from basic_memory.cli.app import installed_build_version


def test_installed_build_reported_when_it_differs_from_the_release_literal():
    """A non-release install must be identifiable from `--version`.

    `__version__` is a literal that release automation rewrites
    (`scripts/update_versions.py` matches `^__version__ = ".*"$`, and
    `tests/test_claude_plugin_hooks.py` reads it the same way), so it names the last
    RELEASE — not the build in use. A fork, a branch or a source checkout therefore
    reported `0.22.1` while its own metadata said `0.22.2.dev<n>+<sha>`.

    That is worse than printing nothing: someone verifying that a patched build is live
    gets a confident, stale answer. The commit-bearing version is the only string that
    can settle it.
    """
    installed = distribution_version("basic-memory")

    if installed == basic_memory.__version__:
        # A released install: nothing extra to say, and nothing extra must be printed.
        assert installed_build_version() is None
    else:
        assert installed_build_version() == installed


def test_release_literal_is_not_derived_from_metadata():
    """`__version__` must stay a plain literal.

    Deriving it from `importlib.metadata` looks like the tidy fix and was tried; it
    breaks `scripts/update_versions.py` and the plugin-hooks suite, both of which parse
    this file as TEXT rather than importing it. This guard states the coupling so the
    same tidy fix is not attempted a second time.
    """
    import re
    from pathlib import Path

    source = (Path(__file__).resolve().parents[1] / "src/basic_memory/__init__.py").read_text(
        encoding="utf-8"
    )
    assert re.search(r'^__version__ = ".+"$', source, re.MULTILINE) is not None
