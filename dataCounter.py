'''/***************************
Autor: Luan Rodrigues
Componente Curricular: Algoritmos I
Concluido em: 26/03/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************/'''
#Contador de dias
contador = 0

#Contador do dia para verificar se já foi inserido
segunda, terca, quarta, quinta, sexta, sabado, domingo, = 0, 0, 0, 0, 0, 0, 0

#Acumulador de consumo de dados TOTAL e Media total
chrome, facebook, instagram, whatsapp, outros, total, media  = 0, 0, 0, 0, 0, 0, 0

#dias e media do chrome
chrome_seg, chrome_ter, chrome_qua, chrome_qui, chrome_sex, chrome_sab, chrome_dom, mediachrome = 0, 0, 0, 0, 0, 0, 0, 0

#dias e media do facebook
face_seg, face_ter, face_qua, face_qui, face_sex, face_sab, face_dom, mediafacebook = 0, 0, 0, 0, 0, 0, 0, 0

#dias e media do instagram
insta_seg, insta_ter, insta_qua, insta_qui, insta_sex, insta_sab, insta_dom, mediainstagram = 0, 0, 0, 0, 0, 0, 0, 0

#dias e media do whatsapp
whats_seg, whats_ter, whats_qua, whats_qui, whats_sex, whats_sab, whats_dom, mediawhatsapp = 0, 0, 0, 0, 0, 0, 0, 0

#dias e media de outros
outros_seg, outros_ter, outros_qua, outros_qui, outros_sex, outros_sab, outros_dom, mediaoutros = 0, 0, 0, 0, 0, 0, 0, 0

#total por dia
totalsegunda, totalterca, totalquarta, totalquinta, totalsexta, totalsabado, totaldomingo = 0, 0, 0, 0, 0, 0, 0

#Verificar se quer zerar os dados
verificar = str()

#Total por app na semana
chromesemana = round((chrome_seg + chrome_ter + chrome_qua + chrome_qui + chrome_sex + chrome_sab + chrome_dom),2)
facesemana = round((face_seg + face_ter + face_qua + face_qui + face_sex + face_sab + face_dom),2)
instasemana = round((insta_seg + insta_ter + insta_qua + insta_qui + insta_sex + insta_sab + insta_dom),2)
whatssemana = round((whats_seg + whats_ter + whats_qua + whats_qui + whats_sex + whats_sab + whats_dom),2)
outrossemana = round((outros_seg + outros_ter + outros_qua + outros_qui + outros_sex + outros_sab + outros_dom),2)

#Total por dia
totalsegunda = round((chrome_seg + face_seg + insta_seg + whats_seg + outros_seg),2)
totalterca = round((chrome_ter + face_ter + insta_ter + whats_ter + outros_ter),2)
totalquarta = round((chrome_qua + face_qua + insta_qua + whats_qua + outros_qua),2)
totalquinta = round((chrome_qui + face_qui + insta_qui + whats_qui + outros_qui),2)
totalsexta = round((chrome_sex + face_sex + insta_sex + whats_sex + outros_sex),2)
totalsabado = round((chrome_sab + face_sab + insta_sab + whats_sab + outros_sab),2)
totaldomingo = round((chrome_dom + face_dom + insta_dom + whats_dom + outros_dom),2)

print('''                                   INSTRUÇÕES   
1 - Você deve inserir as 3 primeiras letras do dia que deseja. Para encerrar este dia, digite 7.\n
2 - Você pode verificar o relatório sempre que houver o menú (instruções no mesmo).\n
3 - Se você inserir um dia que já foi inserido, os dados do mesmo podem ser zerados e substituídos se você quiser.\n''')

#Solicitar dia da semana
dia = str(input('''\033[0;33mDigite as 3 primeiras letras minúsculas do dia que deseja (Ex. 'seg'). Para encerrar o dia, digite 7.
Se não houve consumo de dados, não insira o dia, caso insira, digite 7 para encerrá-lo:\n\033[m
 ---------------------
| [seg] Segunda-Feira |
| [ter] Terça-Feira   |
| [qua] Quarta-Feira  |
| [qui] Quinta-Feira  |
| [sex] Sexta-Feira   |
| [sab] Sabado        |
| [dom] Domingo       | 
 ---------------------\n'''))

