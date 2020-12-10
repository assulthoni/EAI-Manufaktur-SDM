from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal, inputs
from .model import Tunjangan
from app import db
import json

tunjangan_fields = {
    "id_tunjangan": fields.Integer,
    "waktu_hadir": fields.DateTime,
    "id_pegawai": fields.Integer,
    "tunjangan": fields.String,
    "validasi_manager": fields.Boolean  
}

tunjangan_list_fields = {
    'count': fields.Integer,
    'tunjangans': fields.List(fields.Nested(tunjangan_fields)),
}

tunjangan_post_parser = reqparse.RequestParser()
tunjangan_post_parser.add_argument("id_tunjangan", type=int, required=False, location=['json'],
                              help=f'id_tunjangan parameter is required')
tunjangan_post_parser.add_argument("waktu_hadir", type=str, required=False, location=['json'],
                              help=f'waktu_hadir parameter is required')
tunjangan_post_parser.add_argument("id_pegawai", type=int, required=True, location=['json'],
                              help=f'id_pegawai parameter is required')
tunjangan_post_parser.add_argument("tunjangan", type=str, required=True, location=['json'],
                              help=f'tunjangan parameter is required')
tunjangan_post_parser.add_argument("validasi_manager", type=inputs.boolean, required=True, location=['json'],
                              help=f'validasi_manager parameter is required')


class TunjangansResource(Resource):
    def get(self, id_tunjangan=None):
        if id_tunjangan:
            tunjangan = Tunjangan.query.filter_by(id_tunjangan=id_tunjangan).first()
            return marshal(tunjangan, tunjangan_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            tunjangan = Tunjangan.query.filter_by(**args).order_by(Tunjangan.id_tunjangan)
            if limit:
                tunjangan = tunjangan.limit(limit)

            if offset:
                tunjangan = tunjangan.offset(offset)

            tunjangan = tunjangan.all()
            return marshal({
                'count': len(tunjangan),
                'tunjangans': [u for u in tunjangan]
            }, tunjangan_list_fields)

    @marshal_with(tunjangan_fields)
    def post(self):
        args = tunjangan_post_parser.parse_args()
        print(type(args))
        tunjangan = Tunjangan(**args)
        db.session.add(tunjangan)
        db.session.commit()

        return tunjangan

    @marshal_with(tunjangan_fields)
    def put(self, id_tunjangan=None):
        tunjangan = Tunjangan.query.get(id_tunjangan)

        if 'tunjangan' in request.json:
            tunjangan.tunjangan = request.json['tunjangan']

        db.session.commit()
        return tunjangan

    @marshal_with(tunjangan_fields)
    def delete(self, id_tunjangan=None):
        tunjangan = Tunjangan.query.get(id_tunjangan)

        db.session.delete(tunjangan)
        db.session.commit()

        return tunjangan
