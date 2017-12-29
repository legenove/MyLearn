/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FbBillRechargesReceiptIdRestore = function () {
    /*
        @params obj 'data params'
            receipt_id   'integer' receipt id in query
            
        @success
            status 200    type:object
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
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fb/bill/recharges/" + obj.receipt_id + "/restore",
            method: "PUT",
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
    FbBillRechargesReceiptIdRestore: new FbBillRechargesReceiptIdRestore
};