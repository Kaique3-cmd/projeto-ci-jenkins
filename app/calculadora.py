def somar(a: float, b: float) -> float:
    return a + b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não permitida.")
    return a / b
