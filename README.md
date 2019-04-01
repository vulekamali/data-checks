vulekamali automated data checks
================================

Automated checks to ensure data meets the expectations of [OpenSpending](https://openspending.org) and the vulekamali system before going through the upload and data build process.

This is intended to identify issues early and make it quicker to fix issues when adding new data to the site.

This repository describes the datasets and the checks that should be run against them.

The datasets are described as [Data Packages](https://frictionlessdata.io/data-packages/) by files named `datapackage.json` in a directory specific to each dataset.

Each dataset should be in a directory specific to the type of data release (e.g. `epre`, `ene`, `aene`, `aepre`, `annual-report`) under a directory for the specific financial year that is the focus of the release (e.g. `2018-19`)

`datapackage.json` files are automatically discovered and checked against the schema they refer to when changes are uploaded to [this repository on GitHub.com](https://github.com/vulekamali/data-checks) in a [Pull Request](https://help.github.com/en/articles/about-pull-requests)


Developer setup:
----------------

Python version: See .travis.yml

Use a [python virtual environment](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/) to manage dependencies.

Install dependencies:

```bash
pip install -r requirements.txt
```

Running locally:

```bash
python bin/run-checks.py
```
