# DEFINISI DAN SPESIFIKASI TYPE  
# Konstruktor menambahkan elemen di awal, notasi prefix 
# type List: [] atau [e o List] 
# Konstruktor menambahkan elemen di akhir, notasi postfix 
# type List: [] atau [List o e] 

# DEFINISI DAN SPESIFIKASI SELEKTOR  
# FirstElmt(L): List tidak kosong -> elemen  
# {FirstElmt(L) mengembalikan elemen pertama dari L.}  
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya} 

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR  
# Konso: elemen, List -> List  
# {Konso(e, L) menghasilkan sebuah list dari e dan L  
# dengan e sebagai elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}  

def Konso(E: int, L: list) -> list: 
    return [E] + L 

# Aplikasi
print(Konso(7, [2, 4, 6]))

# Konsi: elemen, List -> List
# {Konsi(e, L) menghasilkan sebuah list dari e dan L
# dengan e sebagai elemen terakhir dari L.}
# {Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# Realisasi:

def Konsi(L: list, E: int) -> list: 
    return L + [E]

# Aplikasi
print(Konsi([6, 7, 8], 9))

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt(L): List tidak kosong -> elemen
# {FirstElmt(L) mengembalikan elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# Realisasi:

def FirstElmt(L: list) -> int:
    return L[0]

# Aplikasi
print(FirstElmt([83, 202, 79, 44]))

# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# Realisasi:

def LastElmt(L: list) -> int: 
    return L[-1]

# Aplikasi
print(LastElmt([83, 202, 79, 44])) 

# Head(L): List tidak kosong -> List
# {Head(L) mengembalikan list L tanpa elemen terakhir
# dari L; dapat menghasilkan list kosong.}
# Realisasi:

def Head(L: list) -> list: 
    return L[:-1]

# Aplikasi
print(Head([83, 202, 79, 44]))

# Tail(L): List tidak kosong -> List
# {Tail(L) mengembalikan list L tanpa elemen pertama
# dari L; dapat menghasilkan list kosong.}
# Realisasi:

def Tail(L: list) -> list:
    return L[1:]

# Aplikasi
print(Tail([83, 202, 79, 44]))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isEmpty(L): List -> boolean
# {isEmpty(L) bernilai True jika List merupakan list kosong.}
# Realisasi:

def isEmpty(L: list) -> bool: 
    return L==[]

# Aplikasi
print(isEmpty([]))
print(isEmpty([2, 7]))

# IsOneElmt(L): List -> boolean
# {IsOneElmt(L) bernilai True jika List hanya memiliki
# tepat satu elemen.}
# Realisasi:

def IsOneElmt(L: list) -> bool:
    if isEmpty(L): 
        return False 
    else: 
        return Tail(L)==[] and Head(L)==[]

# Aplikasi
print(IsOneElmt([8]))
print(IsOneElmt([2, 3, 5, 7]))

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST  
# NbElmt(L): List -> integer  
# {NbElmt(L) menghasilkan banyaknya elemen dalam list L.}  

def NbElmt(L: list) -> int:
    if isEmpty(L):
        return 0
    else: 
        return 1 + NbElmt(Tail(L))

# Aplikasi
print(NbElmt([]))
print(NbElmt([2, 7]))
print(NbElmt([83, 202, 79, 44])) 

# Copy: List -> List
# {Copy(L) menghasilkan List yang identik dengan list asal.}
# Realisasi:

def copy(L: list) -> list:
    if isEmpty(L): 
        return[]
    else:
        return Konso(FirstElmt(L), copy(Tail(L)))

# Aplikasi
print(copy([83, 202, 79, 44])) 



# TUGAS LATIHAN
# ElmtKeN: integer ≥ 0, List -> elemen
# {ElmtKeN(N, L) menghasilkan elemen ke-N dari list L.}
# Realisasi

def ElmtKeN(N, L):
    if N == 0:
        return FirstElmt(L)
    else:
        return ElmtKeN(N - 1, Tail(L))

# Aplikasi
print(ElmtKeN(0, [83, 202, 79, 44]))
print(ElmtKeN(2, [83, 202, 79, 44]))

