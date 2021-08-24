# Análise de dados da plataforma QuintoAndar
Acesse aqui: https://analise-quinto-andar.herokuapp.com/

<img src="logo_quinto_andar.png" alt="quinto andar" width="800"/>

## O que realizei neste projeto:
- Realizei o webscrapping para coletar dados da plataforma Quinto Andar, correspondentes a anúncios de imóveis para alugar na cidade de São Paulo;
  - Os dados (features) colhidos foram: URL do anúncio, valores (aluguel, condomínio, iptu, seguro incêndio, taxa de serviço e valor total), metragem (m²), número de quartos, banheiros, vagas de carro, andar, se aceita pet, se há mobília, e se é próximo ao metrô.
- Foram colhidos os dados de 2.778 anúncios da cidade de São Paulo;
- Foi realizado o tratamento dos mesmos dados, deixando-os prontos para as análises estatística descritivas;
- A análise do _dataset_ tratado pode ser consultada clicando no arquivo **4_analise_exploratoria.ipynb**;
- Desenvolvi um website com gráficos interativos (utilizando o Streamlit), para que os dados sejam interpretados em sua totalidade e, também, especificando os bairros desejados;
- Realizei deploy para nuvem (utilizando o Heroku), podendo ser acessado de qualquer dispositivo conectado à internet: https://analise-quinto-andar.herokuapp.com/

## Algumas perguntas que pude responder na etapa analítica:
- Qual o comportamento dos dados do QuintoAndar para uma cidade metropolitana tal qual São Paulo;
  - A plataforma possui viés, pois a maior parte de seus imóveis estão localizados em bairros nobres.
- As features que mais interferem no valor final do aluguel são: bairro, número de banheiros, de quartos e a metragem (m²);
  - As três últimas features possuem coeficiente de correlação de Pearson de 0,7 (forte), influenciando diretamente o valor do imóvel;
  - A feature "bairro", porém, é a que decide maiormente qual será o preço final.
- A maior parte dos anúncios possuem apenas 1 quarto e 1 banheiro. 
  - Quão maior a quantidade dessas features, menor a quantidade de dados;
  - Quão maior a quantidade dessas features, maior o preço do imóvel.

## O que fiz na fase analítica e ainda posso disponibilizar no deploy:
- Agrupar dados por bairro (pois bairros diferentes possuem valores/comportamentos diversos);
- Será encontrada a mediana de cada agrupamento;
- Os anúncios que tiverem um valor menor do que a mediana serão interpretados como lucrativos;
- O valor será obtido dividindo o preço total do aluguel pelo número da metragem (em m²). Ou seja, será considerado o valor por m²;
- O valor de lucro do imóvel será obtido através da diferença entre o valor da mediana no bairro e o valor do imóvel.

## O que ainda não fiz:
- Treinar um modelo de Machine Learning, para analisar e prever o preço do aluguel em dados presentes no corpus de teste e em novas entradas.

# Acesse aqui o site para análise de dados do QuintoAndar: https://analise-quinto-andar.herokuapp.com/
