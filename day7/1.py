from dataclasses import dataclass


@dataclass
class Equation:
    terms: list[int]
    value: int

    @staticmethod
    def parse(data: str) -> "Equation":
        part1, part2 = data.split(": ")
        return Equation([int(x) for x in part2.split()], int(part1))

    def is_valid(self) -> bool:
        # Base case (i.e., we only have one term)
        # Return true if the only term equals the value otherwise false
        if len(self.terms) == 1:
            return self.terms[0] == self.value
        else:
            eq1 = Equation([self.terms[0] * self.terms[1]] + self.terms[2:], self.value)
            eq2 = Equation([self.terms[0] + self.terms[1]] + self.terms[2:], self.value)
            return eq1.is_valid() or eq2.is_valid()


with open("input.txt") as fp:
    lines = fp.read().splitlines()

calibrations = [Equation.parse(line) for line in lines]
print(sum(calibration.value for calibration in calibrations if calibration.is_valid()))
