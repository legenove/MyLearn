/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Accounts = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            nickname   'string' nickname in query
            is_star   'boolean' is star in query
            is_respondent   'boolean' is respondent in query
            order_by   'string' order type in query
            mobile   'string' mobile in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'ref' 
            is_black   'boolean' 
            questions_count   'integer' 
            is_star   'boolean' 
            order_score   'integer' 
            date_updated   'ref' 
            is_admin   'boolean' 
            date_created   'ref' 
            is_verified   'boolean' 
            answers_count   'integer' 
            is_respondent   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts",
            method: "GET",
            data: {
                id: obj.id,
                nickname: obj.nickname,
                is_star: obj.is_star,
                is_respondent: obj.is_respondent,
                order_by: obj.order_by,
                mobile: obj.mobile,
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
    Accounts: new Accounts
};