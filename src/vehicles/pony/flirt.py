from train import PassengerEngineRailbusConsist, DieselRailcarCombineUnitMail, DieselRailcarCombineUnitPax


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="flirt",
        base_numeric_id=970,
        name="FLIRT",
        role="pax_railbus",
        role_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 900,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_2",  # specific to combined mail + pax consist
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_16px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!! wrong length - also no tail light needed, permanent middle car
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!! wrong length
    )

    # https://www.stadlerrail.com/media/pdf/cttfgvl90420_en.pdf
    consist.description = """"""
    consist.foamer_facts = """STADLER FLIRT / CITYLINK"""

    return consist