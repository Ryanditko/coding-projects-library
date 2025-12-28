# 🌤️ API de Clima com Histórico de Consultas

**Nível:** 🟡 Intermediário

## 📝 Descrição

Uma aplicação que exibe a previsão do tempo usando uma API externa e mantém histórico.

## ✨ Funcionalidades

✅ **Buscar clima atual por cidade** - Consulta em tempo real  
✅ **Salvar histórico de buscas no banco de dados** - Registro de consultas  
✅ **Exibir informações** - Temperatura, umidade, vento  
✅ **Design responsivo e interativo** - Interface moderna

## 🎯 Objetivo de Aprendizado

- Consumo de APIs externas
- Tratamento de dados JSON
- Geolocalização
- Banco de dados para histórico
- Interface responsiva
- Cache de requisições

## 💡 Dicas de Implementação

1. **Use OpenWeatherMap ou WeatherAPI** (gratuitas)
2. **Valide o nome da cidade** antes de buscar
3. **Salve cada consulta** no banco (cidade, data, dados)
4. **Implemente cache** para evitar requisições duplicadas
5. **Mostre ícones** representando o clima

## 🛠️ Tecnologias Sugeridas

### JavaScript
- Axios ou Fetch para requisições
- OpenWeatherMap API
- MongoDB ou PostgreSQL para histórico
- React/Vue para interface
- Leaflet para mapas (opcional)

### Python
- Requests para HTTP
- Flask ou FastAPI para backend
- SQLAlchemy para banco
- APIs: OpenWeatherMap, WeatherAPI
- Frontend com templates ou SPA

### Clojure
- clj-http para requisições
- Cheshire para JSON
- PostgreSQL para histórico
- ClojureScript + Reagent frontend
- APIs de clima gratuitas

## 📚 Recursos Úteis

- Documentação de APIs de clima
- Como fazer requisições HTTP
- Conversão de unidades (Celsius/Fahrenheit)
- Ícones de clima (Font Awesome, Weather Icons)

## 🚀 Desafios Extras

- Previsão estendida (7-14 dias)
- Geolocalização automática do usuário
- Múltiplas cidades em favoritos
- Gráficos de temperatura ao longo do dia
- Alertas climáticos
- Comparação entre cidades
- Widget para incorporar em sites
- Notificações de mudanças bruscas

---

**Boa sorte com o projeto! 💪**
