# Calculadora Python com PySide6

Uma calculadora moderna e funcional desenvolvida em Python utilizando a biblioteca PySide6 para a interface gráfica.

## ✨ Funcionalidades

- Operações básicas: adição, subtração, multiplicação e divisão
- Potenciação (^)
- Inversão de sinal (+/-)
- Suporte a números decimais
- Teclado virtual e entrada por teclado físico
- Interface dark mode com tema personalizado
- Tratamento de erros (divisão por zero, overflow)
- Design responsivo e intuitivo

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- PySide6 (Qt for Python)
- qt_material (para estilização)
- pyinstaller (para build do executável)

## 📦 Estrutura do Projeto

```
CALCULADORA_PYTHON/
├── _app/
│   ├── build/               # Arquivos de build
│   ├── dist/  
│   | ├── Calculadora.exe   # Executável gerado 
│   | └── Calculadora.rar   # Executável compactado   
│   └── Calculadora.spec     # Configuração do PyInstaller
├── src/
│   ├── files/
│   │   └── icon.png  # Arquivo do ícone
│   ├── buttons.py       # Lógica dos botões
│   ├── display.py       # Componente de display
│   ├── main_window.py   # Janela principal
│   ├── main.py          # Ponto de entrada
│   ├── styles.py        # Estilos CSS
│   ├── utils.py         # Funções utilitárias
│   └── variables.py     # Variáveis e constantes
└── requirements.txt     # Dependências
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Git (opcional)

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/calculadora-python.git
cd calculadora-python
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

```bash
python -m _app.src.main
```

### Build do Executável

```bash
pyinstaller _app/Calculadora.spec
```

O executável será gerado na pasta `dist/`.

## 🎨 Personalização

Você pode alterar o tema da calculadora editando o arquivo `styles.py` ou modificando a linha em `main.py` que contém:

```python
apply_stylesheet(app, theme='dark_teal.xml', style=qss)
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Desenvolvido com ❤️ por GuihCastro