while dia != 'seg' and dia != 'ter' and dia != 'qua' and dia != 'qui' and dia != 'sex' and dia != 'sab' and dia != 'dom':
    dia = str(input("\033[1;31m\nVocê deve inserir as 3 primeiras letras minúsculas do dia que deseja:\033[m\n")) 
print('\n\033[1;31mDia 1/7\033[m')

#Solicitar aplicativo
print('''\n\033[0;33mInsira o que deseja de acordo com o menú, ao repetir o app antes de encerrar o dia, irá substituir o valor deste app:\033[m\n
 -----------------------
| [1] Chrome            |
| [2] Facebook          |
| [3] Instagram         |
| [4] Whatsapp          |
| [5] Outros            |
| [6] Mostrar relatório |
| [7] Fim do dia        |
| \033[0;31m[0] Sair\033[m              |
 -----------------------''')
aplicativo = int(input())

#Nome do dia
nome_do_dia = str()

#Se escolher o dia específico adicionar ao contador dia e string ser igual ao dia
if dia == 'seg':
    nome_do_dia = 'Segunda-feira'
    segunda += 1
elif dia == 'ter':
    nome_do_dia = 'Terça-Feira'
    terca += 1
elif dia == 'qua':
    nome_do_dia = 'Quarta-Feira'
    quarta += 1
elif dia == 'qui':
    nome_do_dia = 'Quinta-Feira'
    quinta += 1
elif dia == 'sex':
    nome_do_dia = 'Sexta-Feira'
    sexta += 1
elif dia == 'sab':
    nome_do_dia = 'Sábado'
    sabado += 1
elif dia == 'dom':
    nome_do_dia = 'Domingo'
    domingo += 1

#Enquanto numero inserido for diferente do pedido
while aplicativo != 0 and aplicativo != 1 and aplicativo != 2 and aplicativo != 3 and aplicativo != 4 and aplicativo != 5 and aplicativo != 6 and aplicativo != 7:
    aplicativo = int(input("\033[1;31m\nInsira o número correspondente ao menú:\033[m\n"))

#Rodar loop enquanto contador for menor que 7, ou o usuario não pedir para sair
while contador <= 7 and dia != 'sair' and aplicativo != 0:

#Se escolher Chrome
    if aplicativo == 1:
        valor = float(input("\n\033[0;33mInsira a quantidade de dados em bytes consumida pelo Chrome:\033[m\n"))
        while valor < 0 or valor == -0:
            valor = float(input('\033[1;31m\nVocê deve inserir um valor maior ou igual a 0:\033[m\n'))
        if dia == 'seg':
#verificação de aplicativo repetido nos if dia > 0
            if chrome_seg >0:
#subtrair valores antigos inseridos
                chrome -= chrome_seg
                chrome_seg -= chrome_seg
#valor a ser adicionado
            chrome_seg += valor
            chrome += chrome_seg
        elif dia == 'ter':
            if chrome_ter >0:
                chrome-= chrome_ter
                chrome_ter -= chrome_ter   
            chrome_ter += valor
            chrome += chrome_ter
        elif dia == 'qua':
            if chrome_qua >0:
                chrome -= chrome_qua
                chrome_qua -= chrome_qua       
            chrome_qua += valor
            chrome += chrome_qua
        elif dia == 'qui':
            if chrome_qui >0:
                chrome -= chrome_qui
                chrome_qui -= chrome_qui
            chrome_qui += valor
            chrome += chrome_qui
        elif dia == 'sex':
            if chrome_sex >0:
                chrome -= chrome_sex
                chrome_sex -= chrome_sex
            chrome_sex += valor
            chrome += chrome_sex
        elif dia == 'sab':
            if chrome_sab >0:
                chrome -= chrome_sab
                chrome_sab -= chrome_sab        
            chrome_sab += valor
            chrome += chrome_sab
        elif dia == 'dom':
            if chrome_dom >0:
                chrome -= chrome_dom
                chrome_dom -= chrome_dom   
            chrome_dom += valor
            chrome += chrome_dom
