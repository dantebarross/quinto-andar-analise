# Análise de dados da plataforma QuintoAndar
No presente projeto, pretendo realizar webscrapping para coleta de dados da plataforma Quinto Andar, correspondentes a anúncios de imóveis para alugar na cidade de São Paulo.
Os dados desejados de cada anúncio são: valor do aluguel, valor do condomínio, nome do bairro, metragem (m²), número de quartos, banheiros, se há mobília, e se é próximo ao metrô.
Será inserido, manualmente (por não haver este dado no anúncio), de qual região é o imóvel anunciado.


Após a coleta dos dados, será realizado tratamento dos mesmos, deixando-os prontos para análise. Algumas perguntas que pretendo responder na etapa analítica:
- O quanto cada uma das features interfere no preço do aluguel;
- Quais interferem mais.

Após ter a resposta acima, pretendo treinar um modelo, para analisar o comportamento do preço do aluguel ao alterar as features do objeto.



# Webscrapping
Ao procurar por imóveis para alugar na cidade de São Paulo, foram encontrados cerca de 10.000 resultados. Os anúncios vão aparecendo conforme o scroll-down na página é feita. Para colher os links, será realizado o scroll-down até o fim, para então colher, através de informações HTML, o link de cada um.

O caminho do path para a URL de cada anúncio está apresentado abaixo:

//*[@id="app"]/div/main/section[2]/div[2]/div/div[1]/div[3]/div/div/a


/html/body/div[1]/div/main/section[2]/div[2]/div/div[1]/div[3]/div/div/a
