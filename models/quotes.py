from sqlalchemy import Column, String, Integer
from database.init_db import Base

class Quote(Base):
    """
    Quote Model for motivational quotes

    Attributes:
        id (int): Primary key, unique identifier for the quote.
        text (str): The quote text, cannot be empty.
        author (str): The author of the quote, optional.
    """
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    author= Column(String, nullable=True, index=True)

    def __repr__(self):
        return f"<Quote(id={self.id}, author={self.author})>"

    def __str__(self):
        return f'{self.text} - {self.author or "Unknown"}'

    def short_text(self, max_len: int = 50):
        """
        Returns a truncated version of the quote text.

        Args:
            max_len (int): Maximum length of the returned string. Defaults to 50.

        Returns:
            Truncated quote if necessary.
        """
        if len(self.text) > max_len:
            return self.text[:max_len] + "..."
        return self.text
