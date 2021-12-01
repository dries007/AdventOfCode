#!/usr/bin/env groovy

String SAMPLE_1 = """199
200
208
210
200
207
240
269
260
263"""

static def part1(String inp) {
    def depths = AOCLib.linesToInts(inp)
    depths.collate(2, 1, false).count { prev, curr -> curr > prev }
}

static def part2(String inp) {
    def depths = AOCLib.linesToInts(inp)
    depths = depths.collate(3, 1, false).collect{it.sum()}
    println(depths)
    depths.collate(2, 1, false).count { prev, curr -> curr > prev }
}

def inp = AOCLib.getInput('inp1.txt')

println("part1")
println(part1(SAMPLE_1))
println(part1(inp))
println("part2")
println(part2(SAMPLE_1))
println(part2(inp))

