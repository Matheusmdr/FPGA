define p = Character("Thomas", color='#c8ffc8')
define j = Character("Jean", color='#99ffd6')
define ap = Character("Amigo", color='#99ffd6')
define i = Character("Instrutor", color='#D2691E')
define l = Character("Lindsey", color='#ffff4d')
define m = Character("Mulher", color='#ffff4d')
define h = Character("Homem", color='#ff0')
define lu = Character("Luan", color='#ff0')
define m2 = Character("Mulher", color='#fff')
define jo = Character("Joana", color='#fff')


default question_1_thomas = 'Errada'
default question_2_thomas = 'Errada'
default question_3_thomas = 'Errada'
default question_2_jean = 'Errada'
default question_3_jean = 'Errada'
default question_2_lindsey = 'Errada'
default question_3_lindsey = 'Errada'
default lindsey_friendship = 0
default alianca_joana = 0
default troca_respostas_lindsey = 0


# INICIO CAPITULO 1
label start:

    $ question_1_thomas = 'Errada'
    $ question_2_thomas = 'Errada'
    $ question_3_thomas = 'Errada'
    $ question_2_jean = 'Errada'
    $ question_3_jean = 'Errada'
    $ question_2_lindsey = 'Errada'
    $ question_3_lindsey = 'Errada'
    $ lindsey_friendship = 0
    $ alianca_joana = 0
    $ troca_respostas_lindsey = 0

    scene bg corridor

label cena_corredor:
    play music "audio/tema_dialogo_geral.mp3" fadein 1.0 volume 0.3

    p "Bem, chegou a hora..."

    show jean surprised
    with fade

    ap "Cara, eu tô tremendo! Senhor"

    show jean normal

    p "Mesmo aqui, mas ficar nervoso só atrapalha." 
    p "Vamos apenas dar nosso melhor. Se não for o bastante, tem sempre outras empresas por aí."

    show jean angry1

    ap "Eu sei, mas não que nem essa neh. O povo só fala como eles são seletivos nas entrevistas."
    ap "Aliás, nem entrevista é. Que empresa que dá prova escrita pra escolher quem deve entrar?"

    p "Calma Jean, a gente já vai descobrir. Vamos tentar ficar calmos agora ok? É o melhor a se fazer nessa altura do campeonato."

    j "Éeeeeeee eu sei, eu sei... Vamos acabar logo com isso."
    stop music fadeout 1.0

    jump cena_sala 
    with fade

label cena_sala:
    play music "audio/tema_dialogo_inspetor.mp3" fadein 1.0 volume 0.3
    scene bg club

    show instrutor smile1 at left

    i "Certo, deu o horário. Vou começar as instruções."

    p "(Nossa, só 5 pessoas. Eles são mesmo seletivos.)"

    i "Bom dia, eu serei o instrutor de vocês durante o teste. Por favor, deixem qualquer dúvida sobre o exame ao final das instruções que serão dadas agora."

    i "Durante o exame vocês terão que seguir apenas algumas regras. E prestem atenção nelas, pois elas não serão repetidas"

    p "(Não se deram ao trabalho nem de colocar as regras do exame no papel. Que falta de profissionalidade.)"

    i "1ª Regra: As folhas em suas carteiras devem ser preenchidas com as respostas das suas respectivas perguntas. Apenas respostas escritas à caneta preta são válidas. Qualquer rasura ou dano nas folhas anularão completamente as questões."

    i "2ª Regra: As folhas podem começar a ser preenchidas apenas a partir do horário de início que está marcado na lousa. Com o início do exame eu sairei da sala, e apenas retornarei no término do período para recolher as provas e dispensa-los... "

    i "Eu entendo a confusão de vocês, mas sejam pacientes. As próximas regras devem esclarecer suas dúvidas."

    i "3ª Regra: Tudo o período do exame será monitorado pelas câmeras ao redor da sala"

    i "O que significa que se alguém passar mal, quiser ir ao banheiro, terminar o exame mais cedo, ou desistir, pode apenas acenar com a mão 3 vezes olhando para uma câmera; um segurança irá recolher a prova do indivíduo e o levar calmamente para fora da sala."

    p "(Então eles pretendem nos impedir de colar apenas usando câmeras? Isso não parece muito seguro.)"

    p "(E ainda por cima não dá pra ir ao banheiro. Mas, é aceitável eu acho.)"

    i "4ª Regra: Qualquer prova recolhida antes do término do exame será anulada."

    p "(Ok... Isso é um tanto... incomum.)"

    i "5ª Regra: Por fim, a última regra"

    i "Qualquer ato que demonstre descontrole emocional ou físico, como violência, choro, palavras de baixo calão, vômitos, etc. Causarão a retirada imediata do candidato da sala e o recolhimento da prova."
    
    i "Alguma dúvida?"
    
    stop music fadeout 1.0
    
    m "Isso é um absurdo!"
    
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3

    show instrutor surprised at left
    
    show lindsey angry at right
   
    with fade

    m "Vocês não podem simplesmente nos impedir de ir ao banheiro durante um exame! Isso vai contra os direitos humanos."
    
    show instrutor angry1 at left
    
    m "Sem contar que existem pessoas com problemas intestinais ou estomacais que simplesmente não conseguem se segurar!"
    
    show instrutor angry2 at left
    
    i "Bem, senhoraaaa?"
    
    show instrutor angry1 at left
    
    show lindsey angry2 at right
    
    m "Lindsey, SENHORITA Lindsey Spears."
    
    show lindsey angry at right
    
    i "Senhorita Lindsey. Acredito que ouve um mal entendimento de sua parte quanto as regras propostas."

    i "Elas apenas dizem que caso alguém deseje se retirar da sala, como por exemplo, para ir ao banheiro, basta que o candidato em questão acene com a mão 3 vezes para uma câmera enquanto a olha."

    l "Mas isso tira o direito do candidato de continuar a prova quando voltar."

    i "Quando voltar para onde?"

    l "Para a sala!"

    i "Qual sala?"
    
    show lindsey angry2 at right
   
    l "Como “qual sala?”, ESTA!"
    
    show instrutor angry2 at left
   
    show lindsey angry at right
   
    i "Primeiramente, senhorita Lindsey, agradeceria se você não utiliza-se esse tom para se dirigir comigo, ou com qualquer um neste recinto. Principalmente porque estamos quase a dar início ao início do exame."
   
    show instrutor angry1 at left
   
    i "E, se me permite corrigir sua sentença, o candidato não voltará a lugar nenhum, pois ele já estará dispensado da prova após ir ao banheiro."

    l "Mas, esse é o problema!"

    i "Qual?"

    l "O candidato não pode continuar a prova após ir ao banheiro."
    
    i "Sim."
    
    l "Então???"

    i "Então, o que senhorita? Não vejo o problema."

    i "Me parece que você entendeu muito bem as regras."

    l "Sim sim, entender eu entendi."

    i "Ótimo, senhorita! Mas alguma dúvida?"
   
    show lindsey annoyed at right
   
    l "Não, nenhuma. Mas..."

    i "Sim, senhorita Lindsey?"
   
    show lindsey sad at right
   
    l "Bom... Eu... Agradeço o esclarecimento."

    hide lindsey sad

    i "Maravilha. Mais alguma dúvida?"

    p "(Isso foi doloroso de assistir. Até parece que alguém vai ter alguma dúvida depois disso.)"

    i "Não? Nenhuma?"

    i "Perfeito. O exame terá início a partir do momento que eu sair por esta porta, portanto vocês terão 2 horas para termina-lo, e todas as regras ditas anteriormente passarão a valer, a partir de aaaaaaaaa..."

    i "...gora!"

    stop music fadeout 1.0

    jump cena_prova
    with fade

# INICIO CAPITULO 2
label cena_prova:
    scene bg caderno
    play music "audio/tema_protagonista_pensando_respondendo_questoes.mp3" fadein 1.0 volume 0.3

    p "(Seja o que Deus quiser)"

    "Questão" " Em um ambiente empresarial, na qual você trabalha como um engenheiro da computação. Se fosse solicitado a você um tipo de memória na qual só possa ser apagada com luz ultravioleta, qual tipo de memória você recomendaria?"

    p "(Ah sim, eu sei essa!)"

    menu:
        "A) PROM":  
            $ question_1_thomas = "Errada"
        "B) EPROM":
            $ question_1_thomas = "Certa"
        "C) EAPROM":
            $ question_1_thomas = "Errada"
        "D) EEPROM":
            $ question_1_thomas = "Errada"

    p "Tá certo, deve ser isso."

    p "Próxima, então."

    "Questão" "Em um ambiente empresarial, na qual você trabalha como um engenheiro da computação. Se fosse solicitado a você como acessar fragmentos de código, a partir do código fonte de um programa, como você acredita Joana Olympios resolveria esse problema?"
    
    p "(Cara, quem diabos é Joana Olympios?)"

    p "(Odeio essas perguntas que exigem um conhecimento muito específico. Vou pra próxima e volto nessa depois.)"
    
    "Questão" "Em um ambiente empresarial..."

    p "(TÁ TÁ ENTENDI, vamo logo pra pergunta!)"
    
    "Questão" "...Considerando o pensamento de Lindsey Spears, que método é usado para executar dois ou mais programas diferentes em um processador de 1 só núcleo e sem pipeline, porém dando ao usuário a impressão de que todos eles são executados ao mesmo tempo?"
    
    p "(Ah, cara. Mas NÃO É POSSÍVEL...)"
   
    p "(Outra pergunta que exige o pensamento de alguém que NUNCA OUVI...)"
   
    p "(Espera... Lindsey Spears? Esse nome me é familiar, mas não me lembro agora.)"
   
    p "(Ela não é...)"

    menu:
        "a) Uma cientista que vi em um artigo.":
            $ who_is_lindsey_question = "a"
            jump caminhoQ2_derivado_email
        "b) Uma mulher na qual escutei o nome agora pouco.":
            $ who_is_lindsey_question = "b"
            jump caminhoQ2_derivado_principal
        "c) Não lembro; não importa. Basta eu responder o que sei.":
            $ who_is_lindsey_question = "c"
            jump caminhoQ2_derivado_email

