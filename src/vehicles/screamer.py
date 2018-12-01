from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='screamer',
                        base_numeric_id=450,
                        name='Screamer',
                        role='heavy_express_2',
                        power=5000,
                        random_reverse=True,
                        gen=5,
                        pantograph_type='z-shaped-double',
                        intro_date_offset=5)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=85,
                 vehicle_length=8,
                 spriterow_num=0)
