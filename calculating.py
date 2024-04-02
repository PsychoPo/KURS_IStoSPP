from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QScrollBar, QGraphicsTextItem, QTableWidgetItem
from PyQt6.QtGui import QColor, QPen, QFont
from PyQt6.QtCore import Qt
from copy import deepcopy, copy


def full_time(matr, r):
    mcopy = deepcopy(matr)
    cop = deepcopy(matr)

    for n in range(len(r)):
        for i in range(len(mcopy)):
            for j in range(len(mcopy[0])):
                if r[n] - 1 == j:
                    mcopy[i][n] = cop[i][j]

    for i in range(1):
        for j in range(1, len(mcopy[i])):
            mcopy[i][j] = mcopy[i][j] + mcopy[i][j - 1]

    for i in range(1):
        for j in range(1, len(mcopy)):
            mcopy[j][i] = mcopy[j][i] + mcopy[j - 1][i]

    for i in range(1, len(mcopy[i])):
        for j in range(1, len(mcopy)):
            mcopy[j][i] = mcopy[j][i] + max(mcopy[j - 1][i], mcopy[j][i - 1])

    return mcopy[len(mcopy) - 1][len(mcopy[0]) - 1]


def rec1_sokol(matr):
    r = []
    sum = []

    for i in range(len(matr[0])):
        temp_sum = 0
        for j in range(len(matr) - 1):
            temp_sum += matr[j][i]
        sum.append(temp_sum)

    sumcopy = deepcopy(sum)
    sumcopy.sort()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j)

    r = list(dict.fromkeys(r))

    return r


def rec2_sokol(matr):
    r = []
    sum = []

    for i in range(len(matr[0])):
        temp_sum = 0
        for j in range(len(matr)):
            if j == 0:
                pass
            else:
                temp_sum += matr[j][i]
        sum.append(temp_sum)

    sumcopy = deepcopy(sum)
    sumcopy.sort()
    sumcopy.reverse()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j)

    r = list(dict.fromkeys(r))

    return r


def rec3_sokol(matr):
    r = []
    diff = []

    for i in range(len(matr[0])):
        diff1 = 0
        diff2 = 0
        for j in range(len(matr)):
            if j == 0:
                diff1 = matr[j][i]
            elif j == len(matr) - 1:
                diff2 = matr[j][i]
        diff3 = diff2 - diff1
        diff.append(diff3)

    diffcopy = deepcopy(diff)
    diffcopy.sort()
    diffcopy.reverse()

    for k in diffcopy:
        for i in range(len(matr[0])):
            diff1 = 0
            diff2 = 0
            for j in range(len(matr)):
                if j == 0:
                    diff1 = matr[j][i]
                elif j == len(matr) - 1:
                    diff2 = matr[j][i]
            if diff2 - diff1 == k:
                r.append(i)

    r = list(dict.fromkeys(r))

    return r


def sokol_final_seq(matrix, r1, r2, r3):
    p1 = full_time(matrix, r1)
    p2 = full_time(matrix, r2)
    p3 = full_time(matrix, r3)

    for i in range(len(r1)):
        r1[i] = r1[i] + 1
        r2[i] = r2[i] + 1
        r3[i] = r3[i] + 1

    if p1 < p2 and p1 < p3:
        return r1
    elif p2 < p1 and p2 < p3:
        return r2
    else:
        return r3


def rec1_jons(matr):
    r = []
    mcopy = deepcopy(matr[0])
    mcopy.sort()

    for i in mcopy:
        for j in range(1):
            for k in range(len(matr[j])):
                if matr[j][k] == i:
                    r.append(k)

    r = list(dict.fromkeys(r))

    return r


def rec2_jons(matr):
    r = []
    mcopy = deepcopy(matr[len(matr) - 1])
    mcopy.sort()
    mcopy.reverse()

    for i in mcopy:
        for j in range(len(matr) - 1, len(matr)):
            for k in range(len(matr[j])):
                if matr[j][k] == i:
                    r.append(k)

    r = list(dict.fromkeys(r))
    return r


