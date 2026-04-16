# 5. O Script de Seleção Inteligente
# Contexto: Você precisa buscar dados, mas quer que o Python te entregue algo mais útil que uma simples tupla.

# Tarefa: Configure o row_factory = sqlite3.Row. Faça um SELECT * na sua tabela de clientes.

# Ação: Percorra o resultado com um for e imprima uma frase formatada usando as chaves: f"O cliente {row['nome']} usa o email {row['email']}".
