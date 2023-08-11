import pandas as pd


carros_data = {
    'Carro': ['Onix', 'Polo', 'Fiesta', 'City', 'Sandero'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}

carros_df = pd.DataFrame(carros_data)

montadoras_data = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']
}

montadoras_df = pd.DataFrame(montadoras_data)


carros_df.to_csv('carros.csv', index=False)
montadoras_df.to_csv('montadoras.csv', index=False)
