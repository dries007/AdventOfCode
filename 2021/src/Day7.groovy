#!/usr/bin/env groovy

String SAMPLE_1 = "16,1,2,0,4,2,7,1,2,14"


static def part1(String inp) {
    // Intuition says the mean value should be the center easiest to get to
    List<Integer> crabs = inp.split(',').collect{Integer.parseInt(it) }.sort()
    Integer pos = -1
    if (crabs.size() % 2 == 0) {
        // Ugly code alert. No check to see if mean is float. Works out for my inp. YMMV
        pos = (crabs[crabs.size() / 2] + crabs[(crabs.size() / 2) - 1]) / 2 as int
        println('even')
    } else {
        pos = crabs[crabs.size() / 2]
        println('odd')
    }
    println(pos)
    crabs.sum {Math.abs(it - pos)}
}


static def part2(String inp) {
    // Average = center, but ceil or floor depends on who needs to come furthest (I think)
    // But better to calc 2 values and don't have to think too hard about it :P
    List<Integer> crabs = inp.split(',').collect{Integer.parseInt(it) }.sort()
    def avg = crabs.average() as float
    def posF = Math.floor(avg)
    def posC = Math.ceil(avg)
    println("$posF <= $avg <= $posC")
    def sumF = crabs.sum {(0..Math.abs(it - posF)).sum() }
    def sumC = crabs.sum {(0..Math.abs(it - posC)).sum() }
    println("$sumC or $sumF")
    Math.min(sumC, sumF)
}

println(part1(SAMPLE_1))
println(part1(AOCLib.getInput("inp7.txt")))

println(part2(SAMPLE_1))
println(part2(AOCLib.getInput("inp7.txt")))
