# **Riscos de Segurança Atualizado 2021**

## _**Broken Access Control**_
- O controle de acesso aplica políticas de modo que os usuários não possam agir fora de suas permissões pretendidas(Ou seja, são falhas, se o usuário age além do limite de alguma aplicação é uma falha). As falhas normalmente levam à divulgação não autorizada de informações, modificação ou destruição de todos os dados ou à execução de uma função comercial fora dos limites do usuário. 

### As Vulnerabilidades comum de controle de acesso incluem:
---

- Violação do princípio do menor privilégio, em que o acesso só deve ser concedido para determinados recursos, funções ou usúarios, mas está disponível para qualquer pessoa.

- Se você ignorar verificações de controle de acesso modificando a URL(violação de parametro e navegação forçada), o estado interno do aplicativo ou a página HTML, ou usando ferramentas de ataques que modifica solitações de API é mais um tipo de vulnerabilidade 

- Se você permitir a visualização ou edição da conta de outra pessoa também é uma vulnerabilidade.

- Acessar APIs com controle de acesso ausentes para POST, PUT e DELETE.

- Elevaçao de privilégio. Agir como um usuário sem estar logado ou agir como um administrador quando logado como um usuário.

- Manipulação de metadados, como reprodução ou adulteração de um token de controle de acesso **JSON Web Token(JKT)**, ou um cookie ou campo oculto manipulado para elevar privilégios ou abusar da invalidação do JWT. 

- A configuração incorreta do CORS permite acesso à API de origens não autorizadas/não confiáveis.

- Forçar navegação para páginas autenticadas como um usuário não autenticado ou para páginas privilegiadas como um usuário padrão
ls


## _**Como Previnir**_

