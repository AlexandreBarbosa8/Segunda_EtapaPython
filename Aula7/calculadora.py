import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    # Operações de apenas 1 número (Unárias)
    if operacao == "sqrt":
        if num1 < 0:
            return render_template(
                "calculadora.html",
                etapas="Erro: Raiz quadrada de número negativo.",
                resultados="Indefinido"
            )
        resultado = math.sqrt(num1)
        return render_template(
            "calculadora.html",
            etapas=f"√{num1}",
            resultados=resultado
        )

    # Operações de 2 números (Binárias)
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="Erro"
        )
    num2 = float(num2_valor)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2}"

    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2}"

    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2}"

    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas="Erro: Divisão por zero não é permitida.",
                resultados="Indefinido"
            )
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2}"

    elif operacao == "**":
        try:
            resultado = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2}"
        except OverflowError:
            return render_template(
                "calculadora.html",
                etapas="Erro: Resultado muito grande (estouro de memória).",
                resultados="Erro"
            )
        except ValueError:
            return render_template(
                "calculadora.html",
                etapas="Erro: Base negativa com expoente fracionário gera número complexo.",
                resultados="Indefinido"
            )

    elif operacao == "log":
        if num1 <= 0 or num2 <= 0 or num2 == 1:
            return render_template(
                "calculadora.html",
                etapas="Erro: O logaritmando (N1) e a base (N2) devem ser > 0. A base não pode ser 1.",
                resultados="Indefinido"
            )
        resultado = math.log(num1, num2)
        etapas = f"log_{{base {num2}}} ({num1})"

    else:
        return render_template(
            "calculadora.html",
            etapas="Operação inválida.",
            resultados="Erro"
        )

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado
    )
