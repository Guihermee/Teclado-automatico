# Teclado-automatico
Recentemente eu fiz um código para deixar um persongem de um jogo se mexendo sozinho e conseguindo burlar a inatividade do jogo enquanto ganha as recomensas por "jogar"

![image](https://github.com/Guihermee/Teclado-automatico/assets/125518739/df6514cd-0af7-479e-8bbe-5e2283065de2)

Tem essas funções e funciona normalmente, só que é um código simples e um pouco bugado que pode ser bastante melhorado, você mesmo pode criar qualquer aplicativo usando o cx_freeze é só seguir:

1. Colocar o código "pip install cx-Freeze" para instalar o cx-freeze na sua máquina
2. Depois faça seu código ou modifique e torne ele um executável usando o comando "cxfreeze .'nome do arquivo que quer transformar em executavel' " ou seja no nosso caso ficaria ".cxfreeze .clicar.py"
3. feito isso faça um arquivo setup dentro da sua pasta que por padrão é:

```
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Meu App",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)]
)
```
Colocando no includes as bibliotecas que você está usando no seu código, depois em setup você muda o nome, versão e descrição como quiser e no executables o nome do arquivo inicial que o seu programa vai usar para iniciar ele que no nosso caso é o clicar.py

4. E por fim usamos o comando "python .\setup.py build 

E pronto com isso você cria seu executável ou modifica ele


Eu só fiz isso por que meu amigo não entende de programação e queria deixar o personagem dele farmando no PC dele também igual eu, então eu fiz esse código que antes era 4 linha de código nesses 2.py para ajudar ele.
