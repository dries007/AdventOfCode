#!/usr/bin/env groovy

String SAMPLE_1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

static def part1(String inp) {
    int pos = 0
    int depth = 0

    inp.readLines().each {
        def (cmd, x) = it.split(' ')
        x = Integer.valueOf(x as String)
        switch (cmd) {
            case "forward":
                pos += x
                break
            case "down":
                depth += x
                break
            case "up":
                depth -= x
                break
        }
    }

    println("pos: $pos depth: $depth")

    return pos * depth
}

static def part2(String inp) {
    int pos = 0
    int depth = 0
    int aim = 0

    inp.readLines().each {
        def (cmd, x) = it.split(' ')
        x = Integer.valueOf(x as String)
        switch (cmd) {
            case "forward":
                pos += x
                depth += x * aim
                break
            case "down":
                aim += x
                break
            case "up":
                aim -= x
                break
        }
    }

    println("pos: $pos depth: $depth")

    return pos * depth
}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp2.txt")))


println(part2(SAMPLE_1))
println(part2(AOCLib.getInput("inp2.txt")))