# CAMINHO 1 - FINAIS POR EMAIL
label caminhoQ2_derivado_email:
    if who_is_lindsey_question == 'a':
        p "(Acho que me lembro dela de algum artigo científico que li.)"
    else:
        p "(Eu realmente não me lembro, não adianta o quanto eu tente.)"

    
    p "(Bem, isso não importa agora. Acredito que sei as respostas de qualquer forma. Vamos logo para elas.)"
    
    "Questão" "...como acessar fragmentos de código, a partir do código fonte de um programa?"
   
    menu:
        "Rotina de Serviço":
            $ question_2_thomas  = 'Errada'
        "Chamada de Sistema":
            $ question_2_thomas  = 'Errada'
        "Gerência de memória":
            $ question_2_thomas  = 'Errada'
        "Uso de função":
            $ question_2_thomas  = 'Certa'

    p "(Beleza, deve ser isso. Agora a outra deve ser...)"

    "Questão" "...que método é usado para executar dois ou mais programas diferentes em um processador de 1 só núcleo e sem pipeline, porém dando ao usuário a impressão de que todos eles são executados ao mesmo tempo?"
    menu:
        "Escalonamento":
            $ question_3_thomas  = 'Certa'
        "Confinamento":
            $ question_3_thomas  = 'Errada'
        "Sobreposição":
            $ question_3_thomas  = 'Errada'
        "Cooperação":
            $ question_3_thomas  = 'Errada'

    p "(Tá certo! Tudo respondido.)"
    
    p "(Por que será que deram tanto tempo para responder uma prova de 3 questões?)"
    
    p "(Enfim, não tem porque pensar nisso agora.)"
    
    p "(Só vou entregar logo e ir pra casa.)"
    
    stop music fadeout 1.0
    jump finais_curtos_1
    with fade

# FINAIS CURTOS
label finais_curtos_1:
    play music "audio/tema_durante_finais_curtos.mp3" fadein 1.0 volume 0.3
    scene bg quarto
    with fade

    "" "Uma semana se passa. Thomas está em casa e acaba de acordar."
   
    p "UUhhhhaaaa! Ai ai..."
   
    p "Bora fazer um cafezinho."
   
    play sound "audio/toque_celular.mp3" fadein 1.0 volume 0.3
   
    p "Meu Deus gente, acabei de acordar!"
   
    p "O que é agora?"
   
    p "... EITA!"
   
    p 'É UM "EMAIL" DA TESLATECH!'
    
    p "ABRE ABRE ABRE ABRE ABRE..."

    if(question_1_thomas != 'Certa' or question_2_thomas != 'Certa' or question_3_thomas != 'Certa') :
        jump finais_curtos_1_1

    "EMAIL" "Bom dia, Thomas!"
   
    "EMAIL" "A empresa TeslaTech vem por meio deste informar que, ..."
   
    "EMAIL" "Apesar de você ter acertado todas as questões, ..."
   
    "EMAIL" "Infelizmente o senhor não está contratado, pois estamos procurando pessoas com um perfil um tanto diferentes no momento."
   
    "EMAIL" "Mas, não se desanime! Teremos outros testes."
   
    "EMAIL" "Sinta-se livre para tentar novamente ano que vem, por exemplo."
   
    "EMAIL" "Lhe desejamos sorte!"
    
    "EMAIL" "Atenciosamente, TeslaTech."
   
    p "..."
   
    p "... Sério?"
   
    p "“perfil”?"
   
    p "O que eles esperavam exatamente? Eu nem tive uma entrevista ou fiz algum teste de personalidade."
   
    p "Como eles sabem o meu “perfil”?"
   
    p "... Tanto faz."
    
    p "Não vou pensar nisso agora."
    
    p "Tenho mais o que fazer..."
    
    stop music fadeout 1.0
    jump play_again
    with fade

label finais_curtos_1_1:

    "EMAIL" "Bom dia, Thomas!"
   
    "EMAIL" "A empresa TeslaTech vem por meio deste informar que, ..."
   
    "EMAIL" "Infelizmente o senhor não está contratado, pois tinham questões erradas em sua prova e era necessário acertar todas."
   
    "EMAIL" "Mas, não se desanime! Teremos outros testes."
   
    "EMAIL" "Sinta-se livre para tentar novamente ano que vem, por exemplo."
   
    "EMAIL" "Lhe desejamos sorte!"
   
    "EMAIL" "Atenciosamente, TeslaTech."
   
    p "... Droga."
   
    p "Eu me esforcei tanto pra errar alguma questão e não conseguir passar?"
   
    p "Isso não é justo..."

    if(question_2_jean == 'Certa' and question_3_jean == 'Certa'):
        jump finais_curtos_1_2

    stop music fadeout 1.0
    jump play_again
    with fade

label finais_curtos_1_2:
    play sound "audio/toque_ligacao.mp3" fadein 1.0 volume 0.3

    "" "Thomas recebe uma chamada de Jean."
   
    p "(Chamada do Jean? Deve ser algo importante.)"
   
    j "CAAAARAAAAAAA!"
   
    p "AAAHH, não grita no meu ouvido!"
   
    p "O que aconteceu?"
   
    j "Eu PASSEI mano. Nem tô acreditando!"
   
    p "Oh, você passou?"
   
    p "Parabéns mano."
   
    j "Ei que desânimo é esse?"
   
    j "Não me diga que você não conseguiu?"
   
    p "Não, não consegui."
   
    j "NOSSA! Que injusto!"
   
    j "Depois de todo o seu esforço! Eu só consegui passar por sua causa!"
   
    p "Fazer o que, eu errei."
   
    p "Não podia errar nenhuma."
    
    j "Poxa, cara.."
    
    j "Não fica assim não. Você é inteligente, vai conseguir entrar em outra empresa."
    
    p "Talvez."
    
    j "Ei, bora sair mais tarde, não vou comemorar sem você!"
   
    j "E pode deixar que eu pago sua parte."
  
    p "Você vai pagar de verdade ou tá dizendo isso pra “esquecer a carteira” depois?"
   
    j "Não cara, vou pagar MESMO! “True da true”."
   
    p "Aaaaahh, tanto faz. Vou fingir que acredito."
   
    p "Tô sem forças pra discutir."
   
    p "Eu topo."
   
    j "Aí sim! A gente se fala."
   
    j "E se anima cara, manda mensagem para aquela garota."
   
    j "Quem sabe vocês não combinam algo."
   
    p "Acho que não."
   
    j "Manda sim pô! Que que custa?"
   
    p "Vou pensar no caso."
   
    j "Boooooa! Até mais mano."
   
    p "Até."
   
    "" "A chamada é encerrada."
   
    p "Pelo menos eu consegui ajudar o Jean a passar. Já é alguma coisa."
    
    p "E até que ele não deu uma má ideia..."
    
    p "Mas agora não, preciso pensar um pouco."
    
    p "Eu nem sei o que diria."

    if(lindsey_friendship > 0):
        jump finais_curtos_1_3

    stop music fadeout 1.0
    jump play_again
    with fade

label finais_curtos_1_3:
    play sound "audio/toque_celular.mp3" fadein 1.0 volume 0.3
    "" "O celular de Thomas recebe outra notificação."
    
    p "MEU DEUS, que isso agora? É festa?"
    
    p "... Mensagem de “@lynd.spears”... Quem?"
   
    p "... AH, LINDSEY!"

    if(question_2_lindsey == 'Certa' and question_3_lindsey == 'Certa'):
        jump finais_curtos_1_4

    l "Bom dia, Thomas." 
    
    l "Então, eu não sei se você passou no teste ou não."
   
    l "No meu caso, não kkkk."
    
    l "Mas, bem, independente disso."
    
    l "Você me ajudou durante o teste."
    
    l "Além do que você parece um cara legal."
   
    l "Então, como um agradecimento."
   
    l "Eu pensei se a gente não podia sair para comer, sei lá."
   
    l "Por minha conta!"
   
    l "Viu que bom negócio? Kkkk"
   
    l "Mas, olha, é só dessa vez em?"
    
    l "Não se acostume mal."
    
    l "ASSIM, não querendo dizer que vão outras vezes, eu só..."
   
    l "ENFIM!"
    
    l "Espero você me retornar, pra gente definir o local, data, hora, essas coisas."
   
    l "Se você quiser! É claro, não estou te obrigando de forma alguma."
    
    p "Uau, isso é... Bem legal."
    
    p "Mas é uma pena que ela não passou."
    
    p "De toda forma, ela parece muito legal também."
    
    p "Eu que não vou desperdiçar essa chance!"
    
    p "(Até porque é comida de graça...)"

    stop music fadeout 1.0
    jump play_again
    return

label finais_curtos_1_4:
    l "Bom dia, Thomas." 
  
    l "Então, eu não sei se você passou no teste ou não."
   
    l "Bem, eu PASSEI, yyeeyy!"
   
    l "Espero que você tenha conseguido também."
   
    l "Mas, bem, independente disso."
   
    l "Você me ajudou durante o teste."
   
    l "Além do que você parece um cara legal."
    
    l "Então, como um agradecimento."
    
    l "Eu pensei se a gente não podia sair para comer, sei lá."
    
    l "Por minha conta!"
    
    l "Viu que bom negócio? Kkkk"
    
    l "Mas, olha, é só dessa vez em?"
    
    l "Não se acostume mal."
    
    l "ASSIM, não querendo dizer que vão outras vezes, eu só..."
    
    l "ENFIM!"
   
    l "Espero você me retornar, pra gente definir o local, data, hora, essas coisas."
   
    l "Se você quiser! É claro, não estou te obrigando de forma alguma."
   
    p "Uau, isso é... Bem legal."
   
    p "Fico feliz que ela tenha passado, pelo menos."
   
    p "Além do que ela parece muito legal também."
   
    p "Eu que não vou desperdiçar essa chance!"
    
    p "(Até porque é comida de graça...)"

    stop music fadeout 1.0
    jump play_again
    return

label play_again:
    scene bg black
    play music "audio/tema_menu_generico.mp3" fadein 1.0 volume 0.3
    "" "Você gostaria de jogar novamente?"
    menu:
        "Sim":
            stop music fadeout 1.0
            jump start
        "Não":
            return

