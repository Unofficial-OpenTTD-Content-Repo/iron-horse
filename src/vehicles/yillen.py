from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="yillen",
        base_numeric_id=6370,
        name="Yillen",
        role="heavy_freight",
        role_child_branch_num=1,
        replacement_consist_id="vanguard",  # this line is a strange 10/8 infill, and ends here
        power=2200,
        gen=4,
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=80, vehicle_length=5, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=80, vehicle_length=5, spriterow_num=1
    )

    consist.description = """CABBAGE."""
    consist.foamer_facts = """BR Class 15, BR Class 16"""

    return consist