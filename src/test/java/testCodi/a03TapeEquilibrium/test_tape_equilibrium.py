from src.main.java.testCodi.a03TapeEquilibrium.solution_tape_equilibrium \
    import solution_tape_equilibrium
import pytest
from typing import List


@pytest.mark.parametrize(
    "input_array,expected_result",
    [
        ([3, 1, 2, 4, 3], 1),
        ([-1000, 1000], 2000),
        ([1, 1], 0),
        ([1, 2], 1),
        ([5, 6, 2, 4, 1], 4),
        ([1, 2, 3, 4, 2], 0),
        # simple negative
        ([-10, -5, -3, -4, -5], 3),
        ([-2, -3, -4, -1], 0),
        # simple boundary
        ([1, 1, 3], 1),
        ([3, 1, 1], 1),
        ([1, 2, 3, 4, 10], 0),
        ([10, 2, 3, 4, 1], 0),
        # small random
        ([-896, -826, -186, -785, 803, -924, 72, -336, 705, -681, -326, -333,
          -510, -997, -128, -825, 195, -861, -369, -103, 811,
          -815, -716, 580, -958, 823, 147, -470, 676, 538, -
          313, 603, -587, 218, 54, 619, -370, -204, 539, 26, 370,
          277, 333, 781, -28, 337, -251, -937, 509, -637, 641,
          828, 316, -660, -326, -218, -854, -87, 146, -328, -622, -824, 257,
          -975, -296, -542, 64, 448, 819, 278, 984, 929, 260, -534,
          -32, -645, 984, -111, 504, -912, -731, -614, -488, -296,
          -456, -132, -159, -783, -875, -290, -823, -134, -983, 72,
          -853, 389, -192, 971, -475, -55], 39),
        # small range
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
          35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
          50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
          65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
          80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
          95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
          108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
          120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
          132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
          144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
          156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
          168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
          180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
          192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
          204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
          216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227,
          228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240,
          241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
          253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264,
          265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276,
          277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288,
          289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300,
          301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
          313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324,
          325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336,
          337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348,
          349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360,
          361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372,
          373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384,
          385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
          397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408,
          409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420,
          421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431], 234),
        # small
        ([-10, -20, -30, -40, 100], 20),
        # medium random
        ([5, 8, 41, 10, 91, 3, 54, 33, 86, 16, 34, 33, 24, 0, 44, 8, 60, 7,
          31, 45, 91, 9, 14, 79, 2, 92, 57, 26, 84, 77, 34, 80, 20, 61, 53,
          81, 31, 40, 77, 51, 69, 64, 67, 89, 49, 67, 37, 3, 76, 18, 82, 92,
          66, 17, 34, 39, 7, 46, 57, 33, 19, 8, 63, 1, 35, 23, 53, 73, 91,
          64, 100, 97, 63, 23, 48, 17, 100, 44, 75, 4, 13, 19, 25, 35, 27,
          43, 42, 10, 6, 35, 8, 43, 0, 54, 7, 70, 40, 99, 26, 47, 75, 33,
          35, 64, 97, 89, 42, 72, 68, 37, 23, 7, 88, 5, 52, 54, 14, 66, 92,
          78, 39, 12, 98, 52, 63, 81, 39, 6, 13, 67, 35, 87, 74, 99, 67,
          30, 79, 2, 52, 88, 51, 13, 50, 55, 37, 90, 34, 27, 51, 20, 32, 40,
          94, 8, 19, 20, 100, 89, 19, 57, 8, 32, 34, 54, 93, 81, 53, 79, 48,
          73, 78, 25, 84, 58, 49, 39, 22, 50, 12, 64, 90, 79, 61, 49, 70,
          12, 5, 87, 36, 67, 42, 36, 77, 34, 76, 82, 18, 98, 6, 41, 50, 83,
          17, 56, 37, 93, 12, 26, 82, 32, 95, 5, 39, 10, 57, 97, 32, 65, 26,
          44, 57, 25, 69, 50, 91, 27, 96, 18, 2, 66, 74, 48, 4, 100, 14, 87,
          90, 22, 87, 46, 90, 89, 78, 29, 58, 99, 32, 39, 69, 6, 25, 16, 42,
          42, 61, 50, 16, 4, 53, 77, 93, 84, 30,
          87, 47, 28, 9, 44, 55, 28, 19, 95, 6, 94, 41, 79, 11, 57, 76, 44,
          36, 49, 19, 21, 24, 3, 91, 7, 93, 1, 66, 55, 4, 95, 73, 88, 44, 29,
          18, 11, 67, 83, 21, 2, 36, 15, 22, 22, 66, 43, 56, 39, 99, 50, 4,
          14, 73, 92, 12, 46, 87, 55, 1, 52, 29, 21, 94, 10, 83, 76, 59, 32,
          8, 67, 96, 18, 12, 47, 85, 0, 79, 8, 3, 14, 46, 94, 66, 6, 15, 46,
          9, 67, 36, 96, 82, 82, 23, 43, 67, 9, 0, 33, 40, 79, 82, 5, 6, 93,
          29, 12, 80, 79, 61, 77, 86, 86, 26, 42, 99, 37, 63, 85, 88, 60,
          35, 69, 0, 35, 76, 65, 8, 72, 61, 44, 10, 60, 75, 20, 64, 7, 20,
          36, 78, 28, 89, 99, 16, 2, 73, 77, 90, 67, 78, 36, 10, 100, 61,
          27, 90, 7, 5, 25, 13, 41, 62, 52, 55, 12, 54, 98, 33, 80, 64, 76,
          66, 44, 23, 9, 11, 10, 77, 84, 82, 89, 36, 68, 82, 13, 0, 21, 92,
          81, 13, 85, 17, 26, 16, 89, 83, 6, 2, 79, 39, 57, 64, 54, 18, 31,
          60, 79, 34, 2, 14, 28, 97, 43, 50, 42, 87, 80, 15, 67, 55, 90, 6,
          58, 19, 57, 82, 43, 54, 36, 95, 87, 9, 4, 54, 31, 3, 68, 15, 65,
          9, 72, 84, 80, 89, 62, 33, 18, 66, 98, 66, 10, 4, 15, 81, 13, 71,
          58, 36, 42, 26, 41, 18, 53, 66, ], 21),
        ([-945, -909, -572, -887, -53, -960, -437, -651, -105, -833, -646,
          -650, -743, -999, -542, -908, -372, -927, -669, -529, -49, -903,
          -851, -170, -978, -43, -398, -722, -120, -192, -640, -158, -783,
          -361, -447, -150, -669, -582, -192, -462, -281, -330, -300, -65,
          -490, -298, -607, -967, -208, -810, -138, -40, -309, -822, -646,
          -589, -923, -520, -398, -647, -802, -908, -340, -987, -631, -760,
          -441, -240, -45, -329, 42, 13, -338, -755, -492, -814, 42, -533,
          -211, -954, -859, -797, -731, -630, -715, -544, -559, -886, -935,
          -627, -907, -545, -992, -437, -923, -271, -576, 35, -725, -504,
          -211, -649, -634, -329, 19, -72, -560, -246, -287, -609, -754,
          -918, -77, -940, -455, -436, -847, -311, -38, -185, -591, -868,
          24, -457, -339, -157, -595, -935, -858, -298, -633, -85, -223,
          30, -298, -681, -169, -971, -452, -85, -460, -856, -475, -427,
          -613, -62, -643, -715, -468, -787, -662, -582, -14, -916, -793,
          -791, 46, -64, -796, -407, -911, -667, -642, -435, -24, -150,
          -439, -174, -492, -233, -184, -731, -125, -393, -490, -585, - \
          765, -474, -868, -333, -56, -170, -360, -481, -269, -872, -945,
          -95, -620, -297, -558, -624, -191, -640, -208, -138, -811, 27, -935,
          -565, -475, -129, -817, -413, -613, -32, -872, -722, -139, -662, -8,
          -946, -592, -888, -398, 12, -659, -321, -721, -539, -400, -739, -275,
          -474, -49, -711, 3, -809, -980, -307, -229, -499, -956, 49,
          -852, -86, -63, -768, -93, -513, -55, -68, -187, -697, -391,
          31, -664, -594, -277, -935, -734, -824, -563, -554, -362,
          -478, -827, -952, -449, -198, -26, -118, -682, -91, -509,
          -704, -904, -535, -428, -707, -795, -12, -929, -13, -573,
          -169, -884, -401, -200, -542, -626, -482, -796, -778, -747,
          -961, -44, -923, -26, -989, -311, -426, -957, -11, -232,
          -77, -543, -694, -805, -882, -295, -137, -778, -973, -621,
          -840, -764, -767, -304, -544, -411, -591, 33, -478, -956,
          -854, -232, -41, -868, -517, -94, -421, -982, -453, -697,
          -776, -16, -889, -128, -209, -377, -659, -914, -298, 8,
          -812, -868, -501, -106, -995, -171, -910, -967, -847,
          -520, -16, -305, -938, -841, -516, -906, -298, -623], 680)
    ],
)
def test_solution_cyclic_rotation(input_array: List[int],
                                  expected_result: List[int]):
    assert expected_result == solution_tape_equilibrium(input_array)
