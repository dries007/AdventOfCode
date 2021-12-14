#!/usr/bin/env groovy

String SAMPLE_1 = "3,4,3,1,2"

static def part1(String inp) {
    List<Byte> fishes = new ArrayList<>()
    fishes.addAll(inp.split(',').collect{Byte.parseByte(it) })
    for (def i in 1..80) {
        def toAdd = 0
        for (def j in 0..<fishes.size()) {
            def x = fishes[j]
            if (x == 0) {
                toAdd++
                fishes[j] = 6
            } else {
                fishes[j] = x - 1
            }
        }
        fishes += [8] * toAdd
        println("$i: ${fishes.size()}")
    }
    return fishes.size()
}

static def part2(String inp) {
    // "stroke of genius": Use list of nr of fishes of age x as "shift register"/"stack".
    // Example >> 2^31
    List<Long> fishes = inp.split(',').collect{Long.parseLong(it) }
    fishes = (0..8).collect{ fishes.count(it).longValue() }
    println("Init: ${fishes.sum()}")
    for (def i in 1..256) {
        Long n = fishes.pop()
        fishes.add(n)
        fishes[6] += n
        println("$i: ${fishes.sum()}")
    }
}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp6.txt")))

println(part2(SAMPLE_1))
println(part2(AOCLib.getInput("inp6.txt")))