#CAMINHO  2 - ESCOLHAS PRINCIPAIS
label caminhoQ2_derivado_principal:
    p "(Espera... Mas é claro!)"

    p "(A mulher que fez a pergunta ao instrutor, ela é Lindsey Spears!)"
    
    p "(Mas isso é estranho. Será que ela fez algo importante? Eu realmente nunca tinha ouvido falar dela antes.)"
   
    p "(A menos que, nesta prova o objetivo seja... Espera)"

    stop music fadeout 1.0
    play music "audio/tema_dialogo_geral.mp3" fadein 1.0 volume 0.3
    scene bg classroom
    with fade

    show jean smile1 at right

    show joana smile at left

    p "(Quem é a mulher conversando com o Jean??)"

    "" "A outra mulher que estava na sala fazendo o teste, que não era a Lindsey estava conversando com o amigo de Thomas."

    p "(Por que diabos ela está conversando com ele no meio da prova? Isso não é contra as re...)"
   
    p "(Não... Não é contra as regras.)"
    
    p "(Nada nas regras diziam que não podíamos conversar entre si.)"

    p "(E como na minha prova eu tenho uma pergunta referente a Lindsey, é bem possível que na prova dessa mulher tenha uma pergunta referente ao Jean.)"
    
    p "(Ela deve ter decidido perguntar diretamente a ele para saber a resposta; uma solução simples, porém efetiva.)"
    
    hide joana smile 
    
    hide jean smile1
    with fade

    "" "Eles terminam de conversar pouco depois. Ela retorna ao seu assento e escreve algo na prova quase que imediatamente após se sentar."
    
    p "(Entendi, isso provavelmente significa que Joana Olympios é a mulher que acabou de conversar com Jean.)"
    
    p "(É possível eles tenham trocado respostas.)"
    
    p "(Ou que o Jean simplesmente deu a resposta que ela queria... Ele é meio bobo quando se trata de mulheres.)"
   
    p "(De qualquer forma, é melhor eu fazer o mesmo.)"
    
    p "(É o único jeito de eu ter certeza qual a resposta correta.)"
   
    p "(Como eu ainda não tenho certeza quem é a Joana; Lindsey, aqui vou eu.)"
    
    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    show lindsey annoyed
    with fade

    "" "Thomas se aproxima de Lindsey para tentar iniciar uma conversação."

    "" "Quando ela percebe isso esconde a prova imediatamente."

    p "Olá. Você é a Lindsey, não é? Eu ouvi seu nome quando fez a sua pergunta."

    show lindsey angry

    l "..."

    p "(Droga, parece que ela não gostou de eu ter lembrado da pergunta que ela fez, deve ter sido vergonhoso pra ela.)"
    
    p "(Ela também deve estar receosa de conversar com alguém, até porque ninguém tem certeza se conversar é permitido mesmo.)"
    
    p "Eu sinto muito te incomodar, sei que deve estar concentrada na prova."
    
    p "É que eu tenho uma pergunta sobre você nela, e eu queria saber se pode me ajudar a responder."
    
    l "..."
    
    p "(Ainda sem resposta. Ela parece estar ficando incomodada.)"

    p "(Será que seria melhor eu conversar com Joana primeiro e tentar perguntar a ela depois?)"

    menu: 
        "a) Pensar em algo novo para falar para Lindsey (insistir na conversa).":
            $ question_talk_to_lindsey  = 'a'
        "b) Deixar Lindsey em paz por enquanto e ir falar com Joana (desistir da conversa).":
            $ question_talk_to_lindsey  = 'b'
            jump caminhoQ2_2_derivado_principal

    
    p "(Eu não posso simplesmente desistir! Eu preciso dessa resposta.)"
    
    p "(Vamos pensar, se todas provas forem como a minha, e se elas forem justas.)"
    
    p "(Significa que todas tem 2 perguntas sobre pessoas diferentes desta sala. E como tem 5 candidatos, cada pessoa deve aparecer na prova de outras pessoas 2 vezes.)"
    
    p "(Eu não tenho nenhuma pergunta sobre mim, então dentre as 4 pessoas restantes 2 delas devem ter.)"
    
    p "(Existe 50 por cento de chance da prova da Lindsey ter uma pergunta sobre mim. E se isso for verdade nós 2 temos a ganhar trocando as respostas.)"
    
    p "(Se isso não for o bastante para convencer ela a falar comigo eu não sei o que será.)"
    
    p "(Mas, antes preciso descobrir se eu estou na prova dela.)"
    
    p "Então, senhorita Lindsey. Como você sabe eu tenho uma pergunta a responder quanto a você."
    
    p "E eu também sei que você tem uma pergunta a responder quanto a mim."
    
    show lindsey surprised

    l "AN?! Como você..."
    
    show lindsey angry

    p "(Bingo!)"
    
    p "Como eu sei disso não é importante agora, o que importa é que eu tenho uma coisa que você quer, e você tem algo que eu quero."
    
    p "Conversar durante as provas não está contra as regras, e é muita coincidência nossos nomes estarem nas perguntas como se fossemos um novo Alan Turing."
    
    p "E como você falou agora pouco, o risco já foi tomado."
    
    show lindsey annoyed

    l "..."
    
    l "... Huuumm"

    l "Aaaa..."
    
    l "Tá tudo bem, você me convenceu."
    
    l "Não é como se eu tivesse muita escolha de qualquer jeito."
   
    show lindsey normal

    p "(Boa!)"
    
    l "Mas, me diga uma coisa."
    
    p "Sim?"
    
    l "Como você sabia que eu tinha uma pergunta sua?"
    
    l "Pelo visto eu não a escondi o bastante."
    
    p "Bem, na verdade, eu não sabia."
    
    l "An?"
    
    p "As chances de você ter uma pergunta minha eram de 50 por cento, eu apenas fingi que sabia e, ..."
    
    p "Ao julgar pela sua reação, ..."
    
    p "Acabou dando certo."
    
    show lindsey shocked

    l "Nossa, me desculpa senhor THOMAS SELBY."
   
    p "Kkkk não é pra tanto. Foi só um chute."
    
    show lindsey smile

    l "Ainda bem néh, porque do contrário eu teria que abanar minha mão 3 vezes só pra te denunciar."
    
    p "Bem, eu agradeceria."
    
    p "Assim é uma concorrente a menos."
    
    show lindsey delighted2

    l "Kkkkk idiota."
    
    show lindsey smile

    p "Kkkkk."
    
    show lindsey normal
     
    l "..."
    
    p "..."
    
    l "Ah bem, você disse 50 por cento de chance não?"
    
    p "Isso."
    
    l "Significa que eu fui a primeira pessoa que você perguntou então..."
    
    p "Ah... Bem.. É claro!"
    
    p "Foi como eu disse antes. Por causa da sua pergunta eu sabia quem você era."
    
    p "O mais lógico é conversar com você primeiro."
    
    show lindsey smug

    l "Ah sim, claro..."
    
    p "(O que ela tá insinuando com essa resposta?)"
    
    show lindsey normal

    p "Bem, de toda forma."
    
    p "Podemos trocar nossas respostas então?"
    
    l "Ah claro, tudo bem!"

    "" "Thomas e Lindsey trocam as respostas de suas perguntas"

    hide lindsey normal
    with fade

    scene bg caderno
    with fade

   
    $ question_3_thomas  = 'Certa'
   
    
    $ question_2_lindsey  = "Certa"

    $ troca_respostas_lindsey = 1

    p "(Nossa, isso acabou indo bem melhor do que pensei.)"
   
    p "(Foi até que bem divertido conversar com ela.)"
   
    p "(Além disso consegui diminuir um pouco a tensão do teste)" 
    
    
    $ lindsey_friendship = 1


    jump caminhoQ2_2_derivado_principal
    
