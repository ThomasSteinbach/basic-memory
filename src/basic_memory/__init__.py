"""basic-memory - Local-first knowledge management combining Zettelkasten with knowledge graphs"""

# Package version - updated by release automation
#
# DELIBERATELY A LITERAL, and it must stay one: `scripts/update_versions.py` rewrites it
# with the regex `^__version__ = ".*"$`, and `tests/test_claude_plugin_hooks.py` reads it
# the same way to learn the RELEASED version without importing the package. Deriving it
# from `importlib.metadata` was tried and reverted — it breaks both.
#
# It therefore names the last RELEASE, not the build you are running. For that, see the
# `Installed build:` line of `basic-memory --version`, which reports the distribution
# metadata whenever it differs (e.g. `0.22.2.dev146+<sha>` for a build from source).
__version__ = "0.22.1"

# API version for FastAPI - independent of package version
__api_version__ = "v2"
