### Livro Automatize tarefas maçantes com Python - Al Sweigart
### Capítulo 9

#Importando módulo shutil
import shutil,os

#Criando cópias do arquivo txt para outra pasta
shutil.copy(r'C:\Users\Dell\Downloads\jabuticaba.txt', r'C:\Users\Dell\Users\Dell\Desktop\delicious')
shutil.copy('jabuticaba.txt', r'C:\Users\Dell\Users\Dell\Desktop\eggs2.txt')

#Criando cópias de pastas
shutil.copytree(r'C:\Users\Dell\Downloads\img presente baby', r'C:\Users\Dell\Users\Dell\Desktop\img_backup')

#pastas destino já devem existir
#Movendo arquivos para outra pasta
shutil.move(r'C:\Users\Dell\Downloads\jabuticaba.txt', r'C:\Users\Dell\Downloads\eggs')

#movendo arquivo e mudando seu nome
shutil.move(r'C:\Users\Dell\Downloads\jabuticaba.txt', r'C:\Users\Dell\Downloads\eggs\jabuticaba2.txt')

#apagando arquivos e pastas -> TOMAR CUIDADO AO EXECUTAR ISSO, PORQUE É PERMANENTE
os.unlink(r'C:\Users\Dell\Downloads\eggs\jabuticaba.txt')         #apaga arquivo em path
os.rmdir(r'C:\Users\Dell\Downloads\eggs')                         #apaga pasta vazia
shutil.rmtree(r'C:\Users\Dell\Downloads\eggs')                    #apaga pasta e arquivos nela contidos

#send2trash para mandar para a lixeira e não apagar permanentemente
import send2trash
baconFile = open(r'C:\Users\Dell\Downloads\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash(r'C:\Users\Dell\Downloads\bacon.txt')

#os.walk para navegar por todas as pastas, subpastas e arquivos de um path
for folderName, subfolders, filenames in os.walk(r'C:\Users\Dell\Downloads'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

#manipulando arquivos ZIP
import zipfile
ZipFile = zipfile.ZipFile(r"C:\Users\Dell\Downloads\TermsAndContracts.zip")
ZipFile.namelist()
info = ZipFile.getinfo('TermsAndContracts/bexs_agreement.pdf')
info.file_size     #Tamanho do arquivo     
info.compress_size #tamanho do arquivo no zip      
'Compressed file is %sx smaller!' % (round(info.file_size /info.compress_size, 2))  #tamanho da compactação
ZipFile.close()

#loop para obter informação de todos os ARQUIVOS da pasta
for file in ZipFile.namelist()[1:len(ZipFile.namelist())]:
    info = ZipFile.getinfo(file)
    info.file_size    
    info.compress_size    
    print(f'Compressed {file} is {(round(info.file_size /info.compress_size, 2))}x smaller!')
ZipFile.close()

#extraindo itens de arquivo ZIP
ZipFile = zipfile.ZipFile(r"C:\Users\Dell\Downloads\TermsAndContracts.zip")
ZipFile.extractall(r"C:\Users\Dell\Downloads\extracaozip")
ZipFile.close()

#extraindo um único arquivo
ZipFile = zipfile.ZipFile(r"C:\Users\Dell\Downloads\TermsAndContracts.zip")
ZipFile.extract('TermsAndContracts/bexs_agreement.pdf', r"C:\Users\Dell\Downloads\extracaozip")
ZipFile.close()

#Zipando arquivo existente
newZip = zipfile.ZipFile("justificativa_exame_medico.zip",'w')
newZip.write(r"C:\Users\Dell\Downloads\justificativa_exame_medico.txt", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()