#Subtask responsavel por realizar o login no portal do aluno
from extracao_codigo_boleto.scripts.subtasks.login import portal_aluno_login as login
from extracao_codigo_boleto.scripts.subtasks.extrair_boleto import portal_aluno_extrair_boleto as extrair_boleto
#Main
def main():
    login()    
    extrair_boleto();


if __name__ == '__main__':
    main(); 