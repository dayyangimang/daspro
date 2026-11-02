# Nama : Dayyan Mufid 
# nim : 24060126140210

from list_24060126040210 import *

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah list dengan syarat setiap elemen harus unik
# Semua konstruktor, selektor, dan operasi yang telah
# didefinisikan untuk list juga berlaku pada set
#
# Prekondisi: setiap argumen bertipe Set pada fungsi di bawah ini
# diasumsikan sudah memenuhi syarat set (tidak ada elemen duplikat).
# Pengecualian: MakeSet (menerima list biasa) dan IsSet (yang memeriksa syarat tersebut).

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK SET
# Rember: elemen, List -> List
# {Rember(x, L) menghapus sebuah elemen X dari list L.
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.}
# Realisasi:
def Rember(x, L: list) -> list:
    if isEmpty(L): # Basis
        return []
    else: # Rekurens
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))
# Aplikasi:
print(Rember(2, [7, 2, 5, 2, 3])) # [7, 5, 2, 3]
print(Rember(2, [])) # []
print(Rember(2, [3])) # [3]
print(Rember(2, [3, 4, 5, 2, 3, 5, 7, 8, 2])) # [3, 4, 5, 3, 5, 7, 8, 2]

# Tugas Latihan
# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK SET
# Rember2: elemen, List -> List
# {Rember2(x, L) menghapus sebuah elemen dari list L.
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L, maka L tidak berubah.
# List kosong tetap menjadi list kosong.}
def Rember2(x, L: list) -> list:
    if isEmpty(L):
        return []
    else:
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konsi(Rember2(x, Head(L)), LastElmt(L))

# MultiRember: elemen, List -> List
# {MultiRember(x, L) menghapus semua kemunculan elemen x dari list L.
# List baru yang dihasilkan tidak lagi memiliki elemen x.
# List kosong tetap menjadi list kosong.}
def MultiRember(x, L: list) -> list:
    if isEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET DARI LIST
# MakeSet_Versi1: List -> Set
# {MakeSet_Versi1(L) membuat set dari list L dengan menghapus semua
# elemen yang muncul lebih dari satu, menyisakan elemen yang
# sama yang terakhir muncul.}
def MakeSet_Versi1(L: list) -> list:
    if isEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet_Versi1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet_Versi1(Tail(L)))

# MakeSet_Versi2: List -> Set
# {MakeSet_Versi2(L) membuat set dari list L dengan menghapus semua
# elemen yang muncul lebih dari satu, menyisakan elemen yang
# sama yang pertama muncul.}
def MakeSet_Versi2(L: list) -> list:
    if isEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet_Versi2(MultiRember(FirstElmt(L), Tail(L))))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET
# KonsoSet: elemen, Set -> Set
# {KonsoSet(e, H) menambahkan elemen e sebagai elemen pertama dari set H
# dengan syarat e belum merupakan anggota dari set H.}
def KonsoSet(e, H: list) -> list:
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: List -> boolean
# {IsSet(L) bernilai True apabila list L merupakan sebuah set.}
def IsSet(L: list) -> bool:
    if isEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

# IsSubSet: 2 Set -> boolean
# {IsSubset(H1, H2) bernilai True apabila H1 merupakan subset dari H2.}
def IsSubset(H1: list, H2: list) -> bool:
    if isEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False

# IsEqualSet_Versi1: 2 Set -> boolean
# {IsEqualSet_Versi1(H1, H2) bernilai True apabila H1 adalah
# set yang sama dengan H2, dengan mengecek bahwa H1
# merupakan subset dari H2, dan sebaliknya.}
def IsEqualSet_Versi1(H1: list, H2: list) -> bool:
    return IsSubset(H1, H2) and IsSubset(H2, H1)

# IsEqualSet_Versi2: 2 Set -> boolean
# {IsEqualSet_Versi2(H1, H2) bernilai True apabila H1 adalah
# set yang sama dengan H2, dengan mengecek satu per satu elemen H1
# merupakan elemen dari H2 juga dan kedua set memiliki banyak elemen yang sama.}
def IsEqualSet_Versi2(H1: list, H2: list) -> bool:
    if NbElmt(H1) != NbElmt(H2):
        return False
    elif isEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsEqualSet_Versi2(Tail(H1), Rember2(FirstElmt(H1), H2))
        else:
            return False

# IsIntersect: 2 Set -> boolean
# {IsIntersect(H1, H2) bernilai True apabila H1 beririsan dengan H2.}
def IsIntersect(H1: list, H2: list) -> bool:
    if isEmpty(H1):
        return False
    else:
        if IsMember(FirstElmt(H1), H2):
            return True
        else:
            return IsIntersect(Tail(H1), H2)

# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP SET
# MakeIntersect_Versi1: 2 Set -> Set
# {MakeIntersect_Versi1(H1, H2) menghasilkan set baru yang berisikan
# irisan antara elemen H1 dan H2, dengan elemen pertama H1 yang
# beririsan dengan H2 diprioritaskan untuk dimasukkan ke set yang baru.}
def MakeIntersect_Versi1(H1: list, H2: list) -> list:
    if isEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect_Versi1(Tail(H1), H2))
        else:
            return MakeIntersect_Versi1(Tail(H1), H2)

