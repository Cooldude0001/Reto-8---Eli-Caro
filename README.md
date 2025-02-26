# 🍽Reto 8 -  Eli Caro
Para este ejercicio se requirió del uso del código del reto 3 _restaurant_case_, para implementar una nueva clase que itere con todos los elementos de una orden, que pueda ingresar a estructuras ciclicas como `for` y contenga todos los atributos de los elementos de la orden.

## Ejemplo de uso
```python
# Usage example
client_order = Order()

# Items
client_order.add_menuitems_to_bill(Beverage("Coke", 2.5, "Large"))
client_order.add_menuitems_to_bill(Appetizer("Spring Rolls", 5.0, "medium"))
client_order.add_menuitems_to_bill(
    Maincourse("Spaghetti", 12.0).maincourse_accompanied(
        sauce="Bolognesa sauce", separated=False
    )
)

client_order.add_menuitems_to_bill(Beverage("Fanta", 2.5, "small"))
client_order.add_menuitems_to_bill(Appetizer("Sushi", 4.0, "small"))
client_order.add_menuitems_to_bill(Maincourse("Fried mojara", 15.00))

client_order.add_menuitems_to_bill(Beverage("Coke", 2.5, "Large"))
client_order.add_menuitems_to_bill(Appetizer("French fries", 3.5, "medium"))
client_order.add_menuitems_to_bill(Appetizer("Fried yucca", 4.0, "small"))
client_order.add_menuitems_to_bill(Maincourse("Lasagna", 20.0))

# Example of the iteration of Order class
for items in client_order:
    print(f"Item: {items}, Price: ${items.price:.2f}")
```