#printar caso haja valor inserido
        if valor > 0:
            print("\n\033[1;32mAdicionado!\033[m")

#Se escolher Facebook
    elif aplicativo == 2:
        valor = float(input("\n\033[0;33mInsira a quantidade de dados em bytes consumida pelo Facebook:\033[m\n"))
        while valor < 0 or valor == -0:
            valor = float(input('\033[1;31m\nVocê deve inserir um valor maior ou igual a 0:\033[m\n'))
        if dia == 'seg':
            if face_seg >0:
                facebook -= face_seg
                face_seg -= face_seg        
            face_seg += valor
            facebook += face_seg
        elif dia == 'ter':
            if face_ter >0:
                facebook -= face_ter
                face_ter -= face_ter   
            face_ter += valor
            facebook += face_ter
        elif dia == 'qua':
            if face_qua >0:
                facebook-= face_qua
                face_qua -= face_qua
            face_qua += valor
            facebook += face_qua
        elif dia == 'qui':
            if face_qui > 0:
                facebook-= face_qui
                face_qui -= face_qui                
            face_qui += valor
            facebook += face_qui
        elif dia == 'sex':
            if face_sex > 0:
                facebook -= face_sex
                face_sex -= face_sex   
            face_sex += valor
            facebook += face_sex
        elif dia == 'sab':
            if face_sab > 0:
                facebook -= face_sab
                face_sab -= face_sab          
            face_sab += valor
            facebook += face_sab
        elif dia == 'dom':
            if face_dom > 0:
                facebook -= face_dom
                face_dom -= face_dom
            face_dom += valor
            facebook += face_dom
        if valor > 0:
            print("\n\033[1;32mAdicionado!\033[m")
      
#Se escolher instagram 
    elif aplicativo == 3:
        valor = float(input("\n\033[0;33mInsira a quantidade de dados em bytes consumida pelo Instagram:\033[m\n"))
        while valor < 0 or valor == -0:
            valor = float(input('\033[1;31m\nVocê deve inserir um valor maior ou igual a 0:\033[m\n'))
        if dia == 'seg':
            if insta_seg>0:
                instagram -= insta_seg
                insta_seg -= insta_seg              
            insta_seg += valor
            instagram += insta_seg
        elif dia == 'ter':
            if insta_ter>0:
                instagram -= insta_ter
                insta_ter -= insta_ter               
            insta_ter += valor
            instagram += insta_ter
        elif dia == 'qua':
            if insta_qua>0:
                instagram -= insta_qua
                insta_qua -= insta_qua               
            insta_qua += valor
            instagram += insta_qua
        elif dia == 'qui':
            if insta_qui>0:
                instagram -= insta_qui
                insta_qui -= insta_qui           
            insta_qui += valor
            instagram += insta_qui
        elif dia == 'sex':
            if insta_sex>0:
                instagram -= insta_sex
                insta_sex -= insta_sex               
            insta_sex += valor
            instagram += insta_sex
        elif dia == 'sab':
            if insta_sab>0:
                instagram -= insta_sab
                insta_sab -= insta_sab                
            insta_sab += valor
            instagram += insta_sab
        elif dia == 'dom':
            if insta_dom>0:
                instagram -= insta_dom
                insta_dom -= insta_dom        
            insta_dom += valor
            instagram += insta_dom
        if valor > 0:
            print("\n\033[1;32mAdicionado!\033[m")

