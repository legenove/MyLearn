/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            topics   'array' 
            topic_short_title   'string' 
            operation_records   'array' 
            images   'array' 
            is_public   'boolean' 
            _answer   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "",
            method: "GET",
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
            id   'string' string id in path
            content   'string' 
            order_score   'integer' 
            is_recommended   'boolean' 
            review_status   'string' 
            
        @success
            status 200    type:object
            topics   'array' 
            topic_short_title   'string' 
            operation_records   'array' 
            images   'array' 
            is_public   'boolean' 
            _answer   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "",
            method: "PUT",
            data: {
                content: obj.content,
                order_score: obj.order_score,
                is_recommended: obj.is_recommended,
                review_status: obj.review_status
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
    QuestionsId: new QuestionsId
};