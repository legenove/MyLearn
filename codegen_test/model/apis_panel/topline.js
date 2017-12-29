/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Topline = function () {
    /*
        @params obj 'data params'
            is_public   'boolean' is public in query
            is_top   'boolean' is top in query
            order_by   'string' order by in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            operator_id   'ref' 
            date_updated   'ref' 
            order_score   'integer' 
            question   'ref' 
            short_title   'string' 
            is_top   'boolean' 
            is_public   'boolean' 
            date_created   'ref' 
            id   'integer' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topline",
            method: "GET",
            data: {
                is_public: obj.is_public,
                is_top: obj.is_top,
                order_by: obj.order_by,
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
    
    /*
        @params obj 'data params'
            content   'ref' 
            respondent_id   'ref' 
            order_score   'integer' 
            account_id   'ref' 
            short_title   'string' 
            
        @success
            status 201    type:object
            operator_id   'ref' 
            date_updated   'ref' 
            order_score   'integer' 
            question   'ref' 
            short_title   'string' 
            is_top   'boolean' 
            is_public   'boolean' 
            date_created   'ref' 
            id   'integer' 
            question_id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topline",
            method: "POST",
            data: {
                content: obj.content,
                respondent_id: obj.respondent_id,
                order_score: obj.order_score || 0,
                account_id: obj.account_id,
                short_title: obj.short_title
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
    Topline: new Topline
};