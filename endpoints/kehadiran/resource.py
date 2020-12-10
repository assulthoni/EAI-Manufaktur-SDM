from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal, inputs
from .model import Kehadiran
from app import db
import json

kehadiran_fields = {
    "id_kehadiran": fields.Integer,
    "waktu_hadir": fields.DateTime,
    "id_pegawai": fields.Integer,
    "kehadiran": fields.String,
    "validasi_manager": fields.Boolean
}

kehadiran_list_fields = {
    'count': fields.Integer,
    'kehadirans': fields.List(fields.Nested(kehadiran_fields)),
}

kehadiran_post_parser = reqparse.RequestParser()
kehadiran_post_parser.add_argument("id_kehadiran", type=int, required=False, location=['json'],
                              help=f'id_kehadiran parameter is required')
kehadiran_post_parser.add_argument("waktu_hadir", type=str, required=False, location=['json'],
                              help=f'waktu_hadir parameter is required')
kehadiran_post_parser.add_argument("id_pegawai", type=int, required=True, location=['json'],
                              help=f'id_pegawai parameter is required')
kehadiran_post_parser.add_argument("kehadiran", type=str, required=True, location=['json'],
                              help=f'kehadiran parameter is required')
kehadiran_post_parser.add_argument("validasi_manager", type=inputs.boolean, required=True, location=['json'],
                              help=f'validasi_manager parameter is required')


class KehadiransResource(Resource):
    def get(self, id_kehadiran=None):
        if id_kehadiran:
            kehadiran = Kehadiran.query.filter_by(id_kehadiran=id_kehadiran).first()
            return marshal(kehadiran, kehadiran_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            kehadiran = Kehadiran.query.filter_by(**args).order_by(Kehadiran.id_kehadiran)
            if limit:
                kehadiran = kehadiran.limit(limit)

            if offset:
                kehadiran = kehadiran.offset(offset)

            kehadiran = kehadiran.all()
            return marshal({
                'count': len(kehadiran),
                'kehadirans': [u for u in kehadiran]
            }, kehadiran_list_fields)

    @marshal_with(kehadiran_fields)
    def post(self):
        args = kehadiran_post_parser.parse_args()
        print(type(args))
        kehadiran = Kehadiran(**args)
        db.session.add(kehadiran)
        db.session.commit()

        return kehadiran

    @marshal_with(kehadiran_fields)
    def put(self, id_kehadiran=None):
        kehadiran = Kehadiran.query.get(id_kehadiran)

        if 'kehadiran' in request.json:
            kehadiran.kehadiran = request.json['kehadiran']

        db.session.commit()
        return kehadiran

    @marshal_with(kehadiran_fields)
    def delete(self, id_kehadiran=None):
        kehadiran = Kehadiran.query.get(id_kehadiran)

        db.session.delete(kehadiran)
        db.session.commit()

        return kehadiran
