# Links, references, helpful things
- http://stackoverflow.com/questions/21007329/what-is-a-sdl-renderer
	- A *very* helpful post explaining the SDL2 classes, like window, renderer, texture, etc.

- https://github.com/junkdog/artemis-odb/wiki/Introduction-to-Entity-Systems
	- Generally good information about Entity component system

- https://www.gamedev.net/resources/_/technical/game-programming/implementing-component-entity-systems-r3382
	- More advanced post about ECS

# Game specific notes

### Story
An advanced ANCIENT CIVILIZATION develops technology to DARK ENERGY from the DARK ETHER, initially used to infuse ORBS with powers. Eventually, the civilization achieves a SINGULARITY and becomes a single entity. The SINGULARITY lies in wait, drawing in power from the DARK ETHER in order to acquire enough energy to generate a new big bang, and fill the universe with its essence.

The antagonist is an EX-SOLDIER in the RESISTANCE forces fighting against the EMPIRE, when he discovers the planet hosting the ANCIENT CIVILIZATION. He seeks to acquire their power to take over the universe for himself. He has three MERCENRIES to which he bestows some of the ANCIENT CIVILIZATIONS' ORB powers. These MERCENARIES are out to get the HERO. By defeating the MERCENARIES, the HERO may acquire their POWER ORBS.

The opening sequence of the game shows the UNITED GALAXY'S forces under attack from EX-SOLDIER and the THREE MERCENARIES (which introduces them). They kidnap scientists and retreat.

Our HERO is drawn to the planet after chasing the EX-SOLDIER down for his crimes committed against the RESISTANCE. She crash lands on the planet after engaging with the EX-SOLDIERS forces. On the planet she discovers traces of the ANCIENT CIVILIZATION, as well as a LABORATORY set up by the EX-SOLDIER to perform research on the ANCIENT CIVILIZATION's technology.

### Characters

##### HERO

##### EX SOLDIER
An EX SOLDIER in the RESISTANCE forces that betrayed the group by attacking one of their bases, kidnapping RESISTANCE scientists. During the attack he is seen by the HERO, who discovers he is using advanced technology never before seen...

##### SINGULARITY

##### THREE MERCENARIES

####### TWINS
Actually two separate people. One female, one male, both androgynous. Both act together essentially as one person. Tricksters. In ultimate battle with HERO, they fuse together into a single entity using the power of the ANCIENT CIVILIZATION's fusion technology. This is one of the final battles and foreshadows the presence of the SINGULARITY and EX-SOLDIERS synthesis.


 
### Art


### Game play


Hero gets arm extensions, one for each hand (left right), to which orbs can be attached. Each orb has 2 actions, meaning there are 4 actions total per orb combination choice. Two of the same orb can be equipped to each arm. Orbs are what give the hero her unique abilities and give the gameplay depth. For instance, a Sword orb can be used to attack, or to double jump. Two Sword orbs could be attached to slash twice as fast, or to triple jump.

### Orbs

##### Sword orb
Used to launch powerful attacks, or to double jump.

##### Teleport orb
An orb that can be attached to an arm. The orb can be dropped and summoned at will. If the player uses the orb, she will teleport back to its dropped location. This will add unique gameplay elements by allowing for complex puzzle solving, for easier traversal of the entire game world (if the player is smart), and for unique boss battles. The orb can for instance be used to dodge a strong boss attack.

##### On death
The HERO's body transports to a CHRYSALIS (save point, essentially) where she is fully healed. This technology forms the same basis as the teleport orb. HERO may insert only one orb into one save point, but the orb may be moved to different save points.

# Program specific notes

### AI and behaviors

If behavior type == 'following', entity has to have a followingcomponent
behavior type is stored in AI
ai processing system checks behavior type (if entity.ai.behavior == 'following'), etc.
then, if that function gets hit, the entity must have a following component, etc.
the components associated iwth a certain type of behavior must contain all of the
parameters necessary to reason about how the ai will act in the ai processing system
entitys may have more than on etype of behavior
