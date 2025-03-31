from itemregistauth import app, db
from itemregistauth.models.mst_accounts import Mst_account

def test_model_basic_function():
    """モデルを使ったCRUD操作の確認"""

    ### Arrange（準備） ###
    account=Mst_account(user_id="userid9999", password="userid9999")

    ### Act（実行） ### 
    with app.app_context():

        # Create
        db.session.add(account)
        db.session.commit()

        # Read
        Mst_account.query.order_by(Mst_account.user_id).all()

        # Update
        account.password="userid9999mod"
        db.session.commit()

        # Delete
        db.session.delete(account)
        db.session.commit()

    ### Assert（検証） ### 
    assert True
