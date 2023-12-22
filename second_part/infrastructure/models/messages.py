from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from second_part.infrastructure.database import Base


class Messages(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(20))
    message: Mapped[str] = mapped_column(String(100))