# MakeIntersect_Versi2: 2 Set -> Set
# {MakeIntersect_Versi2(H1, H2) menghasilkan set baru yang berisikan
# irisan antara elemen H1 dan H2, dengan elemen pertama H2 yang
# beririsan dengan H1 diprioritaskan untuk dimasukkan ke set yang baru.}
def MakeIntersect_Versi2(H1: list, H2: list) -> list:
    if isEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2), H1):
            return Konso(FirstElmt(H2), MakeIntersect_Versi2(H1, Tail(H2)))
        else:
            return MakeIntersect_Versi2(H1, Tail(H2))

# MakeUnion_Versi1: 2 Set -> Set
# {MakeUnion_Versi1(H1, H2) menghasilkan set baru yang merupakan
# gabungan dari elemen H1 dan H2, dengan elemen H1 yang bukan merupakan
# elemen H2 diletakkan di belakang sebagai elemen terakhir dari set baru.}
def MakeUnion_Versi1(H1: list, H2: list) -> list:
    if isEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion_Versi1(Tail(H1), H2)
        else:
            return Konsi(MakeUnion_Versi1(Tail(H1), H2), FirstElmt(H1))

# MakeUnion_Versi2: 2 Set -> Set
# {MakeUnion_Versi2(H1, H2) menghasilkan set baru yang merupakan
# gabungan dari elemen H1 dan H2, dengan elemen H2 yang bukan merupakan
# elemen H1 diletakkan di belakang sebagai elemen terakhir dari set baru.}
def MakeUnion_Versi2(H1: list, H2: list) -> list:
    if isEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmt(H2), H1):
            return MakeUnion_Versi2(H1, Tail(H2))
        else:
            return Konsi(MakeUnion_Versi2(H1, Tail(H2)), FirstElmt(H2))

# NBIntersect: 2 Set -> integer
# {NBIntersect(H1, H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
# tanpa memanfaatkan fungsi MakeIntersect sebelumnya.}
def NBIntersect(H1: list, H2: list) -> int:
    if isEmpty(H1):
        return 0
    else:
        if IsMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)

# NBUnion: 2 Set -> integer
# {NBUnion(H1, H2) menghasilkan jumlah elemen gabungan pada H1 dan H2
# tanpa memanfaatkan fungsi MakeUnion sebelumnya.}
def NBUnion(H1: list, H2: list) -> int:
    if isEmpty(H1):
        return NbElmt(H2)
    else:
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)

# DEFINISI DAN SPESIFIKASI SOAL LATIHAN TAMBAHAN
# KonsiSet: Set, elemen -> Set
# {KonsiSet(H, e) menambahkan elemen e sebagai elemen terakhir dari set H
# dengan syarat e belum merupakan anggota dari set H.}
def KonsiSet(H: list, e) -> list:
    if IsMember(e, H):
        return H
    else:
        return Konsi(H, e)

# MakeDifference: 2 Set -> Set
# {MakeDifference(H1, H2) menghasilkan set baru yang berisikan selisih
# H1 dan H2, yaitu elemen-elemen H1 yang bukan merupakan elemen H2.
# Urutan elemen pada set baru mengikuti urutan pada H1.}
def MakeDifference(H1: list, H2: list) -> list:
    if isEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeDifference(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeDifference(Tail(H1), H2))

# MakeSymDifference: 2 Set -> Set
# {MakeSymDifference(H1, H2) menghasilkan set baru yang berisikan
# selisih simetris H1 dan H2, yaitu elemen-elemen yang hanya menjadi
# anggota salah satu dari H1 atau H2 (tidak keduanya).
# Hasil diawali elemen-elemen H1 yang bukan elemen H2, lalu diikuti
# elemen-elemen H2 yang bukan elemen H1.
# Boleh memanfaatkan fungsi MakeDifference.}
def MakeSymDifference(H1: list, H2: list) -> list:
    return Konkat(MakeDifference(H1, H2), MakeDifference(H2, H1))

# JaccardSimilarity: 2 Set -> real
# {JaccardSimilarity(H1, H2) menghasilkan bilangan riil yang merupakan
# indeks kemiripan Jaccard dari H1 dan H2, yaitu banyak elemen irisan
# dibagi banyak elemen gabungan.
# Jika H1 dan H2 sama-sama kosong, menghasilkan 0.0.
# Boleh memanfaatkan fungsi NBIntersect dan NBUnion.}
def JaccardSimilarity(H1: list, H2: list) -> float:
    if NBUnion(H1, H2) == 0:
        return 0.0
    else:
        return NBIntersect(H1, H2) / NBUnion(H1, H2)

# KonsoAll: elemen, List of List -> List of List
# {KonsoAll(e, LL) menghasilkan list yang berisikan setiap list pada LL
# yang telah ditambahi elemen e sebagai elemen pertamanya.
# List kosong tetap menjadi list kosong.}
def KonsoAll(e, LL: list) -> list:
    if isEmpty(LL):
        return []
    else:
        return Konso(Konso(e, FirstElmt(LL)), KonsoAll(e, Tail(LL)))

# PowerSet: Set -> Set of Set
# {PowerSet(H) menghasilkan himpunan kuasa dari H, yaitu set yang
# anggotanya adalah semua subset dari H (termasuk set kosong dan H
# itu sendiri). Urutan hasil: subset yang tidak memuat elemen pertama
# H didahulukan, lalu diikuti subset yang memuat elemen pertama H.}
def PowerSet(H: list) -> list:
    if isEmpty(H):
        return [[]]
    else:
        return Konkat(PowerSet(Tail(H)), KonsoAll(FirstElmt(H), PowerSet(Tail(H))))