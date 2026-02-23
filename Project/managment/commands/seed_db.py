import csv
from django.core.management.base import BaseCommand
from project.models import Book, Publisher, Genre, BookMetadata


class Command(BaseCommand):
    help = "Seeds the database from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:

                    # ---------------------
                    # 1️⃣ Publisher (N:1)
                    # ---------------------
                    publisher_obj, _ = Publisher.objects.get_or_create(
                        name=row["publisher"]
                    )

                    # ---------------------
                    # 2️⃣ Book
                    # ---------------------
                    book, created = Book.objects.get_or_create(
                        title=row["title"],
                        defaults={
                            "author": row["author"],
                            "pages": int(row["pages"]),
                            "dds": float(row["dds"]) if row["dds"] else None,
                            "publisher": publisher_obj,
                        },
                    )

                    # If book already exists, ensure publisher is set
                    if not created:
                        book.publisher = publisher_obj
                        book.save()

                    # ---------------------
                    # 3️⃣ Genres (N:N)
                    # ---------------------
                    genre_names = row["genres"].split(",")

                    for name in genre_names:
                        genre_obj, _ = Genre.objects.get_or_create(
                            name=name.strip()
                        )
                        book.genres.add(genre_obj)

                    # ---------------------
                    # 4️⃣ Metadata (1:1)
                    # ---------------------
                    if not hasattr(book, "metadata"):
                        BookMetadata.objects.create(
                            book=book,
                            isbn=row["isbn"],
                            publication_date=row["publication_date"],
                            summary=row["summary"],
                        )

                    self.stdout.write(
                        self.style.SUCCESS(f"Seeded: {book.title}")
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))