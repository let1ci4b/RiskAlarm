"""
PROGRAM: Risk Alarm
author: Leticia Beatriz Souza
created: 2025.05.09
description:
    Simula um sistema de alarme de risco com perceptron simples.
    Classifica situações de risco com base em entrada de sensores:
    gás, temperatura e movimento.
"""

from random import randint, seed
from time import time


class RiskPerceptron:

    def __init__(self): 
        seed(time()) # inicializa o gerador de numeros aleatorios com base no tempo atual
        self.learning_rate = 0.1 # taxa de aprendizado (quao rapido os pesos sao ajustados)
        self.epoch = 300 # numero maximo de ciclos de treinamento (passagens pelo conjunto de dados)
        self.weights = [randint(1, 100) / 100.0 for _ in range(4)]  # inicializa os pesos com valores aleatorios entre 0.01 e 1.00

        # Exemplo: [bias, gas, temp, mov, risco]
        self.examples = [
            [-1, 0, 0, 0, 0],
            [-1, 1, 0, 0, 1],
            [-1, 0, 1, 0, 1],
            [-1, 0, 0, 1, 1],
            [-1, 1, 1, 1, 1],
            [-1, 1, 1, 0, 1],
            [-1, 0, 1, 1, 1],
            [-1, 1, 0, 1, 1],
            [-1, 0, 0, 0, 0],
        ]

    def adjust_weights(self, index, output):

        """ajusta os pesos do perceptron se a saida estiver errada"""

        for i in range(4): # para cada entrada (bias, gas, temp, mov)
            xi = self.examples[index][i] # valor da entrada
            desired = self.examples[index][4] # saida esperada (0 ou 1)
            self.weights[i] += self.learning_rate * (desired - output) * xi  # regra de aprendizagem do perceptron

    def activation(self, gas, temp, mov):

        """Calcula a saída do perceptron com base nas entradas"""

        x = [-1, gas, temp, mov] # inclui o bias fixo -1 como entrada
        total = sum([x[i] * self.weights[i] for i in range(4)]) # soma ponderada das entradas
        return 1 if total > 0 else 0 # 1 se soma > 0, senão 0

    def train(self):

        """treina o perceptron com os exemplos ate acertar todos ou atingir o limite de epochs"""

        for epoch in range(self.epoch): # tenta varias rodadas de treino
            trained = True

            for i in range(len(self.examples)):
                gas = self.examples[i][1]
                temp = self.examples[i][2]
                mov = self.examples[i][3]
                output = self.activation(gas, temp, mov) # previsao da rede

                if output != self.examples[i][4]: # se estiver errado
                    self.adjust_weights(i, output) # ajusta os pesos
                    trained = False

            if trained: # se nenhum erro foi cometido nesta rodada
                print(f"Trained in {epoch + 1} epochs.") # mostra sucesso
                return True
            
        print("Could not train within limit.") # falha apos 300 tentativas
        return False


def run_alarm(perceptron: RiskPerceptron):

    """Executa o sistema de alarme interativo com o usuário"""

    while True:
        print("\nEnter sensor values (0 or 1) or 'exit' to quit.")
        try: # coleta os dados de entrada dos sensores
            gas = input("Gas detected (1=yes, 0=no): ").strip().lower()
            if gas == "exit":
                break
            temp = input("High temperature (1=yes, 0=no): ").strip().lower()
            if temp == "exit":
                break
            mov = input("Movement detected (1=yes, 0=no): ").strip().lower()
            if mov == "exit":
                break

            # converte entradas para inteiros    
            gas = int(gas)
            temp = int(temp)
            mov = int(mov)

            # valida os dados
            if gas not in [0, 1] or temp not in [0, 1] or mov not in [0, 1]:
                raise ValueError()

            # usa o perceptron para prever se ha risco
            result = perceptron.activation(gas, temp, mov)
            print("⚠️  RISK ALARM!" if result == 1 else "✅ Safe environment.")

        except ValueError:
            print("Invalid input. Use only 0 or 1, or type 'exit'.")


def main():

    """Função principal que treina e executa o sistema"""

    print("=== RISK ALARM ===")
    perceptron = RiskPerceptron() # cria o perceptron
    print("Training perceptron...")
    if perceptron.train(): # tenta treinar o modelo
        run_alarm(perceptron) # executa o sistema interativo
    print("Program closed.")


# executa o programa se for rodado diretamente (nao importado)
if __name__ == "__main__":
    main()
