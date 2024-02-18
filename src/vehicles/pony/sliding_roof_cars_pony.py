from train import FlatCarSlidingRoofConsist, FreightCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    consist = FlatCarSlidingRoofConsist(
        roster_id=roster_id,
        base_numeric_id=14270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = FlatCarSlidingRoofConsist(
        roster_id=roster_id,
        base_numeric_id=14280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")