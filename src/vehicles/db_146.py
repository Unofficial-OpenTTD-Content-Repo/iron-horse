from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="db_146",
        base_numeric_id=13090,
        name="DB 146 !! Multisystem",
        role="heavy_express",
        role_child_branch_num=2,
        power=6000,
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        #intro_date_offset=5,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """DB 146 / TRAXX"""

    return consist
