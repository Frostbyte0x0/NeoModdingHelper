import json
from helper import *

starting_options = ["entity", "item", "particle", "undo"]
signature = ""
signature_assets = ""

locations = {}
offsets = {}
offsets_from_bottom = {}


def start_entity(camel_name: str):
    # Model
    temp = load_template("entity_model", camel_name)
    write_to_new_file(locations["MODEL_FOLDER_LOCATION"], f"{camel_name.capitalize()}Model.java", temp)
    # Renderer
    temp = load_template("entity_renderer", camel_name)
    write_to_new_file(locations["RENDERER_FOLDER_LOCATION"], f"{camel_name.capitalize()}Renderer.java", temp)
    # Layers
    temp = load_template("entity_layer", camel_name)
    write_to_file(locations["LAYERS_LOCATION"], temp, offsets["LAYERS_OFFSET"], offsets_from_bottom["LAYERS_OFFSET"])
    # Actual entity class
    temp = load_template("entity_class", camel_name)
    write_to_new_file(locations["ENTITY_FOLDER_LOCATION"], f"{camel_name.capitalize()}Entity.java", temp)
    # Register renderer
    temp = load_template("entity_renderer_registry", camel_name)
    write_to_file(locations["MAIN_MOD_FILE_LOCATION"], temp, offsets["RENDERER_REGISTRY_OFFSET"], offsets_from_bottom["RENDERER_REGISTRY_OFFSET"])
    # Register entity
    temp = load_template("entity_registry", camel_name)
    write_to_file(locations["ENTITY_REGISTRY_LOCATION"], temp, offsets["ENTITY_REGISTRY_OFFSET"], offsets_from_bottom["ENTITY_REGISTRY_OFFSET"])
    # Register layer
    temp = load_template("entity_layer_registry", camel_name)
    write_to_file(locations["LAYER_REGISTRY_LOCATION"], temp, offsets["LAYER_REGISTRY_OFFSET"], offsets_from_bottom["LAYER_REGISTRY_OFFSET"])
    # Register attribute
    temp = load_template("entity_attribute_registry", camel_name)
    write_to_file(locations["ATTRIBUTE_REGISTRY_LOCATION"], temp, offsets["ATTRIBUTE_REGISTRY_OFFSET"], offsets_from_bottom["ATTRIBUTE_REGISTRY_OFFSET"])
    save_last_action("entity " + camel_name)


def undo_entity(camel_name: str):
    # Model
    os.remove(locations["MODEL_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Model.java")
    # Renderer
    os.remove(locations["RENDERER_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Renderer.java")
    # Layers
    temp = load_template("entity_layer", camel_name)
    erase_from_file(locations["LAYERS_LOCATION"], temp)
    # Actual entity class
    os.remove(locations["ENTITY_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Entity.java")
    # Register renderer
    temp = load_template("entity_renderer_registry", camel_name)
    erase_from_file(locations["MAIN_MOD_FILE_LOCATION"], temp)
    # Register entity
    temp = load_template("entity_registry", camel_name)
    erase_from_file(locations["ENTITY_REGISTRY_LOCATION"], temp)
    # Register layer
    temp = load_template("entity_layer_registry", camel_name)
    erase_from_file(locations["LAYER_REGISTRY_LOCATION"], temp)
    # Register attribute
    temp = load_template("entity_attribute_registry", camel_name)
    erase_from_file(locations["ATTRIBUTE_REGISTRY_LOCATION"], temp)


def start_item(camel_name: str):
    # Item
    # - Item json
    temp = load_template("item_json", camel_name)
    write_to_new_file("", f"{camel_name.capitalize()}.json", temp)
    # - Model json
    # - Custom ? custom class : just registry
    # - Register
    temp = load_template("entity_registry", camel_name)
    write_to_file(locations["ENTITY_REGISTRY_LOCATION"], temp, offsets["ENTITY_REGISTRY_OFFSET"],
                  offsets_from_bottom["ENTITY_REGISTRY_OFFSET"])
    save_last_action("item " + camel_name)


def undo_item(camel_name: str):
    # Item
    # - Item json
    # - Model json
    # - Custom ? custom class : just registry
    # - Register
    ...


def start_particle(camel_name: str):
    save_last_action("particle " + camel_name)


def undo_particle(camel_name: str):
    ...


def undo():
    with open("last_action.txt", "r") as f:
        options = f.read().split(" ")

    if len(options) == 3:
        redo(options[2], options[1])
        return

    option = options[0]
    name = options[1]

    match option:
        case "entity":
            undo_entity(name)
        case "item":
            undo_item(name)
        case "particle":
            undo_particle(name)
    save_last_action("undo " + option + " " + name)


def redo(name: str, option: str):
    match option:
        case "entity":
            start_entity(name)
        case "item":
            start_item(name)
        case "particle":
            start_particle(name)
        case "undo":
            undo()


def save_last_action(last_action: str):
    with open("last_action.txt", "w") as f:
        f.write(last_action)


def define_constants(folder: str):
    global signature
    global signature_assets
    global locations
    global offsets
    global offsets_from_bottom

    signature_assets = ("../" + folder + "/src/main/resources/assets" +
                        get_all_folders("../" + folder + "/src/main/resources/assets")[0])
    signature = get_all_folders("../" + folder + "/src/main/java")[0] + "/"
    signature += get_all_folders("../" + folder + "/src/main/java/" + signature)[0] + "/"
    signature += get_all_folders("../" + folder + "/src/main/java/" + signature)[0]
    signature = "../" + folder + "/src/main/java/" + signature + "/"

    with open("constants.json", "r") as f:
        d = json.loads(f.read())
        locations_saved = d["locations"]
        offsets = d["offsets"]
        offsets_from_bottom = d["offsets_from_bottom"]

    locations["MAIN_MOD_FILE_LOCATION"] = signature + [entry.name for entry in os.scandir(signature) if
                                          (not entry.is_dir() and entry.name.endswith(".java"))][0]
    locations["LAYERS_LOCATION"] = signature + "common/entity/client/layers/ModModelLayers.java"
    locations["LAYER_REGISTRY_LOCATION"] = signature + "common/event/ModEventBusEvents.java"
    locations["RENDERER_FOLDER_LOCATION"] = signature + "common/entity/client/renderers"
    locations["MODEL_FOLDER_LOCATION"] = signature + "common/entity/client/models"
    locations["ENTITY_FOLDER_LOCATION"] = signature + "common/entity/custom"
    locations["ENTITY_REGISTRY_LOCATION"] = signature + "common/registry/EntityRegistry.java"
    locations["ATTRIBUTE_REGISTRY_LOCATION"] = signature + "common/event/ModEventBusEvents.java"

    for key, value in locations_saved.items():
        if not value == "":
            locations[key] = value


def start():
    match select_from_menu(starting_options):
        case 0:
            name = input("Name of the new thing (in camel case) > ")
            start_entity(name)
        case 1:
            name = input("Name of the new thing (in camel case) > ")
            start_item(name)
        case 2:
            name = input("Name of the new thing (in camel case) > ")
            start_particle(name)
        case 3:
            undo()


if __name__ == '__main__':
    projects = get_all_folders("../")
    print("Which project?")
    project_folder = projects[select_from_menu(projects)]
    define_constants(project_folder)
    start()
