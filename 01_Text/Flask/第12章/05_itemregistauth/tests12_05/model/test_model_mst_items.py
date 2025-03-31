from itemregistauth import app, db
from itemregistauth.models.mst_items import Mst_items

def test_model_basic_function():
    """モデルを使ったCRUD操作の確認"""

    ### Arrange（準備） ###
    item=Mst_items(name="テスト商品", price=1000)

    ### Act（実行） ### 
    with app.app_context():

        # Create
        db.session.add(item)
        db.session.commit()

        # Read
        Mst_items.query.order_by(Mst_items.id).all()

        # Update
        item.price=900
        db.session.commit()

        # Delete
        db.session.delete(item)
        db.session.commit()

    ### Assert（検証） ### 
    assert True