#Se escolher Whatsapp
    elif aplicativo == 4:
        valor = float(input("\n\033[0;33mInsira a quantidade de dados em bytes consumida pelo Whatsapp:\033[m\n"))
        while valor < 0 or valor == -0:
            valor = float(input('\033[1;31m\nVocê deve inserir um valor maior ou igual a 0:\033[m\n'))
        if dia == 'seg':
            if whats_seg>0:
                whatsapp -= whats_seg
                whats_seg -= whats_seg         
            whats_seg += valor
            whatsapp += whats_seg
        elif dia == 'ter':
            if whats_ter>0:
                whatsapp -= whats_ter
                whats_ter -= whats_ter
            whats_ter += valor
            whatsapp += whats_ter
        elif dia == 'qua':
            if whats_qua>0:
                whatsapp -= whats_qua
                whats_qua -= whats_qua              
            whats_qua += valor
            whatsapp += whats_qua
        elif dia == 'qui':
            if whats_qui>0:
                whatsapp -= whats_qui
                whats_qui -= whats_qui              
            whats_qui += valor
            whatsapp += whats_qui
        elif dia == 'sex':
            if whats_sex>0:
                whatsapp -= whats_sex
                whats_sex -= whats_sex               
            whats_sex += valor
            whatsapp += whats_sex
        elif dia == 'sab':
            if whats_sab>0:
                whatsapp -= whats_sab
                whats_sab -= whats_sab        
            whats_sab += valor
            whatsapp += whats_sab
        elif dia == 'dom':
            if whats_dom>0:
                whatsapp -= whats_dom
                whats_dom -= whats_dom             
            whats_dom += valor
            whatsapp += whats_dom
        if valor > 0:
            print("\n\033[1;32mAdicionado!\033[m")

#Se escolher Outros
    elif aplicativo == 5:
        valor = float(input("\n\033[0;33mInsira a quantidade de dados em bytes consumida por Outros:\033[m\n"))
        while valor < 0 or valor == -0:
            valor = float(input('\033[1;31m\nVocê deve inserir um valor maior ou igual a 0:\033[m\n'))
        if dia == 'seg':
            if outros_seg>0:
                outros -= outros_seg
                outros_seg -= outros_seg                
            outros_seg += valor
            outros += outros_seg
        elif dia == 'ter':
            if outros_ter>0:
                outros -= outros_ter
                outros_ter -= outros_ter               
            outros_ter += valor
            outros += outros_ter
        elif dia == 'qua':
            if outros_qua>0:
                outros -= outros_qua
                outros_qua -= outros_qua                
            outros_qua += valor
            outros += outros_qua
        elif dia == 'qui':
            if outros_qui>0:
                outros -= outros_qui
                outros_qui -= outros_qui                
            outros_qui += valor
            outros += outros_qui
        elif dia == 'sex':
            if outros_sex>0:
                outros -= outros_sex
                outros_sex -= outros_sex               
            outros_sex += valor
            outros += outros_sex
        elif dia == 'sab':
            if outros_sab>0:
                outros -= outros_sab
                outros_sab -= outros_sab             
            outros_sab += valor
            outros += outros_sab
        elif dia == 'dom':
            if outros_dom>0:
                outros -= outros_dom
                outros_dom -= outros_dom              
            outros_dom += valor
            outros += outros_dom
        if valor > 0:
            print("\n\033[1;32mAdicionado!\033[m")

#Mostrar dia atual
    print('\033[1;31mDia atual: ' + nome_do_dia + '\033[m\n' + ('-')*100 + '\n')

#Total e media geral
    total = round((chrome + facebook + instagram + whatsapp + outros), 2)
    media = round((total) / 7,2)
    
#Media por app
    mediachrome = round(chrome / 7, 2)
    mediafacebook = round(facebook / 7, 2)
    mediainstagram = round(instagram / 7, 2)
    mediawhatsapp = round(whatsapp / 7, 2)
    mediaoutros = round(outros / 7, 2)

#Total por dia
    totalsegunda = round((chrome_seg + face_seg + insta_seg + whats_seg + outros_seg),2)
    totalterca = round((chrome_ter + face_ter + insta_ter + whats_ter + outros_ter),2)
    totalquarta = round((chrome_qua + face_qua + insta_qua + whats_qua + outros_qua),2)
    totalquinta = round((chrome_qui + face_qui + insta_qui + whats_qui + outros_qui),2)
    totalsexta = round((chrome_sex + face_sex + insta_sex + whats_sex + outros_sex),2)
    totalsabado = round((chrome_sab + face_sab + insta_sab + whats_sab + outros_sab),2)
    totaldomingo = round((chrome_dom + face_dom + insta_dom + whats_dom + outros_dom),2)
    
