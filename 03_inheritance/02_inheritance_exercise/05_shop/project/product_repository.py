from project.product import Product
from typing import List


class ProductRepository:
    products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for product in ProductRepository.products:
            result.append(f"{product.name}: {product.quantity}")
        return '\n'.join(result)
