class CreditCard:
    """
    Kelas yang digunakan untuk aktifitas transaksi melalui kartu kredit
    """

    # Constructor (digunakan untuk inisialisasi data member dari suatu class)
    def __init__(self, customer, bank, akun, limit):
        """
        Saldo awal adalah nol.
        customer    nama customer tipe string (contoh: 'Asep Surasep')
        bank        nama bank tipe string (contoh: 'Bank Sulap')
        akun        nomor kartu tipe string (contoh: '1111 2222 3333 4444')
        limit       limit kartu kredit tipe float (contoh: 5_000_0000 (dalam rupiah))
        """

        # Biasanya kita gunakan protected member (contoh: penamaan variabel dimulai dengan '_')
        self._customer = customer
        self._bank = bank
        self._akun = akun
        self._limit = limit
        self._balance = 0 # inisialisasi saldo awal 0

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_akun(self):
        return self._akun
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, harga):
        if harga + self._balance > self._limit:
            return False
        else:
            self._balance += harga
            return True
    
    def make_payment(self, amount):
        self._balance -= amount


# cc = CreditCard(
#     'John Doe',
#     'Bank Mandiri',
#     '1234 5678 9101 1121',
#     10_000_000
# )

# print(cc.get_akun())
# print(cc.get_limit())
# print(cc.charge(12_000_000))
# print(cc.get_balance())
# print(cc.charge(1_200_000))
# print(cc.get_balance())
# print(cc.charge(1_100_000))
# print(cc.get_balance())
# print(cc.make_payment(1_000_000))
# print(cc.get_balance())