#Mostrar o relatório
    if aplicativo == 6 or contador == 7 and aplicativo == 7:
            print('''\033[1;37m_'''*60 + '''Relatorio''' + '''_'''*60 + 
f'''\nTotal de dados consumidos na semana: {total} bytes
Media dos dados consumidos na semana: {media} bytes
\nChrome:\n-------
Total: {chrome} bytes
Media: {mediachrome} bytes
\nFacebook:\n---------
Total: {facebook} bytes
Media: {mediafacebook} bytes
\nInstagram:\n---------
Total: {instagram} bytes
Media: {mediainstagram} bytes
\nWhatsapp:\n---------
Total: {whatsapp} bytes
Media: {mediawhatsapp} bytes
\nOutros:\n------
Total: {outros} bytes
Media: {mediaoutros} bytes

\nSegunda-Feira: {totalsegunda} bytes\n-------------------------
Chrome: {chrome_seg} bytes, Facebook: {face_seg} bytes, Instagram: {insta_seg} bytes, Whatsapp: {whats_seg} bytes, Outros: {outros_seg} bytes
\nTerça-Feira: {totalterca} bytes\n-------------------------
Chrome: {chrome_ter} bytes, Facebook: {face_ter} bytes, Instagram: {insta_ter} bytes, Whatsapp: {whats_ter} bytes, Outros: {outros_ter} bytes
\nQuarta-Feira: {totalquarta} bytes\n-------------------------
Chrome: {chrome_qua} bytes, Facebook: {face_qua} bytes, Instagram: {insta_qua} bytes, Whatsapp: {whats_qua} bytes, Outros: {outros_qua} bytes
\nQuinta-Feira {totalquinta}\n-------------------------
Chrome: {chrome_qui} bytes, Facebook: {face_qui} bytes, Instagram: {insta_qui} bytes, Whatsapp: {whats_qui} bytes, Outros: {outros_qui} bytes
\nSexta-Feira: {totalsexta} bytes\n-------------------------
Chrome: {chrome_sex} bytes, Facebook: {face_sex} bytes, Instagram: {insta_sex} bytes, Whatsapp: {whats_sex} bytes, Outros: {outros_sex} bytes
\nSabado: {totalsabado} bytes\n-------------------------
Chrome: {chrome_sab} bytes, Facebook: {face_sab} bytes, Instagram: {insta_sab} bytes, Whatsapp: {whats_sab} bytes, Outros: {outros_sab} bytes
\nDomingo: {totaldomingo} bytes\n-------------------------
Chrome: {chrome_dom} bytes, Facebook: {face_dom} bytes, Instagram: {insta_dom} bytes, Whatsapp: {whats_dom} bytes, Outros: {outros_dom} bytes\n'''+ ('_'*120 + '\n'))

#Solicitar dia novamente  
    if aplicativo == 7:
        if contador >= 7 and aplicativo == 7:
            print('\033[0;1;41mVocê já inseriu todos os dias, repita um dia para corrigí-lo ou digite "sair" para encerrar a semana\033[m')
        dia = str(input("\n\033[0;33mDigite as 3 primeiras letras minúsculas do dia que deseja. Ex. 'seg'. Ou 'sair' para sair do app.\033[m\n"))      
        while dia != 'seg' and dia != 'ter' and dia != 'qua' and dia != 'qui' and dia != 'sex' and dia != 'sab' and dia != 'dom' and dia != 'sair':
            dia = str(input("\n\033[1;31mVocê deve inserir as 3 primeiras letras minúsculas do dia que deseja:\033[m\n"))
#Contador de dias
        contador = 1 + (segunda + terca + quarta + quinta + sexta + sabado + domingo)
#Nome do dia
        nome_do_dia = str()

#Se escolher o dia específico adicionar ao contador dia 
        if dia == 'seg':
            nome_do_dia = 'Segunda-feira'
            segunda += 1
        elif dia == 'ter':
            nome_do_dia = 'Terça-Feira'
            terca += 1
        elif dia == 'qua':
            nome_do_dia = 'Quarta-Feira'
            quarta += 1
        elif dia == 'qui':
            nome_do_dia = 'Quinta-Feira'
            quinta += 1
        elif dia == 'sex':
            nome_do_dia = 'Sexta-Feira'
            sexta += 1
        elif dia == 'sab':
            nome_do_dia = 'Sábado'
            sabado += 1
        elif dia == 'dom':
            nome_do_dia = 'Domingo'
            domingo += 1
    
