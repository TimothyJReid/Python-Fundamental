class Queue:
    def __init__(self):
        self.items = []  # this time we will be using a list to store our items
    def size(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.append(item)  # add an item to the end of the queue
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)  # remove the first index
    def show_queue(self):
        print(self.items)  # prints the list
class IceCreamShop:
    # when we call IceCreamShop(flavors) an instance of a queue is made called orders
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()  # our queue is named orders
    def take_order(self, customer, flavor, scoops):
        while True:# not needed
            # check if the flavor chosen is in the list of flavors in the shop and that the number of scoops is in the right range
            if flavor in self.flavors and scoops in range(1, 4):
                print("order created")
                order = {"customer": customer,
                         "flavor": flavor, "scoops": scoops}
                # puts the order in the list of orders, each element being a dictionary, we say self.orders because we want the ice cream shop to perform the method
                self.orders.enqueue(order)
                return
            else:
                break
    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:  # this word "order" isn't the same as the one in the previous method since we can have the same variable names across different methods because they're local
            # we also say "self.orders.items" because our queue is named orders and the list inside of the queue is called items
            print("Customer:", order["customer"], "-- Flavor:",
                  order["flavor"], "-- Scoops:", order["scoops"])  # printing key values with this
            
    def next_order(self):
        print("\nNext Order Up!")
        # we don't say items here because then we would be looking inside the dequeue method is only for orders not items. items is an attribute
        order = self.orders.dequeue()
        print("Customer:", order["customer"], "-- Flavor:",
              order["flavor"], "-- Scoops:", order["scoops"])
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()













