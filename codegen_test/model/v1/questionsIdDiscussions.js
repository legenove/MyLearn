/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdDiscussions = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            free_key   'string' free key in query
            rewarder_id   'integer' rewarder id in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            account_id   'integer' 
            date_updated   'ref' 
            account_role   'string' 
            content   'string' 
            answer   'ref' 
            date_created   'ref' 
            type   'string' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/discussions",
            method: "GET",
            data: {
                free_key: obj.free_key,
                rewarder_id: obj.rewarder_id,
                offset: obj.offset,
                limit: obj.limit,
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
    
    /*
        @params obj 'data params'
            id   'string' question id in path
            content   'string' 
            
        @success
            status 201    type:object
            status   'string' 
            account_id   'integer' 
            account_role   'string' 
            content   'string' 
            type   'string' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/discussions",
            method: "POST",
            data: {
                content: obj.content
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
    QuestionsIdDiscussions: new QuestionsIdDiscussions
};