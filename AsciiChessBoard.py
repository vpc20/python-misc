#!/usr/bin/python

fen1 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
NO_OF_FEN_RANKS = 8
# fen1 = "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 3 5"
pieces = {'p': '\u265f', 'n': '\u265e', 'b': '\u265d', 'r': '\u265c', 'q': '\u265b', 'k': '\u265a',
          'P': '\u2659', 'N': '\u2658', 'B': '\u2657', 'R': '\u2656', 'Q': '\u2655', 'K': '\u2654'}


class FEN:
    def __init__(self, fen):
        self.fen = fen

    def split_rank(self):
        fen_stripped = self.fen[0:self.fen.find(" ")]  # remove the unnecessary characters from space onwards
        return fen_stripped.split("/", NO_OF_FEN_RANKS)  # split fen string into 8 ranks

    def active_color(self):
        return self.fen.split(" ", 8)[1]

    def white_can_castle_kside(self):
        fen_array = self.fen.split(" ", NO_OF_FEN_RANKS)
        if fen_array[2].find("K") != -1:
            return True
        else:
            return False

    def white_can_castle_qside(self):
        fen_array = self.fen.split(" ", NO_OF_FEN_RANKS)
        if fen_array[2].find("Q") != -1:
            return True
        else:
            return False

    def black_can_castle_kside(self):
        fen_array = self.fen.split(" ", NO_OF_FEN_RANKS)
        if fen_array[2].find("k") != -1:
            return True
        else:
            return False

    def black_can_castle_qside(self):
        fen_array = self.fen.split(" ", NO_OF_FEN_RANKS)
        if fen_array[2].find("q") != -1:
            return True
        else:
            return False

    def en_passant_square(self):
        return self.fen.split(" ", NO_OF_FEN_RANKS)[3]

    def half_move_clock(self):
        return self.fen.split(" ", NO_OF_FEN_RANKS)[4]

    def full_move_number(self):
        return self.fen.split(" ", NO_OF_FEN_RANKS)[5]


def display_ascii_chess_board(board_fen):
    # fen_obj = FEN(board_fen)
    rank_str = board_fen.split_rank()  # split fne into 8 ranks discarding trailing info
    print("  +-----------------+")
    for rank_idx in range(0, NO_OF_FEN_RANKS):  # loop into each rank
        rank_str1 = rank_str[rank_idx]
        rank_str2 = ""
        for i in range(0, len(rank_str1)):
            if rank_str1[i].isdigit():  # number indicates unoccupied square...just print dots
                j = int(rank_str1[i])
                for x in range(0, j):
                    rank_str2 += ". "
            else:
                rank_str2 = rank_str2 + pieces[rank_str1[i]] + " "
        print(str(8 - rank_idx) + " | " + rank_str2 + "|")
    print("  +-----------------+")
    print("    a b c d e f g h  ")


def get_square_num(square_name):
    square_col = int(square_name[1])
    square_row = "@abcdefgh".find(square_name[0])
    # formula is (squareCol - 1) + (square_row - 1)8
    # simplified to equation below
    return square_col + 8 * square_row - 9


# ----------------------------------------------------------------------------

fenObj = FEN(fen1)
print("\n")
print("FEN : " + fenObj.fen)
print("Active color               : " + fenObj.active_color())
print("White can castle kingside  : " + str(fenObj.white_can_castle_kside()))
print("White can castle queenside : " + str(fenObj.white_can_castle_qside()))
print("Black can castle kingside  : " + str(fenObj.black_can_castle_kside()))
print("Black can castle queenside : " + str(fenObj.black_can_castle_qside()))
print("En Passant square          : " + fenObj.en_passant_square())
print("Halfmove Clock             : " + fenObj.half_move_clock())
print("Fullmove Number            : " + fenObj.full_move_number())

print("\nAscii chess board generated from FEN\n")
display_ascii_chess_board(fenObj)

# getSquareNum('a1')
# getSquareNum('h8')

print("Squarenum " + str(get_square_num("a1")))
print("Squarenum " + str(get_square_num("h8")))
