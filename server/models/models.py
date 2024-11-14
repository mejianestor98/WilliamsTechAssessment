from sqlalchemy import create_engine, Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Circuit(Base):
    __tablename__ = 'circuits'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reference = Column(String)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Integer)
    url = Column(String)


class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reference = Column(String)
    number = Column(String)
    code = Column(String)
    forename = Column(String)
    surname = Column(String)
    date_of_birth = Column(String)
    nationality = Column(String)
    url = Column(String)


class Race(Base):
    __tablename__ = 'races'

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    round = Column(Integer)
    circuit_id = Column(Integer, ForeignKey('circuits.id'))
    circuit = relationship('Circuit')
    name = Column(String)
    date = Column(String)
    time = Column(String)
    url = Column(String)
    fp1_date = Column(String)
    fp1_time = Column(String)
    fp2_date = Column(String)
    fp2_time = Column(String)
    fp3_date = Column(String)
    fp3_time = Column(String)
    quali_date = Column(String)
    quali_time = Column(String)
    sprint_date = Column(String)
    sprint_time = Column(String)


class DriverStanding(Base):
    __tablename__ = 'driver_standings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    race = relationship('Race')
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    driver = relationship('Driver')
    points = Column(Float)
    position = Column(Integer)
    position_text = Column(Integer)
    wins = Column(Integer)


class LapTime(Base):
    __tablename__ = 'lap_times'

    id = Column(Integer, primary_key=True, autoincrement=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    race = relationship(Race)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    driver = relationship(Driver)
    lap = Column(Integer)
    position = Column(Integer)
    time = Column(String)
    milliseconds = Column(Integer)


class RaceResult(Base):
    __tablename__ = 'race_results'

    id = Column(Integer, primary_key=True, autoincrement=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    race = relationship(Race)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    driver = relationship(Driver)
    finishing_position = Column(Integer)


def get_engine():
    return create_engine('sqlite:///f1_data.db')


def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=get_engine())
