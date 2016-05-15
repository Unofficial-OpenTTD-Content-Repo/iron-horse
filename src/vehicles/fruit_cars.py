import global_constants
from train import TypeConfig, WagonConsist, BoxCar, GraphicsProcessorFactory

fruit_car_label_refits_allowed = ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS']
cargo_graphics_mappings = {} # template needs this, but box car has zero cargo-specific graphics, all generic

type_config_normal = TypeConfig(base_id = 'fruit_car',
                    template = 'car_with_open_doors_during_loading.pynml',
                    num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    class_refit_groups = [],
                    label_refits_allowed = fruit_car_label_refits_allowed,
                    label_refits_disallowed = [],
                    autorefit = True,
                    default_cargo = 'FRUT',
                    default_capacity_type = 'capacity_freight',
                    cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD)

type_config_narrow_gauge = TypeConfig(base_id = 'fruit_car_ng',
                    template = 'car_with_open_doors_during_loading.pynml',
                    num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                    class_refit_groups = [],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = fruit_car_label_refits_allowed,
                    label_refits_disallowed = [],
                    autorefit = True,
                    default_cargo = 'FRUT',
                    default_capacity_type = 'capacity_freight',
                    cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD,
                    track_type = 'NG')

def main():
    #--------------- antelope ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Fruit Car]',
                        roster = 'antelope',
                        base_numeric_id = 2140,
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1890,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            weight = 14,
                            vehicle_length = 6))

    options = {'template': 'fruit_car_ng_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
