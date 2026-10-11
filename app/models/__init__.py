# Импорт всех моделей в одном месте: так они регистрируются в Base.metadata
# и Base.metadata.create_all() знает, какие таблицы создавать.
from app.models.user import User

__all__ = ["User"]