label caminhoQ2_2_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_geral.mp3" fadein 1.0 volume 0.3
    p "(Certo, de qualquer forma, eu tenho que conversar com a Joana agora.)"
   
    p "(Espero que seja ela mesmo, se não vou passar mó vergonha.)"
   

    
    scene bg classroom
    with fade

    "" "Thomas se aproxima da suposta Joana."
   
    "" "Quando percebe, ela se levanta em frente dele, pouco antes que ele pudesse chegar perto de sua carteira."

    stop music fadeout 1.0
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3

    show joana

    m2 "Olá, posso ajudá-lo em algo?"
   
    p "(Nossa, quanta formalidade.)"
    
    p "(Parece até uma atendente de loja de shopping.)"
   
    p "Oi. Você é a Joana, não?"
   
    jo "Sim, sou. O que quer comigo?"
    
    p "Bem, uma das minhas perguntas cita você. Então eu imaginei se poderíamos trocar respostas."
    
    show joana sleepy

    jo "Ah, sim. Entendo."
    
    jo "Você deve ser o Thomas certo?"
    
    show joana

    p "Sim, mas, como você sabe?"
    
    jo "Eu perguntei ao Jean quem ele conhecia e ele me disse que você era Thomas, o melhor amigo dele."
    
    p "(Jean linguarudo dos infernos. Dando informações a adversária?)"
    
    p "(Por que não diz onde eu moro e meu tipo sanguíneo também?)"
    
    jo "Bem, infelizmente eu não tenho uma pergunta com você."
   
    jo "E simplesmente te ajudar só aumentaria a concorrência."
    
    show joana sad

    jo "Então... É." 
    
    show joana

    p "(Droga! Ela não vai me dar a resposta.)"
    
    p "(E o pior é que não há nada que eu possa oferecer a ela)"
   
    p "(Só se eu conseguir descobrir que pessoa está na questão restante dela)"
    
    p "(Bem, não sou eu nem o Jean. Logo só sobra...)"
   
    l "Para! Por favor, eu não tenho o que falar com você."
   
    p "(O que é isso? Lindsey?)"

    hide joana 

    stop music fadeout 1.0
    play music "audio/tema_dialogo_luan.mp3" fadein 1.0 volume 0.3

    show lindsey angry at left

    show luan smirk at right

    h "Ei ei ei. Não precisa desse estardalhaço todo princesa."
    
    h "Não esquece que se você gritar comigo pode ser desqualificada na hora."
    
    show lindsey angry2 at left

    l "Primeiramente, eu NÃO SOU sua “princesa”."
    
    l "Segundamente, eu não gritei com você. Eu só estou tentando ser direta e inflexível."
    
    show lindsey angry at left

    h "Aaaaahhh qual é princesa. Não precisa falar desse jeito."
   
    h "Eu só estou pedindo uma ajuda com minha pergunta aqui."
    
    h " Se tem o seu nome na prova é por que eles querem que eu pergunte pra você da questão, não é?"
    
    l "Bem, isso já não é problema meu."
    
    l "Eu não tenho nenhum motivo para ajudar um adversário a troco de nada."
    
    h "Ah, não seja por isso."
    
    h "Se é uma recompensa que você quer a gente pode ir pra algum lugar depois da prova, se divertir um pouco, que tal?"
    
    show lindsey angry2 at left

    l "Não! E não se aproxima de mim."
    
    h "Qual é princesa..."
    
    l "Não chega perto! Por favor!"

    show lindsey angry at left
    
    p "(Merda, esse cara tá deixando a Lindsey muito desconfortável.)"
    
    p "(Ela pode acabar se machucando também. Será que eu interfiro?)"

    menu:
        "Ajudar a Lindsey (interferir).":
            $ lindsey_friendship = 1
        "Não fazer nada (não interferir)":
            $ lindsey_friendship = 0
            $ favor_lindsey = 0
            jump caminhoQ2_3_derivado_principal
    
    hide lindsey angry
    with fade

    p "Ei cara, dá pra deixá-la em paz?"
   
    p "Ela claramente não quer te ajudar."
   
    show luan surprised at right

    h "Olha só, senhoras e senhores, temos um herói aqui!"

    show luan smirk at right

    h "Pode ficar tranquilo “amigo”, nós só estamos conversando."
  
    p "Não é o que me parece, ela está muito desconfortável."
   
    p "Não posso deixar você continuar com isso."
    
    show luan angry1 at right

    h "Ah é? E como exatamente você planeja me impedir?"
   
    p "(Droga! Esse cara não me escuta.)"
   
    p "(E eu estou começando a ficar estressado com ele.)"
   
    p "(Será que a única linguagem que esse escroto entende é a violência?)"
   
    p "(Mas se eu começar uma briga eu com certeza vou ser desqualificado)"
   
    p "(AAaaahh o que eu faço agora?)"

    menu:
        "Brigar com o homem (usar de violência).": 
            jump final_desclassificado
        "Convence-lo a parar na conversa (não usar de violência).":
            $ favor_lindsey = 1
            $ lindsey_friendship = 1


    p "Seguinte, “amigo”."
   
    p "Eu sei que você quer a resposta, todos queremos passar."
   
    p "Mas, você não vai conseguir simplesmente forçar ela a dar a resposta."
   
    p "Você não pode a usar a força; você não pode gritar com ela."
   
    p "Além disso, você tá perdendo muito tempo fazendo isso."
   
    p "Se quiser pode até continuar perturbando a guria."
   
    p "Mas, ela não tem nenhuma obrigação de te dar a resposta."
  
    p "Então, porque você não senta na sua carteira, como um bom menino."
  
    p "E termina as outras questões primeiro, sim?"
    
    show luan angry2 at right

    h "Ora seu metidinho de..."
    
    show luan angry1 at right

    p "Olha aí? Viu? Você quase foi desqualificado só de falar comigo."
   
    p "Acho que é o melhor pra todo mundo que você sente e esfrie sua cabeça."
   
    h "..."
    
    h "... Tsc."
    
    h "Isso não acabou moleque."

    hide luan angry1
    with fade

    p "Bem, isso deve resolver."
   
    p "Por enquanto..."
   
    l "Éeee... Então..."
    
    p "Hum?"


    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    show lindsey smile2 
    with fade

    l "Obrigada, por me ajudar."
   
    p "Ah, fica tranquila."
   
    p "Não foi nada demais."
    
    show lindsey normal

    l "Na verdade foi. Você poderia ter sido desqualificado se algo desse errado."
   
    p "É, acho que sim."
   
    l "Então, por que? Porque correu o risco?"
   
    l "Você nem me conhece."
   
    p "Aaaaah, bem. "
    
    p "Era simplesmente o certo a se fazer."
    
    p "E, sei lá."
    
    p "Só queria ter certeza que você fosse ficar bem."
    
    show lindsey surprised

    l "Oh..."

    show lindsey annoyed

    l "Você não precisa ficar me protegendo, você não é meu segurança afinal."
    
    show lindsey smug2

    l "Tudo bem que sou linda como uma princesa, mas não é pra tanto."
    
    p "... É sério isso?"
    
    show lindsey smile

    l "Obrigada mesmo assim."
    
    l "Eu te devo uma."
    
    p "Não se preocupa com isso, estou feliz que você está bem."


    hide lindsey smile 

    
    stop music fadeout 1.0
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3

    show joana
    with fade

    p "Oi, foi mal ter sumido do nada."

    show joana smile2    

    jo "Imagina, seu motivo foi justo."
    
    p "Que bom que pensa assim."
    
    jo "..."

    jump caminhoQ2_4_derivado_principal


label caminhoQ2_3_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3
    "" "O homem continua incomodando Lindsey por mais um tempo."

    hide lindsey angry
    with fade

    show luan smile3

    "" "Pouco depois ele sai de lá. Com um sorriso que dá pra ver de costas."

    hide luan smile3 
    with fade

    p "(Maldito... Ficou a importunando até que ela não pudesse aguentar mais.)"
   
    p "(Eu queria ter feito algo, mas era muito arriscado.)"
    
    p "(Espero que eu não me arrependa disso.)"

    show joana
    with fade

    p "Bem, isso foi... Muito desconfortável."

    show joana angry

    jo "Com certeza. Repugnante eu diria."

    p "Sim, espero que ela esteja bem."

    show joana

    jo "Sim..."

    jump caminhoQ2_4_derivado_principal

