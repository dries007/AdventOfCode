#!/usr/bin/env groovy
import java.util.stream.Stream

String SAMPLE_1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

class Point {
    final int x, y

    Point(int x, int y) {
        this.x = x
        this.y = y
    }

    static Point parse(String s) {
        def (x, y) = s.split(',')
        return new Point(Integer.parseInt(x), Integer.parseInt(y))
    }

    String toString() { x + "," + y }
}

class Line {
    final Point a, b

    Line(Point a, Point b) {
        this.a = a
        this.b = b
    }

    static Line fromInput(String s) {
        def (a, b) = s.split(' -> ')
        return new Line(Point.parse(a), Point.parse(b))
    }

    boolean horizontal() { a.y == b.y }
    boolean vertical() { a.x == b.x }

    String toString() { "Line{" + a + " -> " + b + "}" }
}

static void printBoard(List<List<Integer>> board) {
    println('-' * board[0].size())
    board.each {row ->
        println(row.collect { it == 0 ? '.' : it > 9 ? '#' : it.toString()}.join(''))
    }
    println('-' * board[0].size())
}

static def part1(String inp, int size = 1000) {
    List<Line> lines = inp.lines().map(Line::fromInput).filter{it.horizontal() or it.vertical()}.toList()
    List<List<Integer>> board = Stream.generate{-> [0]*size}.limit(size).toList()
    lines.each {
        if (it.horizontal()) {
            int y = it.a.y
            int x1 = Integer.min(it.a.x, it.b.x)
            int x2 = Integer.max(it.a.x, it.b.x)
            for (def x in x1..x2) {
                board[y][x] += 1
            }
        } else if (it.vertical()) {
            int x = it.a.x
            int y1 = Integer.min(it.a.y, it.b.y)
            int y2 = Integer.max(it.a.y, it.b.y)
            for (def y in y1..y2) {
                board[y][x] += 1
            }
        }
    }
    printBoard(board)
    return board.sum {it.count {it >= 2}}
}

static def part2(String inp, int size = 1000) {
    List<Line> lines = inp.lines().map(Line::fromInput).toList()
    List<List<Integer>> board = Stream.generate{-> [0]*size}.limit(size).toList()
    lines.each {
        if (it.horizontal()) {
            int y = it.a.y
            int x1 = Integer.min(it.a.x, it.b.x)
            int x2 = Integer.max(it.a.x, it.b.x)
            for (def x in x1..x2) {
                board[y][x] += 1
            }
        } else if (it.vertical()) {
            int x = it.a.x
            int y1 = Integer.min(it.a.y, it.b.y)
            int y2 = Integer.max(it.a.y, it.b.y)
            for (def y in y1..y2) {
                board[y][x] += 1
            }
        } else {
            int dx = it.a.x < it.b.x ? 1 : -1
            int dy = it.a.y < it.b.y ? 1 : -1
            int x = it.a.x, y = it.a.y
            while (x != it.b.x && y != it.b.y) {
                board[y][x] += 1
                x += dx
                y += dy
            }
            board[y][x] += 1
        }
    }
    printBoard(board)
    return board.sum {it.count {it >= 2}}
}

println(part1(SAMPLE_1, 10))
println(part1(AOCLib.getInput("inp5.txt")))

println(part2(SAMPLE_1, 10))
println(part2(AOCLib.getInput("inp5.txt")))