def rec4_jons(matr):
    r = []
    sumMatr = []

    for i in range(len(matr[0])):
        sum = 0
        for j in range(len(matr)):
            sum += matr[j][i]
        sumMatr.append(sum)

    mcopy = deepcopy(sumMatr)
    mcopy.sort()
    mcopy.reverse()

    for i in mcopy:
        for j in range(len(sumMatr)):
            if sumMatr[j] == i:
                r.append(j)

    r = list(dict.fromkeys(r))
    return r


def jons_final_seq(r1, r2, r3):
    r = []
    sum = []

    for i in range(len(r1)):
        for a in range(len(r1)):
            if i == r1[a]:
                sum.append(a + 1)
        for b in range(len(r2)):
            if i == r2[b]:
                sum[i] += (b + 1)
        for c in range(len(r3)):
            if i == r3[c]:
                sum[i] += (c + 1)

    sumcopy = deepcopy(sum)
    sumcopy.sort()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j + 1)

    r = list(dict.fromkeys(r))

    return r


def final_matrix(matr, r):
    mcopy = deepcopy(matr)
    cop = deepcopy(matr)

    for n in range(len(r)):
        for i in range(len(mcopy)):
            for j in range(len(mcopy[0])):
                if r[n] - 1 == j:
                    mcopy[i][n] = cop[i][j]

    return mcopy


def sum_x1(matrix, i):
    sum = 0
    for k in range(i):
        sum += matrix[k][0]
    return sum


def sum_x2(matrix, i, j):
    sum = 0
    for a in range(i, i + 1):
        for b in range(j):
            sum += matrix[a][b]
    return sum


