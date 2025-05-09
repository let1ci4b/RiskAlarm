# 🔥 Risk Alarm

## ✍ Descrição
O **Risk Alarm** é um sistema de alarme de risco simples, baseado em um **perceptron**. O projeto simula um sistema de alarme que monitora sensores de **gás**, **temperatura** e **movimento** para determinar se há risco no ambiente.
Ele foi desenvolvido como um exercício para a Unidade Curricular "Inteligência Artificial", do curso Sistemas de Informação, na UNISUL.

O perceptron é treinado com dados de sensores para classificar uma situação como **segura** ou **de risco**, de acordo com os valores fornecidos pelos sensores.

## 🧠 Tecnologias Utilizadas
- **Python** (versão 3.x)
- Algoritmo de **Perceptron** (rede neural simples)

## ❓ Como Funciona
- O perceptron recebe entradas dos sensores (gás, temperatura e movimento), calcula a soma ponderada dos valores com pesos ajustáveis, e ativa o alarme se a situação for classificada como de risco.
- O modelo é treinado com exemplos de entrada e saída desejada e usa aprendizado supervisionado para ajustar os pesos dos sensores.
- Após o treinamento, o sistema permite a interação com o usuário, onde é possível fornecer valores de sensores e verificar se o alarme é disparado.

## 📥 Exemplos de Entrada
- **Gás detectado**: 0 (não), 1 (sim)
- **Temperatura alta**: 0 (não), 1 (sim)
- **Movimento detectado**: 0 (não), 1 (sim)

Com esses valores de entrada, o sistema classifica a situação e informa se o ambiente está seguro ou em risco.

## ⚙ Como Rodar o Projeto

### Requisitos
- **Python 3.x** instalado no seu sistema.

### Instalação
1. Clone o repositório ou baixe o código-fonte.
   
   ```bash
   git clone https://github.com/SEU-USUARIO/risk-alarm.git
