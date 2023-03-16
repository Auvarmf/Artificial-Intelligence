import heapq  # menyediakan implementasi struktur data heap.
# Dalam konteks informed search, heap sering digunakan untuk memprioritaskan node yang akan dieksplorasi selanjutnya berdasarkan f(n), yang merupakan jumlah biaya dari jalur saat ini dan heuristic h(n), yang merupakan perkiraan biaya dari node tersebut ke state tujuan.

# Harry Potter dan teman-temannya mencari Horcrux untuk dihancurkan, sehingga kita membutuhkan fungsi heuristic untuk menghitung estimasi jarak antara dua titik.

# Fungsi untuk menghitung jarak heuristik antara dua posisi


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

# Fungsi informed search


def informed_search(graph, start, goal):
    # Menyimpan nilai heuristik untuk setiap node
    heuristik = {node: heuristic(node, goal) for node in graph}

    # Inisialisasi frontier dan explored set
    frontier = [(0, start)]
    jelajah = set()

    # Menyimpan jalur terpendek dari start ke goal
    jalan = {start: []}

    # Loop hingga frontier kosong
    while frontier:
        # Mengambil node dengan f(n) terkecil dari frontier
        (cost, node) = heapq.heappop(frontier)

        # Jika sudah mencapai goal, kembalikan jalur
        if node == goal:
            return jalan[node] + [node], cost

        # Tambahkan node ke explored set
        jelajah.add(node)

        # Loop untuk setiap tetangga
        for neighbor in graph[node]:
            # Jika tetangga belum dieksplorasi
            if neighbor not in jelajah:
                # Hitung nilai g(n) dan f(n)
                new_cost = cost + graph[node][neighbor]
                prioritas = new_cost + heuristik[neighbor]

                # Tambahkan node ke frontier
                heapq.heappush(frontier, (prioritas, neighbor))
                # Simpan jalur terpendek dari start ke neighbor
                jalan[neighbor] = jalan[node] + [node]

    # Jika tidak ditemukan jalur, kembalikan None
    return None


# Graph yang merepresentasikan tempat-tempat yang ingin dicari Horcrux
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1},
    (2, 1): {(1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1}
}

# graph sebenarnya yang mau dibuat adalah seperti ini
# graph = {
#     'Privet Drive': {'Godric\'s Hollow': 52},
#     'Godric\'s Hollow': {'Hogwarts': 18, 'Malfoy Manor': 50},
#     'Hogwarts': {'Gringotts Wizarding Bank': 27, 'Diagon Alley': 33, 'Ministry of Magic': 40},
#     'Diagon Alley': {'Shrieking Shack': 10},
#     'Shrieking Shack': {'Azkaban': 30},
#     'Malfoy Manor': {'Borgin and Burkes': 20},
#     'Borgin and Burkes': {'Gringotts Wizarding Bank': 15},
#     'Gringotts Wizarding Bank': {'Ministry of Magic': 12},
#     'Ministry of Magic': {'Azkaban': 35},
#     'Azkaban': {}
# }
# tapi sayangnya gak berhasil dan error, mungkin bisa dikasih solusinya kak:)

start = (1, 1)
goal = (2, 2)

jalann, cost = informed_search(graph, start, goal)

# untuk solusi sementara menggunakan dictionary
horcruxDict = {
    "Horcrux 1": "Tom Riddle's diary Destroy by Harry Potter",
    "Horcrux 2": "Marvolo Gaunt's ring Destroy by Albus Doumbledore",
    "Horcrux 3": "Salazar Slytherin's locket Destroy by Ron Weasley",
    "Horcrux 4": "Helga Hufflepuff's cup Destroy by Hermione Granger",
    "Horcrux 5": "Rowena Ravenclaw's diadem Destroy by Harry Potter",
    "Horcrux 6": "Nagini killed by Neville Longbottom",
    "Horcrux 7": "Harry Potter killed by Lord Voldemort",
}

if goal == (0, 0):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 1"])
elif goal == (0, 2):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 2"])
elif goal == (0, 1):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 3"])
elif goal == (1, 0):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 4"])
elif goal == (1, 2):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 5"])
elif goal == (1, 1):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 6"])
elif goal == (2, 2):
    print("Horcrux : ")
    print(horcruxDict["Horcrux 7"])

print("Jalur terpendek : ", jalann)
print("Jarak terpendek : ", cost)
