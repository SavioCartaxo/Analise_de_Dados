import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E', 
                'Produto F', 'Produto G', 'Produto H', 'Produto I', 'Produto J'],
    'Vendas': [320, 580, 410, 700, 550, 640, 460, 300, 540, 450],
    'Data': pd.date_range(start='2023-04-01', periods=10, freq='D'),
    'Preço': [150, 220, 300, 180, 450, 90, 120, 60, 500, 200],
    'Categoria': ['Eletrônicos', 'Roupas', 'Alimentos', 'Eletrônicos', 'Roupas', 
                  'Alimentos', 'Eletrônicos', 'Roupas', 'Alimentos', 'Eletrônicos']
})

# Encontre os 3 produtos mais vendidos (pela quantidade de vendas).

t = data[['Vendas', 'Produto']]
t = t.sort_values('Vendas', ascending=False)
print(t.head(3))