from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="mumble_single",
        base_numeric_id=9180,
        name="Mumble",
        role="pax_railbus",
        role_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 250,
        },
        gen=3,
        buyable_variant_group_id="mumble", # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = """Vitesse. Confort. Exactitude. This railcar has none of those. But it is cheap to run."""
    consist.foamer_facts = """CFC Autorail Billard, CFC X2000/X5000"""

    return consist
