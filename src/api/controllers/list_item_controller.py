from flask import Response
from flask_restx import Namespace, Resource


api = Namespace('list item', description='API for to do list items', path='/list_items')


# GET /list_items/<to_do_list_id> -> to do list'in itemlarını döner
# POST /list_items/<to_do_list_id> -> to do list'e item ekler
@api.route('/<to_do_list_id>')
class GetCreateListItem(Resource):
    def get(self, to_do_list_id: str) -> Response:
        pass

    def post(self, to_do_list_id: str) -> Response:
        pass

# GET /list_items/<list_item_id> -> bir item'ın içeriğin döner
# DELETE /list_items/<list_item_id> -> to do listten item'ı siler
# PUT /list_items/<list_item_id> -> to do list item'ı günceller
# POST /list_items/<list_item_id>/complete -> lsit item'ı bitirir.
