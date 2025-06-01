import json
from helper import *

starting_options = ["entity", "item", "block", "particle", "undo"]
signature = ""
signature_assets = ""

constants = {}
offsets = {}
offsets_from_bottom = {}


def start_entity(camel_name: str):
    # Model
    temp = load_template("entity_model", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_new_file(constants["MODEL_FOLDER_LOCATION"], f"{camel_name.capitalize()}Model.java", temp)
    # Renderer
    temp = load_template("entity_renderer", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_new_file(constants["RENDERER_FOLDER_LOCATION"], f"{camel_name.capitalize()}Renderer.java", temp)
    # Layers
    temp = load_template("entity_layer", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(constants["LAYERS_LOCATION"], temp, offsets["LAYERS_OFFSET"], offsets_from_bottom["LAYERS_OFFSET"])
    # Actual entity class
    temp = load_template("entity_class", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_new_file(constants["ENTITY_FOLDER_LOCATION"], f"{camel_name.capitalize()}Entity.java", temp)
    # Register renderer
    temp = load_template("entity_renderer_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(constants["MAIN_MOD_FILE_LOCATION"], temp, offsets["RENDERER_REGISTRY_OFFSET"], offsets_from_bottom["RENDERER_REGISTRY_OFFSET"])
    # Register entity
    temp = load_template("entity_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(constants["ENTITY_REGISTRY_LOCATION"], temp, offsets["ENTITY_REGISTRY_OFFSET"], offsets_from_bottom["ENTITY_REGISTRY_OFFSET"])
    # Register layer
    temp = load_template("entity_layer_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(constants["LAYER_REGISTRY_LOCATION"], temp, offsets["LAYER_REGISTRY_OFFSET"], offsets_from_bottom["LAYER_REGISTRY_OFFSET"])
    # Register attribute
    temp = load_template("entity_attribute_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(constants["ATTRIBUTE_REGISTRY_LOCATION"], temp, offsets["ATTRIBUTE_REGISTRY_OFFSET"], offsets_from_bottom["ATTRIBUTE_REGISTRY_OFFSET"])
    save_last_action("entity " + camel_name)


def undo_entity(camel_name: str):
    # Model
    erase_file(constants["MODEL_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Model.java")
    # Renderer
    erase_file(constants["RENDERER_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Renderer.java")
    # Layers
    temp = load_template("entity_layer", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(constants["LAYERS_LOCATION"], temp)
    # Actual entity class
    erase_file(constants["ENTITY_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Entity.java")
    # Register renderer
    temp = load_template("entity_renderer_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(constants["MAIN_MOD_FILE_LOCATION"], temp)
    # Register entity
    temp = load_template("entity_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(constants["ENTITY_REGISTRY_LOCATION"], temp)
    # Register layer
    temp = load_template("entity_layer_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(constants["LAYER_REGISTRY_LOCATION"], temp)
    # Register attribute
    temp = load_template("entity_attribute_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(constants["ATTRIBUTE_REGISTRY_LOCATION"], temp)


def start_item(camel_name: str):
    snake_name = camel_to_snake(camel_name)
    # Item json
    temp = load_template("item_json", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_new_file(signature_assets + "items", f"{snake_name}.json", temp)
    # Model json
    temp = load_template("item_model", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_new_file(signature_assets + "models/item", f"{snake_name}.json", temp)
    # Lang
    temp = load_template("item_lang", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    write_to_file(signature_assets + "lang/en_us.json", temp, 1, True)
    # Custom ? custom class : just registry
    if "y" in input("Is it a custom item (should a custom class be made)? (y/n) > ").lower():
        temp = load_template("item_class", camel_name, constants["MOD_ID"], constants["PACKAGE"])
        write_to_new_file(constants["ITEM_FOLDER_LOCATION"], f"{camel_name.capitalize()}Item.java", temp)
        temp = load_template("item_registry_custom", camel_name, constants["MOD_ID"], constants["PACKAGE"])
        write_to_file(constants["ITEM_REGISTRY_LOCATION"], temp, offsets["ITEM_REGISTRY_OFFSET"],
                      offsets_from_bottom["ITEM_REGISTRY_OFFSET"])
        save_last_action("item " + camel_name + " custom")
    else:
        temp = load_template("item_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
        write_to_file(constants["ITEM_REGISTRY_LOCATION"], temp, offsets["ITEM_REGISTRY_OFFSET"],
                      offsets_from_bottom["ITEM_REGISTRY_OFFSET"])
        save_last_action("item " + camel_name + " customn't")


def undo_item(camel_name: str, is_custom: bool):
    snake_name = camel_to_snake(camel_name)
    # Item json
    erase_file(signature_assets + f"items/{snake_name}.json")
    # Model json
    erase_file(signature_assets + f"models/item/{snake_name}.json")
    # Custom ? custom class : just registry
    if is_custom:
        erase_file(constants["ITEM_FOLDER_LOCATION"] + f"/{camel_name.capitalize()}Item.java")
        temp = load_template("item_registry_custom", camel_name, constants["MOD_ID"], constants["PACKAGE"])
        erase_from_file(constants["ITEM_REGISTRY_LOCATION"], temp)
    else:
        temp = load_template("item_registry", camel_name, constants["MOD_ID"], constants["PACKAGE"])
        erase_from_file(constants["ITEM_REGISTRY_LOCATION"], temp)
    # Lang
    temp = load_template("item_lang", camel_name, constants["MOD_ID"], constants["PACKAGE"])
    erase_from_file(signature_assets + "lang/en_us.json", temp)


def start_block(camel_name: str):
    save_last_action("block " + camel_name)


def undo_block(camel_name: str, is_custom: bool):
    ...


def start_particle(camel_name: str):
    save_last_action("particle " + camel_name)


def undo_particle(camel_name: str):
    ...


def undo():
    with open("last_action.txt", "r") as f:
        options = f.read().split(" ")

    option = options[0]
    name = options[1]

    match option:
        case "entity":
            undo_entity(name)
        case "item":
            undo_item(name, options[2] == "custom")
        case "block":
            undo_block(name, options[2] == "custom")
        case "particle":
            undo_particle(name)
        case "undo":
            redo(options[2], options[1])
            return
    save_last_action("undo " + option + " " + name)


def redo(name: str, option: str):
    match option:
        case "entity":
            start_entity(name)
        case "item":
            start_item(name)
        case "block":
            start_block(name)
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
    global constants
    global offsets
    global offsets_from_bottom

    signature_assets = ("../" + folder + "/src/main/resources/assets/" +
                        get_all_folders("../" + folder + "/src/main/resources/assets")[0]) + "/"
    signature = get_all_folders("../" + folder + "/src/main/java")[0] + "/"
    signature += get_all_folders("../" + folder + "/src/main/java/" + signature)[0] + "/"
    signature += get_all_folders("../" + folder + "/src/main/java/" + signature)[0]
    signature = "../" + folder + "/src/main/java/" + signature
    constants["PACKAGE"] = signature.replace("../" + folder + "/src/main/java/", "").replace("/", ".")
    signature += "/"

    with open("constants.json", "r") as f:
        d = json.loads(f.read())
        saved = d["constants"]
        offsets = d["offsets"]
        offsets_from_bottom = d["offsets_from_bottom"]

    constants["MAIN_MOD_FILE_LOCATION"] = signature + [entry.name for entry in os.scandir(signature) if
                                          (not entry.is_dir() and entry.name.endswith(".java"))][0]
    constants["LAYERS_LOCATION"] = signature + "common/entity/client/layers/ModModelLayers.java"
    constants["LAYER_REGISTRY_LOCATION"] = signature + "common/event/ModEventBusEvents.java"
    constants["RENDERER_FOLDER_LOCATION"] = signature + "common/entity/client/renderers"
    constants["MODEL_FOLDER_LOCATION"] = signature + "common/entity/client/models"
    constants["ENTITY_FOLDER_LOCATION"] = signature + "common/entity/custom"
    constants["ENTITY_REGISTRY_LOCATION"] = signature + "common/registry/EntityRegistry.java"
    constants["ATTRIBUTE_REGISTRY_LOCATION"] = signature + "common/event/ModEventBusEvents.java"
    constants["ITEM_REGISTRY_LOCATION"] = signature + "common/registry/ItemRegistry.java"
    constants["ITEM_FOLDER_LOCATION"] = signature + "common/item/custom"
    constants["MOD_ID"] = saved["MOD_ID"] if saved["MOD_ID"] != "" else input("What is the mod id? > ")

    for key, value in saved.items():
        if not value == "":
            if "LOCATION" in key:
                constants[key] = signature + value
            else:
                constants[key] = value


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
            start_block(name)
        case 3:
            name = input("Name of the new thing (in camel case) > ")
            start_particle(name)
        case 4:
            undo()


if __name__ == '__main__':
    projects = get_all_folders("../")
    print("Which project?")
    project_folder = projects[select_from_menu(projects)]
    define_constants(project_folder)
    start()
