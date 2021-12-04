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

static def most_common_bin(lines, boolean inv = false) {
    def one_counts = new int[lines[0].size()]
    lines.each {
        it.chars.eachWithIndex { c, i -> {
            if (c == '1')
                one_counts[i] += 1
        }}
    }
    return one_counts.collect { ((it > lines.size() / 2) ^ inv) ? '1' : '0' }.join()
}

static def part1(String inp) {
    def lines = inp.readLines()
    def ones_common = most_common_bin(lines)
    def zeros_common = most_common_bin(lines, true)
    def gamma = Integer.parseInt(ones_common, 2)
    def epsilon = Integer.parseInt(zeros_common, 2)
    println(gamma)
    println(epsilon)
    return gamma * epsilon
}

static def filter(boolean co2, List<String> lines, int digit = 0) {
    int ones = 0
    int zeros = 0
    lines.each {if (it[digit] == '1') ones ++ else zeros ++ }
    println("digit $digit: zeros=$zeros ones=$ones")

    def mask = '0'
    if (!co2 && (ones == zeros || ones > zeros)) mask = '1'
    if (co2 && ones < zeros) mask = '1'
    println("digit $digit: mask=$mask")

    lines = lines.findAll {it[digit] == mask }
    println("digit $digit: lines=$lines")

    if (lines.size() == 1) return Integer.parseInt(lines[0], 2)

    return filter(co2, lines, digit + 1)
}

static def part2(String inp) {
    def lines = inp.readLines()
    def o2 = filter(false, lines)
    def co2 = filter(true, lines)
    println(o2)
    println(co2)
    return o2 * co2
}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp3.txt")))

println(part2(SAMPLE_1))
println(part2(AOCLib.getInput("inp3.txt")))
