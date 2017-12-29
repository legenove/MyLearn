/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FundAccounts = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            order_by   'string' order by in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            outcome   'integer' 
            account   'ref' 
            balance   'integer' 
            answered_income   'integer' 
            income   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fund_accounts",
            method: "GET",
            data: {
                account_id: obj.account_id,
                order_by: obj.order_by,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
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
    FundAccounts: new FundAccounts
};