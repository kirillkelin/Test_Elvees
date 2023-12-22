from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from second_part.infrastructure.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(20))
    datastr: Mapped[str] = mapped_column(String(12), default=datetime.now().strftime('%y%m%d%H%M%S'))
