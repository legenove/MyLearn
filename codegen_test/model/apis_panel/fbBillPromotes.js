/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FbBillPromotes = function () {
    /*
        @params obj 'data params'
            pay_type   'string' fb pay type in query
            promote_type   'string' promote type in query
            promote_status   'string' promote status in query
            account_id   'integer' account id in query
            date_created   'string' recharge date in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            comment   'string' 
            status   'string' 
            operator_id   'integer' 
            account_id   'integer' 
            promote_type   'string' 
            total_fee   'integer' 
            date_created   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fb/bill/promotes",
            method: "GET",
            data: {
                pay_type: obj.pay_type || "fdb_ios",
                promote_type: obj.promote_type,
                promote_status: obj.promote_status,
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
    FbBillPromotes: new FbBillPromotes
};