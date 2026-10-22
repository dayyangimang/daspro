# DEFINISI DAN SPESIFIKASI TYPE  
# Konstruktor menambahkan elemen di awal, notasi prefix 
# type List: [] atau [e o List] 
# Konstruktor menambahkan elemen di akhir, notasi postfix 
# type List: [] atau [List o e] 


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR  
# Konso: elemen, List -> List  
# {Konso(e, L) menghasilkan sebuah list dari e dan L  
# dengan e sebagai elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}  


def Konso(E: int, L: list) -> list: 
    return [E] + L 
print(Konso(7, [2, 4, 6]))


def Konsi(L: list, E: int) -> list: 
    return L + [E]
print(Konsi([6, 7, 8], 9))


# DEFINISI DAN SPESIFIKASI SELEKTOR  
# FirstElmt(L): List tidak kosong -> elemen  
# {FirstElmt(L) mengembalikan elemen pertama dari L.}  
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya} 


def FirstElmt(L: list) -> int:
    return L[0]
print(FirstElmt([83, 202, 79, 44]))


def LastElmt(L: list) -> int: 
    return L[-1]
print(LastElmt([83, 202, 79, 44])) 


def Head(L: list) -> list: 
    return L[:-1]
print(Head([83, 202, 79, 44]))


def Tail(L: list) -> list:
    return L[1:]
print(Tail([83, 202, 79, 44]))


# DEFINISI DAN SPESIFIKASI PREDIKAT  
# isEmpty(L): List -> boolean  
# {isEmpty(L) bernilai True jika List merupakan list kosong.}  


def isEmpty(L: list) -> bool: 
    return L==[]
print(isEmpty([]))
print(isEmpty([2, 7]))


def IsOneElmt(L: list) -> bool:
    if isEmpty(L): 
        return False 
    else: 
        return Tail(L)==[] and Head(L)==[]
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
print(NbElmt([]))
print(NbElmt([2, 7]))
print(NbElmt([83, 202, 79, 44])) 


def copy(L: list) -> list:
    if isEmpty(L): 
        return[]
    else:
        return Konso(FirstElmt(L), copy(Tail(L)))
print(copy([83, 202, 79, 44])) 


def ElmtKeN(N, L):
    if N == 0:
        return FirstElmt(L)
    else:
        return ElmtKeN(N - 1, Tail(L))

print(ElmtKeN(0, [83, 202, 79, 44]))
print(ElmtKeN(2, [83, 202, 79, 44]))


def IsMember(X, L):
    if isEmpty(L):
        return False
    else:
        if FirstElmt(L) == X:
            return True
        else:
            return IsMember(X, Tail(L))

print(IsMember(79, [83, 202, 79, 44]))
print(IsMember(100, [83, 202, 79, 44]))


def Inverse(L):
    if isEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

print(Inverse([83, 202, 79, 44]))


def Konkat(L1, L2):
    if isEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))

print(Konkat([1, 2], [3, 4]))


def SumElmt(L):
    if isEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

print(SumElmt([83, 202, 79, 44]))


def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)

print(AvgElmt([83, 202, 79, 44]))


def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        return max(FirstElmt(L), MaxElmt(Tail(L)))

print(MaxElmt([83, 202, 79, 44]))


def CountX(X, L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) == X:
            return 1 + CountX(X, Tail(L))
        else:
            return CountX(X, Tail(L))


def MaxNB(L):
    max_val = MaxElmt(L)
    count = CountX(max_val, L)
    return (max_val, count)

print(MaxNB([83, 202, 202, 79, 44, 202]))


def AddList(L1, L2):
    if isEmpty(L1):
        return []
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

print(AddList([1, 2, 3], [4, 5, 6]))


def IsPalindrom(L):
    if isEmpty(L) or IsOneElmt(L):
        return True
    else:
        if FirstElmt(L) == LastElmt(L):
            return IsPalindrom(Head(Tail(L)))
        else:
            return False

print(IsPalindrom(['a', 'b', 'a']))
print(IsPalindrom(['a', 'b', 'c']))


def IsEqual(L1, L2):
    if isEmpty(L1) and isEmpty(L2):
        return True
    elif isEmpty(L1) or isEmpty(L2):
        return False
    else:
        if FirstElmt(L1) == FirstElmt(L2):
            return IsEqual(Tail(L1), Tail(L2))
        else:
            return False

print(IsEqual([1, 2, 3], [1, 2, 3]))
print(IsEqual([1, 2, 3], [1, 2, 4]))


def MinElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        return min(FirstElmt(L), MinElmt(Tail(L)))

print(MinElmt([83, 202, 79, 44]))


def CountN(C, T):
    if isEmpty(T):
        return 0
    else:
        if FirstElmt(T) == C:
            return 1 + CountN(C, Tail(T))
        else:
            return CountN(C, Tail(T))

print(CountN('a', ['a', 'b', 'a', 'c', 'a']))


def Atleast(N, C, T):
    return CountN(C, T) >= N

print(Atleast(3, 'a', ['a', 'b', 'a', 'c', 'a']))
print(Atleast(5, 'a', ['a', 'b', 'a', 'c', 'a']))


def IsXElmtKeN(X, N, L):
    if N >= NbElmt(L):
        return False
    else:
        return ElmtKeN(N, L) == X

print(IsXElmtKeN(79, 2, [83, 202, 79, 44]))
print(IsXElmtKeN(79, 1, [83, 202, 79, 44]))


def DelFirstElmt(L):
    return Tail(L)

print(DelFirstElmt([83, 202, 79, 44]))


def MultiRember(X, L):
    if isEmpty(L):
        return []
    else:
        if FirstElmt(L) == X:
            return MultiRember(X, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(X, Tail(L)))

print(MultiRember(2, [1, 2, 3, 2, 4, 2]))


def CountGenap(L):
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) % 2 == 0:
            return 1 + CountGenap(Tail(L))
        else:
            return CountGenap(Tail(L))

print(CountGenap([83, 202, 79, 44]))


def IndexOf(X, L):
    if isEmpty(L):
        return -1
    if FirstElmt(L) == X:
        return 0
    return -1 if IndexOf(X, Tail(L)) == -1 else 1 + IndexOf(X, Tail(L))

print(IndexOf(79, [83, 202, 79, 44]))
print(IndexOf(100, [83, 202, 79, 44]))