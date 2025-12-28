# 📝 Aplicação de Notas com Markdown

**Nível:** 🟡 Intermediário

## 📝 Descrição

Um editor de notas que suporta formatação Markdown e salva automaticamente.

## ✨ Funcionalidades

✅ **Criar, editar e excluir notas** - CRUD completo de notas  
✅ **Suporte a formatação Markdown** - Preview em tempo real  
✅ **Salvar no armazenamento local ou banco de dados** - Persistência de dados  
✅ **Modo claro e escuro** - Alternância de temas

## 🎯 Objetivo de Aprendizado

- Parsing de Markdown
- Editor de texto avançado
- Preview em tempo real
- Banco de dados ou LocalStorage
- Gerenciamento de múltiplos documentos
- Sistema de temas

## 💡 Dicas de Implementação

1. **Use uma biblioteca Markdown** para converter texto para HTML
2. **Implemente split-view** (editor e preview lado a lado)
3. **Auto-save** após alguns segundos de inatividade
4. **Organize notas** por data de criação/modificação
5. **Adicione busca** para encontrar notas rapidamente

## 🛠️ Tecnologias Sugeridas

### JavaScript
- Bibliotecas: `marked.js` ou `markdown-it` para parsing
- CodeMirror ou Monaco Editor para editor avançado
- LocalStorage ou IndexedDB para persistência
- React/Vue para interface

### Python
- Flask ou Django para backend
- Biblioteca: `markdown2` ou `mistune` para parsing
- SQLite ou PostgreSQL para banco de dados
- HTML/CSS/JS para frontend

### Clojure
- Ring + Compojure para servidor
- Biblioteca: `markdown-clj` para parsing
- Datomic ou PostgreSQL para dados
- ClojureScript + Reagent para frontend

## 📚 Recursos Úteis

- Sintaxe Markdown completa
- Como criar editores de texto
- Debouncing para auto-save
- Sincronização de scroll entre editor e preview

## 🚀 Desafios Extras

- Suporte a tabelas e diagramas Mermaid
- Exportar notas como PDF ou HTML
- Sincronização com nuvem (Dropbox, Google Drive)
- Tags e categorias para organização
- Colaboração em tempo real
- Versionamento de notas
- Atalhos de teclado personalizados

---

**Boa sorte com o projeto! 💪**
