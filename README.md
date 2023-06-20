# MelbourneProject

Este projeto apresenta uma análise exploratória da Base de dados, Modelos ML para previsão de preços de casas e uma API em flask para consumir este modelo. A base de dados são características de imóveis disponiveis em Melbourne, capital costeira do estado de Victoria, no sudeste da Austrália.

## Definição do Problema

Vamos realizar uma limpeza e análise exploratória na base de dados imobiliários em Melborn, Austrália. Em seguida, iremos treinar um modelo de regressão e implementar uma API para consumo deste modelo.

## Dataset: [kaggle-melbourne-housing](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot?select=melb_data.csv)
---
## Estrutura:

- [`data`](./data): diretório com os dados em csv.

- [`model`](./model): diretório com os dados dos modelos e pré-processamento.

- [`model_api`](./model_api): main.py que contém a API em flask.

- [`notebooks`](./notebooks): Notebooks que contém a EDA, Modelos e Teste de Produção.

    - [`eda.ipynb`](./notebooks/eda.ipynb): Jupyter notebook contendo a análise exploratória dos dados

    - [`ml.ipynb`](./notebooks/ml.ipynb): Jupyter notebook contendo o modelo e testes da regressão e árvore de decisão dos dados tratados
    
    - [`prod.ipynb`](./notebooks/prod.ipynb): Jupyter notebook contendo testes do modelo para produção 

- [`requirements.txt`](./requirements.txt): arquivo com bibliotecas utilizadas no projeto.
---
## Descrição da Base

1. **Rooms**: Número de quartos  
2. **Price**: Preço em dólares  
3. **Method**: S - imóvel vendido; SP - imóvel vendido anteriormente; PI - imóvel não vendido; PN - vendido anteriormente e não divulgado; SN - vendido e não divulgado; NB - sem oferta; VB - oferta do vendedor; W - retirado antes do leilão; SA - vendido após o leilão; SS - vendido após o leilão, preço não divulgado. N/A - preço ou maior oferta não disponível.  
4. **Type**: br - quarto(s); h - casa, chalé, vila, semi, terraço; u - unidade, duplex; t - casa de cidade; terreno de desenvolvimento; o res - outros residenciais.  
5. **SellerG**: Agente imobiliário  
6. **Date**: Data da venda  
7. **Distance**: Distância do centro da cidade  
8. **Regionname**: Região geral (Oeste, Noroeste, Norte, Nordeste ... etc)  
9. **Propertycount**: Número de propriedades existentes no subúrbio.  
10. **Bedroom2**: Número de quartos (obtido de outra fonte)  
11. **Bathroom**: Número de banheiros  
12. **Car**: Número de vagas de estacionamento  
13. **Landsize**: Tamanho do terreno  
14. **BuildingArea**: Tamanho da construção  
15. **CouncilArea**: Conselho governante para a área  

---

## Uso

1. Clone este repositório
2. Mude para dentro da pasta usando `cd`
3. Instale os requerimentos via `pip`

```bash
pip install requirements.txt
```
4. Mude para dentro da pasta da API usando 
```bash
cd model_api
```
5. Execute a API
```bash
python main.py
```
6 O Flask indica qual porta em localhost a API estará disponível para consumo. Esta é uma API de desenvovimento.


