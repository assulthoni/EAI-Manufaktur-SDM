from app import db
import enum

class KehadiranEnum(enum.Enum):
    hadir = "hadir"
    sakit = "sakit"
    alpa = "alpa"

class Kehadiran(db.Model):
    __tablename__ = 'tb_kehadiran'

    id_kehadiran = db.Column(db.Integer, primary_key=True)
    waktu_hadir = db.Column(db.Time(timezone=False))
    id_pegawai = db.Column(db.Integer)
    kehadiran = db.Column(db.Enum(KehadiranEnum))
    validasi_manager = db.Column(db.Boolean, default=False, server_default="false")

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id_pegawai, self.nama_pegawai)
