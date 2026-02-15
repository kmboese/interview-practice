import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Problem12 {
    public static void main(String [] args) {
        int num = 48; // "XLVIII"
        List<Integer> inputs = List.of(3749, 58, 1994);
        for (int input : inputs) {
            String result = intToRoman(input);
            System.out.printf("Converting %d to numeral = %s%n", input, result);
        }
    }
    static class Numeral {
        String phrase;
        int value;

        public Numeral(String phrase, int value) {
            this.phrase = phrase;
            this.value = value;
        }

        String getPhrase() {
            return phrase;
        }

        int getValue() {
            return value;
        }
    }

    private static final Map<Integer, Numeral> valueToRomanNumeral;
    static {
        valueToRomanNumeral = new HashMap<>();
        valueToRomanNumeral.put(1, new Numeral("I", 1));
        valueToRomanNumeral.put(5, new Numeral("V", 5));
        valueToRomanNumeral.put(10, new Numeral("X", 10));
        valueToRomanNumeral.put(50, new Numeral("L", 50));
        valueToRomanNumeral.put(100, new Numeral("C", 100));
        valueToRomanNumeral.put(500, new Numeral("D", 500));
        valueToRomanNumeral.put(1000, new Numeral("M", 1000));
        valueToRomanNumeral.put(4, new Numeral("IV", 4));
        valueToRomanNumeral.put(9, new Numeral("IX", 9));
        valueToRomanNumeral.put(40, new Numeral("XL", 40));
        valueToRomanNumeral.put(90, new Numeral("XC", 90));
        valueToRomanNumeral.put(400, new Numeral("CD", 400));
        valueToRomanNumeral.put(900, new Numeral("CM", 900));
    }

    public static String intToRoman(int num) {
        int remainder = num;
        StringBuilder result = new StringBuilder(1000);

        while (remainder > 0) {
            Numeral numeral = convertValueToNumeral(remainder);
            result.append(numeral.getPhrase());
            remainder -= numeral.getValue();
        }

        return result.toString();
    }

    private static Numeral convertValueToNumeral(int value) {
        String valueString = Integer.toString(value);
        int firstNumber = Integer.parseInt(valueString.substring(0, 1));
        int magnitude = getMagnitude(valueString);

        return getNumeral(firstNumber, magnitude);
    }

    private static Numeral getNumeral(int firstDigitValue, int magnitude) {
        if (firstDigitValue != 4 && firstDigitValue != 9) {
            return getMaxNumeral(firstDigitValue*magnitude);
        } else {
            return getSubtractiveNumeral(firstDigitValue, magnitude);
        }
    }

    private static Numeral getSubtractiveNumeral(int firstDigit, int magnitude) {
        return valueToRomanNumeral.get(firstDigit * magnitude);
    }

    private static Numeral getMaxNumeral(int value) {
        Numeral maxNumeral;
        if (value >= 1000) {
            maxNumeral = valueToRomanNumeral.get(1000);
        } else if (value >= 500) {
            maxNumeral = valueToRomanNumeral.get(500);
        } else if (value >= 100) {
            maxNumeral = valueToRomanNumeral.get(100);
        } else if (value >= 50) {
            maxNumeral = valueToRomanNumeral.get(50);
        } else if (value >= 10) {
            maxNumeral = valueToRomanNumeral.get(10);
        } else if (value >= 5) {
            maxNumeral = valueToRomanNumeral.get(5);
        } else {
            maxNumeral = valueToRomanNumeral.get(1);
        }
        return maxNumeral;
    }

    private static int getMagnitude(String valueString) {
        return (int) Math.pow(10, valueString.length() - 1);
    }
}