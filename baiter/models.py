from dataclasses import dataclass


@dataclass
class WOWClass:
    pretty_name: str
    css: str


classes: list[WOWClass] = [
    WOWClass("Warrior","warrior"),
    WOWClass("Paladin","paladin"),
    WOWClass("Hunter","hunter"),
    WOWClass("Rogue","rogue"),
    WOWClass("Priest","preist"),
    WOWClass("Death Knight","deathknight"),
    WOWClass("Shaman","shaman"),
    WOWClass("Mage","mage"),
    WOWClass("Warlock","warlock"),
    WOWClass("Druid","druid"),
    WOWClass("Demon Hunter","demonhunter"),
    WOWClass("Evoker","evoker")
]