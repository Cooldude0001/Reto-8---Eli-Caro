# Restaurant case
class MenuItem:
    """MenuItem class used to create restaurant dishes."""
    
    def __init__(self, name: str, price: float):
        """Initialize a MenuItem object with name and price parameters.

        - param name: Name of the MenuItem object.
        - param price: Price of the MenuItem object.
        """
        self.name = name
        self.price = price
   
    def total_price(self, quantity: int = 1) -> float:
        """Return a float data type of the MenuItem price.

        Calculus based on the quantity of the MenuItem, 1 by defalut.
        """
        return self.price * quantity
    
    def __str__(self):
        """Return a string representation of the MenuItem object."""
        return self.name


# Classes that inherit the class MenuItem  
class Beverage(MenuItem):
    """Beverage class inherit methods and attributes from MenuItem class."""
    
    def __init__(self, name: str, price: float, size: str):
        """Initialize a Beverage object with name, price and size parameters.

        - param name: Name of the Beverage object.
        - param price: Price of the Beverage object.
        - param size: Size of the Beverage object (small, medium, large).
        """

        super().__init__(name, price)
        self.size = size

    def __str__(self):
        """Return a string representation of the Beverage object."""
        return f"{self.name} ({self.size})"


class Maincourse(MenuItem):
    """Maincourse class inherit methods and attributes from MenuItem class."""
    
    def __init__(self, name: str, price: float):
        """Initialize a Maincourse object with name and price parameters.

        - param name: Name of the Maincourse object.
        - param price: Price of the Maincourse object.
        """

        super().__init__(name, price)
    
    def maincourse_accompanied(self, sauce: str, separated: bool = True) -> "Maincourse":
        """Returns a modified Maincourse instance with the sauce added to it.

        - param sauce: Indicates the sauce of the Maincourse object.
        - param separated: Specify if the sauce is served separetly of the 
        Maincourse object, True, by default.
        """
        if sauce != None and separated == True:
            self.name = f"{self.name} with {sauce} separately"
            return self
        elif sauce != None and separated == False:
            self.name = f"{self.name} with {sauce} on the plate"
            return self
        else:
            raise ValueError ("You must specify the sauce to add it.")
    
    def __str__(self):
        """Return a string representation of the Maincourse object."""
        return self.name


class Appetizer(MenuItem):
    """Appetizer class inherit methods and attributes from MenuItem class."""
    
    def __init__(self, name: str, price: float, portion_size: str):
        """Initialize a Appetizer object with name, price and portion_size parameters.

        - param name: Name of the Appetizer object.
        - param price: Price of the Appetizer object.
        - param portion_size: Portion size of the Appetizer object
        (small, medium, large).
        """

        super().__init__(name, price)
        self.portion_size = portion_size

    def __str__(self):
        """Return a string representation of the Appetizer object."""
        return f"{self.name} ({self.portion_size})"

# Definition of Order class iterator
class OrderIterator:
    def __init__(self, order: "Order"):
        """Initialize OrderIterator class with an Order instance to 
        be iterated."""

        self._order = order
        self._index = 0

    def __iter__(self):
        """Returns itself because it is the iterator."""
        return self

    def __next__(self):
        """__next__ defines the logic of the iteration."""
        if self._index < len(self._order.bill_items):
            item = self._order.bill_items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Definition of Order class
class Order:
    """Order class is used to create and calculate the bill."""
    def __init__(self):
        """Initialize an Order with an empty list of items."""
        self.bill_items = []
          
    def __iter__(self):
        """Returns the Iterator of the Order class."""
        return OrderIterator(self)
    
    def add_menuitems_to_bill(self, item: "MenuItem"):
        """Adds a MenuItem object to the order.

        - param item: A MenuItem instance to be added.
        """
        self.bill_items.append(item)
    
    def bill(self, discount: bool = False, discount_percentage: int = 0):
        """Returns the total bill with an optional discount (if any).

        - param discount: Whether to apply a discount.
        - param discount_percentage: Percentage of the discount.
        """
        self.total = float(0)
        
        for item in self.bill_items:
            self.total += item.total_price()
        
        if discount == False:
            return self.total
        else:
            return self.total - (self.total * (discount_percentage / 100))

    def __str__(self):
        """Return a string representation of the Order object."""
        return ", ".join(str(item) for item in self.bill_items)
    

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