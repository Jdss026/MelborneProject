# MelbourneProject

Este projeto apresenta um Modelo ML para previsão de preços de casas com uma base de dados de imóveis disponiveis em Melbourne, capital costeira do estado de Victoria, no sudeste da Austrália.

:book: dataset: -https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot?select=melb_data.csv
---
### Estrutura:

-[`data`](./data): diretório com os dados em csv

-[`eda.ipynb`](./eda.ipynb): Jupyter notebook contendo a análise exploratória dos dados

-[`ml.ipynb`](./ml.ipynb): Jupyter notebook contendo o modelo e testes da regressão e árvore de decisão dos dados tratados
---
### Descrição da Base

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
