# pytest-exit-status

**Pytest** plugin that overrides the exit codes.

![](https://img.shields.io/badge/license-MIT%202.0-blue.svg)

**Pytest** only offers two exit status codes for full test executions (when all collected tests are executed):
- Exit code **0**: All tests had the `passed`, `xpassed`, `xfailed` or `skipped` outcome.
- Exit code **1**: Some tests had the `failed` outcome or there were some errors (setup or teardown errors).

Some continuous integration tools like **Jenkins** support the `unstable` status and it can be frustrating not to take advantage of this pipeline status to highlight test executions with `xfailed` tests.

This plugin aims to modify the exit codes **0** and **1** and to add a new exit code **6**.

The proposed exit codes are:
- Exit code **0**: All tests had the `passed`, `xpassed` or `skipped` outcome.
- Exit code **1**: Some tests had the `failed` outcome.
- Exit code **6**: Some tests had the `xfailed` outcome or there were some errors (setup or teardown errors).

The other exit codes are not modified.

To install the plugin:

```
pip install pytest-exit-status
```

<br/>

If you like this software, consider contributing to the project through [buy me a coffee](https://www.buymeacoffee.com/harmin)
