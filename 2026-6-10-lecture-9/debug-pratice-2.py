def add_item(item, cart=None):
	if cart is None:
		cart = []

	cart.append(item)
	return cart

print(add_item("apple"))
print(add_item("banana"))

cart = add_item("apple")
add_item("peanuts", cart)
print(cart)