label caminhoQ2_4_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3
    p "Bem."

    p "Sobre a resposta da minha questão..."

    show joana surprised

    jo "Eu tenho uma proposta a você."

    p "Como?"

    jo "Tem outra coisa que você pode fazer pra conseguir a resposta..."

    p "Eeeee... Bem..."

    show joana smug2

    jo "Podemos forjar uma aliança."

    p "Aliança? Em que sentido?"

    show joana

    jo "É bem simples..."

    jo "Sabe, eu já estou fazendo este teste pela segunda vez."
    
    show joana sad
    jo "Ano passado eu acabei acreditando em alguém que não devia durante a prova, e isso fez com que eu não passasse..."
    
    p "Oh... Sinto muito por isso."

    show joana smug

    jo "Está tudo bem, este ano vai ser diferente."
    
    jo "Eu me preparei tanto intelectualmente quanto psicologicamente."
    
    jo "E eu posso te AFIRMAR uma coisa."
    
    jo "Com ou sem ajuda, mentindo ou não para mim..."
    
    jo" Eu VOU passar nesta prova."

    p "(Meu Deus, quem me dera eu tivesse essa confiança toda.)"

    show joana 

    jo "Enfim, onde eu quero chegar é..."

    jo "Eu vou passar de uma forma ou outra."
    
    jo "E quando eu passar, é sempre bom ter uma pessoa em quem posso confiar dentro da empresa."
    
    jo "A garota parece facilmente manipulável."
    
    jo "Seu amigo não é muito diferente."
   
    p "(AH MEU, ELE DEU A RESPOSTA DE GRAÇA PRA ELA MESMO?)"
    
    jo "E esse Luan parece do tipo bruto e nojento."
    
    p "(Então esse é nome dele.)"
    
    jo "Logo, você parece ser a melhor opção para estar ao meu lado na empresa."
    
    p "Ah... Bem... Obrigado... Eu acho."
    
    jo "Mas, você precisa provar que é confiável primeiro."
    
    p "Ah, e como eu faria isso?"
    
    jo "Quero que você consiga a resposta desta pergunta com o Luan."
    
    p "Espera, sério? O Luan? O escroto que ficou enchendo a Lindsey?"
    
    show joana sleepy2
    
    jo "Sim."
    
    p "Mas, como eu faria isso? Ele não me parece do tipo flexível."
    
    show joana 

    jo "E não deve ser mesmo. Por isso é um bom teste."
    
    jo "Se você fizer isso, significa que podemos forjar nossa aliança."
    
    jo "E é claro, com ela formada. Te dar a resposta de uma pergunta é o de menos para mim."
    
    p "Certo, eu entendo como isso nos beneficia. "
    
    p "Mas, como eu posso confiar que sua resposta é correta?"
   
    p "Você pode simplesmente estar armando para mim e diminuindo a concorrência me dando uma resposta errada."
    
    show joana surprised
    
    jo "Tens um ótimo ponto."
   
    p "..."

    show joana 

    jo "..."

    p "Então?"
    
    jo "Oh, desculpe."

    show joana smug2

    jo "Eu pensei que tinha ficado implícito."
    
    jo "Você não tem nenhuma segurança que estou falando a verdade."
    
    jo "Você precisa da resposta, eu não."
    
    jo "Eu apenas quero um companheiro dentro da empresa."
    
    jo "Se você não quiser fazer, eu simplesmente vou procurar outras opções quando entrar."
    
    jo "Além do mais, eu já sei a resposta da pergunta do Luan."
    
    jo "Do jeito que ele é provavelmente daria a resposta errada de qualquer modo."
    
    jo "O fato é: ... "
    
    jo "Eu vou passar, você me ajudando ou não."
    
    jo "A pergunta que você se deve fazer é:"
    
    jo "Eu me arrisco, passo e consigo uma aliada?"
    
    jo "Ou eu não me arrisco, podendo não passar, e ainda se passar terei no mínimo uma adversária?"
    
    jo "A escolha é sua."
    
    show joana 

    p "(Cara, o ego dessa mulher é maior que meu grau de miopia.)"
    
    p "(E olha que eu só enxergo 1 palmo à minha frente.)"
    
    p "(Bem, mesmo que eu aceite, não consigo pensar em nenhuma forma de tirar a resposta de Luan por enquanto.)"
    
    p "Eu ainda não tenho certeza. Tenho que pensar um pouco."
    
    jo "Não tem problema. Pense um pouco."
    
    jo "Se você aceita, apenas me retorne a resposta de Luan antes do fim do teste."
    
    "" "Joana diz a pergunta de Luan para Thomas."
   
    jo "Mas, não se esqueça. Eu estou ouvindo tudo."
    
    jo "Como minha prova está feita tenho todo tempo do mundo para te acompanhar."
    
    jo "Eu vou saber se a resposta veio de Luan ou não."
    
    p "Entendi."
   
    p "Bem, eu volto depois com minha resposta."
   
    jo "Boa sorte, Thomas."
   
    jo "Não me faça esperar muito."
    
    show joana smug2

    jo "Se não fico com saudades."
   
    show joana

    p "Éeee... Claro! Não vou."
   
    p "Com licença."

    hide joana 
    with fade

    p "(Ok... Essa garota é um tanto estranha.)"
    
    p "(Honestamente, eu não sei se quero alguém como ela do meu lado.)"
    
    p "(Ela é fria. Inteligente. Mas ignorante.)"
    
    p "(Por outro lado, ter a resposta da questão 2 seria muito bom. Até por que eu não tenho certeza do que responder nela ainda.)"
    
    p "(AAaaaah... Eu não sei.)"
   
    p "(Tenho que pensar melhor so...)"
   
    p "(Espera...)"
    
    p "(O que o Jean está fazendo na carteira do Luan?)"
   
    "" "Thomas observa atentamente a conversa dos dois para ter certeza que nada de ruim aconteceria com seu amigo."
    
    "" "Pouco tempo depois, Jean volta a sua carteira."
   
    p "(Me parece que está tudo bem.)"
   
    p "(Mas é melhor eu checar pra ver se está tudo certo mesmo.)"

    stop music fadeout 1.0
    play music "audio/tema_dialogo_jean.mp3" fadein 1.0 volume 0.3

    show jean smile1
    with fade

    p "Aí Jean."
    
    j "Eae mano."
   
    p "Tá tudo bem? Por que você foi conversar com o traste?"
    
    j "Ah, eu precisava da resposta dele."
    
    j "Acabou que ele também precisava da minha."
    
    j "Então a gente trocou."
   
    p "Ah bom, por um segundo você me preo..."
   
    j "E eu dei uma resposta errada pra ele."
    
    show jean smirk

    p "..."
   
    j "..."
   
    p "Cara... Nossa como eu queria poder gritar agora."
    
    show jean normal

    j "Que foi? Eu não quero que esse escroto passe no teste e fique assediando todas as meninas da empresa."
   
    p "Eu concordo cara, mas e se ele descobrir?"
   
    show jean smile3    

    j "Vai naaaada, o cara tem marra, mas é uma porta."
   
    j "Eu até suspeito que ele me deu a resposta errada."
  
    p "Falou o cara o que deu a resposta de graça pra Joana."
  
    show jean surprised

    j "O quuueeeeê??? Nãaaaoooo."
   
    j "Jamais faria iiiissoooo..."
    
    show jean angry1

    p "Ela me contou."
    
    show jean normal 

    j "... "
   
    j "... Olha"
   
    j "Em minha defesa."

    show jean sad
   
    j "Você não ouviu o tom que ela falou comigo cara..."
   
    show jean normal 

    p "Meu Deus, mano!"
  
    p "Não importa, nem quero saber."
   
    p "Confia em mim, a última coisa que a Joana estava é te dando mole."
  
    p "Se a mãe dela se chamasse Blue Sky ela seria a Era do Gelo 6."
  
    p "... Ou 7, sei lá! Tem muitos."
  
    j "Se é assim, o que vocês ficaram conversando tanto agora pouco?"
    
    show jean smirk 

    p "Eu te conto depois, não é importante agora."
   
    show jean normal 

    j "Huuuuum. Ok."
    
    j "Mas me conta em? Você sabe que eu odeio ficar de fora!"

    p "Boa prova, Jean."
    
    j "Ei ei ei, calma lá amigo."
   
    p "Que foi em?"
   
    show jean smile3 
    
    j "Eu tenho uma pergunta com seu nome aqui."
    
    j "E também queria a sua ajuda pra saber se a resposta do Luan está correta mesmo."
    
    show jean normal

    p "Aaaaah, tá bem."
    
    p "Mas, vamos logo. Não tenho muito tempo."
   
    j "Beleza, primeiro a sua."
   
    "Questão" "A relação entre o disco rígido, com o sistema operacional e os programas de usuário é de ... (responda com uma palavra):"

    menu:
        "Alternância.":
            $ question_2_jean = "Errada"
        "Reorganização.":
            $ question_2_jean = "Errada"
        "Interação.":
            $ question_2_jean = "Errada"
        "Armazenamento.":
            $ question_2_jean = "Certa"


    p "Pronto, deve ser essa."
    j "Valeu. A do Luan agora."
    "Questão" "O método de organizar o armazenamento do sistema operacional e dos programas de usuário na memória RAM é ... (responda com uma palavra):"


    menu:
        "Encaixamento.":
            $ question_3_jean = "Errada"
        "Particionamento.":
            $ question_3_jean = "Certa"
        "Acondicionamento.":
            $ question_3_jean = "Errada"
        "Adicionamento.":
            $ question_3_jean = "Errada"

    show jean smile3 

    j "Ae mano, valeu!"
   
    show jean normal

    p "Tá tranquilo, não se preocupa com isso."
   
    p "Vou voltar para terminar minha prova."
   
    j "Beleza. Boa sorte!"
    
    hide jean normal
    with fade

    stop music fadeout 1.0
    play music "audio/tema_dialogo_geral.mp3" fadein 1.0 volume 0.3

    p "(Ok, agora eu preciso ver sobre aquela “aliança” com a Joana.)"

    if(lindsey_friendship < 1):
        jump caminhoQ2_7_derivado_principal

    p "(Espera, aquela é a Lindsey falando com a Joana?)"

    show lindsey angry2 at right

    show joana angry at left
    with fade

    p "(Nossa, a Lindsey parece muito nervosa. O que será que está acontecendo lá?)"

    hide joana angry
    with fade

    p "(Ela voltou com uma cara de bunda pra carteira. Parece que vai chorar a qualquer momento.)"
    
    p "(Seria melhor eu ir conversar com ela.)"
    
    p "(Mas, tem um problema...)"
    
    show luan smirk  at left
    with fade   

    p "(O tempo do teste está acabando.)"
   
    p "(Se eu tiver que conseguir a resposta para Joana, e ainda dar tempo de terminar a prova, eu preciso conversar com Luan agora.)"
   
    p "(Significa que se eu for conversar com Lindsey, eu provavelmente estarei jogando a aliança com Joana fora.)"
    
    p "(O que eu faço?)"


    menu:
        "Conversar com Lindsey (quebrar aliança)":
            $ nada = 'nada'
        "Conversar com Luan (manter aliança)":
            jump caminhoQ2_7_derivado_principal
    
    # "" "A aliança com Joana foi rompida"


    p "(Honestamente, quem se importa com essa aliança idiota?)"
   
    p "(Fazer tanto sacrifício pra ainda correr o risco de Joana não passar comigo ou a resposta dela ainda estar errada.)"
   
    p "(Pelo menos a Lindsey parece uma pessoa gentil e confiável.)"
   
    p "(Eu prefiro que ela passe comigo do que a Joana.)"
   
    p "(Vou ir falar com ela.)"

    hide luan smirk
    with fade

    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    "" "Thomas se aproxima de Lindsey."

    p "Oi, Lindsey. Tá tudo bem?"
   
    show lindsey annoyed
    l "Oi, Thomas. Está sim."
   
    l "Não se preocupe comigo, pode ir fazer sua prova."
    
    p "Olha, desculpa me intrometer, mas..."
    
    p "Eu posso ver que aconteceu alguma coisa entre você e a Joana."
   
    show lindsey normal 

    l "Ah... Bem..."
    
    p "Pode falar, não tem problema."
    
    l "..."

    show lindsey sad 

    l "Eu preciso da resposta dela."
   
    l "Mas, eu não estou assim por que ela disse “não” ou algo assim."
    
    l "Ela não tem uma pergunta minha então eu entenderia perfeitamente."
    
    l "É que ela falou comigo como se eu fosse nada."
    
    l "Me disse que não tinha nenhum interesse em ajudar ou trabalhar com alguém como eu."
    
    l "Disse que estou despreparada para o cargo e que sou muito “maleável”."
    
    p "É bem a cara dela dizer isso mesmo."
    
    l "Então, você tinha falado com ela e me pareceu que deu tudo certo."
  
    l "Não esperava que ela fosse tão seletiva."
    
    p "Pode falar que ela é escrota, tá tudo bem."
    
    show lindsey delighted2

    l "Kkkk realmente."
    
    p "..."
    
    show lindsey normal

    l "..."
    
    p "Bem... É..."
    
    p "Já que ela não vai te dar a resposta mesmo."
    
    p "Você quer que eu te ajude a responder?"

    if(question_3_thomas != 'Certa'):
        jump caminhoQ2_5_derivado_principal
    
    show lindsey shocked
    
    l "Não! Que isso, não seria justo com você."

    show lindsey normal

    l "Nós já trocamos nossas respostas, eu não posso fazer nada em troca da sua ajuda."
   
    p "Não precisa, eu fico feliz em ajudar."
   
    p "Eu quero que você passe comigo para possamos trabalhar juntos."
   
    l "... Você é estranho."
    
    p "O quê?"
    
    l "Você mal me conhece, por que está me ajudando tanto?"
    
    p "Eu já disse o porquê."
    
    show lindsey annoyed

    l "Huuuumm, não."
    
    l "Não me convenceu."
   
    show lindsey smug

    l "Eu acho que você está escondendo algo de mim senhor Shelby..."
   
    p "Você quer minha ajuda ou não afinal?"
    
    show lindsey delighted2

    l "Kkkkk quero, quero sim."
   
    l "Só estou enchendo seu saco."
    
    p "(Bem, pelo menos ela parece mais calma agora.)"

    jump caminhoQ2_6_derivado_principal

label caminhoQ2_5_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    p "Se você acha injusto comigo, nós podemos trocar nossas respostas."
    
    p "Assim eu também ganho algo."
   
    l "Bem, sim você ganha."
   
    l "Mas eu ainda vou ganhar 1 resposta a mais que você."
  
    p "Não tem problema, sério."
   
    p "Eu fico feliz se você passar comigo de toda forma."
   
    show lindsey smile

    l "É mesmo é? E por que seria isso?"
   
    p "Bem... Eu só..."
  
    p "Não tenho certeza se meu amigo Jean vai conseguir passar."
   
    p "Eeeee você parece a pessoa mais confiável daqui depois dele."
   
    p "Além do mais é ruim ficar sozinho em uma empresa tão grande e exigente."
   
    p "E sem contar também que..."
    
    show lindsey delighted2

    l "Kkkkkkk para para! Kkkk sério."
    
    show lindsey smile

    l "Eu entendi."

    l "Não precisa ficar tão nervoso."
   
    p "Eu não fiquei nervoso! Todas as minhas respostas foram embasadas em lógica e honestidade."
   
    show lindsey smug

    l "Claro, claro. Tô sabendo."
    
    show lindsey normal
   
    l "De qualquer forma, vamos trocar nossas respostas?"
    
    p "Sim, por favor..."
  
    "" "Thomas e Lindsey trocam as respostas de suas perguntas"
  
    l "Tá certo."

    $ question_2_lindsey  = "Certa"
   
    $ question_3_thomas  = 'Certa'
   
    $ troca_respostas_lindsey = 1

    jump caminhoQ2_6_derivado_principal

