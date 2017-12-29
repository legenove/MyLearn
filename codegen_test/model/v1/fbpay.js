/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Fbpay = function () {
    /*
        @params obj 'data params'
            trade_type   'string' 
            target_id   'string' 
            order_type   'string' 订单类型 提问/偷听/赞赏/悬赏/小讲/小讲礼物/小讲合辑
            target_type   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/fbpay",
            method: "POST",
            data: {
                trade_type: obj.trade_type,
                target_id: obj.target_id,
                order_type: obj.order_type,
                target_type: obj.target_type
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
    Fbpay: new Fbpay
};