#Mostrar dia se não houver dia repetido
        if segunda <=1 and terca <=1 and quarta <=1 and quinta <= 1 and sexta <=1 and sabado <=1 and domingo <=1 and dia != 'sair':  
                print(f'\n\033[1;31mDia: {contador}/7\033[m')

#Se segunda-feira for repetida
    if segunda > 1:
#Deseja zerar os dados?
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
#Se escolher zerar os dados
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_seg
                facebook -= face_seg
                instagram -= insta_seg
                whatsapp -= whats_seg
                outros -= outros_seg
                chrome_seg, face_seg, insta_seg, whats_seg, outros_seg = 0, 0, 0, 0, 0    

                segunda -=1
            else:
                contador -=1
                segunda -=1
#Se não quiser zerar os dados   
        else:
            contador -= 1
            segunda -=1

#Se terca-feira for repetida
    elif terca > 1:
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_ter
                facebook -= face_ter
                instagram -= insta_ter
                whatsapp -= whats_ter
                outros -= outros_ter
                chrome_ter, face_ter, insta_ter, whats_ter, outros_ter = 0, 0, 0, 0, 0     

                terca -=1
            else:
                contador -= 1
                terca -= 1
        else:
            contador -= 1
            terca -=1

#Se quarta-feira for repetida
    elif quarta > 1:
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_qua
                facebook -= face_qua
                instagram -= insta_qua
                whatsapp -= whats_qua
                outros -= outros_qua               
                chrome_qua, face_qua, insta_qua, whats_qua, outros_qua = 0, 0, 0, 0, 0      

                quarta -=1 
            else:
                contador -=1
                quarta -= 1
        else:
            contador -= 1
            quarta -=1

#Se quinta-feira for repetida
    elif quinta > 1:
        vverificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_qui
                facebook -= face_qui
                instagram -= insta_qui
                whatsapp -= whats_qui
                outros -= outros_qui                     
                chrome_qui, face_qui, insta_qui, whats_qui, outros_qui = 0, 0, 0, 0, 0
                quinta -=1  
            else:
                contador -= 1
                quinta -= 1 
        else:
            contador -= 1
            quinta -=1

#Se Sexta-feira for repetida
    elif sexta > 1:
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_sex
                facebook -= face_sex
                instagram -= insta_sex
                whatsapp -= whats_sex
                outros -= outros_sex
                chrome_sex, face_sex, insta_sex, whats_sex, outros_sex = 0, 0, 0, 0, 0
                sexta -=1  
            else:
                contador -=1
                sexta-=1
        else:
            contador -= 1
            sexta -= 1

#Se Sabado for repetido
    elif sabado > 1:
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_sab
                facebook -= face_sab
                instagram -= insta_sab
                whatsapp -= whats_sab
                outros -= outros_sab  
                chrome_sab, face_sab, insta_sab, whats_sab, outros_sab = 0, 0, 0, 0, 0

                sabado -= 1
            else:
                contador -= 1
                sabado -= 1
        else:
            contador -= 1
            sabado-= 1

#Se Domingo for repetido
    elif domingo > 1:
        verificar = input("\n\033[1;31mOps, você ja inseriu este dia.\nDigite 's' para voltar para ele, ou 'n' para não voltar:\033[m\n")
        while verificar != 's' and verificar!= 'n':
            verificar = input("\033[1;31m\nVocê deve inserir 's' ou 'n':\033[m\n")
        if verificar == 's':
            zerar_dia = input("\033[1;31m\nDeseja zerar todos os dados deste dia? Digite 's' para sim e 'n' para não\033[m\n")
            while zerar_dia != 's' and zerar_dia != 'n':
                zerar_dia = input("\033[1;31m\nVocê deve inserir 's' ou 'n'\033[m\n")
            if zerar_dia == 's':
                contador -=1

                chrome -= chrome_dom
                facebook -= face_dom
                instagram -= insta_dom
                whatsapp -= whats_dom
                outros -= outros_dom  
                chrome_dom, face_dom, insta_dom, whats_dom, outros_dom = 0, 0, 0, 0, 0  

                domingo -=1
            else:
                contador -= 1
                domingo -= 1
        else:
            contador -= 1
            domingo -=1
            verificar = str()

