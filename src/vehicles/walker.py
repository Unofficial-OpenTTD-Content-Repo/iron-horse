import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'walker',
              base_numeric_id = 1570,
              title = 'Walker [Diesel]',
              replacement_id = '-none',
              power = 950,
              track_type = 'NG',
              speed = 55,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1959,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 50,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
