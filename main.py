class Geometria:
    def area_rectangulo(self, ancho: float, alto: float) -> float:
        return ancho * alto

    def perimetro_rectangulo(self, ancho: float, alto: float) -> float:
        return 2 * (ancho + alto)

    def area_cuadrado(self, lado: float) -> float:
        # Un cuadrado es un rectángulo con ambos lados iguales
        return self.area_rectangulo(lado, lado)

    def perimetro_cuadrado(self, lado: float) -> float:
        # Un cuadrado es un rectángulo con ambos lados iguales
        return self.perimetro_rectangulo(lado, lado)
