from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from database.init_db import SessionLocal
from models.quotes import Quote
from schemas.quotes import QuoteRead, QuoteCreate
import random
from typing import Optional, List

router = APIRouter()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[QuoteRead])
def get_all_quotes(
        skip: int = 0,
        limit: int = 10,
        author: Optional[str] = Query(None, description="Filter by author"),
        db: Session = Depends(get_db)
):
    """
    Get all quotes with optional pagination and author filtering.

    Args:
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to return.
        author (str, optional): Filter quotes by author.
        db (Session, optional): SQLAlchemy database session.

    Returns:
        List[QuoteRead]: List of motivational quotes.
    """
    query = db.query(Quote)
    if author:
        query = query.filter(Quote.author == author)
    return query.offset(skip).limit(limit).all()


@router.get("/random", response_model=QuoteRead)
def get_random_quote(author: Optional[str] = Query(None, description="Filter by author"),
                     db: Session = Depends(get_db)):
    """
    Return a random motivational quote.

    Args:
        author (str, optional): Filter quotes by author.
        db (Session, optional): SQLAlchemy database session.

    Returns:
        QuoteRead: Random quote from the database.

    Raises:
        HTTPException: 404 if no quotes found.
    """
    query = db.query(Quote)
    if author:
        query = query.filter(Quote.author == author)

    count = query.count()
    if count == 0:
        raise HTTPException(status_code=404, detail="No quotes found")

    offset = random.randint(0, count - 1)
    return query.offset(offset).first()


@router.post("/", response_model=QuoteRead, status_code=status.HTTP_201_CREATED)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    """
    Create a new motivational quote in the database.

    Args:
        quote (QuoteCreate): Pydantic model containing the quote text and optional author.
        db (Session, optional): SQLAlchemy database session.

    Returns:
        QuoteRead: The newly created quote, including its ID, text, and author.

    Raises:
        HTTPException:
            - 400 Bad Request if the quote already exists.
            - 500 Internal Server Error for unexpected database errors.
    """
    existing = db.query(Quote).filter(Quote.text == quote.text).first()
    if existing:
        raise HTTPException(status_code=400, detail="Quote already exists")

    new_quote = Quote(text=quote.text, author=quote.author)
    db.add(new_quote)

    try:
        db.commit()
        db.refresh(new_quote)
        return new_quote
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Quote already exists")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
