
import random
from apps.products.models import Brand, Group, Product

def run():
    """
    This script populates the database with a variety of products, brands, and groups.
    """
    # Expanded lists of names for more variety
    brand_names = ["Bosch Rexroth", "Parker Hannifin", "Eaton", "Danfoss", "Kawasaki", "Hawe", "Hydac", "Moog", "Vickers", "Denison"]
    group_names = {
        "Valves": "Valvulas hidraulicas",
        "Pumps": "Bombas hidraulicas",
        "Cylinders": "Cilindros hidraulicos",
        "Motors": "Motores hidraulicos",
        "Filters": "Filtros hidraulicos",
        "Accumulators": "Acumuladores hidraulicos",
        "Hoses": "Mangueras hidraulicas",
        "Fittings": "Conexiones hidraulicas",
    }
    product_adjectives = ["High Performance", "Compact", "Heavy Duty", "Silent", "Efficient", "Submersible", "Proportional", "Servo"]
    product_nouns = ["Pump", "Motor", "Cylinder", "Valve", "Filter", "Accumulator", "Hose", "Fitting"]

    # Create Brands
    brands = []
    for name in brand_names:
        brand, created = Brand.objects.get_or_create(name=name)
        brands.append(brand)
        if created:
            print(f"Brand '{name}' created.")

    # Create Groups
    groups = []
    for name, description in group_names.items():
        group, created = Group.objects.get_or_create(name=name, defaults={'description': description})
        groups.append(group)
        if created:
            print(f"Group '{name}' created.")

    # Create Products
    for _ in range(100):  # Create 100 new products
        brand = random.choice(brands)
        group = random.choice(groups)
        adjective = random.choice(product_adjectives)
        noun = random.choice(product_nouns)
        product_name = f"{adjective} {noun} {random.randint(100, 999)}"
        product_description = f"A high-quality {product_name} from {brand.name}, part of the {group.name} group."

        Product.objects.create(
            name=product_name,
            description=product_description,
            group=group,
            brand=brand,
            is_active=True
        )
    print("Successfully created 100 new products.")
