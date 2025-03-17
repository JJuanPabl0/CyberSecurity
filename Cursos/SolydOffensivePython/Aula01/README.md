# 📌 Guia de Estudos - Cybersecurity

Este documento serve como um guia para iniciar os estudos em **Cybersecurity**, seguindo uma ordem lógica para facilitar a aprendizagem.

## 📖 Ordem de Estudo

### 1️⃣ OWASP (Open Web Application Security Project)
> **Objetivo**: Entender as principais vulnerabilidades de segurança em aplicações web.

- Estudar o **OWASP Top 10**
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Falhas de autenticação
  - Exposição de dados sensíveis
  - Controle de acesso inseguro
  - Outras vulnerabilidades comuns
- Site oficial: [OWASP Top 10](https://owasp.org/www-project-top-ten/)

### 2️⃣ Container Security
> **Objetivo**: Aprender boas práticas de segurança ao trabalhar com Docker e containers.

- Imagens seguras no Docker Hub
- Princípio do **menor privilégio**
- Armazenamento seguro de segredos e credenciais
- Ferramentas para análise de segurança:
  - **Trivy** → Scanner de vulnerabilidades em containers ([Trivy GitHub](https://github.com/aquasecurity/trivy))

### 3️⃣ Políticas de Segurança para Ambientes Corporativos
> **Objetivo**: Compreender como proteger infraestruturas empresariais.

- Controle de acesso e privilégios mínimos
- Políticas de senhas e autenticação
- Gestão de vulnerabilidades e atualizações
- Monitoramento e resposta a incidentes

### 4️⃣ Segurança com Terraform
> **Objetivo**: Aplicar boas práticas de segurança em infraestrutura como código.

- Implementação de regras de segurança no Terraform
- Controle de acesso com IAM (Identity and Access Management)
- Proteção de segredos e credenciais

### 5️⃣ Security Information and Event Management (SIEM)
> **Objetivo**: Aprender como funciona o monitoramento e análise de eventos de segurança.

- Ferramentas SIEM populares
- Coleta e análise de logs de segurança
- Configuração de alertas para atividades suspeitas

### 6️⃣ SonarQube - Segurança de Código
> **Objetivo**: Analisar vulnerabilidades no código-fonte.

- Instalação e configuração do **SonarQube**
- Análise estática de código
- Identificação de falhas de segurança
- Site oficial: [SonarQube](https://www.sonarqube.org/)

## 🛠️ Ferramentas Importantes

Estudar as seguintes ferramentas para análise de segurança em código e dependências:

| Ferramenta | Descrição |
|------------|-----------|
| **Dependency-Track** | Identifica vulnerabilidades em bibliotecas e dependências |
| **Horusec** | Scanner de segurança para código-fonte |
| **Snyk** | Detecta vulnerabilidades em pacotes e containers |
| **Trivy** | Scanner de vulnerabilidades para containers e imagens Docker |
| **TruffleHog** | Busca credenciais e segredos expostos no código |

## 📚 Recursos Adicionais

- [OWASP Foundation](https://owasp.org/)
- [Terraform Security Best Practices](https://developer.hashicorp.com/terraform/tutorials/security/security-best-practices)
- [Container Security - Docker Documentation](https://docs.docker.com/security/)
- [SIEM Explained](https://www.cynet.com/blog/security-information-and-event-management-siem-explained/)

---
🚀 **Bons estudos e boa sorte na jornada de Cybersecurity!**