# 🔗 Encurtador de URL

**Nível:** 🟡 Intermediário

## 📝 Descrição

Um sistema que encurta links longos para facilitar o compartilhamento.

## ✨ Funcionalidades

✅ **Input para inserir a URL original** - Campo de entrada  
✅ **Gerar um link curto único** - Código alfanumérico  
✅ **Registrar o número de acessos** - Analytics básicas  
✅ **API para encurtar URLs via requisição externa** - Endpoints REST

## 🎯 Objetivo de Aprendizado

- Criação de APIs REST
- Geração de IDs únicos
- Redirecionamento HTTP
- Banco de dados relacional
- Validação de URLs
- Analytics e estatísticas

## 💡 Dicas de Implementação

1. **Gere códigos curtos únicos** usando base62 ou nanoid
2. **Valide as URLs** antes de salvar
3. **Armazene no banco** (URL original, código curto, contador de acessos)
4. **Implemente redirecionamento** HTTP 301 ou 302
5. **Crie API endpoints** para criar e consultar links

## 🛠️ Tecnologias Sugeridas

### JavaScript
- Express.js ou Fastify para API
- MongoDB ou PostgreSQL para banco
- Biblioteca: `nanoid` para gerar códigos
- Redis para cache (opcional)

### Python
- Flask ou FastAPI para API
- SQLAlchemy para ORM
- PostgreSQL ou MySQL
- Biblioteca: `shortuuid` ou `nanoid`

### Clojure
- Ring + Compojure para API
- HugSQL para queries
- PostgreSQL
- Biblioteca: `buddy` para segurança

## 📚 Recursos Úteis

- Como gerar IDs únicos curtos
- Redirecionamento HTTP
- Design de APIs REST
- Validação de URLs com regex

## 🚀 Desafios Extras

- URLs customizadas (usuário escolhe o código)
- Expiração automática de links
- QR Code para cada link encurtado
- Dashboard com estatísticas detalhadas
- Proteção contra spam e URLs maliciosas
- Autenticação para gerenciar seus links
- Preview de link antes de redirecionar

---

**Boa sorte com o projeto! 💪**
