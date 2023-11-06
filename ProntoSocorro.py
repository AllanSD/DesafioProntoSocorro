import heapq
import random


fila_de_prioridades = []


def adicionar_paciente(nome, idade, prioridade):
    paciente = (prioridade, nome, idade)
    heapq.heappush(fila_de_prioridades, paciente)


def atender_proximo_paciente():
    if fila_de_prioridades:
        paciente = heapq.heappop(fila_de_prioridades)
        print(f"Atendendo paciente: {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")
        return paciente


def visualizar_fila():
    print("Fila de Pacientes:")
    for paciente in fila_de_prioridades:
        print(f"{paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")


def proximo_paciente():
    if fila_de_prioridades:
        paciente = fila_de_prioridades[0]
        print(f"Próximo paciente na fila: Nome: {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")


ultimos_pacientes_atendidos = []


def listar_ultimos_pacientes_atendidos():
    print("Últimos 5 pacientes atendidos:")
    for i, paciente in enumerate(reversed(ultimos_pacientes_atendidos)):
        print(f"{i+1}. {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")


def gerar_simulacao(numero_pacientes):
    for _ in range(numero_pacientes):
        nome = f"Paciente {random.randint(1, 100)}"
        idade = random.randint(1, 100)
        prioridade = random.randint(1, 10)
        adicionar_paciente(nome, idade, prioridade)


gerar_simulacao(10)

while True:
    print("\nMenu:")
    print("1. Atender próximo paciente")
    print("2. Visualizar fila de pacientes")
    print("3. Mostrar próximo paciente na fila")
    print("4. Listar últimos 5 pacientes atendidos")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        paciente_atendido = atender_proximo_paciente()
        if paciente_atendido:
            ultimos_pacientes_atendidos.append(paciente_atendido)
            if len(ultimos_pacientes_atendidos) > 5:
                ultimos_pacientes_atendidos.pop(0)
    elif escolha == "2":
        visualizar_fila()
    elif escolha == "3":
        proximo_paciente()
    elif escolha == "4":
        listar_ultimos_pacientes_atendidos()
    elif escolha == "5":
        break
    else:
        print("Escolha inválida. Tente novamente.")