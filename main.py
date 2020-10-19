# Python Standard Library imports
import sys

# Meng0import beberapa module
from GameState import GameState
from Board import Board

# Array untuk pengecekan
BOARD_SIZES = ["8", "10", "16"]

# Memproses and menge-pass parameter-parameter command line
if __name__ == "__main__":

    # Mengecek apakah inputan parameter kurang atau tidak
    if len(sys.argv) < 5:
        print("usage: python main.py <size> <t_limit> <type_player_1> <type_player_2>")
        print("type_player: 1 -> human, 2 -> minimax, 3 -> minimax+local")
        sys.exit(-1)

    # Me-unpack parameter menjadi variabel-variabel
    size, t_limit, type_player_1, type_player_2 = sys.argv[1:5]

    # Mengecek variabel-variabel yang diproses tadi
    if size not in BOARD_SIZES:
        print("error: <size> should be [" + ", ".join(BOARD_SIZES) + "]")
        sys.exit(-1)

    if not (size.isdigit() and t_limit.isdigit() and type_player_1.isdigit()
        and type_player_2.isdigit()):
        print("error: <size>, <t_limit>, <type_player_1>, and <type_player_2> should be integers")
        sys.exit(-1)

    # Pengubahan string ke int
    size = int(size)
    t_limit = int(t_limit)
    type_player_1 = int(type_player_1)
    type_player_2 = int(type_player_2)

    # Pengecekan tipe player
    if not(type_player_1 > 0 and type_player_1 < 4):
        print("error: <type_player_1> can only be 1, 2 or 3")
        print("type_player: 1 -> human, 2 -> minimax, 3 -> minimax+local")
        sys.exit(-1)

    if not(type_player_2 > 0 and type_player_2 < 4):
        print("error: <type_player_2> can only be 1, 2 or 3")
        print("type_player: 1 -> human, 2 -> minimax, 3 -> minimax+local")
        sys.exit(-1)

    # print("size", size)
    # print("t_limit", t_limit)
    # print("type_player_1", type_player_1)
    # print("type_player_2", type_player_2)

    board = Board(size, t_limit, type_player_1, type_player_2)
    newGame = GameState(board)
