import time
import asyncio
import curses
from random import randint, choice, random

STARS = ('*', '+', ':', '.')
NUM_STARS = 100


async def blink(canvas, row, column, symbol='*'):
    # time.sleep(random())
    while True:
        canvas.addstr(row, column, symbol, curses.A_INVIS)
        for _ in range(20):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    height, width = canvas.getmaxyx()

    coroutines = [
        blink(canvas, randint(1, height - 2), randint(1, width - 2), choice(STARS)) for _ in range(NUM_STARS)
    ]

    while True:
        for coroutine in coroutines:
            coroutine.send(None)
            canvas.refresh()
        time.sleep(0.1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
