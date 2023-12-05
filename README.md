# pyGRAZ website

This is the website of pyGRAZ, the Python user group Graz.

## Getting started

To work with the website per

1. `git clone` this repository and `cd` into the local work copy.
2. Install [poetry](https://python-poetry.org/).
3. Run
   ```bash
   poetry install
   ```
4. Run
   ```bash
   sh scripts/setup_project.sh
   ```

## Working with the site

The site is written using the [Lektor CMS](https://www.getlektor.com/).

To run the local test server:

```bash
poetry run lektor server
```

Then connect to http://127.0.0.1:5000 and edit or add content.
