from typing import Self, TypeVar, Generic
from unittest import TestCase
from dataclasses import dataclass

from juniorpen01s_ecs import EntityManager, Entity

T = TypeVar("T", int, float, complex)


@dataclass
class Position(Generic[T]):
    x: T
    y: T


class EntityManagerTest(TestCase):
    def setUp(self: Self) -> None:
        self.entity_manager = EntityManager()

    def test_entity_manager_insert_component(self: Self) -> None:
        entity: Entity = self.entity_manager.spawn_entity()
        self.entity_manager.insert_component(entity, Position(1, 2))

    def test_entity_manager_query_component_none(self: Self) -> None:
        self.entity_manager.spawn_entity()
        self.assertTrue(not self.entity_manager.query_component(Position))

    def test_entity_manager_query_component(self: Self) -> None:
        entity: Entity = self.entity_manager.spawn_entity()
        self.entity_manager.insert_component(entity, Position(1, 2))
        self.assertTrue(self.entity_manager.query_component(Position))
