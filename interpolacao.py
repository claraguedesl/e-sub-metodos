from collections.abc import Sequence
from math import isfinite


def interpolacao_lagrange(pontos: Sequence[tuple[float, float]], x: float) -> float:
    if not pontos:
        raise ValueError("Informe pelo menos um ponto.")
    if not isfinite(x):
        raise ValueError("x deve ser um numero finito.")

    for ponto in pontos:
        if len(ponto) != 2:
            raise ValueError("Cada ponto deve conter um par (x, y).")
        if not isfinite(ponto[0]) or not isfinite(ponto[1]):
            raise ValueError("As coordenadas dos pontos devem ser finitas.")

    xs = [ponto[0] for ponto in pontos]
    if len(set(xs)) != len(xs):
        raise ValueError("Os valores de x dos pontos devem ser distintos.")

    resultado = 0.0
    for i, (xi, yi) in enumerate(pontos):
        base = 1.0
        for j, (xj, _) in enumerate(pontos):
            if i != j:
                base *= (x - xj) / (xi - xj)
        resultado += yi * base

    if not isfinite(resultado):
        raise ValueError("O resultado da interpolacao nao e finito.")
    return resultado


def ler_ponto(indice: int, quantidade: int) -> tuple[float, float]:
    while True:
        texto = input(
            f"Ponto {indice} de {quantidade} (digite x,y; exemplo: 0,1): "
        ).strip()
        if texto.startswith("(") and texto.endswith(")"):
            texto = texto[1:-1]

        coordenadas = texto.split(",")
        if len(coordenadas) != 2:
            print(
                "Formato invalido. Digite x e y separados por virgula, como 0,1."
            )
            continue

        try:
            return float(coordenadas[0].strip()), float(coordenadas[1].strip())
        except ValueError:
            print("Coordenadas invalidas. Use numeros, por exemplo: 0,1 ou (0,1).")


def main() -> None:
    print("Interpolacao polinomial pelo metodo de Lagrange")

    try:
        quantidade = int(input("Quantos pontos voce quer usar? "))
        if quantidade <= 0:
            raise ValueError("A quantidade de pontos deve ser positiva.")

        print(f"Digite {quantidade} ponto(s), um por linha.")
        print("Em cada linha, informe x,y. Exemplo: 0,1 (use ponto para decimais).")
        pontos: list[tuple[float, float]] = []
        for indice in range(quantidade):
            pontos.append(ler_ponto(indice + 1, quantidade))

        x_calculo = float(input("Informe o valor de x para interpolar: "))
        valor = interpolacao_lagrange(pontos, x_calculo)
    except (ValueError, OverflowError) as erro:
        print(f"Nao foi possivel calcular: {erro}")
        return

    print(f"Valor interpolado em x = {x_calculo:g}: y = {valor:.6f}")


if __name__ == "__main__":
    main()
