#match, case

number = 9 
match number:
    case 1: 
        print("vegan food")
    case 2:
        print("vegetarian food")
    case 3:
        print("meat food")
    case _:
        print("any food")

N = 6
match N:
    case 0:
        print("N is zero")
    case n if n > 0:
        print("N is positive")
    case n if n < 0:
        print("N is negative")
    case _:
        print("N is not a number")

imc = 20
match imc:
    case value if 0 < value < 18.5:
        print("underweight")
    case value if 18.5 < value <= 29.9:
        print("normal weight")
    case value if 30 <= value <= 34.9:
        print("obesity I")
    case value if 35 <= value <= 39.9:
        print("obesity II")
    case value if 40 <= value:
        print("obesity III")
    case _:
        print("IMC is not a number")