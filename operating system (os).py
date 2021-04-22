#Livro Automatizando tarefas maçantes com Python, Al Sweigart
#Capítulo 8

#Importando pacote OS
import os

#Mudando diretório de trabalho
os.chdir(r'C:\Users\Public\Desktop')

#Criando Diretório
#path = os.path.join('C:','Users','Public','Desktop','Problemas Acabaram','Bom dia','Marcos')
path = r'C:\Users\Public\Desktop\Users\Public\Desktop\Problemas Acabaram\Bom dia\Marcos'
os.makedirs(path,exist_ok = True)

#Entendendo Repositórios absolutos x relativos
os.path.abspath('.')
os.path.abspath('.\\Seus Problemas Acabaram')
os.path.isabs(r'C:\\Users\\Dell\\Seus Problemas Acabaram')

#separação da sring do diretório
path_dirname = os.path.dirname(path)
path_basename = os.path.basename(path)
tupla_dir_name = os.path.split(path)

#tamanho de um arquivo específico
tamanho = os.path.getsize(os.path.join(path,'BaseCursoCompleto.zip'))

#lista de documentos de um diretório
docs = os.listdir(path)

#tamanho total do diretório
totalSize = 0
for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path,filename))

#Verificando se Path existe e se é aqruivo ou diretório
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

#Manipulando aqruivos de texto simples
#Abrindo arquivos (parâmetro 'r' para explicitar leitura)
file_object = open(r'C:\Users\Dell\Downloads\justificativa_exame_medico.txt','r',encoding='utf-8')#, errors='ignore')

#lendo conteúdo dele
file_object.read()

#lendo linhas dele
file_object.seek(0)
file_object.readlines()

#obtendo seu tamanho
file_object.tell()

#criando novo arquivo
new_file = open(r'C:\Users\Dell\Downloads\jabuticaba.txt','w',encoding='utf-8')#, errors='ignore')

#escrevendo no novo arquivo
new_file.write("Jabuticaba só existe no Brasil")

#fechando arquivo novo
new_file.close()

#adicionando conteúdo no arquivo
new_file = open(r'C:\Users\Dell\Downloads\jabuticaba.txt','a',encoding='utf-8')#, errors='ignore')
new_file.write("\n Jabuticaba pode ser qualquer coisa que só tem no Brasil")
new_file.close()

#lendo conteúdo
new_file = open(r'C:\Users\Dell\Downloads\jabuticaba.txt',encoding='utf-8')
conteudo = new_file.read()
new_file.close()
print(conteudo)

#Importando Shelve para salvar dados dos programas Python
import shelve

#Abrindo/Criando arquivo shelve 
shelfFile = shelve.open(r'C:\Users\Dell\Downloads\mydata.txt')

#Criando lista e armazenando-a como valor associado à chave "cats" (tipo dicionário)
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats

#fechando arquivo
shelfFile.close()

#obtendo tipo
type(shelfFile)

#analisando se o armazenamento está correto
shelfFile = shelve.open(r'C:\Users\Dell\Downloads\mydata.txt')
shelfFile['cats']
shelfFile.close()

#analisando chaves e valores do dicionário
shelfFile = shelve.open(r'C:\Users\Dell\Downloads\mydata.txt')
list(shelfFile.keys())
list(shelfFile.values())[0][1]

#Gravando conteúdos em arquivos .py (Criando módulos) -> permite que qualquer um use.
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('MyCats.py','w',encoding='utf-8')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

#importando método e manipulando
import MyCats
MyCats.cats[1]['desc']

##########################################################################################################
#Exemplo : programa de elaboração de atividades
import random

#Passo 1: Armazenar os dados da prova em um dicionário
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield','Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis','Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul','Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton','New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin','Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

randomQuizGenerator = open('randomQuizGenerator.py','w',encoding='utf-8')
randomQuizGenerator.write('capitals = ' + pprint.pformat(capitals) + '\n')
randomQuizGenerator.close()

#Passo 2: Criar o arquivo com a prova e embaralhar a ordem das perguntas
for quizNum in range(35):
    quizFile = open(r'C:\Users\Dell\Downloads\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open(r'C:\Users\Dell\Downloads\'capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)

#Passo 3: Criar as opções de resposta
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

#Passo 4: Gravar conteúdo nos arquivos de prova e de respostas

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()

##########################################################################################################