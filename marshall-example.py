from flask_restful import fields, marshal_with

mfields = { 'a': fields.Raw }

@marshal_with(mfields)
def get():
    print({'a': 100, 'b': 'foo'})
    return {'a': 100, 'b': 'foo'}

get()

