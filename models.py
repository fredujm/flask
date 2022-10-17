from app_coll import db, metadata

class Region(db.Model):
    __tablename__ = "region"
    region_id = db.Column(db.Integer, primary_key=True)
    region_ref = db.Column(db.String, nullable=False)
    region_name = db.Column(db.String, nullable=False)
    thedepts = db.relationship("Department", back_populates="theregion")
    

class Department(db.Model):
    __tablename__ = "department"
    dept_id = db.Column(db.String, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey("region.region_id"), nullable=False)
    dept_ref = db.Column(db.String, nullable=False)
    dept_name = db.Column(db.String, nullable=False)
    theregion = db.relationship("Region",back_populates="thedepts")
    themunis = db.relationship("Municipality", back_populates="thedept")


class Municipality(db.Model):
    __tablename__ = "municipality"
    mun_id = db.Column(db.Integer, primary_key=True)
    dept_id = db.Column(db.String, db.ForeignKey("department.dept_id"), nullable=False)
    mun_name = db.Column(db.String, nullable=False)
    mun_code = db.Column(db.String, nullable=False)
    insee_code = db.Column(db.String, nullable=True)
    gps_lat = db.Column(db.Float, nullable=True)
    gps_lng = db.Column(db.Float, nullable=True)
    thedept = db.relationship("Department",back_populates="themunis")
    