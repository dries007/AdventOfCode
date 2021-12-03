#!/usr/bin/env groovy

String SAMPLE_1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

static def most_common_bin(lines) {
    def one_counts = new int[lines[0].size()]
    lines.each {
        it.chars.eachWithIndex { c, i -> {
            if (c == '1')
                one_counts[i] += 1
        }}
    }
    return one_counts.collect { it > lines.size() / 2 ? 1 : 0 }
}

static def part1(String inp) {
    def lines = inp.readLines()
    def ones_common = most_common_bin(lines)
    def gamma = Integer.parseInt(ones_common.collect { it ? '1' : '0' }.join(), 2)
    def epsilon = Integer.parseInt(ones_common.collect { !it ? '1' : '0' }.join(), 2)
//    println(gamma)
//    println(epsilon)
    return gamma * epsilon
}

static def part2(String inp) {

}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp3.txt")))

//println(part2(SAMPLE_1))
//println(part2(AOCLib.getInput("inp3.txt")))
