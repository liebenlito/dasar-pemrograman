# item1 = "Laptop"
# item1_harga = 1000
# item1_qty = 3
# item1_total_harga = item1_harga * item1_qty
# print(item1_total_harga)

# item2 = "Ponsel"
# item2_harga = 1200
# item2_qty = 2
# item2_total_harga = item2_harga * item2_qty
# print(item2_total_harga)

# class Item:
#     pass

# item1 = Item()
# item1.nama = "Laptop"
# item1.harga = 2000
# item1.qty = 2

# print(type(item1))
# print(type(item1.nama))
# print(type(item1.harga))
# print(type(item1.qty))

# class Item:
#     def __init__(self, nama, harga, qty):
#         self.nama = nama
#         self.harga = harga
#         self.qty = qty

#     def hitung_total_harga(self, x, y):
#         return x * y
    
# item1 = Item("Laptop", 2000, 2)
# item2 = Item("Ponsel", 1500, 3)

# print(item1.nama)
# print(item1.harga)
# print(item1.qty)
# print(item2.nama)
# print(item2.harga)
# print(item2.qty)

#print(item1.hitung_total_harga(item1.harga, item1.qty))
#print(item1.hitung_total_harga(item2.harga, item2.qty))

class Item:
    rate_bayar = 0.8
    def __init__(self, nama: str, harga: float, qty=0):
        assert harga >= 0, f"Harga {harga} tidak lebih dari atau sama dengan 0"
        assert qty >= 0, f"Harga {qty} tidak lebih dari atau sama dengan 0"

        self.nama = nama
        self.harga = harga
        self.qty = qty

    def hitung_total_harga(self):
        return self.harga * self.qty
    
    def diskon(self):
        self.harga = self.harga * self.rate_bayar
    
# item1 = Item("Laptop", 2000, 3)
# item1.diskon()
# print(item1.harga)
# print(item1.hitung_total_harga())

# item2 = Item("Ponsel", 1500, 5)
# item2.rate_bayar = 0.4
# item2.diskon()
# print(item2.harga)

item3 = Item("Komputer", 6000, 2)
print(item3.hitung_total_harga())