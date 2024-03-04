# Atividade Computacional - Análise da Taxa de Pulsação em Repouso

Este projeto computacional visa automatizar a análise da taxa de pulsação em repouso de uma amostra de adultos com idades entre 30 e 35 anos, com o objetivo de avaliar a qualidade de vida dos colaboradores de uma empresa. A análise é baseada em dados coletados em uma pesquisa, disponibilizados no arquivo pulso.txt.

## Contexto

A taxa de pulsação em repouso é um indicador importante da saúde cardiovascular. Segundo a Sociedade de Cardiologia, a taxa de pulsação média ideal para pessoas nesta faixa etária é de 70 bpm (batimentos por minuto), com uma variação percentual aceitável de 11%.

## Objetivo

Desenvolver um programa de computador ou uma planilha eletrônica que:

1. Calcule o valor médio ou provável da taxa de pulsação da amostra.
2. Verifique se o valor provável da amostra está dentro do intervalo indicado pela Sociedade de Cardiologia.
3. Apresente a diferença em porcentagem entre o valor medido e o padrão da Sociedade de Cardiologia para cada funcionário da amostra.
4. Indique se a taxa de pulsação de cada funcionário está dentro do intervalo aceitável, abaixo ou acima do indicado.
5. Quantifique os funcionários dentro do padrão aceitável, acima e abaixo, e plote esses resultados em um gráfico de colunas.

## Fórmulas

- **Erro Absoluto (EA):** |Valor Medido - Valor Padrão|
- **Erro Relativo (ER):** (|Valor Medido - Valor Padrão| / Valor Padrão) * 100%

## Critérios de Avaliação

1. Organização das ideias e sequências de cálculos.
2. Resultados corretos.
3. Funcionamento adequado do programa computacional.

## Como Executar
*Versão do python utilizada 3.11.7*

1. Crie uma venv
    ```python
    python -m venv .venv
    ```

2. Ative a venv

3. Instale as dependecias utilizando o comando a seguir
    ```python
    pip install -r requirements.txt
    ```

4. Execute o script
    ```python
    python main.py
    ```