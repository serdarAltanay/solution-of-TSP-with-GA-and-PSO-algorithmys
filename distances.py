distances_6 = [
    [0, 29, 20, 21, 16, 31],
    [29, 0, 15, 17, 28, 23],
    [20, 15, 0, 30, 26, 40],
    [21, 17, 30, 0, 18, 22],
    [16, 28, 26, 18, 0, 25],
    [31, 23, 40, 22, 25, 0]
]

distances_10 = [
    [0, 29, 20, 21, 16, 31, 29, 20, 21, 16],
    [29, 0, 15, 17, 28, 23, 15, 17, 28, 23],
    [20, 15, 0, 30, 26, 40, 30, 26, 40, 33],
    [21, 17, 30, 0, 18, 22, 18, 22, 21, 27],
    [16, 28, 26, 18, 0, 25, 26, 27, 25, 30],
    [31, 23, 40, 22, 25, 0, 40, 35, 22, 27],
    [29, 15, 30, 18, 26, 40, 0, 14, 19, 28],
    [20, 17, 26, 22, 27, 35, 14, 0, 23, 32],
    [21, 28, 40, 21, 25, 22, 19, 23, 0, 19],
    [16, 23, 33, 27, 30, 27, 28, 32, 19, 0]
]

distances_15 = [
    [0, 72, 78, 40, 39, 62, 94, 48, 74, 56, 74, 53, 85, 77, 77],
    [72, 0, 95, 89, 80, 90, 82, 60, 71, 89, 94, 76, 97, 92, 90],
    [78, 95, 0, 97, 45, 48, 81, 41, 83, 58, 60, 76, 53, 45, 77],
    [40, 89, 97, 0, 91, 63, 73, 98, 73, 85, 72, 73, 83, 93, 70],
    [39, 80, 45, 91, 0, 46, 88, 48, 70, 91, 53, 85, 67, 60, 65],
    [62, 90, 48, 63, 46, 0, 68, 52, 58, 79, 77, 74, 97, 76, 73],
    [94, 82, 81, 73, 88, 68, 0, 72, 76, 91, 75, 58, 90, 90, 94],
    [48, 60, 41, 98, 48, 52, 72, 0, 60, 75, 85, 88, 55, 69, 66],
    [74, 71, 83, 73, 70, 58, 76, 60, 0, 60, 51, 73, 74, 72, 63],
    [56, 89, 58, 85, 91, 79, 91, 75, 60, 0, 65, 96, 80, 73, 97],
    [74, 94, 60, 72, 53, 77, 75, 85, 51, 65, 0, 58, 70, 68, 81],
    [53, 76, 76, 73, 85, 74, 58, 88, 73, 96, 58, 0, 94, 75, 88],
    [85, 97, 53, 83, 67, 97, 90, 55, 74, 80, 70, 94, 0, 82, 72],
    [77, 92, 45, 93, 60, 76, 90, 69, 72, 73, 68, 75, 82, 0, 78],
    [77, 90, 77, 70, 65, 73, 94, 66, 63, 97, 81, 88, 72, 78, 0]
]

distances_20 = [
    [0, 33, 84, 91, 37, 96, 43, 56, 75, 47, 45, 67, 80, 67, 94, 32, 74, 91, 82, 72],
    [33, 0, 64, 90, 44, 61, 45, 79, 79, 96, 55, 77, 70, 76, 58, 99, 91, 97, 75, 56],
    [84, 64, 0, 89, 81, 59, 69, 45, 81, 76, 62, 99, 73, 79, 71, 92, 91, 54, 72, 90],
    [91, 90, 89, 0, 75, 76, 65, 72, 94, 79, 72, 97, 64, 64, 58, 82, 61, 83, 91, 57],
    [37, 44, 81, 75, 0, 76, 88, 81, 51, 59, 83, 80, 47, 62, 57, 56, 70, 75, 69, 82],
    [96, 61, 59, 76, 76, 0, 70, 73, 91, 82, 67, 51, 95, 61, 58, 76, 84, 66, 80, 95],
    [43, 45, 69, 65, 88, 70, 0, 70, 55, 53, 96, 96, 83, 47, 50, 85, 70, 93, 54, 75],
    [56, 79, 45, 72, 81, 73, 70, 0, 90, 58, 59, 74, 69, 77, 80, 72, 74, 94, 55, 90],
    [75, 79, 81, 94, 51, 91, 55, 90, 0, 92, 82, 77, 76, 85, 64, 68, 91, 93, 82, 82],
    [47, 96, 76, 79, 59, 82, 53, 58, 92, 0, 91, 97, 82, 75, 92, 97, 56, 99, 84, 55],
    [45, 55, 62, 72, 83, 67, 96, 59, 82, 91, 0, 74, 56, 52, 59, 71, 80, 88, 67, 78],
    [67, 77, 99, 97, 80, 51, 96, 74, 77, 97, 74, 0, 60, 92, 96, 82, 57, 94, 96, 85],
    [80, 70, 73, 64, 47, 95, 83, 69, 76, 82, 56, 60, 0, 79, 78, 84, 55, 77, 66, 69],
    [67, 76, 79, 64, 62, 61, 47, 77, 85, 75, 52, 92, 79, 0, 76, 76, 59, 81, 69, 91],
    [94, 58, 71, 58, 57, 58, 50, 80, 64, 92, 59, 96, 78, 76, 0, 80, 78, 63, 59, 77],
    [32, 99, 92, 82, 56, 76, 85, 72, 68, 97, 71, 82, 84, 76, 80, 0, 75, 93, 91, 84],
    [74, 91, 91, 61, 70, 84, 70, 74, 91, 56, 80, 57, 55, 59, 78, 75, 0, 82, 88, 64],
    [91, 97, 54, 83, 75, 66, 93, 94, 93, 99, 88, 94, 77, 81, 63, 93, 82, 0, 65, 81],
    [82, 75, 72, 91, 69, 80, 54, 55, 82, 84, 67, 96, 66, 69, 59, 91, 88, 65, 0, 70],
    [72, 56, 90, 57, 82, 95, 75, 90, 82, 55, 78, 85, 69, 91, 77, 84, 64, 81, 70, 0]
]   
