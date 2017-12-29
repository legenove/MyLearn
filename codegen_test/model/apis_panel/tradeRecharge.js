/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TradeRecharge = function () {
    /*
        @params obj 'data params'
            comment   'string' 
            pay_type   'string' 
            promote_type   'string' 
            account_id   'integer' 
            fee_type   'integer' 
            
        @success
            status 201    type:object
            transaction_id   'string' 
            total_fee   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/trade/recharge",
            method: "POST",
            data: {
                comment: obj.comment,
                pay_type: obj.pay_type || "fdb_ios",
                promote_type: obj.promote_type,
                account_id: obj.account_id,
                fee_type: obj.fee_type
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
    TradeRecharge: new TradeRecharge
};