label caminhoQ2_6_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    l "Aqui, a pergunta da Joana é essa:"
    
    "Questão" "O que um computador precisa ter para que programas de usuários sejam executados com a impressão de execução em paralelo e para que eles possam usar o hardware disponível?"

    menu:
        "Sistema límbico":
            $ question_3_lindsey = "Errada"
        "Sistema operacional":
            $ question_3_lindsey = "Certa"
        "Sistema executor":
            $ question_3_lindsey = "Errada"
        "Sistema de pipeline":
            $ question_3_lindsey = "Errada"

    p "Pronto, espero que esteja certa."
    
    l "E eu mais ainda."

    show lindsey delighted2

    p "kkkkk."
   
    l "kkkkk."
   
    p "..."
   
    l "..."
   
    p "Bem, eu vou indo. Preciso terminar minha prova."
   
    l "Ah sim, claro."
   
    l "Boa sorte!"
   
    p "Obrigado, pra você também!"

    hide lindsey delighted2

    jump caminhoQ2_11_derivado_principal

label caminhoQ2_7_derivado_principal:

    hide lindsey angry2
    with fade

    stop music fadeout 1.0
    play music "audio/tema_dialogo_geral.mp3" fadein 1.0 volume 0.3

    
    p "(Querendo ou não, a minha aliança com a Joana não só deve ser minha melhor chance para passar nessa prova, como para me manter na empresa depois.)"
    
    p "(Vou dar um jeito de tirar essa resposta do Luan.)"

    

    "" "Thomas mal se aproxima de Luan e já é repreendido."
    stop music fadeout 1.0
    play music "audio/tema_dialogo_luan.mp3" fadein 1.0 volume 0.3

    show luan angry2

    lu "O que você tá olhando?"
    
    lu "Dá o fora daqui eu não quero nada com você."
    
    p "Talvez você não, mas eu quero."
    
    p "Preciso que você responda uma pergunta para mim."

    show luan smirk

    lu "Kkkkkk tá bom."

    show luan angry1

    lu "Que parte dessa sua grande cabeça, achou que eu iria te ajudar?"
    
    lu "Só porquê troquei resposta com seu amigo? "
    
    lu "Mas ele tinha o que me oferecer."
    
    lu "Eu não tenho nenhuma pergunta sobre você, então..."
    
    lu "O que você possivelmente poderia me oferecer?"
   
    p "Bem..."
    
    p "(Droga! Eu preciso de alguma coisa que ele queira.)"

    if (favor_lindsey  < 1):
        jump caminhoQ2_9_derivado_principal

    menu:
        "Cobrar o favor de Lindsey para receber a resposta (manter aliança).":
            $ nada =  'nada'
        "Desistir de convence-lo (quebrar aliança).":
            jump caminhoQ2_9_derivado_principal

    p "(Eu não queria ter que cobrar de Lindsey, ainda mais por que me parece bem descontável para ela me ajudar com isso.)"
    
    p "(Mas, eu preciso da resposta correta! Eu já cheguei até aqui, não vou amarelar agora.)"
   
    p "Você precisa de uma resposta de Lindsey, certo?"
   
    p "Se me passar a pergunta eu consigo a resposta para você."
    
    show luan smirk

    lu "Ohrorou."
   
    lu "Agora estamos conversando."
   
    lu "Consiga a resposta daquela guria, que eu te respondo o que quiser."
   
    p "Certo, eu volto logo."

    hide luan smirk
    with fade

    show lindsey normal 
    with fade

    p "(Bem, lá vai.)"
    
    p "(Espero que eu não me arrependa disso.)"

    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    p "Oi, Lindsey."
   
    show lindsey smile

    l "Oi, Thomas. O que te traz aqui de novo?"
   
    p "Bem, é que eu preciso de uma ajuda sua sabe."
   
    l "Oh, claro! Eu te devo uma mesmo."
   
    l "O que foi?"

    if(troca_respostas_lindsey == 1):
        jump caminhoQ2_8_derivado_principal

    p "Eu preciso que você responda uma pergunta para mim."
   
    l "Aaaaah, claro. A sua pergunta."
   
    p "Como?"
   
    l "A pergunta que você queria fazer quando veio até mim no começo da prova."
   
    p "Aaaahh, sim. Isso mesmo."
   
    l "Na verdade, eu fico aliviada que você veio até mim."
   
    l "Eu fiquei com vergonha de pedir a você depois do que fez."
   
    p "Ah, imagina... Espera, pedir?"

    show lindsey surprised

    l "Sim! Eu também tenho uma pergunta de você."
    
    show lindsey smile
    
    l "Se você puder responder para mim."
   
    p "Ah, claro! Sem problemas."

    "" "Thomas e Lindsey trocam as respostas de suas perguntas."

    $ troca_respostas_lindsey = 1

    
    $ question_3_thomas  = 'Certa'
   
    
    $ question_2_lindsey = "Certa"

    show lindsey smile2

    l "Brigado, Thomas!"
   
    p "Que isso, eu que agradeço!"
    
    show lindsey normal

    l "Ah, sim."
   
    p "..."

    show lindsey surprised

    l "Você está com uma expressão estranha."
   
    l "Tem alguma coisa que você quer me dizer?"
   
    p "(E agora? Ficaria um clima muito estranho se eu pedisse a resposta do Luan.)"
   
    p "(Eu nem sei se ela daria depois do que aconteceu.)"

    jump caminhoQ2_8_derivado_principal

label caminhoQ2_8_derivado_principal:
    
    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3

    p "(Será que eu pergunto?)"
    
    p "(Eu não quero me arrepender depois.)"

    menu:
        "Cobrar o favor de Lindsey para receber a resposta (manter aliança).":
            $ lindsey_friendship = 0
        "Desistir de perguntar e responder a questão de Joana por si só (quebrar aliança).":
            jump caminhoQ2_10_derivado_principal

    p "Bem, é que eu preciso saber a resposta de uma pergunta, e eu queria saber se você poderia me ajudar."

    show lindsey normal   
    
    l "Ah, é só isso?"
   
    l "Claro! Eu posso te ajudar. Me diga a pergunta."
   
    "" "Thomas diz a pergunta para Lindsey."
   
    l "..."
    
    p "Então, você sabe responder?"
    
    l "Sei sim."
    
    p "Que bom! Fico aliviado."
   
    l "Mas, se você não se incomodar."

    show lindsey annoyed

    l "Queria saber por que você está ajudando o Luan."
   
    p "O Luan? Como assim?"
    
    show lindsey normal

    l "Eu sei que essa é pergunta é dele, ele me disse quando..."
   
    l "... Tentou me convencer."
   
    l "E você tinha até impedido ele."
   
    l "Então por que você está o ajudando agora?"
   
    p "Ah, sabe."
   
    p "É que eu preciso dessa resposta para que eu possa convencer ele a me dar outra que preciso."
   
    p "Então eu queria saber se você poderia me ajudar."
   
    l "... Entendo."
    
    show lindsey annoyed

    l "Então, essa era intensão o tempo todo..."
   
    p "Como?"
  
    l "Nada, não se preocupe."
    
    show lindsey normal

    l "Eu te passo a resposta."
   
    p "Ah, que bom. Obrigado."
   
    "" "Lindsey passa a resposta da pergunta para Thomas."
   
    p "Bem... É só isso que eu queria."
   
    p "Então, obrigado de novo. E boa sorte!"
  
    l "Não seja por isso. Boa sorte pra você também."
    
    hide lindsey normal
    with fade

    p "(Ela realmente ficou muito desconfortável. Me sinto mal.)"
    
    p "(Provavelmente ela deve achar que Luan e eu tenhamos planejado isso desde o começo...)"
    
    p "(Mas enfim, o que está feito está feito.)"
   
    p "(Agora, eu preciso conseguir a resposta com Luan e dize-la a Joana.)"
   
    p "(E rápido! O tempo do teste está acabando.)"

    stop music fadeout 1.0
    play music "audio/tema_dialogo_luan.mp3" fadein 1.0 volume 0.3

    show luan smirk
    with fade

    p "Eu consegui sua resposta, agora quero saber da minha."
   
    lu "Cara, eu nem acredito que você fez isso."
   
    lu "Tu deu uma cavaleiro só pra deixar ela comer na sua mão néh?"
   
    lu "Solta o verbo aí, pode falar."
   
    p "Claro que não! Não enche cara."
   
    p "De qualquer forma, isso não importa pra você. Eu só quero minha resposta, por favor."
    
    show luan smile3
    
    lu "Uuuhhh, que friiiiiio. Kkkkk"
    
    show luan smirk

    lu "Tá certo cara, vamo acabar com isso. "
    
    lu "Quero vazar logo daqui."
   
    p "(Nisso eu consigo concordar com ele.)"
   
    "" "Thomas e Luan trocam as respostas."

    hide luan smirk
    with fade

    stop music fadeout 1.0
    play music "audio/tema_dialogo_joana_ou_conversa_pensativa.mp3" fadein 1.0 volume 0.3

    show joana 
    with fade

    p "Olá, Joana."

    p "Eu consegui a resposta de Luan."
    
    show joana smile 

    jo "Que ótimo. Deixe-me ver."
   
    "" "Você passa a resposta de Luan"
   
    jo "Ah sim, ele te passou uma resposta que parece certa à primeira vista, mas na verdade está errada."
   
    jo "Combina com o tipo de pessoa que ele é."
    
    jo "De toda forma, não importa."
    
    jo "Eu vi tudo o que fez, você se dedicou bastante a isso."
    
    jo "Acredito que posso confiar em você daqui em diante."
    
    jo "E para te provar isso, vou te dizer a resposta de minha pergunta."
    
    p "Obrigado."
    
    "" "Joana diz a resposta da questão de Thomas"
    
    $ question_2_thomas = 'Certa'

    jo "Bem, é isso."
    
    jo "Pode ir terminar sua prova com tranquilidade."
    
    jo "Depois dos resultados conversaremos melhor."
    
    p "Tudo bem, eu vou indo."
    
    show joana smug2 

    jo "Espero que você passe, tenho grandes planos para nós."
    
    jo "Boa sorte."

    hide joana smug2
    with fade

    p "(Já estou vendo que se não passar tudo terá sido em vão.)"
    
    p "(O que será ela quis dizer com grandes planos?)"
    
    p "(Bem, não importa. Penso nisso depois da prova.)"

    # "" "Thomas forjou uma aliança com Joana"
    $ alianca_joana = 1

    jump caminhoQ2_11_derivado_principal

