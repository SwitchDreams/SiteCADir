# Resumo

Alterar URL da página de diretoria de `/institucional/diretoria` para `/institucional/diretorias` conforme solicitação do cliente.

---

## Principais Mudanças

### Backend
- **institucional/urls.py** - Alterada rota de `path('diretoria', ...)` para `path('diretorias', ...)`

---

## Como Testar

1. Acessar `http://localhost:8000/institucional/diretorias`
2. Verificar se a página carrega corretamente
3. Clicar no link "Diretoria" do menu de navegação e confirmar que redireciona para a nova URL
4. Confirmar que a antiga URL (`/institucional/diretoria`) não está mais acessível

---

## Notas Técnicas

- O link no menu de navegação (`templates/base.html`) não precisou ser alterado pois utiliza `{% url %}` do Django, que resolve automaticamente para o caminho correto
- O nome da rota (`institucional_diretoria`) e a função view (`diretoria`) foram mantidos, alterando apenas o caminho da URL

---

## Arquivos Principais

- `institucional/urls.py:19` - Rota alterada de `diretoria` para `diretorias`

---

**Task**: #T E-1
