class AOCLib {
    static String getInput(String name) {
        return new File(name).text
    }

    static List<Integer> linesToInts(String lines) {
        return lines.readLines().collect{ it.strip().toInteger() }
    }
}
