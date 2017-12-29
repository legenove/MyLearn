import tensorflow as tf


with tf.Session() as sess:
    hello = tf.constant('hello, TensorFlow')
    print sess.run(hello)

    a = tf.constant(10)
    b = tf.constant(32)
    print sess.run(a+b)


rows = (db.session.query(RA.account_id, func.row_number().over(
    partition_by=RA.account_id,
    order_by=expression.case((
            (RA.account_type == 'sub', 0),
            (RA.is_default.is_(True), 1)))).label("row_number")).filter(RA.realname==u'刘国阳').subquery())

ras = RA.query.join(rows, RA.account_id == rows.c.account_id).filter(rows.c.row_number == 1).subquery()

query = FA.query.join(ras, FA.account_id == ras.c.account_id).all()

sub_query = RA.query.order_by(expression.case((
            (RA.account_type == 'sub', 0),
            (RA.is_default.is_(True), 1)))).group_by(RA.account_id).all()


