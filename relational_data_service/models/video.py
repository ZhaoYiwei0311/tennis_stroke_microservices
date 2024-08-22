from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from relational_data_service.db import db

class Video(db.Model):
    tablename = 'videos'

    # Reflect the existing columns automatically
    video_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    url: Mapped[str]
    is_live_streamed: Mapped[str]
    length: Mapped[int]
    created_date: Mapped[datetime]
    created_by: Mapped[str]
    updated_date: Mapped[datetime]
    updated_by: Mapped[str]
    is_deleted: Mapped[int]

    def __repr__(self):
        return f'<video {self.video_id, self.created_date}>'

    def to_dict(self):
        """Serialize the model instance to a dictionary."""
        return {
            'video_id': self.video_id,
            'user_id': self.user_id,
            'url': self.url,
            'is_live_streamed': self.is_live_streamed,
            'length': self.length,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'created_by': self.created_by,
            'updated_date': self.updated_date.isoformat() if self.updated_date else None,
            'updated_by': self.updated_by,
            'is_deleted': self.is_deleted
        }