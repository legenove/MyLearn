/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsLibraries = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            operator_id   'integer' operator id in query
            type   'string' library type in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            operator_id   'ref' 
            account_id   'ref' 
            offer   'ref' 
            date_updated   'ref' 
            is_active   'boolean' 
            content   'ref' 
            date_created   'ref' 
            type   'string' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries",
            method: "GET",
            data: {
                account_id: obj.account_id,
                operator_id: obj.operator_id,
                type: obj.type,
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
            is_active   'boolean' 
            type   'string' 
            account_id   'ref' 
            offer   'ref' 
            
        @success
            status 201    type:object
            operator_id   'ref' 
            account_id   'ref' 
            offer   'ref' 
            date_updated   'ref' 
            is_active   'boolean' 
            content   'ref' 
            date_created   'ref' 
            type   'string' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries",
            method: "POST",
            data: {
                content: obj.content,
                is_active: obj.is_active,
                type: obj.type,
                account_id: obj.account_id,
                offer: obj.offer
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
    QuestionsLibraries: new QuestionsLibraries
};