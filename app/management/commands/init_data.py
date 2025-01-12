from django.core.management import BaseCommand

from django.utils import timezone
from app.models import Post, Category, Comment


class Command(BaseCommand):
    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Post.objects.all().delete()
        Category.objects.all().delete()

        # Création des catégories
        category_test = Category.objects.create(name="Tests")
        category_histoire = Category.objects.create(name="Histoire")

        # Articles sur les tests de far breton

        Post.objects.create(
            title="Top 5 des boulangeries de Rennes",
            author="Jeanne Dupont",
            content="Après avoir parcouru les rues de Rennes, nous avons goûté le far breton de 20 boulangeries différentes. Voici notre top 5 des meilleurs fars bretons de la ville, avec une mention spéciale pour la texture crémeuse du far de la boulangerie 'Au bon beurre' et les pruneaux particulièrement fondants chez 'La Fournée Bretonne'...",
            category=category_test,
            likes=-5,
            active=False,
            date_posted=timezone.now(),
        )

        post_1 = Post.objects.create(
            title="Dégustation de far breton :  Dégustation gourmande à la Boulangerie Maison Fontaine",
            author="Marie Martin",
            content="La Boulangerie Maison Fontaine, située au 27 Boulevard Léon Bourgeois à Rennes, est un véritable écrin de délices artisanaux. Ouverte en novembre 2022 par Jean-Jacques et Anne Fontaine, cette boulangerie 100% artisanale m'a donné envie de découvrir leurs spécialités, notamment leur far breton.",
            category=category_test,
            likes=10,
            date_posted=timezone.now(),
        )

        post_2 = Post.objects.create(
            title="Dégustation de far breton : L'Atelier Boulanger, une pépite cachée à Rennes",
            author="Maelis Leclerc",
            content="Niché au 248 rue de Nantes à Saint-Jacques-de-la-Lande, L'Atelier Boulanger s'est rapidement imposé comme une référence dans le paysage boulanger rennais. Réputé pour ses croissants primés et son savoir-faire artisanal, j'ai décidé de tester leur far breton, une spécialité bretonne incontournable.",
            category=category_test,
            likes=8,
            date_posted=timezone.now(),
        )

        Post.objects.create(
            title="Bataille des boulangeries à Quimper",
            author="Suzanne Le Goff",
            content="Quimper, capitale de la Cornouaille, regorge de boulangeries proposant du far breton. Nous avons mis à l'épreuve 8 établissements pour déterminer qui propose le meilleur far de la ville. Entre la recette traditionnelle de 'Chez Mam'Goz' et la version revisitée de 'L'Atelier du Far', le débat fait rage. Découvrez notre classement complet et les critères qui ont fait la différence...",
            category=category_test,
            likes=3,
            date_posted=timezone.now(),
        )

        # Articles sur l'histoire du far breton

        Post.objects.create(
            title="L'évolution des ingrédients du far breton à travers les âges",
            author="Michele Leclerc",
            content="Du blé noir au froment, des pruneaux aux raisins secs, le far breton a connu de nombreuses variations au cours de son histoire. Cet article retrace l'évolution des ingrédients utilisés dans la préparation du far breton, reflétant les changements économiques et culturels de la Bretagne. Découvrez comment le sucre, les œufs et le lait sont devenus des composants essentiels de cette recette ancestrale...",
            category=category_histoire,
            likes=7,
            date_posted=timezone.now(),
        )

        Post.objects.create(
            title="Le far breton : de la table paysanne aux étoiles gastronomiques",
            author="Marion Porez",
            content="Autrefois considéré comme un simple dessert paysan, le far breton a gravi les échelons de la gastronomie française. Ce voyage culinaire fascinant l'a mené des fermes bretonnes aux tables des plus grands restaurants. Explorez comment ce dessert rustique a su séduire les palais les plus raffinés et comment les chefs étoilés réinterprètent aujourd'hui ce classique breton...",
            category=category_histoire,
            likes=12,
            date_posted=timezone.now(),
        )

        # Commentaires sur les articles

        Comment.objects.create(
            author="Jeanne Dupont",
            content="Super article, j'ai hâte de goûter le far de la Boulangerie Maison Fontaine !",
            likes=5,
            post=post_1
        )

        Comment.objects.create(
            author="Jean Martin",
            content="Je suis fan du far breton, merci pour ces bonnes adresses !",
            likes=2,
            post=post_2
        )

        Comment.objects.create(
            author="Francis Leclerc",
            content="Je ne savais pas que le far breton avait une telle histoire, merci pour ces informations !",
            likes=3,
            post=post_2
        )

        self.stdout.write(self.style.SUCCESS("All Done !"))

