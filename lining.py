from helper import load_template, snake_to_camel

# item = """
#     public static final DeferredItem<Item> ^U_LINING_HELMET = ITEMS.register("^L_lining_helmet",
#             (id) -> new LiningItem(LiningMaterials.^U, ArmorType.HELMET,
#                     new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id))));
#     public static final DeferredItem<Item> ^U_LINING_CHESTPLATE = ITEMS.register("^L_lining_chestplate",
#             (id) -> new LiningItem(LiningMaterials.^U, ArmorType.CHESTPLATE,
#                     new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id))));
#     public static final DeferredItem<Item> ^U_LINING_LEGGINGS = ITEMS.register("^L_lining_leggings",
#             (id) -> new LiningItem(LiningMaterials.^U, ArmorType.LEGGINGS,
#                     new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id))));
#     public static final DeferredItem<Item> ^U_LINING_BOOTS = ITEMS.register("^L_lining_boots",
#             (id) -> new LiningItem(LiningMaterials.^U, ArmorType.BOOTS,
#                     new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id))));
#
# """
item = """
output.accept(ItemRegistry.^U_LINING_HELMET);
output.accept(ItemRegistry.^U_LINING_CHESTPLATE);
output.accept(ItemRegistry.^U_LINING_LEGGINGS);
output.accept(ItemRegistry.^U_LINING_BOOTS);
"""


for lining in ["WOOL"]: #["WOOLLY_WOOL", "FROZEN_FUR", "INSULATED_CLOTH", "HEATED_COATING", "FROZEN_PLATING"]:
    upper_lining = lining.upper()
    snake_name = lining.lower()
    camel_name = snake_to_camel(snake_name)


    for armour in ["helmet", "chestplate", "leggings", "boots"]:
        with open("temp/temp.txt", "a") as f:
            f.write(load_template("item_lang", camel_name + "Lining" + armour.capitalize()))
            # f.write(item.replace("^U", upper_lining))
        with open(f"temp/items/{snake_name}_lining_{armour}.json", "w") as f:
            f.write(load_template("item_json", camel_name + "Lining" + armour.capitalize()))
        with open(f"temp/model/{snake_name}_lining_{armour}.json", "w") as f:
            f.write(load_template("item_model", camel_name + "Lining" + armour.capitalize()))
