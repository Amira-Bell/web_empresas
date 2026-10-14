import os
import shutil
from pathlib import Path
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_empresas.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Category, Post

# 1. Superuser
user, created = User.objects.get_or_create(username='admin')
if created:
    user.set_password('admin1234')
    user.email = 'admin@lacaffettiera.com'
    user.first_name = 'Juan'
    user.last_name = 'Barista'
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("Superuser created: admin / admin1234")
else:
    user.first_name = 'Juan'
    user.last_name = 'Barista'
    user.save()
    print("Superuser already exists: admin")

# 2. Categories
cat_data = [
    "Cafés de Especialidad",
    "Bollería y Repostería",
    "Consejos para Baristas",
    "Ofertas y Promociones",
]

categories = {}
for name in cat_data:
    cat, _ = Category.objects.get_or_create(name=name)
    categories[name] = cat
    print(f"Categoría lista: {cat.name}")

# Prepare media folder
media_blog_dir = Path('media') / 'blog'
media_blog_dir.mkdir(parents=True, exist_ok=True)

static_img_dir = Path('core') / 'static' / 'core' / 'img'
img_map = {
    "products-01.jpg": media_blog_dir / 'products-01.jpg',
    "products-02.jpg": media_blog_dir / 'products-02.jpg',
    "products-03.jpg": media_blog_dir / 'products-03.jpg',
    "intro.jpg": media_blog_dir / 'intro.jpg',
}

for src_name, dest_path in img_map.items():
    src_file = static_img_dir / src_name
    if src_file.exists() and not dest_path.exists():
        shutil.copy(src_file, dest_path)

# 3. Posts
posts_data = [
    {
        "title": "Secretos para catar un auténtico café arábica",
        "category": categories["Cafés de Especialidad"],
        "content": (
            "El café arábica de altura se caracteriza por su acidez brillante, notas cítricas "
            "y delicados aromas a jazmín y frutas rojas. Para apreciar todas estas cualidades sensoriales, "
            "es fundamental cuidar la temperatura del agua entre los 90°C y 93°C, y moler el grano instantes antes "
            "de la preparación. En La Caffettiera seleccionamos lotes de pequeños productores que respetan el ciclo de cosecha."
        ),
        "image": "blog/products-01.jpg",
    },
    {
        "title": "El arte del croissant francés: hojaldrado perfecto",
        "category": categories["Bollería y Repostería"],
        "content": (
            "No hay nada como el aroma a mantequilla dorada que inunda nuestro obrador cada mañana a las 6:00 AM. "
            "Para lograr un croissant esponjoso por dentro y crujiente por fuera, dejamos reposar la masa madre durante "
            "24 horas a temperatura controlada. Un proceso paciente que se nota en cada mordisco."
        ),
        "image": "blog/products-02.jpg",
    },
    {
        "title": "Guía práctica: Cómo calibrar tu molinillo de café en casa",
        "category": categories["Consejos para Baristas"],
        "content": (
            "La molienda es el 80% del éxito en cualquier taza de café. Si tu café sale muy rápido y con sabor agrio, "
            "tu molienda es demasiado gruesa (subextracción). Si sale a gotas y amargo, estás moliendo demasiado fino "
            "(sobreextracción). Encuentra el punto medio donde el flujo sea constante como miel tibia."
        ),
        "image": "blog/intro.jpg",
    },
    {
        "title": "Semana especial: Degustación de temporada y descuentos en granos",
        "category": categories["Ofertas y Promociones"],
        "content": (
            "Durante toda esta semana, ven a nuestra tienda y disfruta de un 20% de descuento en todos los paquetes "
            "de café de origen Etiopía Yirgacheffe y Colombia Huila. Además, por cada compra recibirás una muestra "
            "gratuita de nuestros granos de edición limitada tostados para prensa francesa."
        ),
        "image": "blog/products-03.jpg",
    },
]

for p_info in posts_data:
    post, created = Post.objects.get_or_create(
        title=p_info["title"],
        defaults={
            "category": p_info["category"],
            "author": user,
            "content": p_info["content"],
            "image": p_info["image"],
            "published": timezone.now(),
        }
    )
    if created:
        print(f"Post creado: '{post.title}' en categoría '{post.category.name}'")
    else:
        print(f"Post ya existente: '{post.title}'")

print("Inicialización de datos completada con éxito.")
