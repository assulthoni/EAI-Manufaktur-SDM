from app import db
import enum

class KehadiranEnum(enum.Enum):
    hadir = "hadir"
    sakit = "sakit"
    alpa = "alpa"

class Tunjangan(db.Model):
    __tablename__ = 'tb_tunjangan'

    id_tunjangan = db.Column(db.Integer, primary_key=True)
    id_pegawai = db.Column(db.Integer)
    golongan = db.Column(db.String(50))
    nama_tunjangan = db.Column(db.String(50))

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id_pegawai, self.nama_pegawai)
