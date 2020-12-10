from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal, inputs
from .model import Pegawai
from app import db

pegawai_fields = {
    'id_pegawai': fields.Integer,
    'nama_pegawai': fields.String,
    'id_golongan' : fields.Integer,
    'jabatan' : fields.String,
    'tgl_lahir' : fields.DateTime,
    'join_date' : fields.DateTime,
    'id_department' : fields.Integer
}

pegawai_list_fields = {
    'count': fields.Integer,
    'pegawais': fields.List(fields.Nested(pegawai_fields)),
}

pegawai_post_parser = reqparse.RequestParser()
pegawai_post_parser.add_argument('nama_pegawai', type=str, required=True, location=['json'],
                              help='nama_pegawai parameter is required')
pegawai_post_parser.add_argument('id_golongan', type=int, required=True, location=['json'],
                              help='id_golongan parameter is required')
pegawai_post_parser.add_argument('id_department', type=int, required=True, location=['json'],
                              help='d_department parameter is required')
pegawai_post_parser.add_argument('id_pegawai', type=int, required=False, location=['json'],
                              help='id_pegawai parameter is required')
pegawai_post_parser.add_argument('jabatan', type=str, required=True, location=['json'],
                              help='jabatan parameter is required')
pegawai_post_parser.add_argument('tgl_lahir', type=inputs.datetime_from_iso8601, required=True, location=['json'],
                              help='tgl_lahir parameter is required')
pegawai_post_parser.add_argument('join_date', type=inputs.datetime_from_iso8601, required=True, location=['json'],
                              help='join_date parameter is required')


class PegawaisResource(Resource):
    def get(self, id_pegawai=None):
        if id_pegawai:
            pegawai = Pegawai.query.filter_by(id_pegawai=id_pegawai).first()
            return marshal(pegawai, pegawai_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            pegawai = Pegawai.query.filter_by(**args).order_by(Pegawai.id_pegawai)
            if limit:
                pegawai = pegawai.limit(limit)

            if offset:
                pegawai = pegawai.offset(offset)

            pegawai = pegawai.all()
            print(type(pegawai[0]))
            return marshal({
                'count': len(pegawai),
                'pegawais': [u for u in pegawai]
            }, pegawai_list_fields)

    @marshal_with(pegawai_fields)
    def post(self):
        args = pegawai_post_parser.parse_args()

        pegawai = Pegawai(**args)
        db.session.add(pegawai)
        db.session.commit()

        return pegawai

    @marshal_with(pegawai_fields)
    def put(self, id_pegawai=None):
        pegawai = Pegawai.query.get(id_pegawai)

        if 'nama_pegawai' in request.json:
            pegawai.nama_pegawai = request.json['nama_pegawai']

        db.session.commit()
        return pegawai

    @marshal_with(pegawai_fields)
    def delete(self, id_pegawai=None):
        pegawai = Pegawai.query.get(id_pegawai)

        db.session.delete(pegawai)
        db.session.commit()

        return pegawai