# IsMember: elemen, List -> boolean
# {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}
# Realisasi:

def IsMember(X, L):
    if isEmpty(L):
        return False
    else:
        if FirstElmt(L) == X:
            return True
        else:
            return IsMember(X, Tail(L))

# Aplikasi
print(IsMember(79, [83, 202, 79, 44]))
print(IsMember(100, [83, 202, 79, 44]))

# Inverse: List -> List
# {Inverse(L) menghasilkan list L yang dibalik, yaitu
# yang urutan elemennya adalah kebalikan dari list awal.}
# Realisasi:

def Inverse(L):
    if isEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# Aplikasi
print(Inverse([83, 202, 79, 44]))

# Konkat: 2 List -> List
# {Konkat(L1, L2) menghasilkan List yang merupakan hasil
# konkatenasi list L1 dan L2.}
# Realisasi:

def Konkat(L1, L2):
    if isEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))

# Aplikasi
print(Konkat([1, 2], [3, 4]))

# SumElmt(L): List of integer -> integer
# {SumElmt(L) menghasilkan bilangan bulat yang merupakan jumlah
# nilai dari seluruh elemen L.}
# Realisasi:

def SumElmt(L):
    if isEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# Aplikasi
print(SumElmt([83, 202, 79, 44]))

# AvgElmt(L): List of integer -> real
# {AvgElmt(L) menghasilkan bilangan riil yang merupakan rata-rata
# nilai dari seluruh elemen L.}
# {Asumsi: L tidak kosong}
# Realisasi:

def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)

# Aplikasi
print(AvgElmt([83, 202, 79, 44]))

# MaxElmt(L): List of integer -> integer
# {MaxElmt(L) mengembalikan elemen dengan nilai maksimum dari list L.}
# {Asumsi: L tidak kosong}
# Realisasi:

def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) > MaxElmt(Tail(L)):
            return FirstElmt(L)
        else:
            return MaxElmt(Tail(L))

# Aplikasi
print(MaxElmt([83, 202, 79, 44]))

# MaxNB: List of integer (tidak kosong) -> <integer, integer >= 1>
# {MaxNB(L) menghasilkan tipe bentukan yang berisikan bilangan
# maksimum pada list L dan seberapa banyak bilangan itu muncul
# di dalam list.}
# Fungsi bantu: CountElmt(X, L) -> banyaknya kemunculan X di L

def CountX(X, L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) == X:
            return 1 + CountX(X, Tail(L))
        else:
            return CountX(X, Tail(L))

# Realisasi: tipe bentukan direpresentasikan dengan tuple (maks, banyak

def MaxNB(L: list) -> tuple:
    return (MaxElmt(L), CountX(MaxElmt(L), L))

# Aplikasi
print(MaxNB([83, 202, 202, 79, 44, 202]))

# AddList: 2 List of integer -> List
# {AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah
# hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama.}
# {Asumsi: L1 dan L2 memiliki panjang yang sama}
# Realisasi:

def AddList(L1, L2):
    if isEmpty(L1):
        return []
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# Aplikasi
print(AddList([1, 2, 3], [4, 5, 6]))

# IsPalindrom: List of character -> boolean
# {IsPalindrom(L) bernilai True jika L merupakan kata palindrom,
# yakni kata yang sama jika dibaca dari kiri atau kanan.}
# Realisasi:

def IsPalindrom(L: list) -> bool:
    if isEmpty(L) or IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Tail(Head(L)))

# Aplikasi
print(IsPalindrom(['k', 'a', 't', 'a', 'k']))
print(IsPalindrom(['b', 'u', 'k', 'u'])) 

# IsEqual: 2 List -> boolean
# {IsEqual(L1,L2) true jika dan hanya jika kedua list sama, yaitu
# setiap elemen dan urutan kemunculannya sama}
# Realisasi:

def IsEqual(L1, L2):
    if isEmpty(L1) and isEmpty(L2):
        return True
    elif isEmpty(L1) or isEmpty(L2):
        return False
    else:
        return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1), Tail(L2))

