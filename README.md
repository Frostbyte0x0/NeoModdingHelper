Please read the license before using this tool.

This is a tool to help create base files for 
neoforge mods for entities, items, blocks and particles.

You should put the 'Modding Helper' folder in the same folder as your mod

<pre>
/folder
├── Modding Helper <--
│   └── main.py
│   └── templates
│   └── etc
├── Your main mod file
│   └── src
│       └── main
│           └── java
│               └── your files
</pre>

<br>
For the constants json file, you don't need to fill it <em><strong>except 
the 'PACKAGE' and the 'MOD_ID', which are necessary</strong></em>, 
the program should find the files and folders automatically 
<em><strong>if your mod follows this structure</strong></em> : <br>
<pre>
/Your main mod file
├── src
│   └── main
│       └── java
│           └── your.file.signature (ex: org.exodusstudio.frostbite)
│               ├── client
│               │   └── ClientEvent.java (11)
│               ├── common
│               │   ├── block (13)
│               │   │   └── GenericCustomBlock.java
│               │   ├── entity
│               │   │   └── client
│               │   │       └── layers
│               │   │           └── ModModelLayers.java (2)
│               │   │       └── models (5)
│               │   │           └── CustomEntityModel.java
│               │   │       └── renderers (4)
│               │   │           └── CustomEntityRenderer.java
│               │   │   └── custom (6)
│               │   │       └── CustomEntityClass.java
│               │   ├── event
│               │   │   └── ModEventBusEvents.java
│               │   ├── item
│               │   │   └── custom (9)
│               │   │       └── GenericCustomItem.java
│               │   ├── particle (10)
│               │   │   └── CustomParticle.java
│               │   │   └── CustomParticleType.java
│               │   └── registry
│               │       └── BlockRegistry.java (14)
│               │       └── EntityRegistry.java (7)
│               │       └── ItemRegistry.java (8)
│               │       └── ParticleRegistry.java (12)
│               └── YourMainModFile.java (1)
</pre>

If not, you need to put your own paths in the json file for the ones 
that aren't at their place starting from the end of your file signature 
(in the same file as 'common'). 
Here is a guide as to what each key should lead to:  
- PACKAGE: The package path that is at the top of custom classes 
  (ex: org.exodusstudio.frostbite) (necessary),
- MOD_ID: The mod id of the mod (who would have guessed) (necessary),
- MAIN_MOD_FILE_LOCATION: Your main mod file (1),
- LAYERS_LOCATION: The file containing all ModelLayerLocations (2),
- LAYER_REGISTRY_LOCATION: The file where you register the layers (3)
  (here it is done with the EntityRenderersEvent.
  RegisterLayerDefinitions event),
- RENDERER_FOLDER_LOCATION: The folder where the renderer classes should go (4),
- MODEL_FOLDER_LOCATION: The folder where the model classes should go (5),
- ENTITY_FOLDER_LOCATION: The folder where the entity classes should go (6),
- ENTITY_REGISTRY_LOCATION: The registry file for entities (7),
- ATTRIBUTE_REGISTRY_LOCATION: The file where you register the 
  attributes for entities (3) (here it is done with the 
  EntityAttributeCreationEvent event),
- ITEM_REGISTRY_LOCATION: The registry file for entities (8),
- ITEM_FOLDER_LOCATION: The folder where the item classes should go (9)
- PARTICLE_FOLDER_LOCATION: The folder where the particle classes should go (10),
- CLIENT_EVENT_LOCATION: The file where you register the particle providers (11) 
  (here it is done with the RegisterParticleProvidersEvent event),
- PARTICLE_REGISTRY_LOCATION: The file where you register your particle (12)
- BLOCK_FOLDER_LOCATION: The folder where the block classes should go (13),
- BLOCK_REGISTRY_LOCATION: The file where you register your block (14)

Then, in the 'offsets' section, you can put the offset (in lines) 
for when writing to each file. In the 'offsets_from_bottom' section, 
you can specify whether the offset is from the top (false) 
or the bottom (true)

When starting the app, you can choose the project you're working
on, then enter the mod id (which is not saved on exit into the 
constants file), then choose what to do (entity, item, block, 
particle, or undo). The four first choices create and write 
to the files necessary to create the thing, and the 'undo' option 
undoes the last action (no way!): if it created a thing, it will 
remove it, and if it undid something, it will redo it (ex: if you undo 
creating an entity, it will create that entity again). Then it 
asks for the name of the new thing (in camel case, which is 
important if you want your stuff to be named correctly)
