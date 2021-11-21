from datetime import datetime

from alembic import op
from sqlalchemy import table, column

import sqlalchemy as sa


def seed_list_item_statuses():
    list_item_statuses_table = create_status_table('list_item_statuses')

    str_now = get_now_str()

    op.bulk_insert(list_item_statuses_table,
                   [
                       {'id': 1, 'status': 'Pending', 'created_date': op.inline_literal(str_now)},
                       {'id': 2, 'status': 'Completed', 'created_date': op.inline_literal(str_now)},
                       {'id': 3, 'status': 'Deleted', 'created_date': op.inline_literal(str_now)},
                   ], multiinsert=False)


def create_status_table(table_name: str) -> table:
    return table(table_name,
                 column('id', sa.Integer),
                 column('status', sa.String),
                 column('created_date', sa.DateTime))


def get_now_str():
    now = datetime.utcnow()
    return f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute:02d}:{now.second}'
