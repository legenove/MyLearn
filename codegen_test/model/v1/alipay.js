/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Alipay = function () {
    /*
        @params obj 'data params'
            trade_type   'string' 
            order_type   'string' 订单类型 提问/偷听/赞赏/悬赏/小讲/小讲礼物/小讲合辑
            offer   'integer' 支付金额，只有赞赏使用
            target_id   'string' 
            target_type   'string' 
            return_url   'string' 
            
        @success
            status 201    type:object
            payment_url   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/alipay",
            method: "POST",
            data: {
                trade_type: obj.trade_type || "alipay",
                order_type: obj.order_type,
                offer: obj.offer,
                target_id: obj.target_id,
                target_type: obj.target_type,
                return_url: obj.return_url
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Alipay: new Alipay
};