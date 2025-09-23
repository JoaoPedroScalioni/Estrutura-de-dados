from stack import Stack

class MinStack:
    def __init__(self):
        self.main_stack = Stack()
        self.min_stack = Stack()

    def push(self, data):
        self.main_stack.push(data)
        if self.min_stack.is_empty() or data <= self.min_stack.peek():
            self.min_stack.push(data)

    def pop(self):
        if self.main_stack.is_empty():
            raise IndexError("pop de uma pilha vazia")
        min_value = self.min_stack.peek()
        popped_value = self.main_stack.pop()
        if popped_value == min_value:
            self.min_stack.pop()
        return popped_value

    def get_min(self):
        if self.min_stack.is_empty():
            return None
        return self.min_stack.peek()
    
    def peek(self):
        return self.main_stack.peek()

    def is_empty(self):
        return self.main_stack.is_empty()

    def __str__(self):
        return str(self.main_stack)


if __name__ == "__main__":
    minha_pilha = MinStack()

    print("Adicionando: 10, 5, 20, 2")
    minha_pilha.push(10)
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)

    minha_pilha.push(5)
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)

    minha_pilha.push(20)
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)
    
    minha_pilha.push(2)
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)

    print("\nRemovendo o topo (2)...")
    minha_pilha.pop()
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)
    
    print("\nRemovendo o topo (20)...")
    minha_pilha.pop()
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)
    
    print("\nRemovendo o topo (5)...")
    minha_pilha.pop()
    print(f"Pilha atual: {minha_pilha}")
    print(f"Menor valor atual: {minha_pilha.get_min()}")
    print("-" * 20)