from app import db


class Pegawai(db.Model):
    __tablename__ = 'tb_pegawai'

    id_pegawai = db.Column(db.Integer, primary_key=True)
    nama_pegawai = db.Column(db.String(50))
    id_golongan = db.Column(db.Integer)
    jabatan = db.Column(db.String(50))
    tgl_lahir = db.Column(db.DateTime)
    join_date = db.Column(db.DateTime)
    id_department = db.Column(db.Integer)
    # todos = db.relationship('Todo', backref='user', lazy='select')

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id_pegawai, self.nama_pegawai)
