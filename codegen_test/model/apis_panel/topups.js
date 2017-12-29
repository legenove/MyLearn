/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Topups = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            respondent_id   'integer' respondent id in query
            question_id   'string' question id in query
            operator_id   'integer' operator id in query
            operate_type   'string' operate type in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            operator_id   'ref' 
            account_id   'ref' 
            respondent_id   'ref' 
            date_created   'ref' 
            visitor_count   'integer' 
            id   'ref' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topups",
            method: "GET",
            data: {
                account_id: obj.account_id,
                respondent_id: obj.respondent_id,
                question_id: obj.question_id,
                operator_id: obj.operator_id,
                operate_type: obj.operate_type,
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
            duration   'integer' 
            respondent_meta   'array' 
            span   'integer' 充值问题过去的时间
            date_executed   'string' 
            question_meta   'array' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topups",
            method: "POST",
            data: {
                duration: obj.duration,
                respondent_meta: obj.respondent_meta,
                span: obj.span,
                date_executed: obj.date_executed,
                question_meta: obj.question_meta
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
    Topups: new Topups
};