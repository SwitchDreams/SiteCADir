# Testes - Site CaDir

Este documento descreve como executar os testes do projeto.

## Executar Todos os Testes

Para executar todos os testes do projeto:

```bash
python manage.py test
```

## Executar Testes por App

Para executar os testes de um app específico:

```bash
python manage.py test core
python manage.py test eventos
python manage.py test guias
python manage.py test institucional
python manage.py test ouvidoria
python manage.py test programas
```

## Apps Disponíveis

- `core` - App principal com modelos e admin
- `eventos` - Gerenciamento de eventos
- `guias` - Gestão de guias acadêmicos
- `institucional` - Conteúdo institucional
- `ouvidoria` - Sistema de ouvidoria
- `programas` - Programas acadêmicos

## Verbose Output

Para ver saída detalhada dos testes:

```bash
python manage.py test --verbosity=2
```

## Coverage (Opcional)

Para ver a cobertura dos testes (se estiver configurado):

```bash
coverage run --source='.' manage.py test
coverage report
```

## Arquivos de Testes Existentes

Os seguintes arquivos de testes já existem no projeto:
- `core/tests.py`
- `eventos/tests.py`
- `guias/tests.py`
- `institucional/tests.py`
- `ouvidoria/tests.py`
- `programas/tests.py`
