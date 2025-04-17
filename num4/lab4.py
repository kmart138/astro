class Rhino:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length  
        self.leg_length = leg_length  
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Rhino Physical Characteristics:")
        print(f"- Arm length: {self.arm_length} cm")
        print(f"- Leg length: {self.leg_length} cm")
        print(f"- Number of eyes: {self.num_eyes}")
        print(f"- Has a tail? {'Yes' if self.has_tail else 'No'}")
        print(f"- Is furry? {'Yes' if self.is_furry else 'No'}")


def main():
    my_rhino = Rhino(
        arm_length=0.0,  # Removed stray 'y'
        leg_length=120.0,
        num_eyes=2,
        has_tail=True,
        is_furry=False
    )

    my_rhino.describe()


if __name__ == "__main__":
    main()