# Aplikasi
print(IsEqual([1, 2, 3], [1, 2, 3]))
print(IsEqual([1, 2, 3], [1, 2, 4]))

# MinElmt: List of integer (tidak kosong) -> integer
# {MinElmt(L) mengembalikan elemen dengan nilai minimum dari list L.}
# Realisasi:

def MinElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) < MinElmt(Tail(L)):
            return FirstElmt(L)
        else:
            return MinElmt(Tail(L))

# Aplikasi      
print(MinElmt([83, 202, 79, 44]))

# CountN: character, list of character -> integer
# {CountN(C, T) menghasilkan banyaknya kemunculan karakter C
# pada list of character (T)}
# Realisasi:

def CountN(C, T):
    if isEmpty(T):
        return 0
    elif FirstElmt(T) == C:
        return 1 + CountN(C, Tail(T))
    else:
        return CountN(C, Tail(T))

# Aplikasi
print(CountN('a', ['a', 'b', 'a', 'c', 'a']))

# Atleast: integer > 0, character, list of character -> boolean
# {Atleast (N,C,T) benar, jika karakter C minimal muncul N kali
# pada list of character (T)}
# Realisasi:

def Atleast(N, C, T):
    return CountN(C, T) >= N

# Aplikasi
print(Atleast(3, 'a', ['a', 'b', 'a', 'c', 'a']))
print(Atleast(5, 'a', ['a', 'b', 'a', 'c', 'a']))

# IsXElmtKeN (N,L) :elemen, integer ≥ 0, List (tidak kosong) → boolean
# {IsXElmtKeN (L) true jika X adalah elemen ke-N list L, N ≥ 0, dan N ≤
# banyaknya elemen list, false jika tidak}
# (Catatan realisasi: parameter dipakai (X, N, L); indeks mulai 0, jadi N valid jika N < NbElmt(L))
# Realisasi:

def IsXElmtKeN(X, N, L):
    if N >= NbElmt(L):
        return False
    else:
        return ElmtKeN(N, L) == X

# Aplikasi
print(IsXElmtKeN(79, 2, [83, 202, 79, 44]))
print(IsXElmtKeN(79, 1, [83, 202, 79, 44]))

# DelFirstElmt: List of integer (tidak kosong) → List of integer
# DelFirstElmt(Li) mengembalikan list L tanpa elemen pertamanya. kondisi: List L tidak kosong.}
# Realisasi:

def DelFirstElmt(L):
    return Tail(L)

# Aplikasi
print(DelFirstElmt([83, 202, 79, 44]))

# MultiRember: elemen, List -> List
# {MultiRember(X, L) menghapus seluruh kemunculan elemen X dari list L.}
# Realisasi:

def MultiRember(X, L):
    if isEmpty(L):
        return []
    else:
        if FirstElmt(L) == X:
            return MultiRember(X, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(X, Tail(L)))

# Aplikasi
print(MultiRember(2, [1, 2, 3, 2, 4, 2]))

# CountGenap: List of Integer -> integer
# {CountGenap(L) menghasilkan banyaknya elemen bernilai genap
# dalam list L.}
# Realisasi:

def CountGenap(L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) % 2 == 0:
            return 1 + CountGenap(Tail(L))
        else:
            return CountGenap(Tail(L))

# Aplikasi
print(CountGenap([83, 202, 79, 44]))

# IndexOf: integer, list of integer -> integer
# {IndexOf(X, Li) menghasilkan indeks (dimulai dari 0) kemunculan pertama X di list L. Jika Xx tidak ada di
# L, hasilnya -1.}
# Realisasi:

def IndexOf(X: int, L: list) -> int:
    if isEmpty(L):
        return -1
    elif FirstElmt(L) == X:
        return 0
    else:
        if IndexOf(X, Tail(L)) == -1:
            return -1
        else:
            return 1 + IndexOf(X, Tail(L))

# Aplikasi
print(IndexOf(79, [83, 202, 79, 44]))
print(IndexOf(100, [83, 202, 79, 44]))
