from train import HopperCarRandomisedConsist, FreightCar


def main(roster_id):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=12590,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=10690,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=9620,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16860,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=14090,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16880,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16890,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16900,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16910,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=8430,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16930,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = HopperCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16940,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")