from database.init_database import init_database
from database.database import SessionLocal


def init() -> None:
    db = SessionLocal()
    init_database(db)


def main() -> None:
    print("Creating initial data")
    init()
    print("Initial data created")


if __name__ == "__main__":
    main()