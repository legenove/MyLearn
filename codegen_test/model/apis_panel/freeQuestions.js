/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FreeQuestions = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            operator_id   'integer' operator id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            is_active   'boolean' 
            operator_id   'ref' 
            question   'ref' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/free_questions",
            method: "GET",
            data: {
                question_id: obj.question_id,
                operator_id: obj.operator_id,
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
            question_id   'ref' 
            
        @success
            status 200    type:object
            is_active   'boolean' 
            operator_id   'ref' 
            question   'ref' 
            question_id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/free_questions",
            method: "POST",
            data: {
                question_id: obj.question_id
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
    FreeQuestions: new FreeQuestions
};