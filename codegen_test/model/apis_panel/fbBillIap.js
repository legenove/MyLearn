/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FbBillIap = function () {
    /*
        @params obj 'data params'
            pay_type   'string' 
            account_id   'integer' 
            receipt_content   'string' 
            
        @success
            status 201    type:object
            receipt   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fb/bill/iap",
            method: "POST",
            data: {
                pay_type: obj.pay_type || "fdb_ios",
                account_id: obj.account_id,
                receipt_content: obj.receipt_content
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
    FbBillIap: new FbBillIap
};