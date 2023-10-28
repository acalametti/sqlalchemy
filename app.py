# Import the dependencies.
from flask import Flask,jsonify
import sqlalchemy
from sqlalchemy import func, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt

#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with = engine)

# Save references to each table
M = Base.classes.measurement
S = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

str_date = session.query(func.max(M.date)).first()[0]
recent_date = dt.datetime.strptime(str_date,"%Y-%m-%d").date()
pre_year = recent_date - dt.timedelta(365)

#################################################
# Flask Setup
#################################################
app=Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return f"""
    <h2>API routes:</h2>
<li>/api/v1.0/precipitation</li>
<li>/api/v1.0/stations</li>
<li>/api/v1.0/tobs</li>
<li>/api/v1.0/[start]</li>
<li>/api/v1.0/[start]/[end]</li>
"""

@app.route("/api/v1.0/precipitation")
def precipitation():

    #create session (link) 
    session = Session(engine)

    #perform query
    results = d:p for d,p in session.query(M.date, M.prcp).filter(M.date>=pre_year).all() 
    #close session
    session.close()
    
    return jsonify (results)

@app.route("/api/v1.0/stations")
def stations():
    #create session (link) 
    session = Session(engine)

    #perform query
    results = session.query(M.station)
    
    #close session
    session.close()

    return jsonify (results)

@app.route("/api/v1.0/tobs")
def tobs():
        #create session (link) 
    session = Session(engine)

    #perform query
    results = {d:t for d,t in session.query(M.date,M.tobs).filter((M.station == 'USC00519281')&(M.date>=pre_year)).all()}
    
    #close session
    session.close()

    return jsonify (results)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def range(start,end = "2017-08-23"):
     #create session (link) 
    session = Session(engine)

    #perform query 
    results = session.query(func.min(M.tobs),func.avg(M.tobs),func.max(M.tobs)).filter((M.date>=start)&(M.date<=end)).first()

    return {'Min':results[0],'Avg':results[1],'Max':results[2]}