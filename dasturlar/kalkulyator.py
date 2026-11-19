# kalkulyator.py | boshlandi: 2026-11-18

# --- qadam 1: a + b yigindisi ---
a = 12
b = 5
print("Yigindi:", a + b)

# --- qadam 2: ayirma qoshildi ---
print("Ayirma:", a - b)

# --- qadam 3: kopaytma qoshildi ---
print("Kopaytma:", a * b)

# --- qadam 4: bolish (nolga tekshiruv bilan) ---
if b != 0:
    print("Bolinma:", a / b)
else:
    print("Nolga bolib bolmaydi")

# --- qadam 5: darajaga oshirish ---
print("Daraja:", a ** b)

# --- qadam 6: qoldiq ---
print("Qoldiq:", a % b)

# --- qadam 7: ortacha qiymat ---
print("Ortacha:", (a + b) / 2)

# --- qadam 8: eng katta va eng kichik ---
print("Eng katta:", max(a, b))
print("Eng kichik:", min(a, b))

# --- qadam 9: hisobla() funksiyasi ---
def hisobla(x, y):
    return {
        "yigindi": x + y,
        "ayirma": x - y,
        "kopaytma": x * y,
    }

# --- qadam 10: funksiyani chaqirish ---
print(hisobla(20, 4))
