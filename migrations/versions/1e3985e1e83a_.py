"""empty message

Revision ID: 1e3985e1e83a
Revises: 
Create Date: 2020-12-09 12:30:06.283111

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1e3985e1e83a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_gaji')
    op.drop_table('tb_summary_kehadiran')
    op.drop_table('tb_pembayaran_gaji')
    op.drop_table('tb_kehadiran')
    op.drop_table('tb_penggajian')
    op.drop_table('tb_department')
    op.drop_table('tb_tunjangan')
    op.add_column('tb_pegawai', sa.Column('id_departement', sa.Integer(), nullable=True))
    op.alter_column('tb_pegawai', 'id_golongan',
               existing_type=mysql.INTEGER(display_width=10),
               nullable=True)
    op.alter_column('tb_pegawai', 'jabatan',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=50),
               nullable=True)
    op.alter_column('tb_pegawai', 'join_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('tb_pegawai', 'nama_pegawai',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=50),
               nullable=True)
    op.alter_column('tb_pegawai', 'tgl_lahir',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_constraint('tb_pegawai_ibfk_2', 'tb_pegawai', type_='foreignkey')
    op.drop_constraint('tb_pegawai_ibfk_1', 'tb_pegawai', type_='foreignkey')
    op.drop_column('tb_pegawai', 'id_department')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_pegawai', sa.Column('id_department', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False))
    op.create_foreign_key('tb_pegawai_ibfk_1', 'tb_pegawai', 'tb_gaji', ['id_golongan'], ['id_golongan'])
    op.create_foreign_key('tb_pegawai_ibfk_2', 'tb_pegawai', 'tb_department', ['id_department'], ['id_department'])
    op.alter_column('tb_pegawai', 'tgl_lahir',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('tb_pegawai', 'nama_pegawai',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=50),
               nullable=False)
    op.alter_column('tb_pegawai', 'join_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('tb_pegawai', 'jabatan',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=50),
               nullable=False)
    op.alter_column('tb_pegawai', 'id_golongan',
               existing_type=mysql.INTEGER(display_width=10),
               nullable=False)
    op.drop_column('tb_pegawai', 'id_departement')
    op.create_table('tb_tunjangan',
    sa.Column('id_tunjangan', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('id_pegawai', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('golongan', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('nama_tunjangan', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.ForeignKeyConstraint(['id_pegawai'], ['tb_pegawai.id_pegawai'], name='tb_tunjangan_ibfk_1'),
    sa.PrimaryKeyConstraint('id_tunjangan'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_department',
    sa.Column('id_department', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('nama_department', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('id_pegawai_manager', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_department'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_penggajian',
    sa.Column('id_penggajian', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('id_pegawai', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('bulan', sa.DATE(), nullable=False),
    sa.Column('gaji', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('id_tunjangan', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('id_summary', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_summary'], ['tb_summary_kehadiran.id_summary'], name='tb_penggajian_ibfk_2'),
    sa.ForeignKeyConstraint(['id_tunjangan'], ['tb_tunjangan.id_tunjangan'], name='tb_penggajian_ibfk_1'),
    sa.PrimaryKeyConstraint('id_penggajian'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_kehadiran',
    sa.Column('id_kehadiran', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('id_pegawai', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('tanggal', sa.DATE(), nullable=False),
    sa.Column('kehadiran', mysql.ENUM('hadir', 'sakit', 'alpa', '', collation='utf8_bin'), nullable=False),
    sa.Column('validasi_manager', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_pegawai'], ['tb_pegawai.id_pegawai'], name='tb_kehadiran_ibfk_1'),
    sa.PrimaryKeyConstraint('id_kehadiran'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_pembayaran_gaji',
    sa.Column('id_pembayaran', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('tgl_transfer', sa.DATE(), nullable=False),
    sa.Column('status', mysql.ENUM('selesai', 'pending', 'gagal', '', collation='utf8_bin'), nullable=False),
    sa.Column('amount', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('id_penggajian', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_penggajian'], ['tb_penggajian.id_penggajian'], name='tb_pembayaran_gaji_ibfk_1'),
    sa.PrimaryKeyConstraint('id_pembayaran'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_summary_kehadiran',
    sa.Column('id_summary', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('id_pegawai', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('total_kehadiran', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('jml_hari_kerja', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('keterangan', mysql.TEXT(collation='utf8_bin'), nullable=False),
    sa.Column('potongan', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.ForeignKeyConstraint(['id_pegawai'], ['tb_pegawai.id_pegawai'], name='tb_summary_kehadiran_ibfk_1'),
    sa.PrimaryKeyConstraint('id_summary'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_gaji',
    sa.Column('id_golongan', mysql.INTEGER(display_width=10), autoincrement=False, nullable=False),
    sa.Column('golongan', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('gaji', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.PrimaryKeyConstraint('id_golongan'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
