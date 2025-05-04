from collections import defaultdict
import itertools
from itertools import count
from typing import Self, Any

Entity = int


class EntityManager:
    def __init__(self: Self) -> None:
        self._count: count[Entity] = itertools.count()
        self._components: dict[type, dict[Entity, type]] = defaultdict(dict)

    def spawn_entity(self: Self) -> Entity:
        return next(self._count)

    def insert_component(self: Self, entity: Entity, component: Any) -> None:
        self._components[type(component)][entity] = component

    def query_component(self: Self, component_type: type) -> list[type]:
        return list(self._components[component_type].values())

    # def query_components(self: Self, *component_types: type):
    #     entity_sets: list[set[Entity]] = [
    #         set(self._components[component_type]) for component_type in component_types
    #     ]
    #     shared_entities: set[Entity] = set.intersection[Entity](*entity_sets)
    #     for entity in shared_entities:
    #         yield (
    #             self._components[component_type][entity]
    #             for component_type in component_types
    #         )
