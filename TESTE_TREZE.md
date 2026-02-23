# Tests - Site CaDir

This document describes how to run the project tests.

## Run All Tests

To run all project tests:

```bash
python manage.py test
```

## Run Tests by App

To run tests for a specific app:

```bash
python manage.py test core
python manage.py test eventos
python manage.py test guias
python manage.py test institucional
python manage.py test ouvidoria
python manage.py test programas
```

## Available Apps

- `core` - Main app with models and admin
- `eventos` - Event management
- `guias` - Academic guides management
- `institucional` - Institutional content
- `ouvidoria` - Ombudsman system
- `programas` - Academic programs

## Verbose Output

To see detailed test output:

```bash
python manage.py test --verbosity=2
```

## Coverage (Optional)

To see test coverage (if configured):

```bash
coverage run --source='.' manage.py test
coverage report
```

## Existing Test Files

The following test files already exist in the project:
- `core/tests.py`
- `eventos/tests.py`
- `guias/tests.py`
- `institucional/tests.py`
- `ouvidoria/tests.py`
- `programas/tests.py`