label caminhoQ2_9_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_luan.mp3" fadein 1.0 volume 0.3
    show luan smirk

    p "Esquece, não adianta tentar convencer alguém como você."

    lu "Ah cara. Você só sabe me encher!"

    show luan angry2

    lu "Some da minha frente vai!"

    p "Com prazer."

    hide luan angry2
    with fade

    p "(Cara, que perda de tempo.)"

    p "(Tô cansado disso já.)"

    p "(Chega de acordos, chega de alianças, chega de conversas.)"

    p "(Eu só quero terminar minha prova e ir embora.)"


    jump caminhoQ2_11_derivado_principal

label caminhoQ2_10_derivado_principal:
    stop music fadeout 1.0
    play music "audio/tema_dialogo_lindsey_ou_conversa_profunda.mp3" fadein 1.0 volume 0.3
    p "Não, não é nada."
    p "Era uma pergunta idiota."
    p "O tempo tá quase acabando, é melhor eu ir terminar minha prova."
    p "Mas a gente pode conversar depois."

    show lindsey smile

    l "Ah, claro! Tudo bem."
    l "Boa sorte!"
    p "Pra você também!"

    hide lindsey smile 
    with fade

    p "(Acho que é melhor assim. Eu não preciso da resposta da Joana.)"
    p "(Vou voltar para minha carteira e responder eu mesmo!)"

    jump caminhoQ2_11_derivado_principal

label caminhoQ2_11_derivado_principal:
    play music "audio/tema_protagonista_pensando_respondendo_questoes.mp3" fadein 1.0 volume 0.3
    scene bg caderno
    with fade


    p "(Tá certo. Hora de rever as perguntas antes de entregar.)"

    if(question_2_thomas  == 'Certa'):
        jump caminhoQ2_13_derivado_principal
 

label caminhoQ2_12_derivado_principal:
    "Questão" "... como acessar fragmentos de código, a partir do código fonte de um programa?"

    menu:
        "Rotina de Serviço":
            $ question_2_thomas  = 'Errada'
        "Chamada de Sistema":
            $ question_2_thomas  = 'Errada'
        "Gerência de memória":
            $ question_2_thomas  = 'Errada'
        "Uso de função":
            $ question_2_thomas  = 'Certa'

label caminhoQ2_13_derivado_principal:

    if(question_3_thomas  == 'Certa'):
        jump caminhoQ2_14_derivado_principal

    "Questão" "... que método é usado para executar dois ou mais programas diferentes em um processador de 1 só núcleo e sem pipeline, porém dando ao usuário a impressão de que todos eles são executados ao mesmo tempo?"
    menu:
        "Escalonamento":
            $ question_3_thomas  = 'Certa'
        "Confinamento":
            $ question_3_thomas  = 'Errada'
        "Sobreposição":
            $ question_3_thomas  = 'Errada'
        "Cooperação":
            $ question_3_thomas  = 'Errada'

label caminhoQ2_14_derivado_principal:
    p "(Ok, todas as questões estão resolvidas.)"
    p "(Eu só espero que estejam corretas.)"
    p "(Vou entregar a prova logo. Não aguento mais ficar aqui.)"

    if(question_1_thomas == 'Certa' and question_2_thomas == 'Certa' and question_3_thomas == 'Certa'):
        stop music fadeout 1.0
        jump final_completo_1
    else:
        stop music fadeout 1.0
        jump finais_curtos_1

label final_completo_1:

    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3

    scene bg empresa
    with fade

    "" "Uma semana depois do teste, na empresa da TeslaTech..."


    show instrutor smile1

    i "Bom dia a todos!"
   
    i "Primeiramente, eu quero parabenizar todos os novos funcionários que passaram de nosso teste!"
    
    i "Vocês mostraram ter uma mente aberta a possibilidades, sendo ao mesmo tempo focada no objetivo, calma, inteligente e perceptiva."
    
    i "Então, sem mais delongas, eu quero apresentar nossos novos funcionários deste ano a todos..."

    hide instrutor smile1 
    with fade

    if(question_2_jean == 'Certa' and question_3_jean == 'Certa'):
        show jean smile3
        with fade
        i "Jean Portiolli, ..."

        hide jean smile3
        with fade

    #Inserir Joana na tela.

    show joana delighted2
    with fade
    i "Joana Olympios, ..."

    hide joana delighted2
    with fade

    if(question_3_lindsey == "Certa" and question_2_lindsey == "Certa"):
        show lindsey delighted2
        with fade
        i "Lindsey Spears, ..."
        hide lindsey delighted2
        with fade
    
    show instrutor smile1

    i "E Thomas O’Hara!"
    i "Fico muito feliz que todos vocês tenham passado."
    i "Bem vindos à TeslaTech!"
    i "Agora que foram todos devidamente apresentados."
    i "Podem ir em seus devidos lugares. O almoço começa às 11:00."

    hide instrutor smile1
    with fade

    p "(Nossa, quanta sensibilidade...)"
    p "(Mas tudo bem, eu estou feliz por ter passado.)"
    p "(E pelo visto eu não fui o único.)"
    p "(Ai ai, eu só espero não me meter em problemas...)"

    scene bg empresa
    with fade

    "" "Mais tarde, durante o almoço."
    p "(Aaaaahh FINALMENTE! Estou exausto.)"
    p "(Com esse primeiro dia eu tenho até medo dos próximos...)"
    jo "Com licença, Thomas?"
    p "Hum?"

    show joana

    jo "Tudo bem se eu tomar um pouco do seu tempo? Só preciso de 1 minuto."
    p "Ah, claro! Tudo bem."

    if(alianca_joana == 1):
        jump final_completo_1_1

    p "(Contra meu bom senso...)"
    jo "Obrigada."
    jo "Bom, indo direto ao assunto."
    jo "Para mim ficou bem claro que você preferiu não forjar uma aliança comigo."
    jo "Eu não sei quais foram seus motivos, e lhe adianto que eles não me interessam."
    p "(Delicada como sempre...)"
    jo "O que me interessa é que você não está comigo."
    show joana angry
    jo "E o que te interessa, é que quando alguém não está comigo, está contra mim."
    jo "Então, sinto-me na obrigação de avisa-lo, que não deixarei sua vida aqui ser fácil."
    jo "Na verdade, recomendo desista da vaga agora, pelo seu bem."
    jo "Vai ser a última chance que te darei."
    jo "Então, se vier amanhã, saiba que não terá paz."
    jo "Eu vim para vencer, não para fazer amigos."
    jo "Prefiro não me aprofundar nos detalhes de como farei tudo isso."
    jo "O que eu quero saber agora é..."
    jo "Você entendeu bem?"
    p "Ah... Claro, eu entendi."
    p "E você entende que ameaçar pessoas é crime, não entende?"
    jo "Oh, não não não. Por favor, não deixe sua simples mente confundir os fatos."
    jo "Isto, agora, não foi uma ameaça."
    jo "Você vai saber quando eu estiver te ameaçando."
    jo "Por enquanto, eu diria que..."
    jo "Você foi avisado..."
    hide joana angry
    with fade
    p "(Espera, por acaso ela acabou de...)"
    p "(Eu vou fingir que não ouvi a última parte.)"
    p "(Incrível como meu único pedido para este dia acabou de ser desconstruído.)"
    p "(Mas até parece que eu vou simplesmente desistir de tudo depois de todo o trabalho que me deu.)"
    p "(Além do mais, ela de estar blefando.)"
    p "(Eu acho.)"
    p "(Eu espero.)"
    p "(Aaaaaaaah...)"
    p "(É o primeiro dia e eu já estou tendo arrependimentos.)"


    if(question_2_lindsey != "Certa" or question_3_lindsey != "Certa"):
        jump final_completo_1_2


    l "Oi, Thomas!"
    p "Hum?"

    show lindsey smile

    l "Como você está?"
    p "Lindsey! Oi."
    p "Ah, honestamente. Já estou com cansado."

    show lindsey delighted2

    l "Kkkkk entendo. Também achei um tanto puxado."
    show lindsey smile

    l "Mas, eu tenho a impressão que não é por causa disso, néh?"
    p "Como você sabe?"
    show lindsey angry
    l "Ah, eu vi aquela cretina falando com você. Então já supus que não seria coisa boa."
    p "Acertou em cheio."
    p "A verdade é que ela não gostou nem um pouco de ter negado a aliança dela."
    p "Então, ela veio aqui me “avisar” e dar certeza que ela será minha “inimiga”."
    l "Rumpf. Que egocêntrica."
    l "Ela realmente levou essa “aliança” ridícula a sério."
    p "Pois é."
    show lindsey normal
    l "Você devia gravar suas conversas com ela com o celular."
    l "Alguma hora ela iria deixar escapar alguma coisa que você poderia usar contra ela."
    p "Não é uma má ideia."
    p "Se eu pegar ela me ameaçando eu posso levar pra polícia e denunciar ela."
    l "Esse é a ideia!"
    p "Obrigado pela ajuda."
    l "Sem problemas."
    p "..."
    l "...."
    p "....."
    l "... Éeeee então."
    p "Sim?"
    show lindsey smug
    l "Se você quiser, a gente pode se encontrar mais tarde."
    l "Sei lá, comer alguma coisa, para comemorar."
    p "Claro! Seria ótimo."

    show lindsey surprised
    l "Tá marcado então! Eu te mando mensagem depois pra acertar."
    l "Hora eu tenho que comer. Preciso descansar um pouco kkk."
    show lindsey normal
    p "Aaahh, nem me diga kkkk. "
    p "Claro, pode ir. Eu vou ficar um pouco aqui ainda."
    l "Tá certo. Até depois."
    l "Até."

    hide lindsey normal
    with fade

    p "(Bem, nem tudo são espinhos eu acho.)"
    p "(Minha relação com a Lindsey tá cada vez melhor.)"
    p "(Nós conversamos quase a noite toda ontem.)"
    p "(Acho que estamos muito ansiosos com hoje para conseguir dormir.)"
    p "(Me ajudou a relaxar um pouco.)"
    p "(É bom falar com ela...)"
    p "(ENFIM! Chega de ficar pensando nisso.)"
    p "(Vai ser um dia cheio e eu preciso comer.)"

    jump final_completo_1_2


