# Links, references, helpful things
- http://stackoverflow.com/questions/21007329/what-is-a-sdl-renderer
	- A *very* helpful post explaining the SDL2 classes, like window, renderer, texture, etc.

- https://github.com/junkdog/artemis-odb/wiki/Introduction-to-Entity-Systems
	- Generally good information about Entity component system

- https://www.gamedev.net/resources/_/technical/game-programming/implementing-component-entity-systems-r3382
	- More advanced post about ECS


# Program specific notes

### AI and behaviors

If behavior type == 'following', entity has to have a followingcomponent
behavior type is stored in AI
ai processing system checks behavior type (if entity.ai.behavior == 'following'), etc.
then, if that function gets hit, the entity must have a following component, etc.
the components associated iwth a certain type of behavior must contain all of the
parameters necessary to reason about how the ai will act in the ai processing system
entitys may have more than on etype of behavior
