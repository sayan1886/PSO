from dataclasses import dataclass
from os.path import dirname, realpath
from typing import Any
import json
        
@dataclass
class Objective:
    num_of_objective: int
    objective_type: str
    expand : bool

    @staticmethod
    def from_dict(obj: Any) -> 'Objective':
        _num_of_objective = int(obj.get("num_of_objective")) \
                if obj.get("num_of_objective") is not None else 1
        _objective_type = str(obj.get("objective_type")) \
                if obj.get("objective_type") is not None else "min"
        _expand = bool(obj.get("expand")) if obj.get("expand") is not None else True
        return Objective(num_of_objective=_num_of_objective, 
                         objective_type=_objective_type, 
                         expand=_expand)
        
@dataclass
class Range:
    min: float
    max: float
    variable_range: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Range':
        _min = float(obj.get("min")) if obj.get("min") is not None else 0
        _max = float(obj.get("max")) if obj.get("max") is not None else 0
        _variable_range = _min != _max
        return Range(min=_min, max=_max, variable_range=_variable_range)


@dataclass 
class Config:
    objective: Objective
    range: Range
    inertia_weight_constant: float
    cognitive_coefficient: float
    social_coefficient: float
    num_of_chromosomes: int
    num_of_gene: int
    num_of_iterations: int
    num_of_particles: int
    plot_type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        _objective = Objective.from_dict(obj.get("objective")) 
        _range = Range.from_dict(obj.get("range"))
        _inertia_weight_constant = float(obj.get("inertia_weight_constant")) \
                if obj.get("inertia_weight_constant") is not None else 0.5
        _cognitive_coefficient = float(obj.get("cognitive_coefficient")) \
                if obj.get("cognitive_coefficient") is not None else 0.1
        _social_coefficient = float(obj.get("social_coefficient")) \
                if obj.get("social_coefficient") is not None else 0.1
        _num_of_chromosomes = int(obj.get("num_of_chromosomes")) \
                if obj.get("num_of_chromosomes") is not None else 8
        _num_of_gene =  int(obj.get("num_of_gene")) \
                if obj.get("num_of_gene") is not None else 1
        _num_of_iterations = int(obj.get("num_of_iterations")) \
                if obj.get("num_of_iterations") is not None else 10
        _num_of_particles = int(obj.get("num_of_particles")) \
                if obj.get("num_of_particles") is not None else 20
        _plot_type = str(obj.get("plot_type"))
    
        return Config(objective=_objective, range=_range,
                        inertia_weight_constant=_inertia_weight_constant, 
                        cognitive_coefficient=_cognitive_coefficient,
                        social_coefficient=_social_coefficient,
                        num_of_chromosomes=_num_of_chromosomes,
                        num_of_gene=_num_of_gene, 
                        num_of_iterations=_num_of_iterations,
                        num_of_particles=_num_of_particles,
                        plot_type=_plot_type)   
    
    
def __get_config_file_name(exampleName):
    root_dir = dirname(realpath(__file__))
    file_name = root_dir + "/" + exampleName + ".json"
    return file_name    

def get_config(exampleName)->Config:
    config_file_name = __get_config_file_name(exampleName)
    with open(config_file_name,'r') as file:
        configString = file.read()
        
    configJSON = json.loads(configString)
    config = Config.from_dict(configJSON)
    return config