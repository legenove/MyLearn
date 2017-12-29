/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TradeRechargeAndroid = function () {
    /*
        @params obj 'data params'
            promote_type   'string' 
            
        @success
            status 201    type:object
            transaction_id   'string' 
            total_fee   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/trade/recharge/android",
            method: "POST",
            data: {
                promote_type: obj.promote_type
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
    TradeRechargeAndroid: new TradeRechargeAndroid
};