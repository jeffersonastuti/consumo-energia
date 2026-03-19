def calcular_consumo(potencia, horas_dia):
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    return consumo_mensal


def calcular_custo(consumo, valor_kwh=0.75):
    return consumo * valor_kwh


def main():
    print("=== Calculadora de Consumo de Energia ===\n")

    aparelho = input("Nome do aparelho: ")
    
    try:
        potencia = float(input("Potência (em watts): "))
        horas_dia = float(input("Horas de uso por dia: "))
    except ValueError:
        print("\nErro: digite apenas números válidos.")
        return

    consumo = calcular_consumo(potencia, horas_dia)
    custo = calcular_custo(consumo)

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo:.2f} por mês")


if __name__ == "__main__":
    main()