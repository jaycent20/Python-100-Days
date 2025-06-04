"""
简单的迷宫游戏 - 使用WASD键移动玩家从起点到终点。

运行后在终端输入 w/a/s/d 控制方向，q 键退出游戏。
"""

import os

WALL = '#'
PATH = ' '
EXIT = 'E'
PLAYER = 'P'

MAZE_MAP = [
    list("##########"),
    list("#        #"),
    list("# ###### #"),
    list("# #    # #"),
    list("# # ## # #"),
    list("# # ## # #"),
    list("#   ##   #"),
    list("###    ###"),
    list("#      E #"),
    list("##########"),
]


def display(maze, player_pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, row in enumerate(maze):
        line = ''
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                line += PLAYER
            else:
                line += cell
        print(line)


def main():
    maze = [row[:] for row in MAZE_MAP]
    x, y = 1, 1
    display(maze, (x, y))
    while True:
        move = input('移动(w/a/s/d), q退出: ').lower()
        if move == 'q':
            print('游戏结束')
            break
        dx, dy = 0, 0
        if move == 'w':
            dx = -1
        elif move == 's':
            dx = 1
        elif move == 'a':
            dy = -1
        elif move == 'd':
            dy = 1
        else:
            continue
        nx, ny = x + dx, y + dy
        if maze[nx][ny] != WALL:
            x, y = nx, ny
        display(maze, (x, y))
        if maze[x][y] == EXIT:
            print('恭喜通关!')
            break


if __name__ == '__main__':
    main()
