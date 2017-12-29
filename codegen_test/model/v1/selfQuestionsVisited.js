/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfQuestionsVisited = function () {
    /*
        @params obj 'data params'
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            free_type   'string' 
            discussions_count   'integer' 
            is_sticky   'boolean' 
            is_limit_free   'boolean' 
            is_tenant_free   'boolean' 
            is_free_in_30mins   'boolean' 
            has_discussions   'boolean' 
            is_free   'boolean' 
            is_accessible   'boolean' 
            remaining_seconds   'integer' 
            is_fenda_ask   'boolean' 
            answer   'ref' 
            is_all_free   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/questions/visited",
            method: "GET",
            data: {
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
    SelfQuestionsVisited: new SelfQuestionsVisited
};