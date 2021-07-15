if __name__ == "__main__":
    file = open("PLANTILLA_ICO_2021B.txt", "r")
    data = file.readlines()
    file.close()

    data1 = data[58:]

    uas = []
    mat = set()

    for i in range(len(data1)):
        data1[i] = data1[i].replace("\n", "")

    for reg in range(int(len(data1) / 25)):
        ua = data1[reg * 25: (25 * (reg + 1))]
        uas.append(ua)
        mat.add(ua[3])
        print(ua)

    print(mat)
