#Quem quer ser um milinário
#o jogo conterá três blocos, conendo cinco perguntas cada bloco, totalizando em quinze pergutas

vitoria:bool = True   

while vitoria:
    
  perguntas_e_respostas_blc_1 = [
    [('Quando foi fundado o SENAI?', '1942'), '1942', '1950', '1960', '1970'],
    [('Quem é o atual diretor do SENAI?', 'Rafael Lucchesi'), 'Rafael Lucchesi', 'Paulo Skaf', 'Roberto Simões', 'José Ricardo Roriz Coelho'],
    [('O SENAI oferece cursos?', 'Sim'), 'Sim', 'Não', 'Apenas teóricos', 'Apenas práticos'],
    [('Existe férias no SENAI?', 'Sim'), 'Sim', 'Não', 'Depende do curso', 'Apenas no verão'],
    [('O SENAI é uma instituição?', 'Sim'), 'Sim', 'Não', 'Uma empresa', 'Uma ONG']
]
perguntas_e_respostas_blc_2 = [
    [('Qual é a capital do Brasil?', 'Brasília'), 'Brasília', 'Rio de Janeiro', 'São Paulo', 'Salvador'],
    [('Quem pintou a Mona Lisa?', 'Leonardo da Vinci'), 'Leonardo da Vinci', 'Michelangelo', 'Rafael', 'Donatello'],
    [('Qual é o maior planeta do sistema solar?', 'Júpiter'), 'Júpiter', 'Saturno', 'Terra', 'Marte'],
    [('Quem escreveu "Dom Casmurro"?', 'Machado de Assis'), 'Machado de Assis', 'Jorge Amado', 'José de Alencar', 'Lima Barreto'],
    [('Qual elemento tem o símbolo químico O?', 'Oxigênio'), 'Oxigênio', 'Ouro', 'Ósmio', 'Olíbano']
]
perguntas_e_respostas_blc_3 = [
    [('O homem já foi a lua?', 'Sim'), 'Sim', 'Não', 'Apenas para Júpiter', 'Semana que vem'],
    [('Existe vida na Terra?', 'Sim'), 'Sim', 'Não', 'Somente em Marte', 'Somente em Júpiter'],
    [('Qual é o formate da Terra?', 'Plano'), 'Triangular', 'Retangulo', 'Hexagonal', 'Oval'],
    [('Quais são os sexos existem?', 'Masculino e Feminino'), 'Gay e Gay Plus', 'Brum e Paiva', 'Sim', 'Não'],
    [('A agua é dura?', 'Não'), 'Sim', 'Talvez', 'Ok', 'Se quiser sim mano'],
]
pergunta_final = [
    [('Quem é a nossa salvação', 'Jesus Cristo'), 'Jesus Cristo']
]

def verificar_resposta(indice_pergunta, resposta_usuario, perguntas_e_respostas):
    
    resposta, resposta_correta = perguntas_e_respostas[indice_pergunta][0]
    
    if resposta_usuario.lower() == resposta_correta:
        return True
    else:
        return False


