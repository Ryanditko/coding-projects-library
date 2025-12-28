# 🔑 Sistema de Login com Autenticação JWT

**Nível:** 🟡 Intermediário

## 📝 Descrição

Um sistema de login seguro com autenticação via JWT (JSON Web Tokens).

## ✨ Funcionalidades

✅ **Cadastro e login de usuários** - Registro e autenticação  
✅ **Hash de senhas para segurança** - Criptografia de senhas  
✅ **Token JWT para autenticação** - Sessões stateless  
✅ **Controle de acesso a páginas privadas** - Proteção de rotas

## 🎯 Objetivo de Aprendizado

- Autenticação e autorização
- Hash de senhas (bcrypt)
- JSON Web Tokens (JWT)
- Middleware de autenticação
- Proteção de rotas
- Segurança de aplicações web

## 💡 Dicas de Implementação

1. **Hash as senhas** usando bcrypt antes de salvar
2. **Gere token JWT** após login bem-sucedido
3. **Valide o token** em rotas protegidas
4. **Implemente refresh tokens** para renovação
5. **Armazene tokens** de forma segura (httpOnly cookies ou localStorage)

## 🛠️ Tecnologias Sugeridas

### JavaScript
- Express.js para backend
- jsonwebtoken para JWT
- bcrypt para hash de senhas
- Middleware para validação de token
- React/Vue para frontend

### Python
- Flask ou FastAPI
- PyJWT para tokens
- passlib ou bcrypt para senhas
- Decorators para proteção de rotas
- SQLAlchemy para usuários

### Clojure
- Ring + Compojure
- buddy-auth para JWT
- buddy-hashers para senhas
- Middleware para autenticação
- Re-frame para frontend

## 📚 Recursos Úteis

- Como funcionam os JWT
- Boas práticas de segurança
- OWASP Top 10
- Diferença entre autenticação e autorização

## 🚀 Desafios Extras

- OAuth2 com Google/GitHub
- Autenticação de dois fatores (2FA)
- Recuperação de senha por email
- Blacklist de tokens revogados
- Rate limiting para prevenir ataques
- Login com biometria
- Logs de acesso e auditoria
- Perfis de usuário com níveis de acesso

---

**Boa sorte com o projeto! 💪**
