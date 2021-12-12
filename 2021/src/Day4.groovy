#!/usr/bin/env groovy

String SAMPLE_1 = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Board {
    public static final String BOLD = '\033[1m'
    public static final String RESET = '\033[0m'
    public static final String NUMBER = '%2d'
    public static final String MARKED = BOLD + NUMBER + RESET

    private final List<List<Integer>> numbers;
    private final List<List<Boolean>> marked;
    boolean won = false

    Board(String inp) {
        numbers = inp.readLines().collect {it.split().collect{Integer.parseInt(it)}}
        marked = [
                [false, false, false, false, false],
                [false, false, false, false, false],
                [false, false, false, false, false],
                [false, false, false, false, false],
                [false, false, false, false, false],
            ]
    }

    String toString() {
        String str = 'Board{\n'
        numbers.eachWithIndex { List<Integer> row, int y -> {
            row.eachWithIndex { int entry, int x -> {
                str += String.format(marked[y][x] ? MARKED : NUMBER, entry) + ' '
            }}
            str += '\n'
        }}
        str += '}\n'
        return str
    }

    boolean call(int call) {
        boolean flag = false
        numbers.eachWithIndex { List<Integer> row, int y -> {
            row.eachWithIndex { int entry, int x -> {
                if (entry == call) {
                    flag = true
                    marked[y][x] = true
                }
            }}
        }}
        if (flag) {
            List<Integer> rows = marked.collect{ List<Boolean> row -> { row.sum { it ? 1 : 0} as int }} as List<Integer>
            List<Integer> cols = [0, 0, 0, 0, 0]
            for (def y in 0..<5) for (def x in 0..<5) if (marked[y][x]) cols[x] += 1
            return rows.any {it == 5} || cols.any {it == 5}
        }
        return false
    }

    int score() {
        int count = 0
        numbers.eachWithIndex { List<Integer> row, int y -> {
            row.eachWithIndex { int entry, int x -> {
                if (!marked[y][x]) {
                    count += entry
                }
            }}
        }}
        return count
    }
}

static def part1(String inp) {
    List<String> tmp = inp.split(/\n\n/)
    List<Integer> calls = tmp.pop().split(',').collect {Integer.parseInt(it)}
    List<Board> boards = tmp.collect {new Board(it)}
    for (call in calls) {
        println("Calling ${call}")
        for (board in boards) {
            if (board.call(call)) {
                println("Won!: ${board}")
                return board.score() * call
            }
        }
    }
}

static def part2(String inp) {
    List<String> tmp = inp.split(/\n\n/)
    List<Integer> calls = tmp.pop().split(',').collect {Integer.parseInt(it)}
    List<Board> boards = tmp.collect {new Board(it)}
    for (call in calls) {
        println("Calling ${call}")
        for (board in boards) {
            if (board.call(call)) {
                board.won = true
                println("Won!: ${board}")
                if (boards.size() == 1) {
                    return board.score() * call
                }
            }
        }
        boards = boards.findAll {!it.won}
    }
}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp4.txt")))

println(part2(SAMPLE_1))
println(part2(AOCLib.getInput("inp4.txt")))
