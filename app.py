# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Saída formatada
print("\nAparelho:", aparelho)
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
