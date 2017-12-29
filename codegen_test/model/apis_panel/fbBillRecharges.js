/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FbBillRecharges = function () {
    /*
        @params obj 'data params'
            pay_type   'string' fb pay type in query
            recharge_type   'string' recharge type in query
            recharge_status   'string' recharge status in query
            iap_status   'string' iap status in query
            account_id   'integer' account id in query
            date_created   'string' recharge date in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            comment   'string' 
            account_id   'integer' 
            receipt_id   'integer' 
            receipt_content   'string' 
            receipt_result   'string' 
            total_fee   'integer' 
            recharge_type   'string' 
            date_created   'ref' 
            transaction_id   'string' 分答币系统交易号
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fb/bill/recharges",
            method: "GET",
            data: {
                pay_type: obj.pay_type || "fdb_ios",
                recharge_type: obj.recharge_type,
                recharge_status: obj.recharge_status,
                iap_status: obj.iap_status,
                account_id: obj.account_id,
                date_created: obj.date_created,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    FbBillRecharges: new FbBillRecharges
};