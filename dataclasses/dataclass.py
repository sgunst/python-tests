from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class Embedded:
    prop: str


@dataclass
class TestClass:
    test_id: int
    test_name: str
    embed: Embedded
    number: int = 8

    def multiply(self) -> int:
        print(self.test_id * self.number)
        self.blabla = "blabla"  # we add an attribute, but is not part of the dataclass-fields
        return self.test_id * self.number


if __name__ == "__main__":
    a = TestClass(test_id=5, test_name="mijntest", embed=Embedded(prop="lol"))
    a.multiply()
    print(a)
    print(a.__dict__)
    print(asdict(a))
    print(a.__dict__)
    print("hastalavista")
