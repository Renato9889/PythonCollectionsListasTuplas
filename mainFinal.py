#Textando o uso de diversas coleções
from collections import Counter

texto1 = """
Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos. Sua versatilidade permite que ele seja utilizado em tudo, desde o aprendizado de máquinas até a construção de sites, automação de tarefas e testes de software.

Além disso, sua proximidade com a linguagem humana faz com que ele possa ser usado tanto por pessoas que desenvolvem, tanto por quem não necessariamente está inserido neste mercado.

Nesse artigo vamos apresentar questões importantes a respeito da linguagem Python, como o que ele é, como começou, alguns recursos básicos para utilizá-lo, quais as IDEs mais populares entre quem utiliza Python, tipos de dados, bibliotecas e frameworks mais usados, enfim, uma abordagem bem completa. Vamos lá?
"""

texto2 = """
Na atualidade, a criação de aplicações tem como foco arquiteturas que sejam escaláveis e na entrega de soluções em tempo real, além da atenção à componentização e segurança.

Além disso, soma-se a esse cenário a revolução iniciada pelos smartphones, com o uso cada vez mais intenso das mídias sociais e o aumento de soluções de IoT (Internet das Coisas). Nesse contexto, os paradigmas conhecidos no desenvolvimento de aplicações também têm passado por diversas mudanças que vão do Front-end ao Back-end, onde pensamos cada vez mais em uma solução como um todo, levando em consideração o consumo de dados e a disponibilidade de infraestrutura.

E é nessa conjuntura que nasce o Node.js, surgindo como uma solução poderosa e barata para a criação e a manutenção de ambientes de tecnologia com altas demandas. Então, vamos conhecer um pouco sobre essa ferramenta?
"""

texto1_contagem = Counter(texto1.lower())
print(texto1_contagem)

total_aparicoes = sum(texto1_contagem.values())

print(total_aparicoes)

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)