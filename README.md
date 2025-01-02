# AutoPilotPy 🤖💻

### Piloto para automações usando Python
#### *Em progresso*

> Este projeto busca facilitar a criação de automações repetitivas, sejam elas para manipulação de dados em planilhas, interação com GUIs, ou navegação em páginas web. De modo que cada parte da automação possa ser independente porém
> que no fim elas "orquestrem-se" em um método final `run()`.

#### Nele você encontrará a seguinte arquitetura:
```
- modules
  - DTOS:          Módulo que contém scripts para transpor dados entre diferentes partes do projeto (incompleto).
  - gui:           Contém scripts para automação de interfaces gráficas.
  - html:          Módulo para gerenciar e manipular aquivos HTML (incompleto).
  - json:          Módulo para manipular e gerenciar arquivos no formato JSON.
  - spreadsheet:   Scripts para manipulação de planilhas (incompleto).
  - utils:         Utilidades e funções auxiliares comuns ao projeto.
  - web:           Scripts para automação de interações web usando Selenium.
- project
  - models:        Classes que servirão como modelo para o projeto.
  - orchestrators: Pacote onde terá seus arquivos _orchestrator.py, que será o local onde os módulos irão orquestrar fazendo assim o fluxo da automação.
  - pages:         Local onde será armazenada as páginas automatizadas, o "bruto" da automação.
main.py
```

Sendo a única pasta "obrigatória" dentro de project a pasta orchestrators que será onde será unida todas as etapas da automação em um método `run()` que será chamado no arquivo `main.py`, podendo o restante
ser opcional ou até alterado para adaptar-se de acordo com as necessidades.

## Como usar?

1. Clone o repositório
   
   ```
   git clone https://github.com/JoaoPedroPitarelo/AutoPilotPy.git
   ```
2. Crie o ambiente virtual Python

   ```
   python -m venv venv
   ```
3. Ative o ambiente virtual

    *Windows (PowerShell):*
     ```
     ./venv/Scripts/Activate.ps1
     ```
    *Windows (Command Prompt):*
     ```
     .\venv\Scripts\activate.bat
     ```
   *Linux e MacOS (Bash, ZSH)*
    ```
    source ./venv/bin/activate
    ```
4. Instale as dependências
   ```
   pip install -r ./requirements.txt
   ```
5. Execute o projeto
   
    *Linux e MacOS*
    ```
     python3 main.py
    ```
    *Windows*
    ```
     python main.py
    ```

***
## Esse projeto não está nem perto de estar "pronto".

### Módulos Incompletos
- HTML
- Spreadsheet
- DTOs
- SO


Então fique à vontade para contribuir e sugerir novas ideias e melhorias 😎😁 
***

## Contribuindo  
Contribuições são bem-vindas!  
1. Faça um fork do repositório.  
2. Crie uma branch para sua feature ou correção: `git checkout -b minha-feature`.  
3. Envie um pull request com uma descrição clara do que foi alterado.  


## Licença 
Este projeto está licenciado sob a Licença MIT. Você pode usá-lo, modificá-lo e distribuí-lo livremente, desde que mantenha o aviso de direitos autorais.  

[Leia mais sobre a Licença MIT](https://opensource.org/licenses/MIT).