def draw_gantt_chart(matrix, scene, parent):
    colors = ['#EB9D42', '#EBE442', '#8CEB42', '#42EBAE', '#42D7EB',
              '#428FEB', '#4542EB', '#8C42EB', '#C942EB', '#EB4256']

    x_matrix = deepcopy(matrix)
    x1 = 100
    x2 = matrix[0][0] * 10 + x1
    x = 0

    line_y1 = 100
    line_y2 = 140

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            color = QColor(colors[j])

            if i == 0 and j == 0:
                rect = QGraphicsRectItem(
                    x1, line_y1, x2 - x1, line_y2 - line_y1)
                rect.setBrush(color)
                rect.setPen(QPen(color))
                scene.addItem(rect)

                x = x2 - x1
                x_matrix[i][j] = x

                text_item = QGraphicsTextItem(f"{i + 1}")
                text_item.setDefaultTextColor(Qt.GlobalColor.black)
                text_item.setFont(QFont("Arial", 12))
                text_item.setPos(25, line_y1 + 17)
                scene.addItem(text_item)

                line = QGraphicsRectItem(45, line_y1 + 17, 10, 2)
                line.setPen(QPen(Qt.GlobalColor.black))
                scene.addItem(line)

            elif j == 0 and i != 0:
                x = 0
                line_y1 += 50
                line_y2 += 50
                x1 = (sum_x1(matrix, i) * 10) + 100
                x2 = x1 + matrix[i][j] * 10

                rect = QGraphicsRectItem(
                    x1, line_y1, x2 - x1, line_y2 - line_y1)
                rect.setBrush(color)
                rect.setPen(QPen(color))
                scene.addItem(rect)

                x += (x2 - x1) + ((sum_x1(matrix, i) * 10))
                x_matrix[i][j] = x

                text_item = QGraphicsTextItem(f"{i + 1}")
                text_item.setDefaultTextColor(Qt.GlobalColor.black)
                text_item.setFont(QFont("Arial", 12))
                text_item.setPos(25, line_y1 + 17)
                scene.addItem(text_item)

                line = QGraphicsRectItem(45, line_y1 + 17, 10, 2)
                line.setPen(QPen(Qt.GlobalColor.black))
                scene.addItem(line)

            else:
                if i >= 1 and j != 0:
                    if x_matrix[i - 1][j] > x_matrix[i][j - 1]:
                        x1 = (x2 + ((x_matrix[i - 1][j] - x_matrix[i][j - 1])))
                        x2 = x1 + matrix[i][j] * 10

                        rect = QGraphicsRectItem(
                            x1, line_y1, x2 - x1, line_y2 - line_y1)
                        rect.setBrush(color)
                        rect.setPen(QPen(color))
                        scene.addItem(rect)

                        x += (x2 - x1) + \
                            (x_matrix[i - 1][j] - x_matrix[i][j - 1])
                        x_matrix[i][j] = x

                    else:
                        x1 = x2
                        x2 = x1 + matrix[i][j] * 10

                        rect = QGraphicsRectItem(
                            x1, line_y1, x2 - x1, line_y2 - line_y1)
                        rect.setBrush(color)
                        rect.setPen(QPen(color))
                        scene.addItem(rect)

                        x += x2 - x1
                        x_matrix[i][j] = x

                else:
                    x1 = x2
                    x2 = x1 + matrix[i][j] * 10

                    rect = QGraphicsRectItem(
                        x1, line_y1, x2 - x1, line_y2 - line_y1)
                    rect.setBrush(color)
                    rect.setPen(QPen(color))
                    scene.addItem(rect)

                    x += x2 - x1
                    x_matrix[i][j] = x

    line = QGraphicsRectItem(50, 50, 50, (50 * len(matrix)) + 90)
    line.setPen(QPen(Qt.GlobalColor.black))
    scene.addItem(line)

    line = QGraphicsRectItem(50, 140 + (50 * len(matrix)),
                             x_matrix[len(x_matrix) - 1][len(x_matrix[0]) - 1] + 200, 50)
    line.setPen(QPen(Qt.GlobalColor.black))
    scene.addItem(line)

    ox_x = 100
    for i in range((x_matrix[len(x_matrix) - 1][len(x_matrix[0]) - 1] + 100)):
        if i == 0 or i % 50 == 0:
            line = QGraphicsRectItem(ox_x, 140 + (50 * len(matrix)) - 5, 2, 10)
            line.setPen(QPen(Qt.GlobalColor.black))
            scene.addItem(line)

            text_item = QGraphicsTextItem(f"{i + 1}")
            text_item.setDefaultTextColor(Qt.GlobalColor.black)
            text_item.setFont(QFont("Arial", 12))
            text_item.setPos(25, line_y1 + 17)
            scene.addItem(text_item)

            ox_x += 50


def calculate(matrix, rdBtn_johns, rdBtn_PetSok, table_widget):
    if rdBtn_johns.isChecked():
        result = jons_final_seq(rec1_jons(matrix),
                                rec2_jons(matrix),
                                rec4_jons(matrix))
        result_matrix = final_matrix(matrix, result)
        rows = len(result_matrix)
        cols = len(result_matrix[0])
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(cols)
        headers = []
        for i in range(cols):
            headers.append(f"Станок {i+1}")
        table_widget.setHorizontalHeaderLabels(headers)
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(result_matrix[row][col]))
                table_widget.setItem(row, col, item)
        table_widget.resizeColumnsToContents()
        table_widget.resizeRowsToContents()
    elif rdBtn_PetSok.isChecked():
        result = sokol_final_seq(matrix, rec1_sokol(matrix),
                                 rec2_sokol(matrix),
                                 rec3_sokol(matrix))
        result_matrix = final_matrix(matrix, result)
        rows = len(result_matrix)
        cols = len(result_matrix[0])
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(cols)
        headers = []
        for i in range(cols):
            headers.append(f"Станок {i+1}")
        table_widget.setHorizontalHeaderLabels(headers)
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(result_matrix[row][col]))
                table_widget.setItem(row, col, item)
        table_widget.resizeColumnsToContents()
        table_widget.resizeRowsToContents()

    return str(result)