label final_completo_1_1:
    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3
    show joana smile

    jo "Obrigada."
    jo "Bom, indo direto ao assunto."
    jo "Eu fico feliz que você tenha aceitado minha aliança."
    jo "Porque agora podemos ajudar um ao outro aqui dentro."
    jo "Além disso, eu já criei algumas ideias que podem nos levar ao topo daqui rapidinho."
    jo "Mas para isso, precisamos de alguns contatos."
    jo "Então, eu espero poder contar com você para me ajudar a pesquisar o que precisamos e a firmar algumas “amizades” por aqui."
    p "Ah... Tudo bem. Não me parece muito absurdo."
    jo "Oh, não precisa ficar tenso desse jeito!"
    jo "Tudo o que fizermos será inofensivo, e dentro da lei."
    show joana smug
    jo "Bem, mais um do que o outro."
    p "Desculpe, como disse?"
    show joana
    jo "Ah, não se preocupe com isso agora."
    jo "Estamos nos primeiros dias afinal, por enquanto é melhor mantermos a discrição e sermos funcionários produtivos. "
    p "(Como assim manter a discrição?)"
    jo "Bem, por enquanto é só isso."
    jo "Eu entro em contato depois."
    jo "E, Thomas?"
    p "Sim?"
    jo "Não me decepcione, tenho grandes planos para nós."

    hide joana

    p "(Meu Deus...)"
    p "(Essa mulher me dá arrepios.)"
    p "(E o que ela quis dizer com “ter grandes planos para nós”?)"
    p "(...)"
    p "(Ai ai, já tô com dor de cabeça.)"
    p "(Acho que me meti em algo que não devia...)"
    p "(Bem, é melhor eu ir comer logo.)"
    p "(O dia vai ser cheio.)"

    jump final_completo_1_2


label final_completo_1_2:
    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3
    if(question_2_jean == 'Errada' or question_3_jean == 'Errada'):
        jump final_completo_1_3


    "" "Thomas segue em direção à porta do prédio."
    "" "Quando chega lá, se encontra com Jean."

    show jean smile1

    p "Eae mano."
    j "Eae cara."
    p "Nossa que canseira, nem parece primeiro dia."

    show jean normal
    j "Nem me fala."

    show jean smirk
    j "Pelo menos você tem uma donzela para te acalmar neste momento de necessidade."
    p "Ah cala boca, não é nada disso."

    show jean smile2
    j "Já pensei que você não ia vir mais, que iria me deixar aqui, sozinho e desamparado. "
    j "E acima de tudo..."
    j "Cheio de FOME..."
    p "Me poupa, drama queen."
    p "Já que você esperou tanto, pelo menos já decidiu o que comer?"
    j "Sei lá, tem um restaurante aqui perto."
    j "Vamô olhar lá."
    p "Bora então."

    hide jean smile2

label final_completo_1_3:
    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3
    scene bg fora
    with fade

    "" "O dia de trabalho termina e Thomas caminha de volta para casa."
    p "(Meu Deus, que dia.)"
    p "(Cansativo, complicado e principalmente...)"
    p "(LONGO!)"
    p "(Mas apesar de tudo, foi bem interessante.)"
    p "(Eu só espero não me meter em problemas por causa da Joana.)"
    p "(Tenho que tomar cuidado.)"
    if(question_2_jean == 'Errada' and question_3_jean == 'Errada'):
        p "(É uma pena que o Jean não tenha passado.)"
        p "(Eu ficaria mais tranquilo com ele por perto.)"
        p "(Porque, apesar de tudo, ele sempre tá do meu lado.)"
        p "(É melhor eu mandar mensagem depois; ver como ele tá.)"
    p "(Mas enfim, quando eu chegar em casa eu penso nisso.)"
    p "(Por agora, eu só estou feliz que entrei.)"
    p "(Finalmente uma coisa para eu ter orgulho.)"
    if((question_2_lindsey != 'Certa' or question_3_lindsey != 'Certa') and lindsey_friendship > 0 ):
        jump final_completo_1_4
    stop music fadeout 1.0
    jump play_again
    return

label final_completo_1_4:
    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3
    play sound "audio/toque_celular.mp3" fadein 1.0 volume 0.3
    p "(Hum, uma notificação do Instagram?)"
    p "(... Mensagem de “@lynd.spears”... Quem?)"
    p "(... AH, LINDSEY!)"
    l "Bom dia, Thomas."
    l "Então, eu não sei se você passou no teste ou não."
    l "No meu caso, não kkkk."
    l "Mas, bem, independente disso."
    l "Você me ajudou durante o teste."
    l "Além do que você parece um cara legal."
    l "Então, como um agradecimento."
    l "Eu pensei se a gente não podia sair para comer, sei lá."
    l "Por minha conta!"
    l "Viu que bom negócio? Kkkk"
    l "Mas, olha, é só dessa vez em?"
    l "Não se acostume mal."
    l "ASSIM, não querendo dizer que vão outras vezes, eu só..."
    l "ENFIM!"
    l "Espero você me retornar, pra gente definir o local, data, hora, essas coisas."
    l "Se você quiser! É claro, não estou te obrigando de forma alguma."
    p "(Uau, isso é... Bem legal.)"
    p "(É realmente uma pena que ela não passou.)"
    p "(Com a Joana lá, eu iria gostar de ter mais alguém com quem contar.)"
    p "(De toda forma, ela parece muito gente boa.)"
    p "(Eu que não vou desperdiçar essa chance!)"
    p "(Até porque é comida de graça...)"

    stop music fadeout 1.0
    jump play_again
    return

label final_desclassificado:

    scene bg black
    stop music fadeout 1.0

    "" "Thomas parte para cima do homem. Dando um soco surpresa na cara."
    "" "Luan revida com outro soco no rosto, e ambos começam uma briga."
    "" "Não demora muito para aparecerem seguranças, que seguram os dois enquanto os levam para fora da sala."
    "" "Thomas e Luan foram desqualificados."

    play music "audio/tema_durante_finais_completos.mp3" fadein 1.0 volume 0.3
    scene bg fora
    with fade
    #Aqui coloca o fundo de uma praça ou algo parecido, por que o Jean vai estar andando e conversando com o Thomas.
    "" "Alguns dias depois do teste..."

    show jean surprised
   
    j "Caaaara que loucura! Nem acredito que você fez aquilo."
    p "Ah mano, não enche faz favor."
    show jean normal
    j "Não, você me desculpa, mas, bater em um cara."
    j "No meio de um teste."
    j "E ser desqualificado."
    j "Por causa de mulher?"
    p "Eu não a ajudei por ser uma mulher, ok? "
    p "Eu ajudei porque ela precisava e ninguém ia fazer nada se eu não fizesse."
    p "Só isso."
    j "Taaaa booom. Entendi."
    j "Parei."
    p "Obrigado!"
    j "..."
    p "...."
    j "....."
    p "......"

    show jean smirk
    j "Gado."
    p "AH! AGORA EU SOU O GADO?"
    p "Esqueceu que foi tu que deu a resposta pra Joana de bobeira?"

    show jean smile1
    j "Olha só, em minha defesa..."
    p "Lá vem..."
    j "Não não, escuta só."
    j "Eu sei que parece idiota ter dado a resposta..."
    p "E foi."
    j "EU NÃO TERMINEI..."

    j "Maaaaass, se você tivesse ouvido como ela falou comigo..."
    p "Ai meu Deus..."
    j "É SÉRIO CARA, TÔ TE FALANDO! O TOM SABE?"
    p "Você é um idiota."
    j "Olha, nenhum de nós conseguiu o emprego de qualquer jeito."
    j "Deixa o passado enterrado e segue em frente."
    p "Foi você que puxou o assunto de volta animal."
    j "Eeeeee eu estou dizendo para terminar com ele agora."
    j "Não parece justo?"
    j "Terminar o que começou?"
    p "..."
    j "...."
    p "Tá, tanto faz."
    j "Beleza então."
    play sound "audio/toque_celular.mp3" fadein 1.0 volume 0.3
    p "Ah, pronto! O que é agora?"
    p "..."
    j "E aí? Que foi?"
    j "Tá com uma cara de cachorro com fome."
    p "É... Uma mensagem... no Instagram."
    j "... E? De quem? Da sua mãe?"
    show jean smile3
    p "É da Lindsey."

    show jean surprised
    j "É O QUE AMIGO?"
    j "DEIXA VER ISSO!"

    show jean smile1
    p "PERAI CARA, CALMA AI, NEM EU LI AINDA."
    l "Bom dia, Thomas."
    l "Então, eu não sei bem por que você fez aquilo durante o teste."
    l "Foi bem idiota se você perguntar para mim..."
    l "Mas, bem eu não estou aqui para te criticar."
    l "Querendo ou não, você me ajudou fazendo aqui."
    l "Então, como um agradecimento."
    l "Eu pensei se a gente não podia sair para comer, sei lá."
    l "Por minha conta! Claro kkk."
    l "É um agradecimento afinal eu não te chamaria se você precisasse pagar pela comida."
    l "ENFIM!"
    l "Espero você retornar, pra gente definir o local, data e hora."
    l "Se você quiser! É claro, não estou te obrigando de forma alguma."
    p "..."
    j "..."
    p "..."

    show jean surprised
    j "Cara..."
    p "Pois é..."
    j "Quem diria que a sua estratégia da idade média fosse dar certo."
    p "Ai eu mereço."
    j "Não, cara, sério."

    show jean smirk
    j "Meus parabéns."
    p "EU NÃO FIZ AQUILO PENSANDO EM RECOMENPENSA NENHUMA."
    j "Tá. Tá bem."
    p "É sério!"

    show jean smile1
    j "Uhrum, não tudo bem."
    j "Eu acredito."
    p "..."
    j "Mas você vai, não é?"
    p "É claro que eu vou, você acha que eu sou idiota?"
    j "Kkkkkkkkkk um verdadeiro princesso do pau oco."
    p "É “Santo”, “Santinho do pau oco”."
    j "Ah, então você concorda?"
    p "Não! Cara..."
    p "Só..." 
    p "Cala boca."
    j "Kkkkkk tudo bem."
    j "... Por enquanto."
    stop music fadeout 1.0
    jump play_again
    return