#Solicitar dia novamente
    if dia != 'sair' and verificar != 'n':
        print('''\n\033[0;33mInsira o que deseja de acordo com o menú, ao repetir o app, irá substituir o valor do mesmo:\033[m\n
 -----------------------            
| [1] Chrome            |
| [2] Facebook          |
| [3] Instagram         |
| [4] WhatsApp          |
| [5] Outros            |
| [6] Mostrar relatório |
| [7] Fim do dia        |
| \033[0;31m[0] Sair\033[m              |
 -----------------------''')
          
        aplicativo = int(input())
        while aplicativo != 0 and aplicativo != 1 and aplicativo != 2 and aplicativo != 3 and aplicativo != 4 and aplicativo != 5 and aplicativo != 6 and aplicativo != 7:
            aplicativo = int(input("\033[1;31mInsira o número correspondente ao menú:\n\033[m"))
    
    verificar = ''

#Mostrar relatório ao final do app    
print('''\033[1;37m_'''*60 + '''Relatorio''' + '''_'''*60 + 
f'''\nTotal de dados consumidos na semana: {total} bytes
Media dos dados consumidos na semana: {media} bytes
\nChrome:\n-------
Total: {chrome} bytes
Media: {mediachrome} bytes
\nFacebook:\n---------
Total: {facebook} bytes
Media: {mediafacebook} bytes
\nInstagram:\n---------
Total: {instagram} bytes
Media: {mediainstagram} bytes
\nWhatsapp:\n---------
Total: {whatsapp} bytes
Media: {mediawhatsapp} bytes
\nOutros:\n------
Total: {outros} bytes
Media: {mediaoutros} bytes

\nSegunda-Feira: {totalsegunda} bytes\n-------------------------
Chrome: {chrome_seg} bytes, Facebook: {face_seg} bytes, Instagram: {insta_seg} bytes, Whatsapp: {whats_seg} bytes, Outros: {outros_seg} bytes
\nTerça-Feira: {totalterca} bytes\n-------------------------
Chrome: {chrome_ter} bytes, Facebook: {face_ter} bytes, Instagram: {insta_ter} bytes, Whatsapp: {whats_ter} bytes, Outros: {outros_ter} bytes
\nQuarta-Feira: {totalquarta} bytes\n-------------------------
Chrome: {chrome_qua} bytes, Facebook: {face_qua} bytes, Instagram: {insta_qua} bytes, Whatsapp: {whats_qua} bytes, Outros: {outros_qua} bytes
\nQuinta-Feira {totalquinta}\n-------------------------
Chrome: {chrome_qui} bytes, Facebook: {face_qui} bytes, Instagram: {insta_qui} bytes, Whatsapp: {whats_qui} bytes, Outros: {outros_qui} bytes
\nSexta-Feira: {totalsexta} bytes\n-------------------------
Chrome: {chrome_sex} bytes, Facebook: {face_sex} bytes, Instagram: {insta_sex} bytes, Whatsapp: {whats_sex} bytes, Outros: {outros_sex} bytes
\nSabado: {totalsabado} bytes\n-------------------------
Chrome: {chrome_sab} bytes, Facebook: {face_sab} bytes, Instagram: {insta_sab} bytes, Whatsapp: {whats_sab} bytes, Outros: {outros_sab} bytes
\nDomingo: {totaldomingo} bytes\n-------------------------
Chrome: {chrome_dom} bytes, Facebook: {face_dom} bytes, Instagram: {insta_dom} bytes, Whatsapp: {whats_dom} bytes, Outros: {outros_dom} bytes\n'''+ ('_'*120 + '\n'))