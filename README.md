# Análise de dados da plataforma QuintoAndar
No presente projeto, realizei o webscrapping para coletar de dados da plataforma Quinto Andar, correspondentes a anúncios de imóveis para alugar na cidade de São Paulo.
Os dados colhidos foram: URL do anúncio, valores (aluguel, condomínio, iptu, seguro incêndio, taxa de serviço e valor total), metragem (m²), número de quartos, banheiros, vagas de carro, andar, se aceita pet, se há mobília, e se é próximo ao metrô.

Foram colhidos os dados de 2.778 anúncios da cidade de São Paulo.

Após a coleta dos dados, foi realizado o tratamento dos mesmos, deixando-os prontos para a análise estatística descritivas. Algumas perguntas que pretendo responder na etapa analítica:
- O quanto cada uma das features interfere no preço do aluguel;
- Quais interferem mais.

Os dados serão agrupados por bairro, pois bairros diferentes possuem valores/comportamentos diversos:
- Será encontrada a mediana de cada agrupamento;
- Os anúncios que tiverem um valor menor do que a mediana serão interpretados como lucrativos. 
- O valor será obtido dividindo o preço total do aluguel pelo número da metragem (em m²). Ou seja, será considerado o valor por m².
- O valor de lucro do imóvel será obtido através da diferença entre o valor da mediana no bairro e o valor do imóvel.

Após ter a resposta acima, pretendo treinar um modelo, para analisar e prever o preço do aluguel em dados presentes no corpus de teste e em novas entradas.
